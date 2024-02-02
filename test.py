# import requests
# import time

# api_key = "vPlx4lmDIcgMT6QcUhvW0yoNHgXawtKQrqmwOgCEneoNtRbe9JmT1qVdo1WUZjAr" # real
# secret_key = "lll0IA6Gyqf2vn2qijISrzjf5ru99Z6hbnFE20SJxP1kIKr5czyHxPJeYnlHSzwE" # real
# base_url = 'https://api.binance.com/api/v3'

# def get_upcoming_listings():
#     coins_candidate_list = []
#     coins_candidateInfo_list = []
#     endpoint = '/exchangeInfo'    
#     url = f'{base_url}{endpoint}'

#     try:
#         response = requests.get(url)
#         data = response.json()

#         for i, symbol_info in enumerate(data['symbols']):
#             symbol = symbol_info['symbol']
            
#             if (symbol_info['status'] != 'TRADING' and symbol_info['status'] != 'BREAK') or symbol_info['status'] == 'PRE_TRADING':
#                 # coins_candidate_list.append(symbol)
#                 coins_candidateInfo_list.append(symbol_info)

#         print(f"Обнаружено {len(coins_candidateInfo_list)} новых монета в предстоящем листинге!")
#         print(f"Например: {coins_candidateInfo_list[0]['symbol']}: {coins_candidateInfo_list[0]}")

        

#     except Exception as e:
#         print(f"Произошла ошибка: {e}")

# if __name__ == "__main__":
#     get_upcoming_listings()
    


# max_price = 0.872
# cur_price = 0.621
# enter_price = 0.03

# max_price = 0.58
# cur_price = 0.4863
# enter_price = 0.371

# # per_change = 100 - ((cur_price*100)/(max_price - enter_price))
# # per_change_2 = (1 - (cur_price/max_price)) * 100
# # per_change_3 = ((max_price - cur_price)/max_price)*100
# per_change_4 = ((max_price - cur_price)/(max_price - enter_price))*100
# # print(per_change)
# # print(per_change_2)
# # print(per_change_3)
# print(per_change_4)
# # 





# https://binance-docs.github.io/apidocs/spot/en/#exchange-information 19
# https://binance-docs.github.io/apidocs/websocket_api/en/#exchange-information 19



# {'symbol': 'ETHBTC', 'status': 'TRADING', 'baseAsset': 'ETH', 'baseAssetPrecision': 8, 'quoteAsset': 'BTC', 'quotePrecision': 8, 'quoteAssetPrecision': 8, 'baseCommissionPrecision': 8, 'quoteCommissionPrecision': 8, 'orderTypes': ['LIMIT', 'LIMIT_MAKER', 'MARKET', 'STOP_LOSS_LIMIT', 'TAKE_PROFIT_LIMIT'], 'icebergAllowed': True, 'ocoAllowed': True, 'quoteOrderQtyMarketAllowed': True, 'allowTrailingStop': True, 'cancelReplaceAllowed': True, 'isSpotTradingAllowed': True, 'isMarginTradingAllowed': True, 'filters': [{'filterType': 'PRICE_FILTER', 'minPrice': '0.00001000', 'maxPrice': '922327.00000000', 'tickSize': '0.00001000'}, {'filterType': 'LOT_SIZE', 'minQty': '0.00010000', 'maxQty': '100000.00000000', 'stepSize': '0.00010000'}, {'filterType': 'ICEBERG_PARTS', 'limit': 10}, {'filterType': 'MARKET_LOT_SIZE', 'minQty': '0.00000000', 'maxQty': '2496.76429246', 'stepSize': '0.00000000'}, {'filterType': 'TRAILING_DELTA', 'minTrailingAboveDelta': 10, 'maxTrailingAboveDelta': 2000, 'minTrailingBelowDelta': 10, 'maxTrailingBelowDelta': 2000}, {'filterType': 'PERCENT_PRICE_BY_SIDE', 'bidMultiplierUp': '5', 'bidMultiplierDown': '0.2', 'askMultiplierUp': '5', 'askMultiplierDown': '0.2', 'avgPriceMins': 5}, {'filterType': 'NOTIONAL', 'minNotional': '0.00010000', 'applyMinToMarket': True, 'maxNotional': '9000000.00000000', 'applyMaxToMarket': False, 'avgPriceMins': 5}, {'filterType': 'MAX_NUM_ORDERS', 'maxNumOrders': 200}, {'filterType': 'MAX_NUM_ALGO_ORDERS', 'maxNumAlgoOrders': 5}], 'permissions': ['SPOT', 'MARGIN', 'TRD_GRP_004', 'TRD_GRP_005', 'TRD_GRP_006', 'TRD_GRP_008', 'TRD_GRP_009', 'TRD_GRP_010', 'TRD_GRP_011', 'TRD_GRP_012', 'TRD_GRP_013', 'TRD_GRP_014', 'TRD_GRP_015', 'TRD_GRP_016', 'TRD_GRP_017', 'TRD_GRP_018', 'TRD_GRP_019', 'TRD_GRP_020', 'TRD_GRP_021', 'TRD_GRP_022', 'TRD_GRP_023', 'TRD_GRP_024', 'TRD_GRP_025'], 'defaultSelfTradePreventionMode': 'EXPIRE_MAKER', 'allowedSelfTradePreventionModes': ['EXPIRE_TAKER', 'EXPIRE_MAKER', 'EXPIRE_BOTH']}

# import time

# buy_orders_list = []

# def market_order_temp_func():
#     return 2

# for _ in range(3):
#     buy_orders_list.append(market_order_temp_func())
#     time.sleep(1)

# print(buy_orders_list)
