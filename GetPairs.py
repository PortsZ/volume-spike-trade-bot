import json

pair_list = []
url_list = []

def get_url_list():
    with open('get_pairs.json') as d:
        pair_list_json = json.load(d)
        pair_list = pair_list_json["pair_list"]


    for pairs in pair_list:     
        url_list.append( f"wss://stream.binance.com:9443/ws/{pairs.lower()}@kline_5m")
    
    return url_list



    # wss://stream.binance.com:9443/ws/ltcusdt@kline_1m 