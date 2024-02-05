# # import requests
# # import time

# # api_key = "vPlx4lmDIcgMT6QcUhvW0yoNHgXawtKQrqmwOgCEneoNtRbe9JmT1qVdo1WUZjAr" # real
# # secret_key = "lll0IA6Gyqf2vn2qijISrzjf5ru99Z6hbnFE20SJxP1kIKr5czyHxPJeYnlHSzwE" # real
# # base_url = 'https://api.binance.com/api/v3'

# # def get_upcoming_listings():
# #     coins_candidate_list = []
# #     coins_candidateInfo_list = []
# #     endpoint = '/exchangeInfo'    
# #     url = f'{base_url}{endpoint}'

# #     try:
# #         response = requests.get(url)
# #         data = response.json()

# #         for i, symbol_info in enumerate(data['symbols']):
# #             symbol = symbol_info['symbol']
            
# #             if (symbol_info['status'] != 'TRADING' and symbol_info['status'] != 'BREAK') or symbol_info['status'] == 'PRE_TRADING':
# #                 # coins_candidate_list.append(symbol)
# #                 coins_candidateInfo_list.append(symbol_info)

# #         print(f"Обнаружено {len(coins_candidateInfo_list)} новых монета в предстоящем листинге!")
# #         print(f"Например: {coins_candidateInfo_list[0]['symbol']}: {coins_candidateInfo_list[0]}")

        

# #     except Exception as e:
# #         print(f"Произошла ошибка: {e}")

# # if __name__ == "__main__":
# #     get_upcoming_listings()
    


# # max_price = 0.872
# # cur_price = 0.621
# # enter_price = 0.03

# # max_price = 0.58
# # cur_price = 0.4863
# # enter_price = 0.371

# # # per_change = 100 - ((cur_price*100)/(max_price - enter_price))
# # # per_change_2 = (1 - (cur_price/max_price)) * 100
# # # per_change_3 = ((max_price - cur_price)/max_price)*100
# # per_change_4 = ((max_price - cur_price)/(max_price - enter_price))*100
# # # print(per_change)
# # # print(per_change_2)
# # # print(per_change_3)
# # print(per_change_4)
# # # 





# # https://binance-docs.github.io/apidocs/spot/en/#exchange-information 19
# # https://binance-docs.github.io/apidocs/websocket_api/en/#exchange-information 19



# # {'symbol': 'ETHBTC', 'status': 'TRADING', 'baseAsset': 'ETH', 'baseAssetPrecision': 8, 'quoteAsset': 'BTC', 'quotePrecision': 8, 'quoteAssetPrecision': 8, 'baseCommissionPrecision': 8, 'quoteCommissionPrecision': 8, 'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT'], 'icebergAllowed': True, 'ocoAllowed': True, 'quoteOrderQtyMarketAllowed': True, 'allowTrailingStop': True, 'cancelReplaceAllowed': True, 'isSpotTradingAllowed': True, 'isMarginTradingAllowed': True, 'filters': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.00001000', 'maxPrice': '922327.00000000', 'tickSize': '0.00001000'}, {'filterType': 'LOT_SIZE', 'minQty': '0.00010000', 'maxQty': '100000.00000000', 'stepSize': '0.00010000'}, {'filterType': 'ICEBERG_PARTS', 'limit': 10}, {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '2496.76429246', 'stepSize': '0.00000000'}, {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000, 'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000}, {'filterType': 'PERCENT_PRICE_BY_SIDE', 'bidMultiplierUp': '5', 'bidMultiplierDown': '0.2', 'askMultiplierUp': '5', 'askMultiplierDown': '0.2', 'avgPriceMins': 5}, {'filterType': 'NOTIONAL', 'minNotional': '0.00010000', 'applyMinToMarket': True, 'maxNotional': '9000000.00000000', 'applyMaxToMarket': False, 'avgPriceMins': 5}, {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}], 'permissions': ['SPOT', 'MARGIN', 'TRD_GRP_004', 'TRD_GRP_005', 'TRD_GRP_006', 'TRD_GRP_008', 'TRD_GRP_009', 'TRD_GRP_010', 'TRD_GRP_011', 'TRD_GRP_012', 'TRD_GRP_013', 'TRD_GRP_014', 'TRD_GRP_015', 'TRD_GRP_016', 'TRD_GRP_017', 'TRD_GRP_018', 'TRD_GRP_019', 'TRD_GRP_020', 'TRD_GRP_021', 'TRD_GRP_022', 'TRD_GRP_023', 'TRD_GRP_024', 'TRD_GRP_025'], 'defaultSelfTradePreventionMode': 'EXPIRE_MAKER', 'allowedSelfTradePreventionModes': ['EXPIRE_TAKER', 'EXPIRE_MAKER', 'EXPIRE_BOTH']}

