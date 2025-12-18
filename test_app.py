import requests
import time

for i in range(5):
    try:
        response = requests.get("http://localhost:8501/healthz")
        if response.status_code == 200:
            print("testi onnistui")
            exit(0)
    except requests.exceptions.ConnectionError:
        print(f"yritetään yhdistää({i+1}/5)")
        time.sleep(3)

print("testi epäonnistui")
exit(1)
