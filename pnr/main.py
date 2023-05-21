import requests
import json
import re
import sms
if __name__ == "__main__":
    URL = "https://www.confirmtkt.com/pnr-status/2160975913"
    resp = requests.get(URL, verify =False)
    print(resp.status_code)
    s = resp.text

    s = s.split("\n")
    with open("C:/Users/V Vignesh/Desktop/pnr/data", 'r') as f:
        pre_data = f.read()

    result = ""
    for i in s:
        if re.search(r"data = {.*?};", i):
            i=i[7:-2]
            data = json.loads(i)
            for j in data["PassengerStatus"]:
                result += str(j["CurrentStatus"])
                result += "\n"
    with open("C:/Users/V Vignesh/Desktop/pnr/data", 'w') as f:
        f.write(result)
    print(result)

    if result!=pre_data:
        #pass
        sms.send_sms(result)

