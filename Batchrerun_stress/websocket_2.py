import asyncio
import websockets, json, ssl

async def hello():
    async with websockets.connect('wss://192.168.33.133:8443',header={'Authorization: Basic YWRtaW46Q3VtdWx1c0Ax', 'dataset=defaultDs','content-type=application/json;charset=utf-8'}, ssl=ssl.SSLContext(protocol=ssl.PROTOCOL_TLS)) as websocket:
        data = 'hi'
        await websocket.send(json.dumps([json.dumps({"function":"subscribe", "alertIds":[3]})]))
        print("> {}".format(data))

        response = await websocket.recv()
        print("< {}".format(response))

asyncio.get_event_loop().run_until_complete(hello())