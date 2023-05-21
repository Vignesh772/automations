import requests

# "variables_values": message,

def send_sms(message):

    url = "https://www.fast2sms.com/dev/bulkV2"

    querystring = {
            "authorization": "<your_key_here>",
            "message": message,
            "language": "english",
            "route": "q",
            "variables_values": message,
            "sender_id":"TXTIND",
            "numbers": "9910776747"}

    headers = {
            'cache-control': "no-cache"
    }
    try:
            response = requests.request("GET", url,headers = headers,params = querystring, verify =False)
            print(response.text, response)
            print("SMS Successfully Sent")
    except:
            print("Oops! Something wrong")
# send_sms("0")
