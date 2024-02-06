import asyncio
import logging, os, inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.ERROR)
current_file = os.path.basename(__file__)

load_dotenv()

class BASIC_PARAMETRS():
    def __init__(self):        
        self.SOLI_DEO_GLORIA = 'Soli Deo Gloria!'      
        self.market = 'spot'
                
    def init_api_key(self):
        self.tg_api_token = os.getenv("TG_API_TOKEN", "")
        self.api_key  = os.getenv(f"BINANCE_API_PUBLIC_KEY", "")
        self.api_secret = os.getenv(f"BINANCE_API_PRIVATE_KEY", "") 
        self.seq_control_token = os.getenv(f"SEQ_TOKEN", "")
        self.header = {
            'X-MBX-APIKEY': self.api_key
        }    

class URL_TEMPLATES(BASIC_PARAMETRS):
    def __init__(self) -> None:
        super().__init__()        
        self.URL_PATTERN_DICT= {}              

    def init_urls(self):       
        self.URL_PATTERN_DICT['current_price_url'] = "https://api.binance.com/api/v3/ticker/price"
        self.URL_PATTERN_DICT['all_tikers_url'] = "https://api.binance.com/api/v3/ticker/24hr"
        self.URL_PATTERN_DICT['create_order_url'] = 'https://api.binance.com/api/v3/order'
        self.URL_PATTERN_DICT['exchangeInfo_url'] = 'https://api.binance.com/api/v3/exchangeInfo'
        self.URL_PATTERN_DICT['balance_url'] = 'https://api.binance.com/api/v3/account'
        self.URL_PATTERN_DICT['get_all_orders_url'] = 'https://api.binance.com/api/v3/openOrders'
        self.URL_PATTERN_DICT['cancel_all_orders_url'] = 'https://api.binance.com/api/v3/openOrders'
        self.URL_PATTERN_DICT['positions_url'] = 'https://api.binance.com/api/v3/account'            
        self.URL_PATTERN_DICT["klines_url"] = 'https://api.binance.com/api/v3/klines'

class RISKK(URL_TEMPLATES):
    def __init__(self) -> None:
        super().__init__()        
        self.tp_mode = 'S' 
        self.TP_rate = 4 # %      
        self.SL_ratio = 3  # %        
    def risk_init(self):
        self.risk_ralations = self.TP_rate/self.SL_ratio

class ORDER_PARAMS(RISKK):
    def __init__(self) -> None:
        super().__init__()
        self.depo = '7usdt' # usdt

class OTHERSS(ORDER_PARAMS):
    def __init__(self) -> None:
        super().__init__()

    def others_init(self):
        self.buy_sell_tumbler = asyncio.Lock()
        self.stop_cycle = False
        self.x_percentage_ceiling = 49

class INIT_PARAMS(OTHERSS):
    def __init__(self) -> None:
        super().__init__()
        self.init_itits()

    def init_itits(self):
        print('helloo')
        self.init_api_key()       
        self.init_urls()   
        self.risk_init()   
        self.others_init()   

# params = INIT_PARAMS()
# print(params.test_flag)
# python params_init.py
