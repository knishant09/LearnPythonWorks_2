import requests, json

remoteapi = "http://192.168.33.232:8000/api/remoteCommand"

headers = {'content-type': 'application/json'}


def call_remoteapi(cmd):
    print(cmd)
    inputJSON = {}
    inputJSON['ip'] = "192.168.33.141"
    inputJSON['userName'] = "megha"
    inputJSON['password'] = "megha!234"
    inputJSON['port'] = 22
    inputJSON['command'] = cmd
    print(inputJSON)

    response = requests.post(url=remoteapi, data=json.dumps(inputJSON), headers=headers)
    print(response.json())
    if response.status_code == 200:
        data = response.json()
        return data["commandsOutputs"]


dt = call_remoteapi(["pwd"])
print(dt)