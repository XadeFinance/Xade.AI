
master_llm_fewshot = [
    # Example 1 – In-Depth Analysis of Top 5 ReFi Agents
    """
    USER QUERY:
    Give me in-depth analysis of the top 5 ReFi agents in the market.

    MASTER LLM OUTPUT:

    About the Agent:
    🚀 ReFi Alpha: Your Regenerative Finance Powerhouse 🌱

    ReFi Alpha is your go-to AI analyst for uncovering the hottest Regenerative Finance (ReFi) projects in crypto. Armed with on-chain analytics, deep market intelligence, and real-time social sentiment tracking, it delivers precision-crafted buy/sell insights for sustainability-driven investors. ♻️
    🔍 What ReFi Alpha Does Best:
    ✅ Analyzes top 5 ReFi protocols in real-time 📊
    ✅ Deciphers complex on-chain data into clear, actionable strategies 💡
    ✅ Tracks sustainability trends & market sentiment 🌍

    ReFi Alpha is sharp, data-driven, and no-nonsense—expect concise insights, high-impact alpha, and eco-conscious strategies that help you invest with both profit and purpose. Because in DeFi, the future is regenerative. 🚀♻️

    
    High-Level Execution Plan:
      1. Identification Phase:
         - Recognize that “ReFi” is a niche topic not covered in the predefined sectors.
         - Specify that the Data Agent must use the LunarCrush Topics API solely for identifying the top 5 ReFi coins (identification-only).
      2. Data Retrieval Phase:
         - Once the coins are identified, instruct the Data Agent to collect detailed market and on-chain data via the Mobula API.
         - Retrieve social sentiment data using the LunarCrush Coin V1 API.
      3. Analysis Phase:
         - Direct the Analysis Agent to integrate these data streams to generate comprehensive insights and actionable recommendations.

    - Rationale & Chain-of-Thought:
      - Isolating the identification step is critical because ReFi isn’t a predefined sector.
      - Using distinct APIs ensures that each agent specializes—one for identifying coins and the other for gathering detailed data—avoiding redundancy.

    - Execution Flow Overview:
      - The plan flows as follows: Query assessment → Identification (via LunarCrush Topics API) → Data retrieval (via Mobula and LunarCrush Coin V1) → Analysis synthesis.
    """,

    # Example 2 – Latest News Updates on Specific Coins
    """
    USER QUERY:
    Give me the latest news updates on Ethereum, Arbitrum, Injective, and Stacks.

    MASTER LLM OUTPUT:

    About the Agent:
      📰 BlockPulse: Your High-Speed Crypto News Oracle ⚡

      BlockPulse is your real-time AI-powered news aggregator, built to scan, filter, and decode the most impactful crypto headlines before the market reacts. 🚀 From Ethereum’s latest upgrade to Arbitrum ecosystem moves, regulatory shake-ups, and DeFi innovations, BlockPulse ensures you’re always ahead of the curve.

      🔍 What BlockPulse Does Best:
      ✅ Aggregates & analyzes crucial crypto news in real time 🏎️
      ✅ Filters signal from noise—no hype, just market-moving insights 📡
      ✅ Tracks social sentiment to predict potential price shifts 📊

      With a lightning-fast, no-BS approach, BlockPulse delivers concise, high-impact updates so you never miss the next big crypto play. Because in DeFi, timing is everything. ⏳🔥

      
    High-Level Execution Plan:
      1. Query Assessment:
         - Identify that the query is coin-specific and centers on retrieving the latest news and social sentiment.
      2. Data Retrieval Phase:
         - Direct the Data Agent to fetch the latest news updates for each specified coin using the appropriate LunarCrush news endpoints.
      3. Analysis Phase:
         - Instruct the Analysis Agent to distill and synthesize the news data, identifying key trends and correlating them with market sentiment.

    - Rationale & Chain-of-Thought:
      - Direct coin queries bypass the need for an identification phase, enabling a streamlined approach.
      - This focused strategy ensures that news aggregation is current and precisely targeted for each coin.

    - Execution Flow Overview:
      - The execution flow: Query assessment → Direct news retrieval via LunarCrush → Analysis and summarization.
    """,

    # Example 3 – Top Projects on Polygon
    """
    **USER QUERY:**
    What are the top projects on Polygon right now?

    **MASTER LLM BLUEPRINT OUTPUT:**

    About the Agent:
      Introducing PolygonPulse—a next-gen AI analyst laser-focused on unraveling the fast-moving world of the Polygon blockchain. By combining real-time market analytics, deep on-chain insights, and social sentiment tracking, it delivers clear, data-driven strategies for traders and investors navigating the Polygon DeFi ecosystem.

      ⚡ PolygonPulse: Your Edge in the Polygon Ecosystem 🌐

      PolygonPulse doesn’t just track trends—it identifies momentum before it explodes. Whether it’s liquidity surges, trading volume spikes, or ecosystem shifts, this AI ensures you stay ahead of the curve in one of DeFi’s most vibrant networks.

      🔍 What PolygonPulse Does Best:
      ✅ Pinpoints high-growth projects gaining traction on Polygon 🚀
      ✅ Analyzes liquidity, trading volumes, and whale movements 📊
      ✅ Deciphers social sentiment to predict potential breakouts 🔥

      With precise, no-fluff insights, PolygonPulse delivers the alpha you need to capitalize on the next big move in the Polygon ecosystem. Because in DeFi, timing is everything. ⏳💎


    High-Level Execution Plan:
      1. **Query Assessment:**
        - Recognize that the query is blockchain-specific (Polygon) and that Polygon is not part of the predefined LunarCrush sectors.
      2. **Data Retrieval Phase:**
        - Instruct the Data Agent to use the LunarCrush Coins v2 API exclusively to fetch comprehensive data on Polygon projects. No filters are applied, allowing the API to return all relevant data for the Polygon blockchain.
      3. **Analysis Phase:**
        - Direct the Analysis Agent to rank these projects based on metrics such as trading volume, liquidity, and on-chain interactions.

    - **Rationale & Chain-of-Thought:**
      - For blockchain-specific queries outside of predefined sectors, relying solely on the LunarCrush Coins v2 API ensures data consistency and leverages its versatility for multiple use cases.
      - A clear, linear process ensures targeted data retrieval and accurate project ranking.

    - **Execution Flow Overview:**
      - The process flows as follows: Query assessment → Data retrieval via LunarCrush Coins v2 API → Analysis and ranking.
    """,

    # Example 4 – Detailed Analysis of the DeSci Sector
    """
    USER QUERY:
    Give me a detailed analysis of the DeSci (Decentralized Science) sector in crypto.

    MASTER LLM OUTPUT:

    About the Agent:
    Introducing DeSciOracle—an AI analyst at the frontier of Decentralized Science (DeSci). Designed to decode the intersection of blockchain and scientific innovation, DeSciOracle tracks funding trends, groundbreaking research, and decentralized collaborations to provide a crystal-clear view of the evolving DeSci landscape.

    🔬 DeSciOracle: Your Gateway to the Future of Science & Blockchain 🚀

    DeSciOracle isn’t just another AI—it’s a visionary guide into how blockchain is disrupting traditional scientific models. By analyzing on-chain funding, community sentiment, and the latest research breakthroughs, it delivers insights that matter for investors, researchers, and innovators shaping the future of science.

    🔍 What DeSciOracle Does Best:
    ✅ Identifies top DeSci projects & funding trends before they go mainstream 🌍
    ✅ Analyzes innovation pipelines to predict the next big scientific leap 🔭
    ✅ Tracks real-time community sentiment to assess adoption potential 📊

    With a forward-thinking, research-driven approach, DeSciOracle ensures you stay ahead in the race to decentralize science. Because in the DeSci revolution, knowledge is power—and blockchain is the key. 🔑💡

    
    High-Level Execution Plan:
      1. Query Assessment:
         - Recognize that DeSci is a predefined sector within LunarCrush.
      2. Data Retrieval Phase:
         - Instruct the Data Agent to retrieve sector-specific data (coins, posts, and news) using the LunarCrush Sector API.
         - Supplement this with detailed market data via the Mobula API.
      3. Analysis Phase:
         - Direct the Analysis Agent to integrate market, social, and news data to produce a thorough analysis, highlighting trends, risks, and opportunities in the DeSci sector.

    - Rationale & Chain-of-Thought:
      - Leveraging predefined sector endpoints enhances efficiency and accuracy.
      - Separating social/news data (via LunarCrush) from market data (via Mobula) ensures a robust, multidimensional analysis.

    - Execution Flow Overview:
      - The blueprint is: Query assessment → Data retrieval (using LunarCrush Sector API & Mobula API) → Data synthesis and comprehensive analysis.
    """,
    
        # Example 5 – Multi-Sector Query: NFTs and DeFi
    """
    USER QUERY:
    Provide an analysis of the latest trends in both the NFTs and DeFi sectors.

    MASTER LLM OUTPUT:

    🌐 About the Agent:
      Meet TrendFusion—the ultimate AI trendspotter that bridges the gap between NFTs and DeFi. By fusing insights from on-chain analytics, social sentiment, and market movements, TrendFusion deciphers how DeFi liquidity and NFT hype intertwine, giving users a complete picture of digital asset trends.

      🚀 TrendFusion: Where DeFi Meets NFTs 🎨📊

      TrendFusion isn’t just tracking markets—it’s connecting the dots. Whether it’s NFT-backed lending, liquidity surges, or trending collections, this AI ensures you see the bigger picture before the market moves.

      🔍 What TrendFusion Does Best:
      ✅ Analyzes DeFi & NFT trends side-by-side for cross-market insights 🔄
      ✅ Deciphers liquidity flows, social sentiment, and on-chain activity 📡
      ✅ Identifies hidden correlations that drive both sectors forward 🔥

      With a sharp, pattern-seeking mindset, TrendFusion delivers next-level market intelligence—because in crypto, understanding the fusion of trends is the real alpha. ⚡🔗

      
    High-Level Execution Plan:
      1. Query Assessment:
         - Identify that the query targets two distinct, predefined sectors: NFTs and DeFi.
         - Since both sectors are predefined, there is no need for identification APIs.
      2. Data Retrieval Phase:
         - Instruct the Data Agent to retrieve sector-specific data (coins, posts, and news) for NFTs and DeFi using the LunarCrush Sector API.
         - Supplement with relevant market data from the Mobula API if necessary.
      3. Analysis Phase:
         - Direct the Analysis Agent to independently analyze the data from each sector and then synthesize comparative insights to highlight similarities, differences, and overall trends.

    - Rationale & Chain-of-Thought:
      - Handling multi-sector queries requires parallel processing to ensure clear and distinct data streams for each sector.
      - This separation allows for accurate comparative analysis and prevents data conflation, ensuring robust insights.

    - Execution Flow Overview:
      - The process flows as follows: Query assessment → Retrieve data for NFTs and DeFi separately → Synthesize and compare insights.
    """,

    # Example 6 – Historical Analysis of Bitcoin
    """
    USER QUERY:
    Give me a historical trend analysis of Bitcoin over the past 5 years.

    MASTER LLM OUTPUT:

    📜 About the Agent:
      Meet SatoshiChronicle—your AI-powered Bitcoin historian and trend analyst. With an encyclopedic knowledge of Bitcoin’s market cycles, halvings, and macro events, it deciphers the past to predict the future. By analyzing decades of price action, institutional shifts, and on-chain data, SatoshiChronicle provides a long-term perspective on Bitcoin’s trajectory.

      🔍 SatoshiChronicle: Unlocking Bitcoin’s Past to Forecast Its Future 🔮

      SatoshiChronicle isn’t here for short-term noise—it’s built for macro-level insights. Whether it’s post-halving trends, historic bull/bear cycles, or the impact of major regulatory events, this AI helps HODLers, traders, and institutions make data-driven decisions with historical context.

      🔍 What SatoshiChronicle Does Best:
      ✅ Tracks Bitcoin’s long-term market cycles & historical price action 📈
      ✅ Correlates macro events with BTC price movements for deeper insights 🌎
      ✅ Provides institutional-grade, long-horizon trend analysis 🏛️

      With a deep, research-first mindset, SatoshiChronicle is your AI companion in understanding Bitcoin’s past, present, and future—because in crypto, history doesn’t just repeat, it rhymes. 🔄⏳

      
    High-Level Execution Plan:
      1. Query Assessment:
         - Recognize that the query is coin-specific and requires an analysis of historical trends spanning 5 years.
      2. Data Retrieval Phase:
         - Direct the Data Agent to retrieve historical time-series market data for Bitcoin using Mobula and/or LunarCrush time-series endpoints.
         - Instruct retrieval of historical social sentiment data, if available, to provide contextual insights.
      3. Analysis Phase:
         - Direct the Analysis Agent to conduct a detailed trend analysis, correlating market data with major historical events and shifts in community sentiment.
         - Emphasize the identification of long-term trends, cycles, and potential catalysts for future movements.

    - Rationale & Chain-of-Thought:
      - Historical analysis demands robust, continuous data and careful correlation with past events.
      - This approach ensures that trends are interpreted within a broader historical context, yielding reliable insights.

    - Execution Flow Overview:
      - The blueprint is: Query assessment → Retrieve historical market and sentiment data → Perform trend analysis and event correlation.
    """,

    # Example 7 – Wallet Portfolio Analysis via Mobula's Wallet Explorer API
    """
    USER QUERY:
    Provide a detailed analysis of the wallet portfolio for wallet address 0xABC123XYZ.

    MASTER LLM OUTPUT:

    💼 About the Agent:
      Introducing AlphaLedger—your AI-powered portfolio intelligence engine. Designed for crypto investors who demand precision, AlphaLedger provides deep, real-time insights into wallet composition, asset distribution, and historical performance trends. Whether you’re optimizing holdings or tracking whale movements, this AI ensures you stay in control of your crypto strategy.

      📊 AlphaLedger: Master Your Crypto Portfolio Like a Pro 🚀

      AlphaLedger doesn’t just show your balances—it deciphers them. From real-time market valuations to historical P&L tracking, it delivers actionable insights that help you maximize gains and mitigate risks.

      🔍 What AlphaLedger Does Best:
      ✅ Breaks down wallet asset distribution for clear portfolio insights 🏦
      ✅ Analyzes historical performance trends to refine investment strategy 📈
      ✅ Identifies risk exposure & diversification opportunities for smarter decisions ⚖️

      With a sharp, data-driven mindset, AlphaLedger transforms wallet data into strategic intelligence—because in crypto, knowledge is the ultimate asset. 🔥📊


    High-Level Execution Plan:
      1. Query Assessment:
         - Recognize that the query is wallet-specific, focusing on detailed portfolio analysis for a given wallet address.
         - Note that the analysis should include current holdings and, optionally, historical trends.
      2. Data Retrieval Phase:
         - Instruct the Data Agent to retrieve current wallet portfolio data using Mobula’s Wallet Explorer API (e.g., /wallet/portfolio endpoint).
         - Optionally, specify the retrieval of historical balance data (/wallet/history) or transaction counts (/warehouse/wallet-transactions-count) for added context.
      3. Analysis Phase:
         - Direct the Analysis Agent to integrate the portfolio data with current market metrics from the Mobula Market API.
         - Instruct the Analysis Agent to analyze asset distribution, overall valuation, and historical trends.
         - If data is insufficient, mandate that the Analysis Agent clearly state: "Insufficient data available for reliable insights."
    
    - Rationale & Chain-of-Thought:
      - Wallet analysis requires a specialized approach, distinct from coin or sector analysis.
      - Leveraging the Mobula Wallet Explorer API ensures detailed retrieval of portfolio information, while supplementary data enhances context.
      - Transparent handling of data limitations is essential to maintain analytical integrity.

    - Execution Flow Overview:
      - The blueprint outlines: Query assessment → Retrieve wallet portfolio (and supplementary) data via Mobula → Integrate market data → Synthesize a comprehensive wallet analysis.
    """,
    """
    USER QUERY:
    Provide a comprehensive analysis of trending projects in crypto.

    MASTER LLM OUTPUT:

    📈 About the Agent:
        Introducing AlphaTrend—your AI-powered crypto trendspotter and market oracle. With an unparalleled ability to detect emerging projects, AlphaTrend deciphers real-time market data, on-chain movements, and social sentiment to deliver next-level insights before the crowd catches on.

        🚀 AlphaTrend: Your Guide to the Next Big Crypto Plays 🔥

        AlphaTrend isn’t just another market analyst—it’s your edge in the fast-moving crypto world. By fusing LunarCrush and Mobula API insights, it filters signal from noise to pinpoint the hottest projects gaining momentum.

        🔍 What AlphaTrend Does Best:
        ✅ Scans real-time market data to identify emerging crypto trends 🚀
        ✅ Analyzes social sentiment & engagement metrics for early signals 🧠
        ✅ Evaluates project performance & sustainability for smarter decisions 📊

        With a sharp, trend-driven mindset, AlphaTrend keeps you ahead of market shifts, ensuring you never miss the next moonshot. Because in crypto, timing is everything. ⏳⚡


    High-Level Execution Plan:
    1. Query Assessment:
        - Recognize that the query targets trending projects across the entire crypto market, necessitating a broad, integrated view.
        - Identify that the LunarCrush Coins v2 API is ideal for capturing a comprehensive snapshot of trending projects (via aggregated market cap, social engagement, and trading volume metrics).
        - Note: For detailed individual project analysis, LunarCrush Coin v1 can be used; however, the focus here is on market-wide trends.
    2. Data Retrieval Phase:
        - Instruct the Data Agent to use the LunarCrush Coins v2 API to retrieve a full list of trending projects, ensuring the API call is filtered and sorted based on user-specified criteria (e.g., highest social engagement, market cap, or trading volume).
        - Additionally, direct the Data Agent to supplement this data with detailed market metrics from the Mobula API to capture trading dynamics, liquidity, and on-chain activity.
    3. Analysis Phase:
        - Direct the Analysis Agent to synthesize the aggregated data into a comprehensive report.
        - The report should identify key trending projects, highlight emerging market trends, and evaluate overall market sentiment, thereby providing a holistic view of the crypto market.
    
    - Rationale & Chain-of-Thought:
    - Utilizing the LunarCrush Coins v2 API as the identifier ensures broad coverage of trending projects across the market.
    - Integrating supplementary data from Mobula deepens the analysis by adding insights into trading volumes, liquidity, and on-chain behavior.
    - Filtering and sorting the data according to user-defined parameters focuses the analysis on the most significant projects, reducing noise and enhancing actionable insights.
    
    - Execution Flow Overview:
    - The blueprint flows as follows: Query assessment → Retrieve trending projects using LunarCrush Coins v2 (filtered/sorted as per criteria) + Supplement with Mobula market data → Synthesize and deliver a comprehensive analysis of trending crypto projects.
    """
]


