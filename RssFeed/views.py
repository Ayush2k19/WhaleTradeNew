from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
# Create your views here.
from .feedparser import parse

from datetime import date, datetime

today = date.today()


def index(request):
    NewsFeed1 = parse("https://cointelegraph.com/rss")
    NewsFeed2 = parse("https://news.bitcoin.com/feed/")
    NewsFeed3 = parse(
        "https://www.reddit.com/r/CryptoCurrency/top/.rss?format=xml")

    cointelegraph, bitcoin, reddit = [], [], []

    i = NewsFeed1.entries
    for a in i:
        datetime1 = a.published[5:25]
        dict = {
            'title': a.title[0:75],
            'img': a.links[1].href,
            'link': a.link,
            'date': a.published[5:16],

            'datetime2': datetime.strptime(datetime1, '%d %b %Y %H:%M:%S'),
            'tag': a.tags[0].term,
            'name': "CoinTelegraph"
        }
        cointelegraph.append(dict)

    i = NewsFeed2.entries

    for a in i:
        b = a.summary
        c = parse(b)
        img = c.feed.img["src"]

        datetime1 = a.published[5:25]

        dict = {
            'title': a.title[0:75],
            'link': a.link,
            'date': a.published[5:16],

            'datetime2': datetime.strptime(datetime1, '%d %b %Y %H:%M:%S'),
            'tag': a.tags[0].term,
            'img': img,
            'name': "Bitcoin"
        }
        bitcoin.append(dict)

    i = NewsFeed3.entries
    for a in i:

        c = a.content[0].value
        b = parse(c)
        datetime1 = a.updated[0:10] + " " + a.updated[11:19]

        if b.feed.has_key('img'):
            img = b.feed.img["src"]

            dict = {
                'title': a.title[0:75],
                'link': a.link,
                'date': a.updated[0:10],

                'datetime2': datetime.strptime(datetime1, '%Y-%m-%d %H:%M:%S'),
                'tag': a.tags[0].term,
                'img': img,
                'name': "Reddit"
            }
            reddit.append(dict)

        else:
            pass

    l = cointelegraph+bitcoin+reddit
    lf = sorted(l, key=lambda i: i['datetime2'], reverse=True)
    l1 = lf[0:9]
    l2 = lf[9:27]

    a = l1[0]
    b = l1[1]
    c = l1[2]
    d = l1[3]
    e = l1[4]
    f = l1[5]
    g = l1[6]
    h = l1[7]
    i = l1[8]

    context = {
        'a': a,
        'b': b,
        'c': c,
        'd': d,
        'e': e,
        'f': f,
        'g': g,
        'h': h,
        'i': i,
        'l2': l2,
        'today': today
    }
    return render(request, 'index.html', context)


