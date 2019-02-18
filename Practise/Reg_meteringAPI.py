import requests, json
from configparser import SafeConfigParser
from Practise.metering_payloads import Metering_payload
from json import JSONEncoder



class Reg_meteringAPI():

    def __init__(self, ip, auth):
        self.ip = ip
        self.auth = auth

    def run_metering(self):
        requests.packages.urllib3.disable_warnings()

        met = Metering_payload()

        loads = {}
        loads.update(met.payloads())
        print(met.payloads())

        request_payload = []
        response_status = []
        response_json = []


        for i in range(len(loads)):
            print("Response for Load %d" %i)

            headers = {
                'Authorization': self.auth,
                'x-waitTime': '10',
                'content-type': 'application/json'

            }

            params = (
                ('action', 'getMeteringReportData'),
            )

            payload = json.dumps(loads["load{}".format(i)], cls=json.JSONEncoder)
            print(payload)


            print("****************")

            post_url = "https://" + self.ip + ":8443/meteringapi.do"

            response = requests.post(post_url, headers=headers, params=params, data=payload, verify=False)

            request_payload.append(payload)
            response_json.append(response.json())
            response_status.append(response.status_code)

        return response_status, response_json,  request_payload



    def create_html(self, status, response, payload):


        self.payload = payload
        self.status = status
        self.response = response



        strTable = "<html><table border =1><tr align = 'center'> <td align = center>IP: {}</td> </tr><tr><th>Sl. no</th><<th>Payload</th><th>Status</th><th>Response</th></tr>".format(self.ip)

        for i in range(len(self.payload)):

            strRW = "<tr><td align = center>" + str(i) + "</td><td>" + self.payload[i] + "</td> <td>" + str(self.status[i]) + "</td> <td>" + str(self.response[i]) + "</td> </tr>"
            strTable = strTable + strRW


        strTable = strTable + "</table></html>"

        hs = open("Metering_API_Regression_Run.html", 'w')
        hs.write(strTable)



def main():


    parser = SafeConfigParser()
    parser.read('config.ini')

    vm_ip = parser.get('VM_Details', 'ip')
    vm_auth = parser.get('VM_Details', 'auth')

    print(vm_ip, vm_auth)

    obj = Reg_meteringAPI(vm_ip, vm_auth)
    payload, status, response = obj.run_metering()
    obj.create_html(payload, status, response)


if __name__ == "__main__":
    main()