data_fewshot = [
    # Example 1 – In-Depth Analysis of Top 5 ReFi Agents
    """
    USER QUERY:
    Give me in-depth analysis of the top 5 ReFi agents in the market.

    MASTER LLM OUTPUT:

    About the Agent:
    🚀 ReFi Alpha: Your Regenerative Finance Powerhouse 🌱

    ReFi Alpha is your go-to AI analyst for uncovering the hottest Regenerative Finance (ReFi) projects in crypto. Armed with on-chain analytics, deep market intelligence, and real-time social sentiment tracking, it delivers precision-crafted buy/sell insights for sustainability-driven investors. ♻️
    🔍 What ReFi Alpha Does Best:
    ✅ Analyzes top 5 ReFi protocols in real-time 📊
    ✅ Deciphers complex on-chain data into clear, actionable strategies 💡
    ✅ Tracks sustainability trends & market sentiment 🌍

    ReFi Alpha is sharp, data-driven, and no-nonsense—expect concise insights, high-impact alpha, and eco-conscious strategies that help you invest with both profit and purpose. Because in DeFi, the future is regenerative. 🚀♻️

    
    High-Level Execution Plan:
      1. Identification Phase:
         - Recognize that “ReFi” is a niche topic not covered in the predefined sectors.
         - Specify that the Data Agent must use the LunarCrush Topics API solely for identifying the top 5 ReFi coins (identification-only).
      2. Data Retrieval Phase:
         - Once the coins are identified, instruct the Data Agent to collect detailed market and on-chain data via the Mobula API.
         - Retrieve social sentiment data using the LunarCrush Coin V1 API.
      3. Analysis Phase:
         - Direct the Analysis Agent to integrate these data streams to generate comprehensive insights and actionable recommendations.

    - Rationale & Chain-of-Thought:
      - Isolating the identification step is critical because ReFi isn’t a predefined sector.
      - Using distinct APIs ensures that each agent specializes—one for identifying coins and the other for gathering detailed data—avoiding redundancy.

    - Execution Flow Overview:
      - The plan flows as follows: Query assessment → Identification (via LunarCrush Topics API) → Data retrieval (via Mobula and LunarCrush Coin V1) → Analysis synthesis.


    DATA AGENT OUTPUT:
    
    DATA AGENT CHAIN-OF-THOUGHT:
    - The query requires an in-depth analysis of the top 5 ReFi projects, including buy/sell ratings.
    - Since “ReFi” or "Regenerative Finance" is not a standard sector, I must treat it as a niche topic.
    - I must first identify the relevant coins using the LunarCrush Topics API.
    - After identification, I should call the social data for the coins using LunarCrush Coin V1 and market data using Mobula Market Multi-data for coin1,coin2,coin3,coin4,coin5.
    - In this identification step, only coin symbols should be used—not asset names, addresses, or IDs.
    - After Lunarcrush Topics, the APIs that need to be queried are:
      - A Mobula API call (using `/market/multi-data`) to fetch detailed market and on-chain data for these coins.
      - Individual LunarCrush Coins v1 API calls to fetch social sentiment for each coin.
    - These API calls align with the query as this data should be enough for the Analysis Agent to provide a buy/sell rating for identified ReFi projects. Also, all these endpoints exist.
    - This approach also soemwhat aligns with the Master LLM’s suggestion but is more specific and completely accurate.
    - Now, I must create the final API call structure based on the identified coins and the required data.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "lunarcrush",
        "endpoint": "/public/topic/refi/v1",
        "description": "Identify trending topics related to ReFi and extract the top 5 ReFi coin symbols.",
        "nested_calls": [
          {
            "provider": "mobula",
            "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3,coin4,coin5",
            "description": "Retrieve detailed market and on-chain data for the identified ReFi coins using their symbols."
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin1/v1",
            "description": "Retrieve social sentiment data for coin1"
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin2/v1",
            "description": "Retrieve social sentiment data for coin2."
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin3/v1",
            "description": "Retrieve social sentiment data for coin3."
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin4/v1",
            "description": "Retrieve social sentiment data for coin4."
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin5/v1",
            "description": "Retrieve social sentiment data for coin5."
          }
        ]
      }
    ]
    ```
    """,

    # Example 2 – Latest News Updates on Specific Coins
    """
    USER QUERY:
    Give me the latest news updates on Ethereum, Arbitrum, Injective, and Stacks.

    MASTER LLM OUTPUT:

    About the Agent:
      📰 BlockPulse: Your High-Speed Crypto News Oracle ⚡

      BlockPulse is your real-time AI-powered news aggregator, built to scan, filter, and decode the most impactful crypto headlines before the market reacts. 🚀 From Ethereum’s latest upgrade to Arbitrum ecosystem moves, regulatory shake-ups, and DeFi innovations, BlockPulse ensures you’re always ahead of the curve.

      🔍 What BlockPulse Does Best:
      ✅ Aggregates & analyzes crucial crypto news in real time 🏎️
      ✅ Filters signal from noise—no hype, just market-moving insights 📡
      ✅ Tracks social sentiment to predict potential price shifts 📊

      With a lightning-fast, no-BS approach, BlockPulse delivers concise, high-impact updates so you never miss the next big crypto play. Because in DeFi, timing is everything. ⏳🔥

      
    High-Level Execution Plan:
      1. Query Assessment:
         - Identify that the query is coin-specific and centers on retrieving the latest news and social sentiment.
      2. Data Retrieval Phase:
         - Direct the Data Agent to fetch the latest news updates for each specified coin using the appropriate LunarCrush news endpoints.
      3. Analysis Phase:
         - Instruct the Analysis Agent to distill and synthesize the news data, identifying key trends and correlating them with market sentiment.

    - Rationale & Chain-of-Thought:
      - Direct coin queries bypass the need for an identification phase, enabling a streamlined approach.
      - This focused strategy ensures that news aggregation is current and precisely targeted for each coin.

    - Execution Flow Overview:
      - The execution flow: Query assessment → Direct news retrieval via LunarCrush → Analysis and summarization.

    DATA AGENT OUTPUT:

    DATA AGENT CHAIN-OF-THOUGHT:
    •	The user specifically requests the latest news updates and social sentiment for four coins: Ethereum (ETH), Arbitrum (ARB), Injective (INJ), and Stacks (STX).
    •	This is a coin-specific query with known symbols, so there is no need for an identification phase.
    •	The user wants news updates, which can be obtained from the LunarCrush topics news endpoint.
    •	The user also wants social sentiment data, which is available via the LunarCrush Coins v1 endpoint.
    •	There is no mention of market or on-chain data, so Mobula API calls are not necessary.
    •	To fulfill the request, I will construct separate calls for each coin—one for news and one for social sentiment.
    •	This approach directly addresses the user’s query while maintaining consistency with the Master LLM suggestions and the new instructions.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "lunarcrush",
        "endpoint": "/public/topics/ETH/news/v1",
        "description": "Retrieve the latest news updates for Ethereum (ETH)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/ETH/v1",
        "description": "Retrieve social sentiment data for Ethereum (ETH)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/topics/ARB/news/v1",
        "description": "Retrieve the latest news updates for Arbitrum (ARB)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/ARB/v1",
        "description": "Retrieve social sentiment data for Arbitrum (ARB)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/topics/INJ/news/v1",
        "description": "Retrieve the latest news updates for Injective (INJ)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/INJ/v1",
        "description": "Retrieve social sentiment data for Injective (INJ)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/topics/STX/news/v1",
        "description": "Retrieve the latest news updates for Stacks (STX)."
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/STX/v1",
        "description": "Retrieve social sentiment data for Stacks (STX)."
      }
    ]
    ```
    """,

    # Example 3 – Top Projects on Polygon
    """
    USER QUERY:
    What are the top projects on Polygon right now?

  MASTER LLM OUTPUT:

    About the Agent:
      Introducing PolygonPulse—a next-gen AI analyst laser-focused on unraveling the fast-moving world of the Polygon blockchain. By combining real-time market analytics, deep on-chain insights, and social sentiment tracking, it delivers clear, data-driven strategies for traders and investors navigating the Polygon DeFi ecosystem.

      ⚡ PolygonPulse: Your Edge in the Polygon Ecosystem 🌐

      PolygonPulse doesn’t just track trends—it identifies momentum before it explodes. Whether it’s liquidity surges, trading volume spikes, or ecosystem shifts, this AI ensures you stay ahead of the curve in one of DeFi’s most vibrant networks.

      🔍 What PolygonPulse Does Best:
      ✅ Pinpoints high-growth projects gaining traction on Polygon 🚀
      ✅ Analyzes liquidity, trading volumes, and whale movements 📊
      ✅ Deciphers social sentiment to predict potential breakouts 🔥

      With precise, no-fluff insights, PolygonPulse delivers the alpha you need to capitalize on the next big move in the Polygon ecosystem. Because in DeFi, timing is everything. ⏳💎


    High-Level Execution Plan:
      1. **Query Assessment:**
        - Recognize that the query is blockchain-specific (Polygon) and that Polygon is not part of the predefined LunarCrush sectors.
      2. **Data Retrieval Phase:**
        - Instruct the Data Agent to use the LunarCrush Coins v2 API exclusively to fetch comprehensive data on Polygon projects. No filters are applied, allowing the API to return all relevant data for the Polygon blockchain.
      3. **Analysis Phase:**
        - Direct the Analysis Agent to rank these projects based on metrics such as trading volume, liquidity, and on-chain interactions.

    - **Rationale & Chain-of-Thought:**
      - For blockchain-specific queries outside of predefined sectors, relying solely on the LunarCrush Coins v2 API ensures data consistency and leverages its versatility for multiple use cases.
      - A clear, linear process ensures targeted data retrieval and accurate project ranking.

    - **Execution Flow Overview:**
      - The process flows as follows: Query assessment → Data retrieval via LunarCrush Coins v2 API → Analysis and ranking.


    DATA AGENT OUTPUT:

    DATA AGENT CHAIN-OF-THOUGHT:
    - The query requires identifying the top projects on polygon and their analysis
    - Since Polygon is not a predefined or standard sector but it is a blockchain, I must treat it as a blockchain specific query.
    - I must first identify the relevant coins using the Mobula Blockchain Pairs API.
    - In this identification step, only coin symbols should be used—not asset names, addresses, or IDs. I should also include a sorting parameter. "volume_5min" should be appropriate for the user query.
    - After identification, I should call the social data for the coins using LunarCrush Coin V1 and market data using Mobula Market Multi-data for coin1,coin2,coin3,coin4,coin5.
    - After Mobula Blockchain Pairs, the APIs that need to be queried are:
      - A Mobula API call (using `/market/multi-data`) to fetch detailed market and on-chain data for these coins.
      - Individual LunarCrush Coins v1 API calls to fetch social sentiment for each coin.
    - These API calls align with the query as this data should be enough for the Analysis Agent to provide analysis for trending projects on Polygon. Also, all these endpoints and parameters exist.
    - This approach also soemwhat aligns with the Master LLM’s suggestion but is more specific and completely accurate.
    - Now, I must create the final API call structure based on the identified coins and the required data.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "mobula",
        "endpoint": "/market/blockchain/pairs?blockchain=Polygon&sortBy=volume_5min&sortOrder=desc",
        "description": "Retrieve a list of trending projects on the Polygon blockchain, sorted by trading volume (or the most relevant metric inferred from the query).",
        "nested_calls": [
          {
            "provider": "mobula",
            "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3",
            "description": "Retrieve detailed market, on-chain, and social data for the identified coins in a batch call using Mobula Multi-Data Batch."
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin1/v1",
            "description": "Retrieve social sentiment data for coin1"
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin2/v1",
            "description": "Retrieve social sentiment data for coin2."
          },
          {
            "provider": "lunarcrush",
            "endpoint": "/public/coins/coin3/v1",
            "description": "Retrieve social sentiment data for coin3."
          }
        ]
      }
    ]
    ```
    """,

    # Example 4 – Detailed Analysis of the DeSci Sector
    """
    USER QUERY:
    Give me a detailed analysis of the DeSci (Decentralized Science) sector in crypto.

    MASTER LLM OUTPUT:

    About the Agent:
    Introducing DeSciOracle—an AI analyst at the frontier of Decentralized Science (DeSci). Designed to decode the intersection of blockchain and scientific innovation, DeSciOracle tracks funding trends, groundbreaking research, and decentralized collaborations to provide a crystal-clear view of the evolving DeSci landscape.

    🔬 DeSciOracle: Your Gateway to the Future of Science & Blockchain 🚀

    DeSciOracle isn’t just another AI—it’s a visionary guide into how blockchain is disrupting traditional scientific models. By analyzing on-chain funding, community sentiment, and the latest research breakthroughs, it delivers insights that matter for investors, researchers, and innovators shaping the future of science.

    🔍 What DeSciOracle Does Best:
    ✅ Identifies top DeSci projects & funding trends before they go mainstream 🌍
    ✅ Analyzes innovation pipelines to predict the next big scientific leap 🔭
    ✅ Tracks real-time community sentiment to assess adoption potential 📊

    With a forward-thinking, research-driven approach, DeSciOracle ensures you stay ahead in the race to decentralize science. Because in the DeSci revolution, knowledge is power—and blockchain is the key. 🔑💡

    
    High-Level Execution Plan:
      1. Query Assessment:
         - Recognize that DeSci is a predefined sector within LunarCrush.
      2. Data Retrieval Phase:
         - Instruct the Data Agent to retrieve sector-specific data (coins, posts, and news) using the LunarCrush Sector API.
         - Supplement this with detailed market data via the Mobula API.
      3. Analysis Phase:
         - Direct the Analysis Agent to integrate market, social, and news data to produce a thorough analysis, highlighting trends, risks, and opportunities in the DeSci sector.

    - Rationale & Chain-of-Thought:
      - Leveraging predefined sector endpoints enhances efficiency and accuracy.
      - Separating social/news data (via LunarCrush) from market data (via Mobula) ensures a robust, multidimensional analysis.

    - Execution Flow Overview:
      - The blueprint is: Query assessment → Data retrieval (using LunarCrush Sector API & Mobula API) → Data synthesis and comprehensive analysis.

      
    DATA AGENT OUTPUT

    DATA AGENT CHAIN-OF-THOUGHT:
    - The user query requests a "detailed analysis" of the "DeSci (Decentralized Science) sector" in crypto.
    - According to the API Selection Guidelines, for predefined sectors like "DeSci", the LunarCrush Coins v2 API is the most suitable resource for retrieving sector-specific coin data.
    - I will use the LunarCrush Coins v2 API endpoint: `/public/coins/v2`.
    - To specifically target the DeSci sector, I will apply the `filter=DeSci` parameter, as the LunarCrush Coins v2 API documentation indicates that the `filter` parameter is used to "filter by sub categories / sector".
    - To ensure the Analysis Agent receives the most relevant and actively traded projects within the DeSci sector, I will sort the results by `volume_24h` in descending order using the parameters `sortBy=volume_24h&sortOrder=desc`. This will prioritize coins with higher trading volume, which are generally indicative of market interest and activity.  The LunarCrush Coins v2 API documentation confirms that `volume_24h` is a valid option for the `sortBy` parameter.
    - After retrieving the list of DeSci coins from LunarCrush, I will initiate nested API calls to fetch detailed market and on-chain data for these coins.
    - For market and on-chain data, the Mobula API's `/market/multi-data` endpoint is the optimal choice. It allows fetching comprehensive market data for multiple assets simultaneously, improving efficiency.
    - I will dynamically populate the `symbols` parameter of the Mobula `/market/multi-data` endpoint with the coin symbols identified by the LunarCrush Coins v2 API call.  This will ensure that market data is retrieved specifically for the DeSci projects identified.
    - In all API calls, I will adhere to the guideline of using coin symbols exclusively for asset identification.
    - This approach aligns with the Master LLM's suggested execution plan and strictly follows the API Selection Guidelines for predefined sectors, ensuring a comprehensive and efficient data retrieval strategy for the detailed analysis of the DeSci sector.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/v2?filter=DeSci&sort=volume_24h",
        "description": "Retrieve a ranked list of coins belonging to the DeSci sector from LunarCrush Coins v2 API. Results are filtered to the 'DeSci' sector and sorted by 24-hour trading volume (descending) to prioritize actively traded projects.",
        "nested_calls": [
          {
            "provider": "mobula",
            "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3,coin4,coin5",
            "description": "Retrieve detailed market and on-chain data for the DeSci coins identified by the LunarCrush API call. The `symbols` parameter will be dynamically populated with the list of coin symbols from the LunarCrush response."
          }
        ]
      }
    ]
    ```
    """,
    
        # Example 5 – Multi-Sector Query: NFTs and DeFi
    """
    USER QUERY:
    Provide an analysis of the latest trends in both the NFTs and DeFi sectors.

    MASTER LLM OUTPUT:

    🌐 About the Agent:
      Meet TrendFusion—the ultimate AI trendspotter that bridges the gap between NFTs and DeFi. By fusing insights from on-chain analytics, social sentiment, and market movements, TrendFusion deciphers how DeFi liquidity and NFT hype intertwine, giving users a complete picture of digital asset trends.

      🚀 TrendFusion: Where DeFi Meets NFTs 🎨📊

      TrendFusion isn’t just tracking markets—it’s connecting the dots. Whether it’s NFT-backed lending, liquidity surges, or trending collections, this AI ensures you see the bigger picture before the market moves.

      🔍 What TrendFusion Does Best:
      ✅ Analyzes DeFi & NFT trends side-by-side for cross-market insights 🔄
      ✅ Deciphers liquidity flows, social sentiment, and on-chain activity 📡
      ✅ Identifies hidden correlations that drive both sectors forward 🔥

      With a sharp, pattern-seeking mindset, TrendFusion delivers next-level market intelligence—because in crypto, understanding the fusion of trends is the real alpha. ⚡🔗

      
    High-Level Execution Plan:
      1. Query Assessment:
         - Identify that the query targets two distinct, predefined sectors: NFTs and DeFi.
         - Since both sectors are predefined, there is no need for identification APIs.
      2. Data Retrieval Phase:
         - Instruct the Data Agent to retrieve sector-specific data (coins, posts, and news) for NFTs and DeFi using the LunarCrush Sector API.
         - Supplement with relevant market data from the Mobula API if necessary.
      3. Analysis Phase:
         - Direct the Analysis Agent to independently analyze the data from each sector and then synthesize comparative insights to highlight similarities, differences, and overall trends.

    - Rationale & Chain-of-Thought:
      - Handling multi-sector queries requires parallel processing to ensure clear and distinct data streams for each sector.
      - This separation allows for accurate comparative analysis and prevents data conflation, ensuring robust insights.

    - Execution Flow Overview:
      - The process flows as follows: Query assessment → Retrieve data for NFTs and DeFi separately → Synthesize and compare insights.


    DATA AGENT OUTPUT

    DATA AGENT CHAIN-OF-THOUGHT:
    - The user is asking for an analysis of the latest trends in the NFTs and DeFi sectors.
    - NFTs and DeFi are predefined sectors. Thus, I can directly query LunarCrush Coins v2 API with sector filters.
    - I will use LunarCrush Coins v2 API (`/public/coins/v2`) twice, once for each sector (NFT and DeFi) using `filter=NFT` and `filter=DeFi` respectively.
    - For each sector, I will sort the results by `volume_24h` in descending order using `sort=volume_24h` to identify actively traded projects.
    - To get detailed market data for the identified coins in both sectors, I will use Mobula's `/market/multi-data` endpoint in nested calls.
    - The `symbols` parameter in Mobula API calls will be populated with coin symbols from LunarCrush responses, using placeholders like `coin1,coin2,coin3,coin4,coin5`.
    - This approach provides sector-specific coin data from LunarCrush and detailed market data from Mobula, suitable for trend analysis of both NFTs and DeFi sectors.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/v2?filter=NFT&sort=volume_24h",
        "description": "Retrieve a ranked list of coins belonging to the NFT sector from LunarCrush Coins v2 API, sorted by 24-hour trading volume (descending) to identify actively traded NFT projects.",
        "nested_calls": [
          {
            "provider": "mobula",
            "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3,coin4,coin5",
            "description": "Retrieve detailed market and on-chain data for the top NFT coins identified by the LunarCrush API call."
          }
        ]
      },
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/v2?filter=DeFi&sort=volume_24h",
        "description": "Retrieve a ranked list of coins belonging to the DeFi sector from LunarCrush Coins v2 API, sorted by 24-hour trading volume (descending) to identify actively traded DeFi projects.",
        "nested_calls": [
          {
            "provider": "mobula",
            "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3,coin4,coin5",
            "description": "Retrieve detailed market and on-chain data for the top DeFi coins identified by the LunarCrush API call."
          }
        ]
      }
    ]
    """,

    # Example 6 – Historical Analysis of Bitcoin
    """
    USER QUERY:
    Give me a historical trend analysis of Bitcoin over the past 5 years.

    MASTER LLM OUTPUT:

    📜 About the Agent:
      Meet SatoshiChronicle—your AI-powered Bitcoin historian and trend analyst. With an encyclopedic knowledge of Bitcoin’s market cycles, halvings, and macro events, it deciphers the past to predict the future. By analyzing decades of price action, institutional shifts, and on-chain data, SatoshiChronicle provides a long-term perspective on Bitcoin’s trajectory.

      🔍 SatoshiChronicle: Unlocking Bitcoin’s Past to Forecast Its Future 🔮

      SatoshiChronicle isn’t here for short-term noise—it’s built for macro-level insights. Whether it’s post-halving trends, historic bull/bear cycles, or the impact of major regulatory events, this AI helps HODLers, traders, and institutions make data-driven decisions with historical context.

      🔍 What SatoshiChronicle Does Best:
      ✅ Tracks Bitcoin’s long-term market cycles & historical price action 📈
      ✅ Correlates macro events with BTC price movements for deeper insights 🌎
      ✅ Provides institutional-grade, long-horizon trend analysis 🏛️

      With a deep, research-first mindset, SatoshiChronicle is your AI companion in understanding Bitcoin’s past, present, and future—because in crypto, history doesn’t just repeat, it rhymes. 🔄⏳

      
    High-Level Execution Plan:
      1. Query Assessment:
         - Recognize that the query is coin-specific and requires an analysis of historical trends spanning 5 years.
      2. Data Retrieval Phase:
         - Direct the Data Agent to retrieve historical time-series market data for Bitcoin using Mobula and/or LunarCrush time-series endpoints.
         - Instruct retrieval of historical social sentiment data, if available, to provide contextual insights.
      3. Analysis Phase:
         - Direct the Analysis Agent to conduct a detailed trend analysis, correlating market data with major historical events and shifts in community sentiment.
         - Emphasize the identification of long-term trends, cycles, and potential catalysts for future movements.

    - Rationale & Chain-of-Thought:
      - Historical analysis demands robust, continuous data and careful correlation with past events.
      - This approach ensures that trends are interpreted within a broader historical context, yielding reliable insights.

    - Execution Flow Overview:
      - The blueprint is: Query assessment → Retrieve historical market and sentiment data → Perform trend analysis and event correlation.

      
    DATA AGENT OUTPUT

    DATA AGENT CHAIN-OF-THOUGHT:
    - The user is requesting a "historical trend analysis" of "Bitcoin" over the "past 5 years", now extending the end date to "upto feb 2024".
    - This remains a coin-specific query focused on historical data and trend analysis.
    - I will continue to use LunarCrush's `/public/coins/:coin/time-series/v2` for combined market and social data and Mobula's `/market/history` for supplementary market data, as these API choices are still appropriate.
    - For LunarCrush, the `/public/coins/BTC/time-series/v2` endpoint will be used with `coin=BTC`, `interval=all`, and `bucket=day` parameters, as before, to get daily aggregated data over the maximum historical range.
    - For Mobula's `/market/history` endpoint, I will update the `to` parameter to reflect the new end date of "upto feb 2024". I will use **February 1st, 2024** as a representative date for "upto feb 2024".
    - The `asset` parameter for Mobula will remain "Bitcoin".
    - The `from` parameter will remain January 1, 2019, to cover approximately the "past 5 years" ending in early February 2024.
    - `period=1h` for Mobula will be maintained to ensure hourly market data granularity.
    - The updated timeframe for Mobula will be from January 1, 2019, to February 1st, 2024, using corresponding Unix timestamps in milliseconds.
    - By updating the `to` timestamp in the Mobula API call and adjusting the chain-of-thought, the Data Agent now correctly addresses the user's request for a historical trend analysis of Bitcoin up to February 2024, while still leveraging the strengths of both LunarCrush and Mobula APIs for comprehensive data retrieval.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/BTC/time-series/v2",
        "description": "Retrieve historical market and social data for Bitcoin over the past 5 years (up to February 2024) from LunarCrush. Data is aggregated daily for long-term trend analysis.",
        "parameters": {
          "coin": "BTC",
          "bucket": "day",
          "interval": "all"
        }
      },
      {
        "provider": "mobula",
        "endpoint": "/market/history",
        "description": "Retrieve supplementary historical market metrics for Bitcoin over the past 5 years (up to February 2024) from Mobula, with hourly granularity for detailed market trend analysis.",
        "parameters": {
          "asset": "Bitcoin",
          "from": "1546300800000",  // January 1, 2019, in milliseconds
          "to": "1706726400000",    // February 1, 2024, in milliseconds
          "period": "1h"
        }
      }
    ]
    ```
    """,

    # Example 7 – Wallet Portfolio Analysis via Mobula's Wallet Explorer API
    """
    USER QUERY:
    Provide a detailed analysis of the wallet portfolio for wallet address 0xABC123XYZ.

    MASTER LLM OUTPUT:

    💼 About the Agent:
      Introducing AlphaLedger—your AI-powered portfolio intelligence engine. Designed for crypto investors who demand precision, AlphaLedger provides deep, real-time insights into wallet composition, asset distribution, and historical performance trends. Whether you’re optimizing holdings or tracking whale movements, this AI ensures you stay in control of your crypto strategy.

      📊 AlphaLedger: Master Your Crypto Portfolio Like a Pro 🚀

      AlphaLedger doesn’t just show your balances—it deciphers them. From real-time market valuations to historical P&L tracking, it delivers actionable insights that help you maximize gains and mitigate risks.

      🔍 What AlphaLedger Does Best:
      ✅ Breaks down wallet asset distribution for clear portfolio insights 🏦
      ✅ Analyzes historical performance trends to refine investment strategy 📈
      ✅ Identifies risk exposure & diversification opportunities for smarter decisions ⚖️

      With a sharp, data-driven mindset, AlphaLedger transforms wallet data into strategic intelligence—because in crypto, knowledge is the ultimate asset. 🔥📊


    High-Level Execution Plan:
      1. Query Assessment:
         - Recognize that the query is wallet-specific, focusing on detailed portfolio analysis for a given wallet address.
         - Note that the analysis should include current holdings and, optionally, historical trends.
      2. Data Retrieval Phase:
         - Instruct the Data Agent to retrieve current wallet portfolio data using Mobula’s Wallet Explorer API (e.g., /wallet/portfolio endpoint).
         - Optionally, specify the retrieval of historical balance data (/wallet/history) or transaction counts (/warehouse/wallet-transactions-count) for added context.
      3. Analysis Phase:
         - Direct the Analysis Agent to integrate the portfolio data with current market metrics from the Mobula Market API.
         - Instruct the Analysis Agent to analyze asset distribution, overall valuation, and historical trends.
         - If data is insufficient, mandate that the Analysis Agent clearly state: "Insufficient data available for reliable insights."
    
    - Rationale & Chain-of-Thought:
      - Wallet analysis requires a specialized approach, distinct from coin or sector analysis.
      - Leveraging the Mobula Wallet Explorer API ensures detailed retrieval of portfolio information, while supplementary data enhances context.
      - Transparent handling of data limitations is essential to maintain analytical integrity.

    - Execution Flow Overview:
      - The blueprint outlines: Query assessment → Retrieve wallet portfolio (and supplementary) data via Mobula → Integrate market data → Synthesize a comprehensive wallet analysis.


    DATA AGENT OUTPUT

    DATA AGENT CHAIN-OF-THOUGHT:
    - The user query requests a "detailed analysis" of the "wallet portfolio" for the specific wallet address "0xABC123XYZ".
    - This is a wallet-specific query, and according to API selection guidelines and available resources, Mobula's Wallet API is the most appropriate provider for wallet portfolio data.
    - To retrieve the current portfolio holdings for the specified wallet, I will use the Mobula `/wallet/portfolio` endpoint.
    - For the `/wallet/portfolio` endpoint, I will include the parameter `wallet=0xABC123XYZ` to specify the target wallet address for the portfolio analysis. This will retrieve a snapshot of the current assets held in the wallet.
    - To provide a more comprehensive "detailed analysis," I will also include historical context by retrieving the wallet's historical balance data.
    - For historical balance data, I will use the Mobula `/wallet/history` endpoint, also with the parameter `wallet=0xABC123XYZ` to target the same wallet address. This will provide time-series data of the wallet's balance over time.
    - Using both `/wallet/portfolio` for current holdings and `/wallet/history` for historical balance provides a robust dataset for the Analysis Agent to perform a detailed wallet portfolio analysis, including asset distribution and performance trends over time.
    - This approach aligns with the Master LLM’s plan to utilize Mobula's Wallet Explorer API for wallet-specific queries and ensures retrieval of both current and historical data for a comprehensive analysis.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "mobula",
        "endpoint": "/wallet/portfolio?wallet=0xABC123XYZ",
        "description": "Retrieve current portfolio holdings and asset distribution for the wallet address 0xABC123XYZ using Mobula's Portfolio API."
      },
      {
        "provider": "mobula",
        "endpoint": "/wallet/history?wallet=0xABC123XYZ",
        "description": "Retrieve historical balance data for the wallet address 0xABC123XYZ using Mobula's Wallet History API to provide context on portfolio performance over time."
      }
    ]
    ```
    """,
    """
    USER QUERY:
    Provide a comprehensive analysis of trending projects in crypto.

    MASTER LLM OUTPUT:

    📈 About the Agent:
        Introducing AlphaTrend—your AI-powered crypto trendspotter and market oracle. With an unparalleled ability to detect emerging projects, AlphaTrend deciphers real-time market data, on-chain movements, and social sentiment to deliver next-level insights before the crowd catches on.

        🚀 AlphaTrend: Your Guide to the Next Big Crypto Plays 🔥

        AlphaTrend isn’t just another market analyst—it’s your edge in the fast-moving crypto world. By fusing LunarCrush and Mobula API insights, it filters signal from noise to pinpoint the hottest projects gaining momentum.

        🔍 What AlphaTrend Does Best:
        ✅ Scans real-time market data to identify emerging crypto trends 🚀
        ✅ Analyzes social sentiment & engagement metrics for early signals 🧠
        ✅ Evaluates project performance & sustainability for smarter decisions 📊

        With a sharp, trend-driven mindset, AlphaTrend keeps you ahead of market shifts, ensuring you never miss the next moonshot. Because in crypto, timing is everything. ⏳⚡


    High-Level Execution Plan:
    1. Query Assessment:
        - Recognize that the query targets trending projects across the entire crypto market, necessitating a broad, integrated view.
        - Identify that the LunarCrush Coins v2 API is ideal for capturing a comprehensive snapshot of trending projects (via aggregated market cap, social engagement, and trading volume metrics).
        - Note: For detailed individual project analysis, LunarCrush Coin v1 can be used; however, the focus here is on market-wide trends.
    2. Data Retrieval Phase:
        - Instruct the Data Agent to use the LunarCrush Coins v2 API to retrieve a full list of trending projects, ensuring the API call is filtered and sorted based on user-specified criteria (e.g., highest social engagement, market cap, or trading volume).
        - Additionally, direct the Data Agent to supplement this data with detailed market metrics from the Mobula API to capture trading dynamics, liquidity, and on-chain activity.
    3. Analysis Phase:
        - Direct the Analysis Agent to synthesize the aggregated data into a comprehensive report.
        - The report should identify key trending projects, highlight emerging market trends, and evaluate overall market sentiment, thereby providing a holistic view of the crypto market.
    
    - Rationale & Chain-of-Thought:
    - Utilizing the LunarCrush Coins v2 API as the identifier ensures broad coverage of trending projects across the market.
    - Integrating supplementary data from Mobula deepens the analysis by adding insights into trading volumes, liquidity, and on-chain behavior.
    - Filtering and sorting the data according to user-defined parameters focuses the analysis on the most significant projects, reducing noise and enhancing actionable insights.
    
    - Execution Flow Overview:
    - The blueprint flows as follows: Query assessment → Retrieve trending projects using LunarCrush Coins v2 (filtered/sorted as per criteria) + Supplement with Mobula market data → Synthesize and deliver a comprehensive analysis of trending crypto projects.
    
    
    DATA AGENT OUTPUT

    DATA AGENT CHAIN-OF-THOUGHT:
    - The user is asking for a "comprehensive analysis of trending projects in crypto."
    - To identify "trending projects", LunarCrush Coins v2 API (`/public/coins/v2`) is an excellent resource as it provides metrics like AltRank™, Galaxy Score™, social volume, and market metrics, specifically designed to identify trending cryptocurrencies.
    - I will use LunarCrush Coins v2 API to get a broad overview of trending projects across the crypto market.
    - To rank projects by trendiness, I will sort the LunarCrush Coins v2 API results using `sort=alt_rank`. AltRank™ is a LunarCrush proprietary metric that measures a coin's performance relative to the entire crypto universe, with a lower AltRank indicating stronger relative performance and thus higher trendiness. Sorting by descending AltRank will therefore prioritize the most trending projects according to LunarCrush's algorithm.
    -  The LunarCrush Coins v2 API response already includes both market and social data for each coin, providing a solid base for trend analysis.
    - To enrich the analysis with more granular market and on-chain data, I will supplement the LunarCrush data with detailed metrics from Mobula's `/market/multi-data` endpoint.
    - I will use a nested call to Mobula's `/market/multi-data` API, populating the `symbols` parameter with placeholders (`coin1,coin2,coin3,coin4,coin5`) representing the top trending coin symbols identified by the LunarCrush Coins v2 API call.
    - By combining the broad trend identification and comprehensive metrics from LunarCrush Coins v2 with the detailed market and on-chain data from Mobula, the Analysis Agent will have a robust dataset to perform a "comprehensive analysis of trending projects in crypto."
    - This approach efficiently leverages the strengths of both APIs: LunarCrush for identifying trends and providing high-level metrics, and Mobula for in-depth market and on-chain details.

    FINAL API CALL STRUCTURE:
    ```json
    [
      {
        "provider": "lunarcrush",
        "endpoint": "/public/coins/v2?sort=alt_rank",
        "description": "Retrieve a ranked list of trending crypto projects from LunarCrush Coins v2 API, sorted by AltRank™ (descending) to identify the most rapidly trending projects based on LunarCrush's proprietary metrics, including social and market data.",
        "nested_calls": [
          {
            "provider": "mobula",
            "endpoint": "/market/multi-data?symbols=coin1,coin2,coin3,coin4,coin5",
            "description": "Retrieve detailed market and on-chain data for the top trending crypto projects identified by the LunarCrush API call, using Mobula's Multi-Data endpoint to supplement the trend analysis with granular metrics."
          }
        ]
      }
    ]
    ```
    """
]