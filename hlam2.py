# from api_binance import UTILS_API
# import asyncio
# import time
# import logging
# import os
# import inspect
# from dotenv import load_dotenv

# logging.basicConfig(filename='config_log.log', level=logging.INFO)
# current_file = os.path.basename(__file__)

# load_dotenv()

# class LOGICC(UTILS_API):
#     def __init__(self) -> None:
#         super().__init__()

#     # async def write_variable_to_file(self, variable, filename='data_info.txt'):
#     #     try:
#     #         with open(filename, 'w') as file:
#     #             file.write(str(variable))
#     #         print("Variable has been successfully written to the file.")
#     #     except Exception as e:
#     #         print(f"An error occurred: {e}")

#     async def get_current_symbols(self, i):
#         data_info = None
#         symbol = None
#         symbol_list = []

#         try:
#             data_info = await self.get_exchange_info(symbol)           
#             # await self. write_variable_to_file(data_info)

#             # symbol_list = [x['symbol'] for x in data_info['symbols'] if x['symbol'].upper().endswith('USDT') and x['status'] != 'BREAK']
                    
#             symbol_list = [x['symbol'] for x in data_info['symbols'] if x['symbol'].upper().endswith('USDT') and x['status'] != 'BREAK' and x['symbol'] != 'BTCUSDT'] # Test
#             # print(data_info['symbols'][0])

#             # print(f"len_symbols_list: {len(symbol_list)}") 
            
            
#             if i == 3:
#                 symbol_list = symbol_list + ['BTCUSDT'] # Test
            
#         except Exception as ex:
#             logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
#             return 0, []

#         return len(symbol_list), symbol_list

#     async def run_screener(self):
#         print(f"Запускаем run_screener!")        
#         first_iteration_flag = True        
#         start_len_symbol_list, start_symbol_list = 0, []
#         current_len_symbol_list, current_symbol_list = 0, []
#         i = 0 # Test
#         while True:

#             try:
#                 if self.stop_cycle:
#                     return []
#                 i += 1
#                 current_len_symbol_list, current_symbol_list = await self.get_current_symbols(i)
#                 if first_iteration_flag:
#                     first_iteration_flag = False
#                     if current_len_symbol_list != 0:
#                         start_len_symbol_list, start_symbol_list = current_len_symbol_list, current_symbol_list
#                     else:
#                         return []
                    
#                 if current_len_symbol_list > start_len_symbol_list:
#                     start_symbol_set, current_symbol_set = set(start_symbol_list), set(current_symbol_list)
#                     new_coin = list(current_symbol_set - start_symbol_set)
#                     if new_coin:
#                         return new_coin
#                 elif current_len_symbol_list < start_len_symbol_list:
#                     start_len_symbol_list, start_symbol_list = current_len_symbol_list, current_symbol_list

#                 await asyncio.sleep(0.1)
#             except Exception as ex:
#                 logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 
        

#     async def buy_orders_controller(self, new_coin):
#         buy_orders_list = []

#         try:
#             if new_coin:
#                 try:
#                     # print(f"Создаем новый ордер на покупку: символ {symbol}")                      
#                     open_market_order = None
#                     qnt = None
#                     success_flag = False 
#                     depo = self.depo
#                     is_selling = 1                   
#                     qnt, _ = await self.calc_qnt_func(new_coin, depo)
#                     # print(f"{symbol}: item['qnt']: {item['qnt']}")                    
#                     if qnt:                        
#                         open_market_order, success_flag = await self.make_market_order(new_coin, qnt, is_selling)
#                         # print(f"open_market_order:  {open_market_order}") 
#                 except Exception as ex:
#                     logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

#                 return open_market_order, success_flag
                
#         except Exception as ex:
#             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")                    
                    
#         return open_market_order, success_flag       

#     async def sell_orders_controller(self, buy_orders_list):

#         # print(f"sell_orders_controller: {buy_orders_list}")               
        
#         finish_flag = False
#         price_symbol_list = []
#         sell_orders_list = []
#         sell_counter = 0       
#         last_update_time = time.time()
#         seven = 7
                
#         price_symbol_list = [{"symbol": x[0]['symbol'], "qnt": x[0]["executedQty"], "enter_price": float(x[0]['fills'][0]['price']), "cur_price": None, "to_seven_counter": 0, "price_history_list": [], "max_price": 0, "in_condition": False, "in_closing": False} for x in buy_orders_list if x[1]]
            
#         while True:
#             if price_symbol_list:
#                 current_time = time.time()
#                 if (current_time - last_update_time)/self.INTERVAL_CLOSEPRICE_MONITORING >= 1:
#                 if not finish_flag:
#                     for i, x in enumerate(price_symbol_list):
#                         try:
#                             if not price_symbol_list[i]["in_condition"]:
#                                 percentage_x = None
#                                 tp_condition_1 = False
#                                 tp_condition_2 = False
#                                 symbol, enter_price = x["symbol"], x["enter_price"]
#                                 price_symbol_list[i]["cur_price"] = await self.get_current_price(symbol)
#                                 # percentage_x = (price_symbol_list[i]["cur_price"] - x["enter_price"]) / x["enter_price"]
#                                 # price_symbol_list[i]["price_history_list"].append(price_symbol_list[i]["cur_price"])
#                                 # price_symbol_list[i]["max_price"] = max(price_symbol_list[i]["price_history_list"])

#                                 # print(f'price_symbol_list[i]["price_history_list"]: {price_symbol_list[i]["price_history_list"]}')

#                                 # print(f'price_symbol_list[i]["max_price"]: {price_symbol_list[i]["max_price"]}')
                                
