from params_init import INIT_PARAMS
import asyncio
import time
from datetime import datetime
import telebot
from telebot import types
import math
import time
import hmac
import hashlib
import requests
# import ccxt

import logging
import os
import inspect
from dotenv import load_dotenv

logging.basicConfig(filename='config_log.log', level=logging.INFO)
current_file = os.path.basename(__file__)

# load_dotenv()

class CONFIG_BINANCE(INIT_PARAMS):

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

        try:            
            response = requests.request(url=url, **kwards)
            return response.json()
        except Exception as ex:
            logging.error(f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")            

        return response

class CONNECTOR_TG(CONFIG_BINANCE):
    def __init__(self):  
        super().__init__()      
        self.bot = telebot.TeleBot(self.tg_api_token)
        self.menu_markup = self.create_menu()
        self.reserved_frathes_list = ["START","GO", "STOP", "DEPO", "LOG", "1", "2", "y", "n"] + [self.seq_control_token]                  

    def create_menu(self):
        menu_markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
        button1 = types.KeyboardButton("GO")
        button2 = types.KeyboardButton("STOP")
        button3 = types.KeyboardButton("DEPO")  
        button4 = types.KeyboardButton("LOG")
        button5 = types.KeyboardButton("START")

        menu_markup.add(button1, button2, button3, button4, button5)        
        return menu_markup
    
class TG_ASSISTENT(CONNECTOR_TG):
    def __init__(self) -> None:
        super().__init__()

    def date_of_the_month(self):        
        current_time = time.time()        
        datetime_object = datetime.fromtimestamp(current_time)       
        formatted_time = datetime_object.strftime('%d')
        return int(formatted_time)   

    def connector_func(self, message, response_message):
        retry_number = 3
        decimal = 1.1       
        for i in range(retry_number):
            try:
                self.bot.send_message(message.chat.id, response_message)                
                return message.text
            except Exception as ex:
                logging.exception(
                    f"An error occurred in file '{current_file}', line {inspect.currentframe().f_lineno}: {ex}")

                time.sleep(1.1 + i*decimal)        
                   
        return None