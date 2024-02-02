# start_list = [1,2,3,4,5,6,7,8,9]
# cur_list = [1,2,3,4,5,6,7,8,9,10]
# start_list_set = set(start_list)
# cur_list_set = set(cur_list)

# if len(cur_list_set) > len(start_list_set):

#     new_coin = cur_list_set - start_list_set 
#     print(list(new_coin))



# import asyncio
# import aiohttp
# import json
# import time
# import random
# from datetime import datetime
# import logging, os, inspect

# logging.basicConfig(filename='config_log.log', level=logging.INFO)
# current_file = os.path.basename(__file__)

# class LIVE_MONITORING():

#     def __init__(self) -> None:
#         super().__init__()

#     async def websocket_handler(self):
#         url = 'wss://stream.binance.com:9443/stream?streams='  
#         # stream = f"{symbol.lower()}@kline_1s" 
#         stream = "option_pair"


#         try:
#             while True:
#                 print('hello')
#                 ws = None   

#                 try:
#                     async with aiohttp.ClientSession() as session:
#                         async with session.ws_connect(url) as ws:
#                             subscribe_request = {
#                                 "method": "SUBSCRIBE",
#                                 "params": [stream],
#                                 "id": random.randrange(11, 111111)
#                             }

#                             try:
#                                 data_prep = await ws.send_json(subscribe_request)
#                             except Exception as ex:
#                                 logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}") 

#                             async for msg in ws:
#                                 if msg.type == aiohttp.WSMsgType.TEXT:
#                                     try:
#                                         data = json.loads(msg.data)   
#                                         print(data)                                     
#                                         # symbol = data.get('data', {}).get('s')    
                                    
#                                     except Exception as ex:
#                                         logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
#                                         await asyncio.sleep(1)
#                                         continue
#                             await asyncio.sleep(1)
#                             continue
#                 except Exception as ex:
#                     logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
#                     await asyncio.sleep(7)
#                     continue
#         except Exception as ex:
#             logging.exception(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")
#         finally:
#             if ws and not ws.closed:
#                 await ws.close()
#             await asyncio.sleep(1)  
            
#             return True

# live_monitor = LIVE_MONITORING()     
# upgraded_data = asyncio.run(live_monitor.websocket_handler())
# # print(upgraded_data)

# python monitoringg.pys