# 🚀 Deploy BAHART Bot on Render - Complete Guide

## Step 1: Get Telegram Bot Token ✅

**Your Bot Details:**
```
Bot Token: 8711442671:AAFqeokh9RyaD-dMEXJtk0drNJ24GzQk8H0
Username: @LALIxLOVE
User ID: 6562788255
```

---

## Step 2: Update Your GitHub Repository

### Create `.env` file in your repo root:

```bash
TELEGRAM_BOT_TOKEN=8711442671:AAFqeokh9RyaD-dMEXJtk0drNJ24GzQk8H0
TELEGRAM_ADMIN_ID=6562788255
POCKET_OPTION_SESSION_TOKEN=27abb5e58c1d57e2aa2a4567042f64e3
POCKET_OPTION_UID=81704775
ENVIRONMENT=production
LOG_LEVEL=INFO
```

### Git commands:

```bash
git add .env Procfile runtime.txt
git commit -m "Add bot credentials and deployment config"
git push origin main
```

---

## Step 3: Create Render Account

1. Go to **https://render.com**
2. Click **Sign Up**
3. Use GitHub account (easiest method)
4. ✅ Account created!

---

## Step 4: Deploy on Render (Step-by-Step)

### Step 4.1: Connect GitHub Repository

1. After login, click **New +** button (top right)
2. Select **Web Service**
3. Click **Connect account** next to GitHub
4. Authorize Render
5. Select repository: `Devilhacks9058/BAHART-BOT-`
6. Click **Connect**

### Step 4.2: Configure Deployment Settings

**Fill in these fields:**

| Field | Value |
|-------|-------|
| Name | `bahart-trading-bot` |
| Environment | `Python 3` |
| Region | `Ohio` (or nearest) |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python main.py` |

### Step 4.3: Add Environment Variables

1. Scroll down to **Environment Variables** section
2. Click **Add Environment Variable**
3. Add each variable:

```
TELEGRAM_BOT_TOKEN = 8711442671:AAFqeokh9RyaD-dMEXJtk0drNJ24GzQk8H0
TELEGRAM_ADMIN_ID = 6562788255
POCKET_OPTION_SESSION_TOKEN = 27abb5e58c1d57e2aa2a4567042f64e3
POCKET_OPTION_UID = 81704775
ENVIRONMENT = production
LOG_LEVEL = INFO
```

4. Click **Create Web Service**
5. ⏳ Wait 5-10 minutes for deployment

---

## Step 5: Verify Deployment

### Check Deployment Status:

1. Go to Render Dashboard
2. Click **bahart-trading-bot**
3. Check **Logs** tab
4. Look for: `BAHART TRADING BOT INITIALIZING` ✅

### Test Bot on Telegram:

1. Open Telegram
2. Search: `@LALIxLOVE`
3. Send message: `/start`
4. Bot should respond with welcome message ✅

---

## Step 6: Available Commands

After bot is live, use these Telegram commands:

```
/start     - Start the bot
/status    - View bot status
/signals   - Get latest trading signals
/analysis  - View market analysis
/portfolio - See open positions
/balance   - Check account balance
/help      - Get help
/settings  - Configure bot settings
```

---

## Step 7: Keep Bot Running 24/7

### Option 1: Free Plan (Limited)
- ❌ Bot stops after 15 mins of inactivity
- ❌ Takes 30 secs to restart
- ❌ Auto-deletes after 30 days

### Option 2: Paid Plan (Recommended) ✅

1. Go to Render Dashboard
2. Click your service: `bahart-trading-bot`
3. Click **Settings** → **Plan**
4. Select **Pay-as-you-go**
5. Cost: ~$7/month ($0.10/hour)
6. ✅ Bot runs 24/7!

---

## Step 8: Monitor Your Bot

### View Real-Time Logs:

1. Render Dashboard → Your Service
2. Click **Logs** tab
3. Scroll to see:
   - Bot startup messages
   - Signal generation logs
   - Trade execution
   - Any errors

### Check Metrics:

1. Click **Metrics** tab
2. Monitor:
   - CPU Usage
   - Memory Usage
   - Network I/O
   - Uptime %

---

## Step 9: Update Bot Code (Auto Deploy)

Whenever you update code on GitHub, Render auto-deploys! 🚀

### To Update:

```bash
# Make changes to your code
git add .
git commit -m "Update bot features"
git push origin main

# Render automatically:
# 1. Detects the push
# 2. Rebuilds the app
# 3. Deploys new version
# ✅ Done!
```

---

## Troubleshooting

### ❌ Bot Not Responding?

**Check logs in Render Dashboard:**
```
Dashboard → Your Service → Logs
```

**Common Issues:**

1. **Invalid Token**
   - Error: `Unauthorized`
   - Fix: Verify token is correct in .env

2. **Missing Environment Variables**
   - Error: `KeyError: 'TELEGRAM_BOT_TOKEN'`
   - Fix: Add all 6 variables in Render settings

3. **Port Already in Use**
   - Error: `Address already in use`
   - Fix: Render handles ports automatically

4. **Dependencies Missing**
   - Error: `ModuleNotFoundError`
   - Fix: Update requirements.txt and push to GitHub

---

## Quick Summary

✅ **Bot Token:** 8711442671:AAFqeokh9RyaD-dMEXJtk0drNJ24GzQk8H0
✅ **User ID:** 6562788255
✅ **Username:** @LALIxLOVE
✅ **Repository:** https://github.com/Devilhacks9058/BAHART-BOT-
✅ **Deployment:** Render.com
✅ **Auto-deploy:** Enabled (push to GitHub = auto deploy)
✅ **Uptime:** 24/7 (with paid plan)

---

## Next Steps

1. ✅ Create Render account
2. ✅ Connect GitHub repository
3. ✅ Add environment variables
4. ✅ Deploy bot
5. ✅ Test on Telegram
6. ✅ Upgrade to paid plan
7. ✅ Monitor logs
8. ✅ Make updates

---

## Support Links

- 📖 Render Docs: https://render.com/docs
- 🤖 Telegram Bot API: https://core.telegram.org/bots
- 💬 GitHub: https://github.com/Devilhacks9058/BAHART-BOT-

**Happy Trading! 🚀📈**