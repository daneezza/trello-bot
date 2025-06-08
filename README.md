# 🛠️ Trello Bot Automation with Python & Selenium

This project automates Trello login and task card creation using **Python**, **Selenium WebDriver**, and **environment variables** for secure credential handling.

## 📹 Demo
[Watch Demo in LinkedIn](https://www.linkedin.com/posts/daneezza_python-selenium-automation-activity-7337475056270204928-oxDq?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEtxqBkBjn4ib2_jj6dl_DJLw5n-McAInYE)

---

## 🚀 Features

- Secure login to Atlassian/Trello using credentials from `.env` or GitHub Secrets
- Navigates to the Trello board and adds a new card
- Uses Selenium for browser automation
- Simulates smooth user-like interactions
- Works with Chrome and WebDriver Manager

---

## 🔧 Tech Stack

- **Python 3.10+**
- **Selenium**
- **WebDriver Manager**
- **python-dotenv**
- **ChromeDriver**

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/trello-bot.git
cd trello-bot
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a .env file in the directory:**
   
- BASE_URL=https://id.atlassian.com/login
- EMAIL=your-email@example.com
- PASSWORD=your-password

4. **Run the Bot:**

```bash
python trello_bot.py
```

  
