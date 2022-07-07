from dateutil.parser import parse
import json
from urllib import request
from urllib.request import Request, urlopen

def ctftime_contest():
    ctftime_url = "https://ctftime.org/api/v1/events/?limit=15"
    answ = Request(ctftime_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"})
    resp = urlopen(answ).read()

    # Decode response json into utf8 then load
    # into a dictionary using json module 
    resp_body = resp.decode('utf8')
    events = json.loads(resp_body)

    # Initialize string to return
    contests_string = "CAPTURE THE FLAGS\n\n"
    
    for event in events:
        
        # Iterate over the dictionary to extract 
        # info for all on-line competitions
        if event['onsite'] == True:
            continue

        contests_string += "Name: {}\n".format(event['title'])
       
        time_meta = event['start']
        time_comp = parse(time_meta).isoformat(' ')
        time = time_comp.split('+')[0]
        contests_string += "From: {}\n".format(time)
        
        time_meta = event['finish']
        time_comp = parse(time_meta).isoformat(' ')
        time = time_comp.split('+')[0]
        contests_string += "To: {}\n".format(time)
        
        contests_string += "Format: {}\n".format(event['format'])
        contests_string += "Duration: {} Days {} Hours\n\n".format(event['duration']['days'], event['duration']['hours'])

    return contests_string


if __name__ == "__main__":
    print(ctftime_contest())
