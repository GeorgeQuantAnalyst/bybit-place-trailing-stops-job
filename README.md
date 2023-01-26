# bybit-place-trailing-stops-job
Schedule job for entering a trailing stop loss based on open futures positions on the Bybit exchange. Job run in regular intervals defined in CRON table.

**Equation of trailing stop**
```
trailing_stop_loss_move = abs(entry_price-stop_loss_price)
```

## Keywords
**Schedule job**

In programming, a scheduled job is a task that is set to run at a specific time or at regular intervals. It's also known as a cron job or a scheduled task. Scheduled jobs are used to automate repetitive tasks, such as data backups, sending email reports, or updating a database.

**Algo trading**

Algo trading, also known as algorithmic trading, is the use of computer programs and algorithms to automatically execute trades in financial markets. The idea behind algo trading is to use sophisticated mathematical models and algorithms to analyze market data and make decisions about buying and selling assets in a faster and more efficient way than a human trader could. Algo trading is widely used in the stock, forex, and futures markets, and it can be used for a variety of different trading strategies, such as trend following, mean reversion, and statistical arbitrage. Algo trading is becoming increasingly popular among institutional investors and traders, due to its ability to execute trades quickly and with a high degree of accuracy.

**Bybit exchange**

Bybit is a cryptocurrency exchange that specializes in derivatives trading, particularly in the field of futures trading. It was founded in 2018 and it's based in Singapore. Bybit offers trading in a variety of digital assets, such as Bitcoin, Ethereum, EOS, and XRP, and it allows users to trade with leverage, up to 100x. The exchange uses a transparent and fair trading model, with a matching engine capable of processing up to 100,000 orders per second. Bybit offers a user-friendly and customizable trading interface, and also provide a mobile trading app for users to trade on-the-go. The platform also has a strong focus on security, implementing measures such as multi-signature technology and cold wallet storage to protect its users’ assets. It also offers a 24/7 customer support. Bybit is a growing exchange, and it's becoming increasingly popular among professional traders and institutional investors.

## How to build
```bash
make build
```

## How to prepare
```bash
make prepare
```

## How to run
```bash
make run
```

## Technologies
* Python 3
* Pandas
* Pybit

## Usefully links
* [CHANGELOG](CHANGELOG.md)
* [Pybit documentation](https://github.com/bybit-exchange/pybit)

## Contact
You can reach out for support on the [GeorgeQuantAnalyst](https://t.me/GeorgeQunatAnalyst) telegram chat.

## Contributors


<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
     <td align="center"><a href="https://github.com/GeorgeQuantAnalyst"><img src="https://avatars.githubusercontent.com/u/112611533?v=4" width="100px;" alt=""/><br /><sub><b>GeorgeQuantAnalyst</b></sub></a><br /><a href="https://github.com/GeorgeQuantAnalyst" title="Ideas">🤔</a></td>
    <td align="center"><a href="https://github.com/LucyQuantAnalyst"><img src="https://avatars.githubusercontent.com/u/115091833?v=4" width="100px;" alt=""/><br /><sub><b>LucyQuantAnalyst</b></sub></a><br /><a href="https://github.com/LucyQuantAnalyst" title="Code">💻</a></td>
  </tr>
</table>
