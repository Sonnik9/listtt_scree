from api_binance import UTILS_API
import asyncio
import time
import logging
import os
import inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

load_dotenv()

money_emoji = "💰"
rocket_emoji = "🚀"
lightning_emoji =  "⚡"
clock_emoji = "⌚"
film_emoji = "📼"
percent_emoji = "📶"
repeat_emoji = "🔁"
upper_trigon_emoji = "🔼"
lower_trigon_emoji = "🔽"
confirm_emoji = "✅"
link_emoji = "🔗"


class LOGICC(UTILS_API):
    def __init__(self) -> None:
        super().__init__()

    async def get_current_symbols(self):
        data_info = None
        symbol = None
        symbol_list = []

        try:
            data_info = await self.get_exchange_info(symbol)           
            symbol_list = [x['symbol'] for x in data_info['symbols'] if x['symbol'].upper().endswith('USDT') and x['status'] != 'BREAK']
                    
            # symbol_list = [x['symbol'] for x in data_info['symbols'] if x['symbol'].upper().endswith('USDT') and x['status'] != 'BREAK' and x['symbol'] != 'BTCUSDT'] # Test
           
            # if i == 2:
            #     symbol_list = symbol_list + ['BTCUSDT'] # Test
            
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
            return 0, []

        return len(symbol_list), symbol_list

    async def run_screener(self):
        print(f"Запускаем run_screener!")        
        first_iteration_flag = True        
        start_len_symbol_list, start_symbol_list = 0, []
        current_len_symbol_list, current_symbol_list = 0, []
        # i = 0 # Test
        while True:

            try:
                if self.stop_cycle:
                    return "The run_screener was stoped"
                # i += 1
                current_len_symbol_list, current_symbol_list = await self.get_current_symbols()
                if first_iteration_flag:
                    first_iteration_flag = False
                    if current_len_symbol_list != 0:
                        start_len_symbol_list, start_symbol_list = current_len_symbol_list, current_symbol_list
                    else:
                        return None
                    
                if current_len_symbol_list > start_len_symbol_list:
                    start_symbol_set, current_symbol_set = set(start_symbol_list), set(current_symbol_list)
                    new_coin = list(current_symbol_set - start_symbol_set)
                    if new_coin:
                        return new_coin[0]
                elif current_len_symbol_list < start_len_symbol_list:
                    start_len_symbol_list, start_symbol_list = current_len_symbol_list, current_symbol_list

                await asyncio.sleep(0.5)
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
                return "Some problems with run_screener..."
        

    async def buy_orders_controller(self, new_coin):

        for i in range(1):
            try:
                buy_market_order = None
                success_flag = False 
                if i == 0:
                    qnt = self.qnt   
                else:
                    qnt = None                    
                    qnt, _ = await self.calc_qnt_func(new_coin, self.depo)
                    # print(f"qnt: {qnt}")

                buy_market_order, success_flag = await self.make_market_order(new_coin, qnt, side='BUY')
                if success_flag:
                    return buy_market_order
                    
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")  

        return None   

    async def sell_orders_controller(self, buy_orders_dict):

        sell_market_order = None 
        symbol = None
        qnt = None
        # tp_condition_1 = False    
        # tp_condition_2 = False   
        success_flag = False     
        last_update_time = time.time()

        while True:
            try:                
                current_time = time.time()
                if (current_time - last_update_time)/self.waiting_toselling_time >= 1:

                    symbol = buy_orders_dict['symbol']        
                    qnt = buy_orders_dict["executedQty"]                                                            

                    sell_market_order, success_flag = await self.make_market_order(symbol, qnt, side='SELL')
                    if success_flag:
                        return sell_market_order
                    else:
                        return None
               
                await asyncio.sleep(1)
                
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
                return None


    async def main_controller(self, message):
        new_coin = None
        buy_orders_dict = None
        sell_orders_dict = None
        first_cycle = False # Test         

        while True:     

            try:
                if not first_cycle: # Test
                    first_cycle = True               
                    new_coin = await self.run_screener()
                    if new_coin:
                        # print(f"new_coin: {new_coin}")
                        buy_orders_dict = await self.buy_orders_controller(new_coin)
                        # response_message = f"BUY ORDER:\n\n{buy_orders_dict}"
                        # message.text = self.connector_func(message, response_message)
                        if buy_orders_dict:
                            if self.is_make_sell_logic_flag:
                                sell_orders_dict = await self.sell_orders_controller(buy_orders_dict)
                                if sell_orders_dict:
                                    response_message = f"SELL ORDER:\n\n{sell_orders_dict}"                                
                                else:
                                    response_message = "Some problems with SELL order..."
                            else:
                                response_message = f"BUY ORDER:\n\n{buy_orders_dict}" + '\n\n' + "Please go into your trading terminal for contlolling sell logic!"

                        else:
                            response_message = "Some problems with BUY order..."
                        message.text = self.connector_func(message, response_message)

                    else: 
                        response_message = new_coin                       
                        message.text = self.connector_func(message, response_message)

                else:
                    response_message = f"Something like this)"
                    message.text = self.connector_func(message, response_message)
                    return

            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
    
            await asyncio.sleep(1)
            # print('Tik')

                
