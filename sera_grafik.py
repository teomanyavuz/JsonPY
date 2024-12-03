import json
import matplotlib.pyplot as plt

with open("ayar.json", "r") as f:
    ayar = json.load(f)

with open("idx1.json", "r") as f:
    idx1 = json.load(f)

with open("idx5.json", "r") as f:
    idx5 = json.load(f)

temp = idx1["result"][0]["Temp"]  
humidity = idx1["result"][0]["Humidity"]  
co2 = int(idx5["result"][0]["Data"].split()[0]) 

temp_status = ayar["icsAlt"] <= temp <= ayar["icsUst"]
humidity_status = ayar["icnAlt"] <= humidity <= ayar["icnUst"]
co2_status = ayar["co2Alt"] <= co2 <= ayar["co2Ust"]

data = [temp, humidity, co2]
labels = ["İç Sıcaklık (°C)", "İç Nem (%)", "Hava Kalitesi (ppm)"]
statuses = [temp_status, humidity_status, co2_status]
colors = ["green" if status else "red" for status in statuses]

plt.bar(labels, data, color=colors)
plt.title("Sera Sensör Verileri")
plt.ylabel("Değer")
plt.xlabel("Sensör Türü")
plt.ylim(0, max(data) + 10)  
plt.show()