#                                 # print(f"to_seven_counter: {price_symbol_list[i]['to_seven_counter']}")
#                                 if price_symbol_list[i]["to_seven_counter"] >= 7:  

#                                     try:
#                                         tp_condition_1 = ((price_symbol_list[i]["max_price"] - price_symbol_list[i]["cur_price"])/(price_symbol_list[i]["max_price"] - enter_price)) * 100 >= 7
#                                     except:
#                                         pass
                                        
#                                     tp_condition_2 = percentage_x >= self.x_percentage_ceiling

#                                     tp_condition_2 = True # Test
                                        
#                                 else:
#                                     price_symbol_list[i]["to_seven_counter"] += 1

#                                 if tp_condition_1 or tp_condition_2:
#                                     price_symbol_list[i]["in_condition"] = True
                                    
#                                     async with self.buy_sell_tumbler:

#                                         try:
#                                             open_market_order = None                                            
#                                             success_flag = False
#                                             qnt = x['qnt']                                   
#                                             is_selling = -1                                        
                                            
#                                             open_market_order, success_flag = await self.make_market_order(symbol, qnt, is_selling)
#                                             # print(f"open_market_order:  {open_market_order}") 
#                                         except Exception as ex:
#                                             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

#                                         sell_orders_list.append((open_market_order, success_flag))
#                                     if success_flag:
#                                         price_symbol_list[i]["in_closing"] = True
#                                     sell_counter += 1
#                                 if sell_counter == len(price_symbol_list):
#                                     finish_flag = True
#                                 # await asyncio.sleep(0.1)
#                         except Exception as ex:
#                             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
                
#                 else:
#                     return sell_orders_list
#             else:
#                 return []

#             if not self.stop_cycle:                
#                 await asyncio.sleep()
#             else:
#                 return sell_orders_list


#     async def main_controller(self, message):
#         return_run_screener = None  
#         return_sell_orders_controller = None 
#         in_run_screener = False
#         first_cycle = False # Test
#         sell_controller_tasks = []
#         buy_orders_list = []        
#         sell_orders_list = []   
#         total_sell_orders_list = []
#         new_coins_list = []
#         simafor_list = [0]     

#         while True:        
#             try:
#                 # print(f"simafor_list:{simafor_list}")                        
#                 if sell_controller_tasks:
#                     if any(task.done() for task in sell_controller_tasks):
#                         sell_orders_list = [task for task in sell_controller_tasks if task.done()][0]
#                         sell_orders_list = sell_orders_list.result()                        
#                         sell_controller_tasks = [task for task in sell_controller_tasks if not task.done()]
                                                
#                         try:
#                             if any(x[1] for x in sell_orders_list):                                
#                                 if sell_orders_list:
#                                     total_sell_orders_list += sell_orders_list
#                                     print(f"sell_orders_list: {total_sell_orders_list}")   
#                                     response_message = f"SELL ORDERS: {sell_orders_list}"
#                                     message.text = self.connector_func(message, response_message)               
#                                 print("Что-то получилось! Проверь результаты!")
#                         except Exception as ex:
#                             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

#                     if all(task.done() for task in sell_controller_tasks):
#                         response_message = "All sell_controller_tasks completed!"
#                         message.text = self.connector_func(message, response_message)  
#                         print("All sell_controller_tasks completed!")
#                         if not in_run_screener:
#                             simafor_list.append(0) 
#                         sell_controller_tasks = []

#                 await asyncio.sleep(0.01)  
#                 if self.stop_cycle:
#                     continue
#             except Exception as ex:
#                 logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
            
#             try:
#                 if 0 in simafor_list and not first_cycle: # Test
#                 # if 0 in simafor_list:                    
#                     simafor_list = [x for x in simafor_list if x != 0]
#                     return_run_screener = asyncio.create_task(self.run_screener())
#                     in_run_screener = True

#                 if return_run_screener and return_run_screener.done():
#                     new_coins_list = return_run_screener.result()
#                     in_run_screener = False
#                     first_cycle = True # Test
                  
#                     print(f"new listing: {new_coins_list}")
#                     return_run_screener = None
#                     if new_coins_list:
#                         response_message = f"new listing: {new_coins_list}"
#                         message.text = self.connector_func(message, response_message)
#                         simafor_list.append(1)    
#                         print(f"simafor_list:{simafor_list}")    

#                 if 1 in simafor_list:                        
#                     simafor_list = [x for x in simafor_list if x != 1]     
#                     # print('skdjvbskfvbk')             
#                     async with self.buy_sell_tumbler:
#                         buy_orders_list = await self.buy_orders_controller(new_coins_list)
#                         new_coins_list = []
#                         if buy_orders_list:
#                             response_message = f"BUY ORDERS: {buy_orders_list}"
#                             message.text = self.connector_func(message, response_message)
#                             simafor_list.append(2)
#                             if not in_run_screener:
#                                 simafor_list.append(0)   
#                         else:
#                             print("Some problems with returning buy_orders_list")                         

#                 if 2 in simafor_list:
#                     print("2 in simafor_list")
#                     try:
#                         simafor_list = [x for x in simafor_list if x != 2]
#                         if any(x[1] for x in buy_orders_list):                            
#                             print(f"buy_orders_list: {buy_orders_list}")                                                         
#                             return_sell_orders_controller = asyncio.create_task(self.sell_orders_controller(buy_orders_list))
#                             buy_orders_list = []
#                             sell_controller_tasks.append(return_sell_orders_controller)
                                
#                     except Exception as ex:
#                         logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

#             except Exception as ex:
#                 logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
    
#             await asyncio.sleep(1)
#             print('Tik')

