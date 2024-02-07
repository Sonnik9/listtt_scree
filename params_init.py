import asyncio
import json
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
        keyy_str = os.getenv('keyy', '')
        self.keyy = json.loads(keyy_str) if keyy_str else {}

        self.tg_api_token = self.keyy["TG_API_TOKEN"]
        self.api_key = self.keyy["BINANCE_API_PUBLIC_KEY"]
        self.api_secret = self.keyy["BINANCE_API_PRIVATE_KEY"]
        # print(self.api_key) 
        # print(self.api_secret) 
        self.seq_control_token = self.keyy["SEQ_TOKEN"]
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
        self.qnt = 0.00017
        self.depo = '7usdt'
        self.is_make_sell_logic_flag = False
        # self.depo = '330usdt' # usdt

class TG_INIT_VAR(ORDER_PARAMS):
    def __init__(self) -> None:
        super().__init__()

    def init_tg_var(self):
        self.block_acess_flag = False
        self.start_day_date = False
        self.start_flag = False
        self.dont_seq_control = False
        self.seq_control_flag = False
        self.depo_redirect_flag = False
        self.block_acess_counter = 0

class OTHERSS(TG_INIT_VAR):
    def __init__(self) -> None:
        super().__init__()

    def others_init(self):
        self.buy_sell_tumbler = asyncio.Lock()
        self.stop_cycle = False
        self.waiting_toselling_time = 59

class INIT_PARAMS(OTHERSS):
    def __init__(self) -> None:
        super().__init__()
        self.init_itits()

    def init_itits(self):
        print('helloo1')
        self.init_api_key()       
        self.init_urls()   
        self.risk_init()   
        self.others_init()   
        self.init_tg_var()

# params = INIT_PARAMS()
# print(params.test_flag)
# python params_init.py
