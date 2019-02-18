import websocket, json, ssl



try:
    import thread
except ImportError:
    import _thread as thread
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    def run(*args):
       print("**************")
       msg = ws.send(json.dumps([json.dumps({"function":"subscribe", "alertIds":[3]})]))
       print(msg)
       result = ws.recv()
       print('Result: {}'.format(result))
       ws.close()
       print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)

    url = "wss://192.168.33.133:8443"
    try:
        ws = websocket.WebSocketApp(url,
                             on_message = on_message,
                              on_error = on_error,
                              on_close = on_close,
                              header = {'Authorization: Basic YWRtaW46Q3VtdWx1c0Ax', 'dataset=defaultDs','content-type=application/json;charset=utf-8'}

                                    )

        ws.on_open = on_open

    except Exception as e:
        print("Error While Connecting : %s" % str(e))

    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

