import requests
from bs4 import BeautifulSoup


okx_net_headers = {
    'authority' : 'www.okx.com',
    'method':'GET',
    'path':'/zh-hans/price',
    'scheme' :'https',
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding' : 'gzip, deflate, br, zstd',
    'accept-language' :'zh-CN,zh;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}


coin_full_name={
    'BTC': 'bitcoin-btc',
    'ETH': 'ethereum-eth',
    'XRP': 'xrp-xrp',
    'USDT': 'tether-usdt',
    'BNB': 'bnb-bnb',
    'SOL': 'solana-sol',
    'USDC':'usd-coin-usdc',
    'DOGE':'dogecoin-doge',
    'STETH':'lido-staked-ether',
    'TRX':'tron-trx',
    'ADA':'cardanp-ada',
    'WBTC':'wrapped-bitcoin-wbtc',
    'SUI':'sui-sui',
    'XLM':'stellar-slm',
    'LINK':'chainlink-link',
    'HBAR':':edera-hbar',
    'BCH':'bitcoin-cash-bch',
    'AVAX':'avalanche-avax LTC:litecoin-ltc',
    'LTC':'litecoin-ltc',
    'LEO':'unus-sed-leo-leo',
    'TON':'toncoin-ton',
    'SHIB':'shiba-lnu-shib',
    'UNI':'uniswap-uni',
    "DOT":"polkadot-dot",
    'PEPE':'pepe-pepe',
    'AAVE':'aave-aave',
    'CRO':'cronos-cro',
    'OKB':'okb-okb',
    'DAI':'dai-dai',
    'NEAR':'near-protocol',
    'ETC':'ethereum-classic-etc',
    'PI':'pi-network-pi',
    'ONDO':'ondo-ondo',
    'APT':'aptos-apt',
    'ICP':'internet-computer-icp',
    'JITOSOL':'jito-staked-sol-jitosol',
    'PENGU':'pudgy-penguins-pengu',
    'BONK':'bonk-bonk',
    'ALGO':'algorand',
    'ARB':'arbitrum-arb',
    'ATOM':'cosmos-atom',
    'RENDER':'ender-render',
    'WLD':'worldcoin-wld',
    'POL':'polygon-pol',
    'MKR':'maker-mkr',
    'TRUMP':'official-trump-trump',
    'FET':'fetch-ai-fet',
    'FIL':'filecoin-fil',
    'FLR':'flare-network-flr',
    'JUP':'jupiter-jup'
}

coin_news_net_header = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}