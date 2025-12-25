code = """import json
import pandas as pd
import re

meta_path = locals()['var_function-call-1304167582762502927']
articles_path = locals()['var_function-call-4198962169091228890']

with open(meta_path, 'r') as f:
    meta_data = json.load(f)
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Phrases to check in raw text
phrases = [
    "wall street", "federal reserve", "central bank", "dow jones", "stock market", 
    "s&p", "standard & poor", "initial public offering"
]

# Words to check in tokenized text
keywords = [
    "business", "businesses", "economy", "economies", "economic", "market", "markets", 
    "stock", "stocks", "trade", "trading", "finance", "finances", "financial", 
    "bank", "banks", "banking", "investment", "investments", "investor", "investors", 
    "money", "currency", "currencies", "dollar", "dollars", "euro", "euros", 
    "profit", "profits", "revenue", "revenues", "sale", "sales", "tax", "taxes", 
    "debt", "debts", "inflation", "rate", "rates", "fed", "company", "companies", 
    "corporation", "corporations", "corporate", "firm", "firms", "industry", "industries", 
    "sector", "sectors", "ceo", "ceos", "cfo", "cfos", "share", "shares", 
    "asset", "assets", "fund", "funds", "capital", "deal", "deals", "merger", "mergers", 
    "acquisition", "acquisitions", "buyout", "buyouts", "ipo", "ipos", "bid", "bids", 
    "growth", "recession", "spending", "job", "jobs", "unemployment", "oil", 
    "price", "prices", "cost", "costs", "consumer", "consumers", "retail", "commercial", 
    "dividend", "dividends", "earnings", "deficit", "deficits", "budget", "budgets",
    "nasdaq", "nyse", "forex"
]
keywords_set = set(keywords)

def is_business_final(text):
    text_lower = text.lower()
    # Check phrases
    for p in phrases:
        if p in text_lower:
            return True
    
    # Check tokenized words
    clean_text = re.sub(r'[^a-z0-9]', ' ', text_lower)
    words = set(clean_text.split())
    if not words.isdisjoint(keywords_set):
        return True
    
    return False

df['is_business'] = df.apply(lambda row: is_business_final(str(row['title']) + " " + str(row['description'])), axis=1)

business_df = df[df['is_business']]

counts = business_df.groupby('year').size()
all_years = list(range(2010, 2021))
counts = counts.reindex(all_years, fill_value=0)
average = counts.mean()

print(f"Counts: {counts.to_dict()}")
print(f"Average: {average}")

print("__RESULT__:")
print(json.dumps(average))"""

env_args = {'var_function-call-1304167582762502927': 'file_storage/function-call-1304167582762502927.json', 'var_function-call-641571560304296616': 'file_storage/function-call-641571560304296616.json', 'var_function-call-5674583780523164016': [{'_id': '6944d845bdad7807dc849895', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d845bdad7807dc849896', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d845bdad7807dc849897', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d845bdad7807dc849898', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d845bdad7807dc849899', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-4198962169091228890': 'file_storage/function-call-4198962169091228890.json', 'var_function-call-16544878985627064892': 84.0, 'var_function-call-13466724560110333408': 0.0, 'var_function-call-16025191490921363899': 'debug', 'var_function-call-6034586069982487846': {'sample_titles': ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Wall St. Bears Claw Back Into the Black', 'Google IPO Auction Off to Rocky Start', 'Dollar Falls Broadly on Record Trade Gap', 'Eurozone economy keeps growing'], 'match_count_simple': 0}, 'var_function-call-221665197530956759': 73.81818181818181}

exec(code, env_args)
