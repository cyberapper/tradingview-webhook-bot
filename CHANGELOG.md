# CHANGELOG



## v0.4.0 (2024-02-29)

### Chore

* chore(pyproject.toml): set prerelease flag to false to disable creating prerelease versions ([`50f33d9`](https://github.com/cyberapper/tradingview-webhook-bot/commit/50f33d991a36ec60c7857b0008f55fb84454faa9))

### Feature

* feat: add docker-compose development configuration file

The `compose-dev.yml` file has been added to the project. This file is used for configuring the development environment using Docker Compose.

refactor: remove docker-compose production configuration file

The `docker-compose.yml` file has been deleted from the project. This file was no longer needed and has been removed.

feat: add tests package and test files

The `tests` package has been added to the project, along with the `__init__.py` file and the `test_emitter.py` file. These files are used for writing tests for the `emitter.py` module.

feat: add emitter.py module

The `emitter.py` module has been added to the `tradingview_webhook_bot` package. This module is responsible for emitting events in the webhook bot application.

chore(pyproject.toml): add pika and python-dotenv dependencies ([`6a1ce28`](https://github.com/cyberapper/tradingview-webhook-bot/commit/6a1ce2863683807f708ada0d2366f1b077de2e0d))


## v0.4.0-rc.1 (2024-02-28)

### Feature

* feat(.env.example): add .env.example file with placeholder for Telegram bot token

The .env.example file is added to the project. This file serves as an example for the required environment variables and their format. In this case, a placeholder for the Telegram bot token is added as `TG_TOKEN=&lt;telegram_bot_token&gt;`. This will help developers to easily set up their environment by copying this file and replacing the placeholder with the actual Telegram bot token. ([`c4ae490`](https://github.com/cyberapper/tradingview-webhook-bot/commit/c4ae490e75208c0b72c2d03f46255696dc8db815))


## v0.3.0 (2024-02-14)

### Feature

* feat(main.py): add new /broadcast endpoint to handle broadcasting alerts to multiple chat ids

fix(main.py): remove unnecessary print statements in broadcast function ([`21847d9`](https://github.com/cyberapper/tradingview-webhook-bot/commit/21847d955a54c551222717a6dc561de5a235950a))

* feat(handler.py): add new broadcast_message function to handle sending broadcast alerts to multiple chat ids ([`70d0590`](https://github.com/cyberapper/tradingview-webhook-bot/commit/70d05902611f4a0f51f4c2e10cf553e6f9a57d06))


## v0.2.0 (2024-02-13)

### Feature

* feat(handler.py): add sending alerts to multiple telegram chat id support ([`acda603`](https://github.com/cyberapper/tradingview-webhook-bot/commit/acda603ad4a5c2918156f1e7bf383d3d00b241c8))

### Unknown

* Merge branch &#39;alg-33-feature-initiate-tradingview-webhook-repo&#39; into develop ([`3258d28`](https://github.com/cyberapper/tradingview-webhook-bot/commit/3258d287a9507c7ba2c510f3703a9ba6f168503b))


## v0.1.0-rc.1 (2024-02-09)

### Chore

* chore: remove unused files and configurations

- Removed `.github/FUNDING.yml` file as it is no longer needed.
- Removed `.github/ISSUE_TEMPLATE/bug-report---.md` file as it is no longer needed.
- Removed `.github/ISSUE_TEMPLATE/config.yml` file as it is no longer needed.
- Removed `.github/ISSUE_TEMPLATE/feature-request---.md` file as it is no longer needed.
- Removed `.github/workflows/stale.yml` file as it is no longer needed.
- Removed `assets/bmac.png` file as it is no longer needed.
- Removed `assets/logo.png` file as it is no longer needed.

feat: add new files and configurations

- Added `compose.yml` file for docker-compose configuration.
- Added `deployments/gcp/cloudbuild.yaml` file for Google Cloud Build configuration.
- Added `docs/assets/algo724_logo.png` file for documentation.
- Added `docs/index.md` file for documentation.
- Added `mkdocs.yml` file for documentation configuration.
- Added `pyproject.toml` file for Python project configuration.
- Added `tradingview_webhook_bot/__init__.py` file for initializing the TradingView webhook bot.
- Added `tradingview_webhook_bot/config.py` file for configuring the TradingView webhook bot.
- Added `tradingview_webhook_bot/handler.py` file for handling alerts in the TradingView webhook bot. ([`a8d1540`](https://github.com/cyberapper/tradingview-webhook-bot/commit/a8d15409140d7a1d9f9130738eb9d0827f225da7))

### Feature

* feat: initial commit ([`f3ba2f6`](https://github.com/cyberapper/tradingview-webhook-bot/commit/f3ba2f6f03242012969c0db6039d5ceb58b0331b))

### Unknown

* Removed sponsor page ([`d1d7699`](https://github.com/cyberapper/tradingview-webhook-bot/commit/d1d7699e246b6fa0d95af7415115d04bb215c69c))

* Merge pull request #87 from fabston/dependabot/pip/waitress-2.1.1

Bump waitress from 2.0.0 to 2.1.1 ([`1df7d5c`](https://github.com/cyberapper/tradingview-webhook-bot/commit/1df7d5c49b2f259cfecd976ba3d93841aed9c354))

* Bump waitress from 2.0.0 to 2.1.1

Bumps [waitress](https://github.com/Pylons/waitress) from 2.0.0 to 2.1.1.
- [Release notes](https://github.com/Pylons/waitress/releases)
- [Changelog](https://github.com/Pylons/waitress/blob/master/CHANGES.txt)
- [Commits](https://github.com/Pylons/waitress/compare/v2.0.0...v2.1.1)

---
updated-dependencies:
- dependency-name: waitress
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`768007e`](https://github.com/cyberapper/tradingview-webhook-bot/commit/768007e386d34d4ab2ab0a0e99eaef5573ff2ea2))

* Update README.md ([`3306a06`](https://github.com/cyberapper/tradingview-webhook-bot/commit/3306a060e8533f31fdaf774c5c72bc6755eb24e8))

* Update README.md ([`fbd51f9`](https://github.com/cyberapper/tradingview-webhook-bot/commit/fbd51f98de507e4d5354943aa384dc41a8fa936b))

* Update README.md ([`3556ec9`](https://github.com/cyberapper/tradingview-webhook-bot/commit/3556ec9dda8b146a7bf3239d7472e7772ac1957e))

* Merge pull request #78 from sakuyamaij/patch-1

Update typo in README.md ([`f357dbd`](https://github.com/cyberapper/tradingview-webhook-bot/commit/f357dbd631454ca32203964ccd814bac727d4ad6))

* Update README.md

typo fix ([`ba35391`](https://github.com/cyberapper/tradingview-webhook-bot/commit/ba353919a415733cf7a910c25da6820f60418ecf))

* Fixed underscore issue in msg body ([`2dbbcfd`](https://github.com/cyberapper/tradingview-webhook-bot/commit/2dbbcfd98c3fb705bd83b0aee00de940602274cb))

* Minor updates ([`6f0df8a`](https://github.com/cyberapper/tradingview-webhook-bot/commit/6f0df8aaf11cc219027c9435c9bb4b0aa10426c5))

* Updated stale.yml ([`90d5558`](https://github.com/cyberapper/tradingview-webhook-bot/commit/90d5558fa362fc4f3a996ac47d24990ef8e317f0))

* Beautified code ([`dca330c`](https://github.com/cyberapper/tradingview-webhook-bot/commit/dca330cde582092c4f6e987f1974dab4be740b78))

* Updated issue templates ([`e55d973`](https://github.com/cyberapper/tradingview-webhook-bot/commit/e55d973f5b359d774efd53efd4589f284b9af9ef))

* Updated README.md ([`82d62ff`](https://github.com/cyberapper/tradingview-webhook-bot/commit/82d62ffceecbc0d832a92e253b821167c3df86ac))

* Updated Funding ([`9637bbe`](https://github.com/cyberapper/tradingview-webhook-bot/commit/9637bbeadba4671d82115ec1557395a677be45fa))

* Updated readme ([`8bd3ad8`](https://github.com/cyberapper/tradingview-webhook-bot/commit/8bd3ad8bc19f8a77f3be0b2866840bdf3bdbe75e))

* Remove markdown on Tweets and Emails ([`2c3d981`](https://github.com/cyberapper/tradingview-webhook-bot/commit/2c3d9815e5513bb7c1bb43592aa80e5ebc9a47f0))

* Fixed Twitter message body. ([`43096d6`](https://github.com/cyberapper/tradingview-webhook-bot/commit/43096d6b3fec30407bba9a4ccf061a8f1573e6ec))

* Updated readme ([`aafac69`](https://github.com/cyberapper/tradingview-webhook-bot/commit/aafac69c8ad44604ad49981f0f45478889cd41b2))

* Clean up and beautify code ([`cb43128`](https://github.com/cyberapper/tradingview-webhook-bot/commit/cb431288d7f0ddba77a1c4daa2eedf34aa5aa93a))

* Added Issue Template ([`997420f`](https://github.com/cyberapper/tradingview-webhook-bot/commit/997420fb5925767501596a7d7c7a2a16b94d3902))

* Added Stale Workflow ([`9e22295`](https://github.com/cyberapper/tradingview-webhook-bot/commit/9e222957d6ed17afe3e51a3d9869ce870d679eb5))

* Minor updates ([`f49d6cd`](https://github.com/cyberapper/tradingview-webhook-bot/commit/f49d6cdc4e5ed834494702c2e5b4c418be326a60))

* Added BMAC to Readme ([`7ae204e`](https://github.com/cyberapper/tradingview-webhook-bot/commit/7ae204ed9300c17cb80980639e4cb9cabe25b6c1))

* Update Readme

Mentioned PM2 Support to run the app in the background and on boot. ([`f56e0b9`](https://github.com/cyberapper/tradingview-webhook-bot/commit/f56e0b94a76b9b6df69e7109f20b22deca3127f9))

* Implemented Slack Support ([`7868203`](https://github.com/cyberapper/tradingview-webhook-bot/commit/7868203264606b47de300d13aa0e80c3d32abb65))

* Updated Readme ([`127ed28`](https://github.com/cyberapper/tradingview-webhook-bot/commit/127ed28bbf43aec9864d7cf4278de39393d297bf))

* Updated encoding for Telegram Messages ([`8a2a5c8`](https://github.com/cyberapper/tradingview-webhook-bot/commit/8a2a5c80b5b56ffd173083a3009faab75ce810b9))

* Few bug fixes

- Fixed underscore issue
- Fixed Timestamp issue ([`025dbcc`](https://github.com/cyberapper/tradingview-webhook-bot/commit/025dbcc58d52f888b62f2d89f69fd7a047ffc05e))

* Several updates &amp; improvements. Read description: 

- Webhook feed updated to json
- Send Telegram / Discord alerts to different channels
- Discord alerts are being sent as embed
- Security key improvement
- Minor bug fixes ([`9b93667`](https://github.com/cyberapper/tradingview-webhook-bot/commit/9b93667a52f0489bd8e943c28e18453dbf8646a0))

* Updated README logo ([`2f52744`](https://github.com/cyberapper/tradingview-webhook-bot/commit/2f5274436bf8546d299b9c0394ab90fb3784e4c5))

* Merge pull request #15 from jagzmz/patch-1

Fixup Readme ([`9e9cad5`](https://github.com/cyberapper/tradingview-webhook-bot/commit/9e9cad5affdda424688f3b052813890fc8facbde))

* Fixup Readme

i think u meant a `cd` command. ([`98b142b`](https://github.com/cyberapper/tradingview-webhook-bot/commit/98b142b58fddf63dd37f2b4dab15f40077009faa))

* Updated README ([`2e04304`](https://github.com/cyberapper/tradingview-webhook-bot/commit/2e04304ebcf09ce23f108f66a27544e0778168ce))

* Updated README ([`0155c9b`](https://github.com/cyberapper/tradingview-webhook-bot/commit/0155c9b35bce17c14c399ca029e0d751aa6a11d2))

* Config: send alerts fix ([`ac956c1`](https://github.com/cyberapper/tradingview-webhook-bot/commit/ac956c1d89362200d3550f238a3025d4073e80d9))

* Code cleanup ([`d3f46f8`](https://github.com/cyberapper/tradingview-webhook-bot/commit/d3f46f83da936fe7c75111aefb9fa54c973a9aa4))

* Readme update ([`4bb027e`](https://github.com/cyberapper/tradingview-webhook-bot/commit/4bb027e480e4d770428c4b6539d7975d2e3ffec9))

* Readme updates ([`1b63bb5`](https://github.com/cyberapper/tradingview-webhook-bot/commit/1b63bb5946cf492cee80eadf6a047b8ae57243b9))

* Merge pull request #8 from jon4hz/master

add security code and docker ([`316b17e`](https://github.com/cyberapper/tradingview-webhook-bot/commit/316b17e0e2d0836ff4cf35046a8a41eec2d0a9c4))

* dokerize ([`c648e11`](https://github.com/cyberapper/tradingview-webhook-bot/commit/c648e1132a8fdc9e4d5d7c788c482d48591c071f))

* add security code ([`02a8529`](https://github.com/cyberapper/tradingview-webhook-bot/commit/02a8529fc4d9a494410e3d2ec5b3926ec19466cc))

* Minor updates ([`8d57704`](https://github.com/cyberapper/tradingview-webhook-bot/commit/8d57704b120f2029d150fafdb392624916b16efb))

* Minor changes ([`339e843`](https://github.com/cyberapper/tradingview-webhook-bot/commit/339e843326cc942cd7ca69cf7ad5247b4ef3135b))

* Updated Readme ([`257b5cd`](https://github.com/cyberapper/tradingview-webhook-bot/commit/257b5cdfb08a8136d2e49b0b4d11c8c82706074c))

* Added Telegram Markdown support ([`30665e8`](https://github.com/cyberapper/tradingview-webhook-bot/commit/30665e805102d5f5adab63e468f9a80f2288f573))

* Added option to whitelist words

- Easily add whitelisted words in config.py
- Better error handling ([`b35a293`](https://github.com/cyberapper/tradingview-webhook-bot/commit/b35a293a658b4d19d169777ce15d46d00ae6cd19))

* simplified handler.py ([`f2a5f5c`](https://github.com/cyberapper/tradingview-webhook-bot/commit/f2a5f5c5ec5560d0f4ad585f0f34bd07ca731676))

* Minor changes to the readme ([`353c136`](https://github.com/cyberapper/tradingview-webhook-bot/commit/353c136fb7b8ca7c0fe517f4bb4ca196c0106926))

* Few minor updates ([`246c680`](https://github.com/cyberapper/tradingview-webhook-bot/commit/246c6807bd66c58090c6e6cc57d06b1302bb451e))

* Create FUNDING.yml ([`831d960`](https://github.com/cyberapper/tradingview-webhook-bot/commit/831d96029135b7271f3c97f3980fc6fd8b457d86))

* Updated the readme ([`5f3296e`](https://github.com/cyberapper/tradingview-webhook-bot/commit/5f3296e605d5433958c47d520d95f5a2475056b2))

* Added Twitter support

You are now also able to send alerts to twitter. Can be enabled in config.py ([`5ffe8d5`](https://github.com/cyberapper/tradingview-webhook-bot/commit/5ffe8d5f60eda80c0457a89311ff54c532b1849d))

* Added email support ([`6b0e1d9`](https://github.com/cyberapper/tradingview-webhook-bot/commit/6b0e1d932a8c9662aaf456cc347d31334d2bb574))

* Updated readme and posting mechanism ([`1d6a278`](https://github.com/cyberapper/tradingview-webhook-bot/commit/1d6a278f87c5b282a77284b9aac06f266f63af4b))

* Update README.md

Typo fix in Readme ([`0550790`](https://github.com/cyberapper/tradingview-webhook-bot/commit/05507908b8717a33839c4d096d73b45860dd4ab3))

* Update README.md

Readme update ([`aacd22c`](https://github.com/cyberapper/tradingview-webhook-bot/commit/aacd22cf9eab48361836c9d15389bb11d34c2b2c))

* Add files via upload

Initial release ([`fb0d826`](https://github.com/cyberapper/tradingview-webhook-bot/commit/fb0d8260ee052f27d210eec8f3b8f2a665be134a))

* Initial commit ([`f46e0a8`](https://github.com/cyberapper/tradingview-webhook-bot/commit/f46e0a83677fb6ab2d70c476324ab7cba60f4d0c))
