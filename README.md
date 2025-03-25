# 🔔 Notifying Webscraper

A simple Python script that checks a website for updates and notifies you when a product is available.

Originally built to track 3D printer stock, but you can customize it for any product or page.

---

## ⚙️ Features

- Scrapes a webpage for specific content
- Sends Windows notifications
- Optionally opens your browser when stock is available
- Optional email alerts (fill in your credentials at the bottom)

---

## 🚀 How to Use

1. Install dependencies:
    ```bash
    pip install requests bs4 win10toast
    ```

2. Update the script:
    - Replace the product URLs
    - Update the `div`/class you want to check
    - (Optional) Fill in your email info if you want email alerts

3. Run the script:
    ```bash
    python notify_scraper.py
    ```

---

## 📝 Notes

- This script is built for **Windows** (uses `win10toast`, `winsound`)
- Be respectful when scraping — keep delays in place (e.g. `time.sleep(600)`)

---

## 📬 Email Setup

To enable email notifications:
- Use an [App Password from Gmail](https://myaccount.google.com/apppasswords)
- Replace `sender_email`, `receiver_email`, and `password` in the script

---

## 🛑 Disclaimer

This project is for personal or educational use only.  
Please don't use it to overload or spam any website.