def resources(request):
    c_wallets = [
        {'name': "My Ether Wallet",
         'link': "https://www.myetherwallet.com/",
         'img': "../static/links/wallets/myetherwallet.png",
         'pop': "abc"},
        {'name': "Blockchani Wallet",
         'link': "https://www.blockchain.com/wallet",
         'img': "../static/links/wallets/blockchainwallet.png",
         'pop': "def"},
        {'name': "Cryptonator Online Wallet",
         'link': "https://www.cryptonator.com/",
         'img': "../static/links/wallets/cryptonator.png",
         'pop': "agh"},
        {'name': "Coinbase Wallet",
         'link': "https://wallet.coinbase.com/",
         'img': "../static/links/wallets/coinbase.png",
         'pop': "pqr"},
        {'name': "Btc.com Wallet",
         'link': "https://wallet.btc.com/",
         'img': "../static/links/wallets/btc.com.png",
         'pop': "mnc"}

    ]

    h_wallets = [
        {'name': "Ledger",
         'link': "https://www.ledger.com",
         'img': "../static/links/hardwarewallets/ledger.png",
         'pop': "abc"},
        {'name': "Trezor",
         'link': "https://trezor.io/",
         'img': "../static/links/hardwarewallets/trezor.jpg",
         'pop': "abc"},
        {'name': "CoolWallet",
         'link': "https://www.coolwallet.io/",
         'img': "../static/links/hardwarewallets/coolwallet.png",
         'pop': "abc"},
        {'name': "BitLox",
         'link': "https://www.bitlox.com/",
         'img': "../static/links/hardwarewallets/bitlox.png",
         'pop': "abc"},
        {'name': "KeepKey",
         'link': "https://shapeshift.com/keepkey",
         'img': "../static/links/hardwarewallets/keepkey.png",
         'pop': "abc"}

    ]

    c_exchanges = [
        {'name': "Binance",
         'link': "https://www.binance.com/en?ref=15269217",
         'img': "../static/links/cryptoexchange/binance.png",
         'pop': "abc"},
        {'name': "Coinbase",
         'link': "https://www.coinbase.com/",
         'img': "../static/links/cryptoexchange/coinbase.png",
         'pop': "abc"},
        {'name': "BitMEX",
         'link': "https://www.bitmex.com/",
         'img': "../static/links/cryptoexchange/Bitmex.png",
         'pop': "abc"},
        {'name': "Huobi Global",
         'link': "https://www.huobi.com/en-us/",
         'img': "../static/links/cryptoexchange/huobi.png",
         'pop': "abc"},
        {'name': "KuCoin",
         'link': "https://www.kucoin.com/",
         'img': "../static/links/cryptoexchange/kucoin.png",
         'pop': "abc"}
    ]

    c_news = [
        {'name': "Cointelegraph",
         'link': "https://cointelegraph.com/",
         'img': "../static/links/news/cointelegraph.jpg",
         'pop': "abc"},
        {'name': "Coindesk",
         'link': "https://www.coindesk.com/",
         'img': "../static/links/news/coindesk.jpg",
         'pop': "abc"},
        {'name': "NewsBitcoin",
         'link': "https://news.bitcoin.com/",
         'img': "../static/links/news/bitcoin.com.png",
         'pop': "abc"},
        {'name': "CCN",
         'link': "https://www.ccn.com/",
         'img': "../static/links/news/ccn.png",
         'pop': "abc"},
        {'name': "BitcoinMagazine",
         'link': "https://bitcoinmagazine.com/",
         'img': "../static/links/news/bitcoinmagazine.png",
         'pop': "abc"}
    ]

    c_forums = [
        {'name': "Bitcointalk",
         'link': "https://bitcointalk.org/",
         'img': "../static/links/forums/bitcointalk.png",
         'pop': "abc"},
        {'name': "Bitcoin.com forum",
         'link': "https://forum.bitcoin.com/",
         'img': "../static/links/forums/bitcoin.com.png",
         'pop': "abc"},
        {'name': "Beermoneyforum",
         'link': "https://www.beermoneyforum.com/",
         'img': "../static/links/forums/beermoneyforum.png",
         'pop': "abc"},
        {'name': "Cryptocurrencytalk",
         'link': "https://cryptocurrencytalk.com/",
         'img': "../static/links/forums/cryptocurrencytalk.png",
         'pop': "abc"},
        {'name': "Mastersofcrypto Forum",
         'link': "https://mastersofcrypto.com/forum/",
         'img': "../static/links/forums/masterofcrypto.png",
         'pop': "abc"}
    ]

    r_cryptocurrency = [
        {'name': "r/Bitcoin",
         'link': "https://www.reddit.com/r/Bitcoin/",
         'img': "../static/links/reddit/r_bitcoin.png",
         'pop': "abc"},
        {'name': "r/Cryptocurrency",
         'link': "https://www.reddit.com/r/Cryptocurrency/",
         'img': "../static/links/reddit/r_cryptocurrency.png",
         'pop': "abc"},
        {'name': "r/ethereum",
         'link': "https://www.reddit.com/r/ethereum/",
         'img': "../static/links/reddit/r_ethererum.png",
         'pop': "abc"},
        {'name': "r/btc",
         'link': "https://www.reddit.com/r/btc/",
         'img': "../static/links/reddit/r_btc.png",
         'pop': "abc"},
        {'name': "r/litecoin",
         'link': "https://www.reddit.com/r/litecoin/",
         'img': "../static/links/reddit/r_litecoin.png",
         'pop': "abc"}
    ]

    b_mining_software = [
        {'name': "MinerGate",
         'link': "https://minergate.com/",
         'img': "../static/links/miningsoftwares/minergate.png",
         'pop': "abc"},
        {'name': "BTCMiner",
         'link': "https://mining.bitcoin.com/",
         'img': "../static/links/miningsoftwares/btcminer.png",
         'pop': "abc"},
        {'name': "RPCminer",
         'link': "https://en.bitcoin.it/wiki/RPC_Miner",
         'img': "../static/links/miningsoftwares/rpcminer.png",
         'pop': "abc"},
        {'name': "GUIMiner",
         'link': "https://cnguiminer.com/",
         'img': "../static/links/miningsoftwares/guiminer.png",
         'pop': "abc"},
        {'name': "GroupFabric",
         'link': "https://www.groupfabric.com/",
         'img': "../static/links/miningsoftwares/groupfabric.png",
         'pop': "abc"}
    ]

    m_pools = [
        {'name': "F2Pool",
         'link': "https://www.f2pool.com/",
         'img': "../static/links/minigpools/f2pool.png",
         'pop': "abc"},
        {'name': "Antpool",
         'link': "https://antpool.com/",
         'img': "../static/links/minigpools/antpool.png",
         'pop': "abc"},
        {'name': "SlushPool",
         'link': "https://slushpool.com/home/",
         'img': "../static/links/minigpools/slushpools.png",
         'pop': "abc"},
        {'name': "ViaBTC",
         'link': "https://www.viabtc.com/?lang=en_US",
         'img': "../static/links/minigpools/viabtc.png",
         'pop': "abc"},
        {'name': "Bitminter",
         'link': "https://bitminter.com/",
         'img': "../static/links/minigpools/btcminter.png",
         'pop': "abc"}
    ]

    u_ico = [
        {'name': "Fidelityhouse",
         'link': "https://icobench.com/ico/fidelity-house",
         'pop': "abc"},
        {'name': "Membrana",
         'link': "https://icobench.com/ico/membrana",
         'pop': "abc"},
        {'name': "Poof Of Toss",
         'link': "https://icobench.com/ico/toss",
         'pop': "abc"},
        {'name': "Elrond",
         'link': "https://elrond.com/",
         'pop': "abc"},
        {'name': "Aidus",
         'link': "https://aidus.io/",
         'pop': "abc"}
    ]

    airdrops = [
        {'name': "ICO Drops",
         'link': "https://icodrops.com/",
         'img': "../static/links/airdrop/ico_drops.png",
         'pop': "abc"},
        {'name': "Gift.ONE",
         'link': "https://www.facebook.com/GiftONE2018/",
         'img': "../static/links/airdrop/gift.one.png",
         'pop': "abc"},
        {'name': "Airdrop Alert",
         'link': "https://airdropalert.com/",
         'img': "../static/links/airdrop/air_dropalert.png",
         'pop': "abc"},
        {'name': "AirdropBob",
         'link': "https://www.airdropbob.com/",
         'img': "../static/links/airdrop/air_dropbob.png",
         'pop': "abc"},
        {'name': "Coin Airdrops",
         'link': "https://coinairdrops.com/",
         'img': "../static/links/airdrop/coin_airdrops.png",
         'pop': "abc"}
    ]

    c_calender = [

        {'name': "Coindar",
         'link': "https://coindar.org/",
         'img': "../static/links/calender/coin_dar.png",
         'pop': "abc"},
        {'name': "CoinMarketCal",
         'link': "https://coinmarketcal.com/en/",
         'img': "../static/links/calender/coinmarket_cal.png",
         'pop': "abc"},
        {'name': "Coin Events",
         'link': "https://www.coinevents.co/",
         'img': "../static/links/calender/coinevents.jfif",
         'pop': "abc"},
        {'name': "Cryptoknowmics",
         'link': "https://www.cryptoknowmics.com/coin-events",
         'img': "../static/links/calender/cryptoknowmics.png",
         'pop': "abc"},
        {'name': "Coins Calender",
         'link': "https://coinscalendar.com/",
         'img': "../static/links/calender/coins_calender.png",
         'pop': "abc"}
    ]

    charting = [
        {'name': "Coinmarketcap",
         'link': "https://coinmarketcap.com/",
         'img': "../static/links/charting/coinmarketcap.png",
         'pop': "abc"},
        {'name': "Investing.com",
         'link': "https://www.investing.com/",
         'img': "../static/links/charting/investing.com.png",
         'pop': "abc"},
        {'name': "Tradingview",
         'link': "https://in.tradingview.com/",
         'img': "../static/links/charting/tradingview.png",
         'pop': "abc"},
        {'name': "Etherscan.io",
         'link': "https://etherscan.io/",
         'img': "../static/links/charting/etherscan.png",
         'pop': "abc"},
        {'name': "Blockchain",
         'link': "https://www.blockchain.com/",
         'img': "../static/links/charting/blockchain.com.png",
         'pop': "abc"}
    ]

    c_gambling = [
        {'name': "Luckygames.io",
         'link': "https://luckygames.io/",
         'img': "../static/links/gambling/luckygames.png",
         'pop': "abc"},
        {'name': "bitStarz",
         'link': "https://www.bitstarz.com/",
         'img': "../static/links/gambling/bitstarz logo.png",
         'pop': "abc"},
        {'name': "Nitrogensports",
         'link': "https://nitrogensports.eu/",
         'img': "../static/links/gambling/Nitrogensports.jpg",
         'pop': "abc"},
        {'name': "Primedice",
         'link': "https://primedice.com/",
         'img': "../static/links/gambling/primedice.png",
         'pop': "abc"},
        {'name': "mBit Casino",
         'link': "https://www.mbitcasino.com/",
         'img': "../static/links/gambling/mBit.png",
         'pop': "abc"}

    ]

    c_tracking = [
        {'name': "CoinTracking",
         'link': "https://cointracking.info/",
         'img': "../static/links/tracking/cointracking.png",
         'pop': "abc"},
        {'name': "coin.fyi",
         'link': "https://coin.fyi/",
         'img': "../static/links/tracking/coin.fyi.png",
         'pop': "abc"},
        {'name': "Blox",
         'link': "https://www.blox.io/",
         'img': "../static/links/tracking/blox.png",
         'pop': "abc"},
        {'name': "Altpocket",
         'link': "https://altpocket.io/",
         'img': "../static/links/tracking/altpocket.png",
         'pop': "abc"},
        {'name': "Blockfolio",
         'link': "https://blockfolio.com/",
         'img': "../static/links/tracking/blockfolio.png",
         'pop': "abc"}
    ]

    context = {
        'c_wallets': c_wallets,
        'h_wallets': h_wallets,
        'c_exchanges': c_exchanges,
        'c_news': c_news,
        'c_forums': c_forums,
        'r_cryptocurrency': r_cryptocurrency,
        'b_mining_software': b_mining_software,
        'm_pools': m_pools,
        'u_ico': u_ico,
        'airdrops': airdrops,
        'c_calender': c_calender,
        'charting': charting,
        'c_gambling': c_gambling,
        'c_tracking': c_tracking

    }
    return render(request, 'resources.html', context)


def trending(request):
    return render(request, "trending.html")


def registeration(request):
    return render(request, "register.html")


def telegramShow(request):
    return render(request, "telegram_show.html")


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')
    #fields= '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('home')
    # fields=['title','body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
