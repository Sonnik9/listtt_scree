from api_binance import UTILS_API
import asyncio
import logging
import os
import inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

class MAINN(UTILS_API):
    def __init__(self) -> None:
        super().__init__()

    async def get_current_symbols(self):
        data_info = None
        symbol_list = []

        try:
            data_info = await self.get_exchange_info()            
            symbol_list = [x['symbol'] for x in data_info['symbols'] if x['symbol'].upper().endswith('USDT') and x['status'] != 'BREAK']
            # print(data_info['symbols'][0])
            print(f"symbols_list: {len(symbol_list)}")
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
            return 0, []

        return len(symbol_list), symbol_list

    async def run_screener(self):
        print(f"Запускаем run_screener!")        
        first_iteration_flag = True        
        start_len_symbol_list, start_symbol_list = 0, []
        current_len_symbol_list, current_symbol_list = 0, []
        while True:
            try:
                current_len_symbol_list, current_symbol_list = await self.get_current_symbols()
                if first_iteration_flag:
                    first_iteration_flag = False
                    if current_len_symbol_list != 0:
                        start_len_symbol_list, start_symbol_list = current_len_symbol_list, current_symbol_list
                    else:
                        return []
                    
                elif current_len_symbol_list > start_len_symbol_list:
                    start_symbol_set, current_symbol_set = set(start_symbol_list), set(current_symbol_list)
                    coins_candidate_list = list(current_symbol_set - start_symbol_set)
                    if coins_candidate_list:
                        return coins_candidate_list
                elif current_len_symbol_list < start_len_symbol_list:
                    start_len_symbol_list, start_symbol_list = current_len_symbol_list, current_symbol_list

                await asyncio.sleep(10)
            except Exception as ex:
                logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
        

    async def buy_orders_controller(self, new_coins_list, is_selling):
        new_coins_list = None
        buy_orders_list = []

        if new_coins_list:
            for symbol in new_coins_list:
                print(f"Создаем новый ордер на покупку: символ {symbol}")
                buy_orders_list.append(await self.market_order_temp_func(symbol, is_selling, depo = None))                    
                await asyncio.sleep(1)
        return buy_orders_list        

    async def sell_orders_controller(self, buy_orders_list):
        price_symbol_list = []
        tp_condition_1 = False
        tp_condition_2 = False
        sell_counter = 0
        finish_flag = False
        sell_orders_list = []
        price_symbol_list = [{"symbol": x[0]['symbol'], "enter_price": float(x[0]['fills'][0]['price']), "cur_price": None, "price_history_list": [], "max_price": 0, "in_closing": False} for x in buy_orders_list if x[1]]
            
        while True:
            if not finish_flag:
                for i, x in enumerate(price_symbol_list):
                    if not price_symbol_list[i]["in_closing"]:
                        symbol, enter_price = x["symbol"], x["enter_price"]
                        price_symbol_list[i]["cur_price"] = await self.get_current_price(symbol)
                        price_symbol_list[i]["price_history_list"].append(price_symbol_list[i]["cur_price"])
                        price_symbol_list[i]["max_price"] = max(price_symbol_list[i]["price_history_list"])
                        
                        if ((price_symbol_list[i]["max_price"] - price_symbol_list[i]["cur_price"])/(price_symbol_list[i]["max_price"] - enter_price)) * 100 >= 7:
                            tp_condition_1 = True
                        if price_symbol_list[i]["cur_price"] >= enter_price * 49:
                            tp_condition_2 = True
                        if tp_condition_1 or tp_condition_2:
                            is_selling = -1
                            async with self.buy_sell_tumbler:
                                sell_orders_list.append(await self.market_order_temp_func(symbol, is_selling, depo=None))
                            price_symbol_list[i]["in_closing"] = True
                            sell_counter += 1
                        if sell_counter == len(price_symbol_list):
                            finish_flag = True
                        await asyncio.sleep(1)
            else:
                return sell_orders_list
            
            await asyncio.sleep(7)

    async def main_controller(self):
        tasks = []
        buy_orders_list = []
        sell_orders_list = []        
        in_run_screener_flag = False
        in_buy_orders_controller_flag = False
        in_sell_orders_controller_flag = False
        return_run_screener = None  
        return_sell_orders_controller = None      
        new_coins_list = []
        while True:
            if not in_run_screener_flag:
                in_run_screener_flag = True
                task1 = [self.run_screener()]
                tasks.append(task1)
                return_run_screener = asyncio.gather(*task1)

            if return_run_screener and return_run_screener.done():
                result_run_screener = return_run_screener.result()
                new_coins_list = result_run_screener[0]
                return_run_screener = None
                in_buy_orders_controller_flag = False

            if new_coins_list:
                if not in_buy_orders_controller_flag:
                    in_buy_orders_controller_flag = True
                    is_selling = 1
                    async with self.buy_sell_tumbler:
                        buy_orders_list = await self.buy_orders_controller(new_coins_list, is_selling)
                        new_coins_list = []

            if not in_sell_orders_controller_flag and buy_orders_list:
                try:
                    if any(x[1] for x in buy_orders_list):                              
                        task2 = [self.sell_orders_controller(buy_orders_list)]
                        buy_orders_list = []
                        tasks.append(task2)
                        return_sell_orders_controller = asyncio.gather(*task2)
                        in_run_screener_flag = False
                        in_sell_orders_controller_flag = True
                except Exception as ex:
                    print(ex)

            if return_sell_orders_controller and return_sell_orders_controller.done():
                result_sell_orders_controller = return_sell_orders_controller.result()
                sell_orders_list = result_sell_orders_controller[0]
                return_sell_orders_controller = None
                if any(x[1] for x in sell_orders_list):
                    in_sell_orders_controller_flag = False
                    print("Что-то получилось! Проверь результаты!")

            await asyncio.sleep(2)
            print('Tik')

if __name__ == "__main__":    
    mainnn = MAINN()
    asyncio.run(mainnn.main_controller())
