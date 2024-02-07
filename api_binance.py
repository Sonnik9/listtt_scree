# from params_init import INIT_PARAMS
from connector import TG_ASSISTENT
import math
# import ccxt
import logging, os, inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

# load_dotenv()

class GET_API(TG_ASSISTENT):
    def __init__(self) -> None:
        super().__init__()        

    async def get_exchange_info(self, symbol):  

        exchangeInfo = None
        params = {}

        try:
            url = self.URL_PATTERN_DICT['exchangeInfo_url']  
            if symbol:
                params = {'symbol': symbol}      
            exchangeInfo = await self.HTTP_request(url, method='GET', params=params)
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

    async def make_market_order(self, symbol, qnt, side):
                
        response = None
        success_flag = False
        try:
            url = self.URL_PATTERN_DICT['create_order_url']
            # print(url)
            params = {}        
            params["symbol"] = symbol              
            params["type"] = 'MARKET'             
            params["quantity"] = qnt     
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
                # print(f'depo*2: {depo*2}')
                usdt_flag = True
            elif depo.endswith(f"{symbol.replace('USDT', '').strip()}"):           
                qnt = float(depo.replace(f"{symbol.replace('USDT', '').strip()}", '').strip())
                # print(f'qnt*2: {qnt*2}')

            symbol_info = await self.get_exchange_info(symbol)

            if symbol_info:                
                symbol_data = next((item for item in symbol_info["symbols"] if item['symbol'] == symbol), None)

            if symbol_data:
                tick_size = float(symbol_data['filters'][0]["tickSize"])
                lot_size_filter = next((f for f in symbol_data.get('filters', []) if f.get('filterType') == 'LOT_SIZE'), None)
                if lot_size_filter:
                    quantity_precision = -int(math.log10(float(lot_size_filter.get('stepSize', '1'))))
                    # print(f"quantity_precision: {quantity_precision}")

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

