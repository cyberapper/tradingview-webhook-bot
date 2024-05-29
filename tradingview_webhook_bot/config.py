import os

# TradingView Example Alert Message:
# { "key":"9T2q394M92", "telegram":"-1001298977502", ... }

sec_key = os.getenv("KEY", "")

# Telegram Settings
send_telegram_alerts = os.getenv("TG_ENABLE", True)
tg_token = os.getenv("TG_TOKEN", "")
channel = os.getenv("TG_CHANNEL", 1504960565)

# Discord Settings
send_discord_alerts = False
discord_webhook = ""

# Slack Settings
send_slack_alerts = False
slack_webhook = ""

# Twitter Settings
send_twitter_alerts = False
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

# Email Settings
send_email_alerts = False
email_sender = ""
email_receivers = ["", ""]
email_subject = "Trade Alert!"
email_port = 465
email_host = ""
email_user = ""
email_password = ""

# RabbitMQ Settings
rabbitmq_url = os.getenv("RABBITMQ_URL", "")

# GCP Pub/Sub Settings
pubsub_project_id = os.getenv("PUBSUB_PROJECT_ID", "")
pubsub_topic_id = os.getenv("PUBSUB_TOPIC_ID", "")
pubsub_event_id = os.getenv("PUBSUB_EVENT_ID", "crescendo.tvWebhook.signalReceived")
