# Discord Bot Project

This is a Discord bot built with Python using the [discord.py](https://discordpy.readthedocs.io/en/stable/) library.

## 🔧 Prerequisites

- Python 3.8 or higher installed
- A Discord Developer account: [Create an application](https://discord.com/developers/applications/)
- Git (optional)

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/KaningNoppasin/Discord-Bot
cd Discord-Bot
```

---

### 2. Create a Virtual Environment

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows:
```cmd
python -m venv venv
venv\Scripts\activate
```

---

### 3. Deactivate the Virtual Environment (same for all platforms)

```bash
deactivate
```

---

### 4. Copy Environment Configuration

```bash
cp .env.example .env
```

> ⚠️ On Windows (Command Prompt), use `copy .env.example .env` instead.

---

### 5. Install Required Packages

#### macOS/Linux:
```bash
pip3 install -r requirements.txt
```

#### Windows:
```cmd
pip install -r requirements.txt
```

---

### 6. Run the Bot

#### macOS/Linux:
```bash
python3 main.py
```

#### Windows:
```cmd
python main.py
```

---

## 📚 Resources

- [Discord Developer Portal](https://discord.com/developers/applications/)
- [discord.py Documentation](https://discordpy.readthedocs.io/en/stable/)

---

## 📝 Notes

Make sure to configure your `.env` file with the correct values such as your Discord bot token and other required environment variables before running the bot.

