# 📊 Currency Dashboard – NBU Exchange Rates

## 📌 Опис
Цей проєкт демонструє, як можна використати **відкрите API НБУ** для збору щоденних курсів валют (USD, EUR, PLN) за останні 2 роки та побудувати інтерактивний дашборд у Tableau.

📍 Основні кроки:
- Збір даних із API НБУ через Python
- Збереження даних у CSV
- Побудова інтерактивного дашборду в **Tableau Public**

---

## 🌍 Онлайн-дашборд
👉 [Переглянути дашборд на Tableau Public](https://public.tableau.com/app/profile/anatoliy.zavdoveev/viz/currencyUAH/Sheet1?publish=yes)

(Додайте сюди скріншот dashboard.png)

---

## 🚀 Як запустити Python-скрипт

1️⃣ **Встановіть залежності**
```bash
pip install -r requirements.txt
```

2️⃣ **Запустіть скрипт**
```bash
python get_data.py
```

👉 У папці з’явиться файл `nbu_rates.csv` з курсами валют за 2 роки.

---

## 🔧 Використані інструменти
- **Python:** pandas, requests
- **Tableau Public** – для візуалізації
- **GitHub** – для зберігання коду та документації

---

## 📤 Джерело даних
- [API Національного банку України](https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json)
