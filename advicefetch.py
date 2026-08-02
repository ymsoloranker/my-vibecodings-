import json
import urllib.request

url = "https://api.adviceslip.com/advice"

try:
    req = urllib.request.urlopen(url)
    data = json.loads(req.read().decode("utf-8"))
    advice = data["slip"]["advice"]
    print(f"💡 Daily Advice: {advice}")
except Exception as e:
    print("Could not fetch advice:", e)