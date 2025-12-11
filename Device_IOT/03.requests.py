
## Modulul requests este folosit pentru comunicare HTTP
import requests





## CLIENT HTTP IN PYTHON
response = requests.get("https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT")
print(response)
print(response.content)