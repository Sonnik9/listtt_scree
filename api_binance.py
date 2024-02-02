from params_init import INIT_PARAMS
import math
import time
import hmac
import hashlib
import requests
# import ccxt
import logging, os, inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

load_dotenv()

class CONFIG_API(INIT_PARAMS):

    def __init__(self) -> None:
        super().__init__()

    async def get_signature(self, params):
        try:
            params['timestamp'] = int(time.time() *1000)
            params_str = '&'.join([f'{k}={v}' for k,v in params.items()])
            hash = hmac.new(bytes(self.api_secret, 'utf-8'), params_str.encode('utf-8'), hashlib.sha256)        
            params['signature'] = hash.hexdigest()
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return params
   
    async def HTTP_request(self, url, **kwards):

        response = None
        multipliter = 2

        for i in range(2):
            try:
                # print('hi')
                response = requests.request(url=url, **kwards)
                # print(response)
                if response.status_code == 200:
                    break
                else:
                    time.sleep((i+1) * multipliter)              
   
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
                time.sleep((i+1) * multipliter)
        try:
            response = response.json()
        except:
            pass

        return response

class GET_API(CONFIG_API):
    def __init__(self) -> None:
        super().__init__()        

    async def get_exchange_info(self):  

        exchangeInfo = None

        try:
            url = self.URL_PATTERN_DICT['exchangeInfo_url']        
            exchangeInfo = await self.HTTP_request(url, method='GET', headers=self.header)
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return exchangeInfo
    
    async def get_current_price(self, symbol):        
               
        current_price = None
        url = self.URL_PATTERN_DICT['current_price_url']
        params = {'symbol': symbol}
        
        try:
            current_price = await self.HTTP_request(url, method='GET', params=params)            
            # current_price = float([x['price'] for x in current_price if x['symbol'] == symbol])
            current_price = float(current_price["price"])
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return current_price  

class POST_API(GET_API):
    def __init__(self) -> None:
        super().__init__()

    async def make_order(self, item, is_selling, target_price, market_type):
                
        response = None
        success_flag = False
        try:
            url = self.URL_PATTERN_DICT['create_order_url']
            # print(url)
            params = {}        
            params["symbol"] = item["symbol"]   
            # print(params["symbol"])  
            params["type"] = market_type
            # print(params["type"])  
            params["quantity"] = item['qnt']      
        
            if market_type == 'LIMIT':            
                params["price"] = target_price
                params["timeInForce"] = 'GTC' 
                # params['recvWindow'] = 5000
    
            if is_selling == 1:
                side = 'BUY'
            elif is_selling == -1:
                side = "SELL" 
            params["side"] = side 

            params = await self.get_signature(params)
            # print(params)
            response = await self.HTTP_request(url, method='POST', headers=self.header, params=params)
            # print(response)
            if response and 'clientOrderId' in response and response['side'] == side:
                success_flag = True
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return response, success_flag

class UTILS_API(POST_API):
    def __init__(self) -> None:
        super().__init__()

    async def count_multipliter_places(self, number):        
        number_str = str(number)
        if '.' in number_str:
            return len(number_str.split('.')[1])
        return 0
    
    async def calc_qnt_func(self, symbol, depo): 
        symbol_info = None
        symbol_data = None 
        price_precision = None
        price = None
        quantity_precision = None
        qnt = None
        quantity = None       
        usdt_flag = False
        minNotional = None 
        maxNotional = None

        try:
            depo = depo.upper()

            if depo.endswith('USDT'):
                depo = float(depo.replace('USDT', '').strip())
                print(f'depo*2: {depo*2}')
                usdt_flag = True
            elif depo.endswith(f"{symbol.replace('USDT', '').strip()}"):           
                qnt = float(depo.replace(f"{symbol.replace('USDT', '').strip()}", '').strip())
                print(f'qnt*2: {qnt*2}')

            symbol_info = await self.get_exchange_info(symbol)

            if symbol_info:                
                symbol_data = next((item for item in symbol_info["symbols"] if item['symbol'] == symbol), None)

            if symbol_data:
                tick_size = float(symbol_data['filters'][0]["tickSize"])
                lot_size_filter = next((f for f in symbol_data.get('filters', []) if f.get('filterType') == 'LOT_SIZE'), None)
                if lot_size_filter:
                    quantity_precision = -int(math.log10(float(lot_size_filter.get('stepSize', '1'))))
                    print(f"quantity_precision: {quantity_precision}")

                minNotional = float(next((f['minNotional'] for f in symbol_data['filters'] if f['filterType'] == 'NOTIONAL'), None))
                maxNotional = float(next((f['maxNotional'] for f in symbol_data['filters'] if f['filterType'] == 'NOTIONAL'), None))
                
                price_precision = await self.count_multipliter_places(tick_size)               
                # print(f'cur price: {price}')
                price = await self.get_current_price(symbol)

                if not usdt_flag:
                    depo = qnt * price
                if depo <= minNotional:
                    depo = minNotional               
                elif depo >= maxNotional:
                    depo = maxNotional
                
                quantity = round(depo / price, quantity_precision)

        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

        return quantity, price_precision
    
# ///////////////////////////////////////////////////////////////////////////////////
    async def market_order_temp_func(self, symbol, is_selling, depo):
        item = {}        
        item["symbol"] = symbol       
        open_market_order = None
        # ////////////////////////
        depo = self.depo
        # ////////////////////////

        try:                    
            item['qnt'], _ = await self.calc_qnt_func(symbol, depo)
            # print(f"{symbol}: item['qnt']: {item['qnt']}")        
            # print(f"{symbol}: item['item['price_precision']']: {item['price_precision']}") 
            if item['qnt']:
                
                success_flag = False
                market_type = 'MARKET'
                target_price = None       
                open_market_order, success_flag = await self.make_order(item, is_selling, target_price, market_type)
                print(f"open_market_order:  {open_market_order}") 
        except Exception as ex:
            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

        return open_market_order, success_flag