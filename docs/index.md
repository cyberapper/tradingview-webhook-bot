# TradingView Webhook Bot

![algo724](./assets/algo724_logo.png)

> ___🪐 When strategies meet applications___

_Algo724 is building the best quantitative, scalable and evolving trading architecture solution, connecting world-class assets for financial institutions and retails_

## Introduction

The **TradingView Webhook Bot** ⚙️ listens to [TradingView](https://tradingview.com) alerts via [webhooks](https://www.tradingview.com/support/solutions/43000529348-i-want-to-know-more-about-webhooks/) using [flask](https://flask.palletsprojects.com/en/1.1.x/).
All alerts can be instantly sent to Telegram, Discord, Twitter and/or Email.

## Features



### Document server
```shell
# Start developer guide server
mkdocs serve
```
### Submit build to GCP artifact registry
```shell
gcloud config set project crescendo-410412
gcloud builds submit --region=asia-east1 --config deployments/gcp/cloudbuild.yaml
```


## Reference

::: tradingview_webhook_bot.handler