# # import time

# # buy_orders_list = []

# # def market_order_temp_func():
# #     return 2

# # for _ in range(3):
# #     buy_orders_list.append(market_order_temp_func())
# #     time.sleep(1)

# # print(buy_orders_list)


# import asyncio
# import random

# class YourClass:
#     def __init__(self):
#         self.buy_sell_tumbler = asyncio.Lock()
#         self.shared_variable = None  # Общая переменная для хранения результата run_screener

#     async def run_screener(self):
#         # Ваш код для run_screener
#         await asyncio.sleep(4)
#         # print('fvjksfjkfvjkfvjkfjk')

#         return [random.randrange(0,10)]

#     async def buy_orders_controller(self, asklfjvn):
#         # Ваш код для buy_orders_controller
#         print('buy_orders_controller')
#         await asyncio.sleep(1)
#         return [(random.randrange(0,10),"buy"), (random.randrange(0,10),"buy")]

#     async def sell_orders_controller(self, asflvjn):
#         # Ваш код для sell_orders_controller
#         print('sell_orders_controller')
#         await asyncio.sleep(11)
#         return [(random.randrange(0,10),"sell"), (random.randrange(0,10),"sell")]

#     async def main_controller(self):
#         tasks = []
#         buy_orders_list = []
#         sell_orders_list = []    
#         total_sell_orders_list = []
#         simafor_list = [0]        

#         return_run_screener = None  
#         return_sell_orders_controller = None      
#         new_coins_list = []

#         async def producer():
#             nonlocal simafor_list, new_coins_list
#             while True:
#                 # print('k<sdfjbv')
#                 print(f"simafor_list: {simafor_list}")
#                 try:
#                     if 0 in simafor_list:
#                         simafor_list.remove(0)
#                         self.shared_variable = await self.run_screener()
#                         if self.shared_variable:
#                             simafor_list.append(1)
#                             print(f"new_coins_list: {self.shared_variable}")
                    
#                 except Exception as ex:
#                     print(ex)

#                 await asyncio.sleep(1)

#         async def consumer_buy():
#             nonlocal simafor_list, buy_orders_list
#             while True:
#                 try:
#                     if 1 in simafor_list:
#                         simafor_list.remove(1)                    
#                         async with self.buy_sell_tumbler:
#                             buy_orders_list = await self.buy_orders_controller(self.shared_variable)
#                             self.shared_variable = []
#                             if buy_orders_list:
#                                 simafor_list.extend([0, 2])
#                                 # print(f"buy_orders_list: {buy_orders_list}")
                        
#                 except Exception as ex:
#                     print(ex)
#                 await asyncio.sleep(1)

#         async def consumer_sell():
#             nonlocal simafor_list, buy_orders_list, sell_orders_list, total_sell_orders_list
#             while True:
#                 try:
#                     if 2 in simafor_list:
#                         simafor_list.remove(2)
#                         if any(x[1] for x in buy_orders_list):   
#                             print(f"buy_orders_list: {buy_orders_list}")                           
#                             sell_orders_list = await self.sell_orders_controller(buy_orders_list)
#                             if sell_orders_list:
#                                 total_sell_orders_list += sell_orders_list
#                                 print(f"sell_orders_list: {total_sell_orders_list}")
#                 except Exception as ex:
#                     print(ex)
#                 await asyncio.sleep(1)

#         producer_task = asyncio.create_task(producer())
#         consumer_buy_task = asyncio.create_task(consumer_buy())
#         consumer_sell_task = asyncio.create_task(consumer_sell())

#         await asyncio.gather(producer_task, asyncio.sleep(3), consumer_buy_task, consumer_sell_task)
#         await consumer_buy_task
#         await consumer_sell_task

# asyncio.run(YourClass().main_controller())



import asyncio
import random
import logging
import os
import inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

