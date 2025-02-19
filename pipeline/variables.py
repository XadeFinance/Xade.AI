import json

sectors = [    
    "AI",
    "AI-Agents",
    "Analytics",
    "Base-Ecosystem",
    "Bitcoin-Ecosystem",
    "BRC-20",
    "DAO",
    "DeFAI",
    "DeFi",
    "DePin",
    "DeSci",
    "Events",
    "Exchange-Tokens",
    "Fan-Tokens",
    "Gambling",
    "Gaming & Metaverse",
    "Layer-1",
    "Layer-2",
    "Lending/Borrowing",
    "Liquid-staking-Derivatives",
    "Made-In-USA",
    "Memecoins",
    "NFT",
    "Oracles",
    "Real-Estate",
    "Real-World-Assets",
    "Runes",
    "SocialFi",
    "Solana-Ecosystem",
    "Sports",
    "Stablecoin",
    "Stacks-Ecosystem",
    "Storage",
    "Wallets",
    "Zero-Knowledge-Proofs"]

with open('pipeline/lunarcrush-endpoints.json', 'r') as file:
    lunarcrush_endpoints = json.load(file)

with open('pipeline/mobula-endpoints.json', 'r') as file:
    mobula_endpoints = json.load(file)

data_output_format = """
DATA AGENT CHAIN-OF-THOUGHT:
- The query targets a predefined sector: DeSci.
- I will use the LunarCrush Coins V2 API to identify the top coins related to DeSci as well as their social metrics.
- Supplement this with detailed market and on-chain metrics via the Mobula API for the identified coins.
- Remember: Use coin symbols only.
- This approach ensures efficiency by leveraging predefined sector endpoints without requiring an identification phase.

FINAL API CALL STRUCTURE:
```json
[
  {
    "provider": "lunarcrush",
    "endpoint": "/public/coins/list/v2?filter=DeSci",
    "description": "Retrieve coins, posts, and news related to the DeSci sector using coin symbols.",
    nested_calls: [
      {
        "provider": "mobula",
        "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3",
        "description": "Retrieve detailed market and on-chain data for the identified DeSci coins."
      }
    ],
  }
]
```
"""

avoid_tokens = [
    "BTC", "ETH", "WBTC", "stETH", "rETH", "cbETH", "LSETH", "USDC", "USDT", "USDC.e",
    "BNB", "MATIC", "AVAX", "SOL", "ADA", "DOT", "DAI", "ETC", "OP", "ARB", "UNI", "LDO",
    "sfrxETH", "mETH", "eETH", "ankrETH", "BETH", "sETH2", "oETH", "WBETH", "PETH", 
    "wstETH", "vETH", "SWETH", "RETH2", "RSETH"
]

sorting_parameters = {
    "alt_rank": "AltRank™ evaluates both market and social data. This ranking system assesses an asset's price movement alongside its social activity indicators, offering a comprehensive view of its current standing in the crypto market.",
    "galaxy_score": "The LunarCrush Galaxy Score™ is a proprietary score that is constantly measuring a cryptocurrency against itself with respect to the community metrics pulled in from across the web.",
    "sentiment": "% of posts (weighted by interactions) that are positive. 100% means all posts are positive, 50% is half positive and half negative, and 0% is all negative posts."
    }

with open('pipeline/blockchains.json', 'r') as file:
    blockchain_ids = json.load(file)

blockchain_ids = { entry["name"]: entry["chainId"] for entry in blockchain_ids["data"] }