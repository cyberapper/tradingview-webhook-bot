# TradingView Webhook Bot

![algo724](./assets/algo724_logo.png)

## About
The **TradingView Webhook Bot** ⚙️ listens to [TradingView](https://tradingview.com) alerts via [webhooks](https://www.tradingview.com/support/solutions/43000529348-i-want-to-know-more-about-webhooks/) using [flask](https://flask.palletsprojects.com/en/1.1.x/).
All alerts can be instantly sent to Telegram, Discord, Twitter and/or Email.

## Features
- Telegram Support using the [Python Telegram](https://github.com/python-telegram-bot/python-telegram-bot) libary
- Discord Support using [webhooks](https://support.discord.com/hc/de/articles/228383668-Webhooks-verwenden)
- Slack Support using [webhooks](https://api.slack.com/messaging/webhooks)
- Twitter Support using the [tweepy](https://github.com/tweepy/tweepy) libary
- Email Support using [smtplib](https://docs.python.org/3/library/smtplib.html)
- Dynamically send alerts to different Telegram and/or Discord channels
- TradingView `{{close}}`, `{{exchange}}` etc. variables support. Read more [here](https://www.tradingview.com/blog/en/introducing-variables-in-alerts-14880/)

## Installation
1. Edit and update [`config.py`](https://github.com/fabston/TradingView-Webhook-Bot/blob/master/config.py)
1. Setup TradingView alerts. An example alert message would be:
    ```json
    {
     "key": "9T2q394M92",
     "telegram": "-1001277977502",
     "discord": "789842341870960670/BFeBBrCt-w2Z9RJ2wlH6TWUjM5bJuC29aJaJ5OQv9sE6zCKY_AlOxxFwRURkgEl852s3",
     "slack": "T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX",
     "msg": "Long *#{{ticker}}* at `{{close}}`"
    }
    ```
    - `key` is mandatory! It has to match with `sec_key` in [`config.py`](https://github.com/fabston/TradingView-Webhook-Bot/blob/master/config.py). It's an extra security measurement to ensure nobody else is executing your alerts
    - `telegram`, `discord`, `slack` is optional. If it is not set it will fall back to the config.py settings
    - `msg` can be anything. Markdown for [Telegram](https://core.telegram.org/api/entities) and [Discord](https://support.discord.com/hc/en-us/articles/210298617-Markdown-Text-101-Chat-Formatting-Bold-Italic-Underline-) is supported as well
        - TradingViews variables like `{{close}}`, `{{exchange}}` etc. work too. More can be found [here](https://www.tradingview.com/blog/en/introducing-variables-in-alerts-14880/)
    - Your webhook url would be `http://<YOUR-IP>/webhook`
1. If you use a firewall be sure to open the corresponding port
1. Run the bot with `python main.py`

### Docker
1. `docker-compose build`
1. `docker-compose up`

*It is recommended to run flask on a different port like 8080. It is then necessary to forward port 80 to 8080.*
