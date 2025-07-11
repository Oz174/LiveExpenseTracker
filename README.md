# 💰 Real-Time Google Sheets Expense Tracker with WhatsApp Alerts

A live Python project to track remaining monthly balance from a Google Sheet and send alerts via WhatsApp when spending exceeds threshold.

---

## 📌 Project Goals

- Connect Python to Google Sheets
- Read monthly expenses and balance targets
- Send WhatsApp alert if balance is below threshold
- Run live, watching for updates in real time

---

## 🧱 Project Structure

```
expense_alert_project/
│
├── credentials.json         # Google API credentials
├── main.py                  # Main controller script (live loop)
├── sheets_reader.py         # Fetches and parses Google Sheet data
├── utils.py                 # Contains logic for alert generation
├── notifier.py              # Sends WhatsApp alerts via Twilio
├── .env                     # Stores Twilio secrets
├── requirements.txt         # Dependencies
└── README.md                # Project description
```

---

## ✅ Step-by-Step Progress

### 🔹 **1. Spreadsheet Setup**

**Google Sheet contains two tabs:**

- `Expenses` with: `Date | Expense | Category`
- `Targets` with:
  - `current remaining`: e.g., 1200
  - `target remaining`: e.g., 1000

---

### 🔹 **2. Google Sheets API Setup**

- Created project in Google Cloud Console
- Enabled:
  - Google Sheets API
  - **Google Drive API** ✅ *(required to open by name)*
- Created **Service Account**
- Downloaded `credentials.json`
- Shared the Google Sheet with the service account email

---

### ⚠️ Error: `403 - insufficientPermissions`

```
gspread.exceptions.APIError: 403 - Request had insufficient authentication scopes
```

**✅ Fix:**  
- Added this scope in `sheets_reader.py`:

```python
SCOPES = [
  'https://www.googleapis.com/auth/spreadsheets.readonly',
  'https://www.googleapis.com/auth/drive.readonly'
]
```

- Regenerated the `credentials.json` after enabling Drive API

---

### 🔹 **3. Python Integration**

Used `gspread` to read:

```bash
pip install gspread google-auth
```

Fetched data from both sheets using:
```python
values = sheet.values_batch_get(["Expenses!A2:C100", "Targets!A1:B2"])
```

---

### 🔹 **4. Alert Logic**

Created `generate_alert()` in `utils.py`:

- If remaining is **≥ 20% above** → ✅ good
- Else → ⚠️ alert

```python
def generate_alert(current, target, threshold=0.20):
    deviation = (current - target) / target
    percent = round(deviation * 100)

    if deviation >= threshold:
        return f"✅ You are {percent}% above your target remaining balance."
    else:
        return f"⚠️ You are only {percent}% above (or below) target. Monitor your spending!"
```

---

### 🔹 **5. WhatsApp Integration (Twilio)**

```bash
pip install twilio python-dotenv
```

Set up:
- Twilio trial account
- Joined WhatsApp sandbox by sending `join <code>` to `+14155238886`
- Created `.env`:

```env
TWILIO_SID=ACxxxxxxxx
TWILIO_AUTH=xxxxxxxxx
TWILIO_FROM=whatsapp:+14155238886
TWILIO_TO=whatsapp:+20xxxxxxxxxx
```

---

### ⚠️ Error: `Twilio Error 63007`

```
Unable to create record: Twilio could not find a Channel with the specified From address
```

**✅ Fix:**  
- Added `whatsapp:` prefix to both numbers in `.env`
- Verified number joined the sandbox via WhatsApp

---

### 🔹 **6. Real-Time Monitoring Mode**

Implemented a `while True` loop in `main.py`:

```python
CHECK_INTERVAL = 30  # seconds
ALERT_SENT = False

while True:
    ...
    if deviation:
        if not ALERT_SENT:
            send_whatsapp_alert(message)
            ALERT_SENT = True
    else:
        ALERT_SENT = False

    time.sleep(CHECK_INTERVAL)
```

**🔄 Runs live**, reacts to Google Sheet changes as you type!

---

## ✅ Final Result

- ✅ Fully functional live alert system
- ✅ Secure with `.env`
- ✅ Modular Python design
- ✅ Real-time Google Sheet sync
- ✅ WhatsApp alerts working via Twilio Sandbox

---

## 🚀 Future Ideas

| Feature | Description |
|--------|-------------|
| 📊 Charts | Show spending trends and limits |
| 🧠 GPT Budget Advisor | Suggest how to save based on history |
| 📨 Email Reports | Monthly spending summaries |
| 🗃️ Expense Archive | Save monthly backups to CSV |
| 🏷️ Category Alerts | Alert if e.g. "Cigs" > budget |

---

### ⏱️ Total Build Time: ~2 Hours  
🎉 Congrats on completing your live budget alert system!
