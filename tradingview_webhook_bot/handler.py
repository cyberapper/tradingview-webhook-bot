import smtplib
import ssl
from email.mime.text import MIMEText
import json

import tweepy
from discord_webhook import DiscordEmbed, DiscordWebhook
from slack_webhook import Slack
from telegram import Bot
from google.cloud import pubsub_v1

from tradingview_webhook_bot import config


def send_alert(data):
    msg = data["msg"].encode("latin-1", "backslashreplace").decode("unicode_escape")
    publish_to_pubsub(data)  # Publish alert to GCP Pub/Sub

    if config.send_telegram_alerts:
        tg_bot = Bot(token=config.tg_token)
        try:
            if len(data["telegram"].split(",")) > 1:
                for chat_id in data["telegram"].split(","):
                    tg_bot.sendMessage(chat_id, msg, parse_mode="MARKDOWN")
            else:
                tg_bot.sendMessage(data["telegram"], msg, parse_mode="MARKDOWN")
        except KeyError:
            tg_bot.sendMessage(config.channel, msg, parse_mode="MARKDOWN")
        except Exception as e:
            print("[X] Telegram Error:\n>", e)

    if config.send_discord_alerts:
        try:
            webhook = DiscordWebhook(url="https://discord.com/api/webhooks/" + data["discord"])
            embed = DiscordEmbed(title=msg)
            webhook.add_embed(embed)
            webhook.execute()
        except KeyError:
            webhook = DiscordWebhook(url="https://discord.com/api/webhooks/" + config.discord_webhook)
            embed = DiscordEmbed(title=msg)
            webhook.add_embed(embed)
            webhook.execute()
        except Exception as e:
            print("[X] Discord Error:\n>", e)

    if config.send_slack_alerts:
        try:
            slack = Slack(url="https://hooks.slack.com/services/" + data["slack"])
            slack.post(text=msg)
        except KeyError:
            slack = Slack(url="https://hooks.slack.com/services/" + config.slack_webhook)
            slack.post(text=msg)
        except Exception as e:
            print("[X] Slack Error:\n>", e)

    if config.send_twitter_alerts:
        tw_auth = tweepy.OAuthHandler(config.tw_ckey, config.tw_csecret)
        tw_auth.set_access_token(config.tw_atoken, config.tw_asecret)
        tw_api = tweepy.API(tw_auth)
        try:
            tw_api.update_status(status=msg.replace("*", "").replace("_", "").replace("`", ""))
        except Exception as e:
            print("[X] Twitter Error:\n>", e)

    if config.send_email_alerts:
        try:
            email_msg = MIMEText(msg.replace("*", "").replace("_", "").replace("`", ""))
            email_msg["Subject"] = config.email_subject
            email_msg["From"] = config.email_sender
            email_msg["To"] = config.email_sender
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(config.email_host, config.email_port, context=context) as server:
                server.login(config.email_user, config.email_password)
                server.sendmail(config.email_sender, config.email_receivers, email_msg.as_string())
                server.quit()
        except Exception as e:
            print("[X] Email Error:\n>", e)


def publish_to_pubsub(data):
    if config.pubsub_project_id == "" or config.pubsub_topic_id == "":
        return
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(config.pubsub_project_id, config.pubsub_topic_id)
    try:
        payload = {
            "source": "Tradingview",
            "type": "alert",
            "msg": data["msg"]
        }
        publisher.publish(topic_path, data=json.dumps(payload).encode("utf-8"), event=config.pubsub_event_id)
        print("[✓] Published message to Pub/Sub")
    except Exception as e:
        print("[X] Pub/Sub Error:\n>", e)
