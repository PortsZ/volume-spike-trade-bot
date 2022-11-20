import json 
 
with open('pairs.json') as f:
    data = json.load(f)
    pair_list = []

for symbols in data:
    symbol = symbols.get('symbol')

    
    if symbol.endswith("USDT"):
        pair_list.append(symbol)
    

f.close()




with open('get_pairs.json') as d:
    last_pairs = json.load(d)
    print(last_pairs)
    last_pairs["pair_list"] = pair_list
    
    
with open('get_pairs.json', 'w') as f:
    json.dump(last_pairs, f)

f.close()