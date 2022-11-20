import websockets
import asyncio
import os.path as path
import shutil # copy files
import json
from SendEmail import send_email as alert


async def listen(url):
    async with websockets.connect(url) as ws:
        while True: #listening to the coins
            msg = await ws.recv()
            listen.parsed_msg = json.loads(msg)

            parsed_msg = listen.parsed_msg["k"]
            pair = parsed_msg["s"]
            volume = parsed_msg["v"]
            candle_open = parsed_msg["o"]
            candle_close = parsed_msg["c"]
            is_candle_closed = parsed_msg["x"]


            if path.isfile(f'pairData/data_{pair}.json') == False:
                print(f"\n----------------------Pair {pair} Created----------------------\n")
                shutil.copyfile('pairData/dataTemplate.json', f'pairData/data_{pair}.json')
            
            
            f = open(f'pairData/data_{pair}.json')

            try:
                data = json.load(f)
            except json.decoder.JSONDecodeError:
                print(f"Error decoding {pair} JSON! - API EMPTY")
            
            
            
            if data == {}:
                data["last_volume"] = volume
                data["last_candle_open"] = candle_open
                data["last_candle_close"] = candle_close


            last_volume = data["last_volume"]
            last_candle_open = data["last_candle_open"]
            last_candle_close = data["last_candle_close"]


            f.close()
            
                

            if is_candle_closed:

                # print(f"{pair} Last Volume: {last_volume}\n\n")
                
                

                if last_volume == 0:
                    last_volume = volume


                if last_candle_open == 0:
                    last_candle_open = candle_open

                if last_candle_close == 0:
                    last_candle_close = candle_close

                if float(last_volume)*5 < (float(volume)) and last_volume != 0:
                    
                    alert(pair, candle_open, candle_close, volume, last_candle_open, last_candle_close, last_volume)

                data["last_volume"] = volume
                data["last_candle_open"] = candle_open
                data["last_candle_close"] = candle_close

                with open(f'pairData/data_{pair}.json', 'w') as f:
                    json.dump(data, f)
                f.close()
            

def serve(url):
    print(f"connected on {url}")
    asyncio.get_event_loop().run_until_complete(listen(url))