class TG_MANAGER(LOGICC):
    def __init__(self):
        super().__init__()

    def run(self):  
        try:          
            @self.bot.message_handler(commands=['start'])
            @self.bot.message_handler(func=lambda message: message.text == 'START')
            def handle_start_input(message):
                if self.block_acess_flag:
                    response_message = "Don't bullshit!"
                    message.text = self.connector_func(message, response_message)
                else:
                    # print(int('adrjg,'))
                    self.init_itits() 
                    self.start_day_date = self.date_of_the_month()          
                    self.bot.send_message(message.chat.id, "Please enter a secret token...", reply_markup=self.menu_markup)                   
                    self.start_flag = True

            @self.bot.message_handler(func=lambda message: self.start_flag)
            def handle_start_redirect(message):
                # print('skfjvsfjk')
                try:
                    cur_day_date = None                    
                    value_token = message.text.strip()
                    # print(value_token)
                    cur_day_date = self.date_of_the_month()
                    # print(cur_day_date)
                    # print(self.start_day_date)

                    if self.start_day_date != cur_day_date:
                        self.start_day_date = cur_day_date
                        self.block_acess_flag = False 
                        self.block_acess_counter = 0

                    if value_token == self.seq_control_token and not self.block_acess_flag:
                        self.seq_control_flag = True 
                        # print(self.seq_control_flag)
            
                        response_message = "Token verification was successful! Please select an option!"
                        message.text = self.connector_func(message, response_message)  
                        self.start_flag = False        

                            
                    elif value_token != self.seq_control_token and not self.block_acess_flag:
                        self.dont_seq_control = True
                        # print(self.dont_seq_control)
        
                        self.block_acess_counter += 1
                        if self.block_acess_counter >= 3:
                            self.block_acess_flag = True
                            self.start_flag = False 
                            response_message = "The number of attempts has been exhausted. Please try again later..."
                            message.text = self.connector_func(message, response_message)
                        else:
                            response_message = "Please put a valid token!"
                            message.text = self.connector_func(message, response_message)

                    else:
                        print('something else...')
                except Exception as ex:
                    logging.exception(
                        f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")  
            # ////////////////////////////////////////////////////////////////////////////////////////////////
            
            @self.bot.message_handler(func=lambda message: message.text == 'GO' and self.seq_control_flag and not self.block_acess_flag)
            def handle_go(message): 
                response_message = "Please waiting"
                message.text = self.connector_func(message, response_message)  
                zdlfkn = asyncio.run(self.main_controller(message))
                stop_messege = 'Run screener was stoped'
                message.text = self.connector_func(message, stop_messege)
            @self.bot.message_handler(func=lambda message: message.text == 'STOP' and self.seq_control_flag and not self.block_acess_flag)
            def handle_stop(message): 
                self.stop_cycle = True

            @self.bot.message_handler(func=lambda message: message.text == 'DEPO' and self.seq_control_flag and not self.block_acess_flag)
            def handle_depo(message): 
                try: 
                    response_message = "Please enter depo (e.g: 50usdt) or (e.g: 0.001btc)"
                    message.text = self.connector_func(message, response_message)  
                    self.depo_redirect_flag = True    
                except Exception as ex:
                    logging.exception(
                        f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

            @self.bot.message_handler(func=lambda message: self.depo_redirect_flag)
            def handle_depo_redirect(message): 
                try: 
                    self.depo = message.text.strip()
                    response_message = f"Depo was chenged on {self.depo}"
                    message.text = self.connector_func(message, response_message)  
                    self.depo_redirect_flag = False  
                except Exception as ex:
                    logging.exception(
                        f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
           
           
            @self.bot.message_handler(func=lambda message: message.text == 'LOG' and self.seq_control_flag and not self.block_acess_flag)
            def handle_log(message): 
                try:
                    response_message = "Please check file 'config_log.log' in your workspace directori!"
                    message.text = self.connector_func(message, response_message)
                except Exception as ex:
                    logging.exception(
                        f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")


                    
# //////////////////////////////////////////////////////////////////////////////////////////////////////////

            @self.bot.message_handler(func=lambda message: not self.seq_control_flag and (message.text == 'GO' or message.text == 'STOP' or message.text == 'DEPO' or message.text == 'LOG'))
            def handle_seqq(message): 
                try:
                    response_message = "Please tab START and put a valid token!"
                    message.text = self.connector_func(message, response_message)
                except Exception as ex:
                    logging.exception(
                        f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////

            self.bot.polling()
        except Exception as ex:
            logging.exception(
                f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")                   

def main():
    my_bot = TG_MANAGER()
    my_bot.run()

if __name__=="__main__":
    main()
