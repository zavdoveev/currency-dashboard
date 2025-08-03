"""
get_data.py — збір курсів валют НБУ (USD, EUR, PLN) за 2 роки.

✅ Отримує дані з API НБУ
✅ Зберігає їх у nbu_rates.csv
✅ Використовується для аналізу та побудови Tableau Dashboard
"""

import pandas as pd
import datetime
import requests

# 📅 Діапазон дат (останні 2 роки)
start_date = datetime.date(2023, 8, 1)
end_date = datetime.date(2025, 8, 1)

data = []

date = start_date
while date <= end_date:
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?date={date.strftime('%Y%m%d')}&json"
    r = requests.get(url)
    if r.status_code == 200:
        json_data = r.json()
        for item in json_data:
            if item['cc'] in ['USD', 'EUR', 'PLN']:
                data.append({
                    'date': date,
                    'currency': item['cc'],
                    'rate': item['rate']
                })
    date += datetime.timedelta(days=1)

# 💾 Зберігаємо дані у CSV
df = pd.DataFrame(data)
df.to_csv("nbu_rates.csv", index=False)
print("✅ Збережено nbu_rates.csv")
print(df.head())