class YourClass:
    def __init__(self):
        self.buy_sell_tumbler = asyncio.Lock()
        self.stop_triger = False

    async def run_screener(self):
        # Ваш код для run_screener
        await asyncio.sleep(4)
        # print('fvjksfjkfvjkfvjkfjk')

        return [random.randrange(0,10)]

    async def buy_orders_controller(self, asklfjvn):
        # Ваш код для buy_orders_controller
        print('buy_orders_controller')
        await asyncio.sleep(1)
        return [(random.randrange(0,10),"buy"), (random.randrange(0,10),"buy")]

    async def sell_orders_controller(self, asflvjn):
        # Ваш код для sell_orders_controller
        self.counter += 1
        print('sell_orders_controller')
        await asyncio.sleep(11)
        return [(random.randrange(0,10),"sell"), (random.randrange(0,10),"sell")]
    
    async def main_controller(self):
        sell_controller_tasks = []
        buy_orders_list = []
        
        sell_orders_list = []   
        total_sell_orders_list = [] 

        simafor_list = [0]     
        in_run_screener = False 

        return_run_screener = None  
        return_sell_orders_controller = None      
        new_coins_list = []

        while True:
        
            try:                        
                if sell_controller_tasks:
                    if any(task.done() for task in sell_controller_tasks):
                        sell_orders_list = [task for task in sell_controller_tasks if task.done()][0]
                        sell_orders_list = sell_orders_list.result()
                        # print(sell_orders_list)
                        sell_controller_tasks = [task for task in sell_controller_tasks if not task.done()]
                        # print(sell_controller_tasks)
                        
                        try:
                            if any(x[1] for x in sell_orders_list):                                
                                if sell_orders_list:
                                    total_sell_orders_list += sell_orders_list
                                    print(f"sell_orders_list: {total_sell_orders_list}")                  
                                print("Что-то получилось! Проверь результаты!")
                        except Exception as ex:
                            logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

                    if all(task.done() for task in sell_controller_tasks):
                        print("All tasks completed")
                        if not in_run_screener:
                            simafor_list.append(0) 
                        sell_controller_tasks = []

                await asyncio.sleep(0.01)  
                if self.counter == 3:
                    continue
            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
            
            try:
                if 0 in simafor_list:                    
                    simafor_list = [x for x in simafor_list if x != 0]
                    return_run_screener = asyncio.create_task(self.run_screener())
                    in_run_screener = True

                if return_run_screener and return_run_screener.done():
                    new_coins_list = return_run_screener.result()
                    in_run_screener = False
                  
                    print(f"new_coins_list: {new_coins_list}")
                    return_run_screener = None
                    if new_coins_list:
                        simafor_list.append(1)        

                if 1 in simafor_list:                        
                    simafor_list = [x for x in simafor_list if x != 1]                  
                    async with self.buy_sell_tumbler:
                        buy_orders_list = await self.buy_orders_controller(new_coins_list)
                        new_coins_list = []
                        if buy_orders_list:
                            simafor_list.append(2)
                            if not in_run_screener:
                                simafor_list.append(0)                            

                if 2 in simafor_list:
                    try:
                        simafor_list = [x for x in simafor_list if x != 2]
                        if any(x[1] for x in buy_orders_list): 
                            async with self.buy_sell_tumbler:
                                print(f"buy_orders_list: {buy_orders_list}")                    
                                buy_orders_list = []                               
                                return_sell_orders_controller = asyncio.create_task(self.sell_orders_controller(buy_orders_list))
                                sell_controller_tasks.append(return_sell_orders_controller)
                                
                    except Exception as ex:
                        logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

            except Exception as ex:
                logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
    
            await asyncio.sleep(2)
            print('Tik')

asyncio.run(YourClass().main_controller())

# import asyncio

# async def task1():
#     print("Task 1 started")
#     await asyncio.sleep(2)
#     print("Task 1 completed")
#     return 'first'

# async def task2():
#     print("Task 2 started")
#     await asyncio.sleep(1)
#     print("Task 2 completed")
#     return 'sec'

# async def task3():
#     print("Task 3 started")
#     await asyncio.sleep(3)
#     print("Task 3 completed")
#     return 'thrd'

# async def main():
#     first_flag = True
#     tasks = []
#     while True:
#         if first_flag:
#             first_flag = False
#             # Создаем задачи, используя asyncio.create_task
#             task1_instance = asyncio.create_task(task1())
#             task2_instance = asyncio.create_task(task2())
#             task3_instance = asyncio.create_task(task3())
#             tasks.append(task1_instance)
#             tasks.append(task2_instance)
#             tasks.append(task3_instance)

#         # Ждем завершения хотя бы одной задачи
#         done, _ = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

#         for task in done:
#             task_instance = task.result()
#             print(f"{task_instance} completed")

#         # Если все задачи завершены, выходим из цикла
#         if all(task.done() for task in [task1_instance, task2_instance, task3_instance]):
#             print("All tasks completed")
#             tasks = []
#             first_flag = True

#         await asyncio.sleep(1)
#         print('Tik')

# # Запускаем основную программу
# asyncio.run(main())

