code = """import json
import pandas as pd
from collections import Counter
import re

# Load metadata
with open(locals()['var_function-call-10515657940082611823'], 'r') as f:
    metadata_list = json.load(f)

# Load articles
with open(locals()['var_function-call-6954192202394339732'], 'r') as f:
    articles_list = json.load(f)

# Convert to DataFrames
df_meta = pd.DataFrame(metadata_list)
df_articles = pd.DataFrame(articles_list)

# Ensure article_id is int in both
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Extract Year
df['year'] = pd.to_datetime(df['publication_date']).dt.year

# Filter for years 2010-2020 (The metadata query already did this, but good to ensure)
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Classification Logic
business_keywords = [
    "business", "economy", "market", "stock", "trade", "finance", "money", "investment", 
    "bank", "profit", "loss", "revenue", "sales", "company", "corporation", "inflation", 
    "tax", "job", "employment", "dollar", "euro", "yen", "currency", "share", "ipo", 
    "merger", "acquisition", "deal", "oil", "gas", "price", "cost", "interest rate", 
    "fed", "central bank", "wall street", "nasdaq", "dow jones", "investor", "credit", "debt"
]
sports_keywords = [
    "sport", "game", "match", "team", "player", "coach", "score", "win", "lose", "victory", 
    "defeat", "cup", "league", "season", "championship", "tournament", "olympic", "football", 
    "soccer", "basketball", "baseball", "tennis", "golf", "hockey", "cricket", "rugby", "athlete"
]
tech_keywords = [
    "technology", "tech", "science", "computer", "software", "hardware", "internet", "web", 
    "online", "digital", "mobile", "phone", "app", "google", "microsoft", "apple", "facebook", 
    "amazon", "nasa", "space", "robot", "device", "gadget", "chip", "processor", "server", 
    "data", "network", "cyber", "virus", "hacker", "research", "study", "scientist"
]
world_keywords = [
    "world", "international", "government", "president", "minister", "country", "nation", 
    "state", "war", "peace", "conflict", "military", "army", "police", "attack", "bomb", 
    "terror", "protest", "election", "vote", "politics", "policy", "diplomacy", "un", "eu", 
    "nato", "treaty", "law", "court", "justice", "crime", "disaster", "earthquake", "flood"
]

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    
    counts = {
        'Business': sum(text.count(k) for k in business_keywords),
        'Sports': sum(text.count(k) for k in sports_keywords),
        'Sci/Tech': sum(text.count(k) for k in tech_keywords),
        'World': sum(text.count(k) for k in world_keywords)
    }
    
    # Heuristics for overlap (e.g. "Google" in tech vs business)
    # If "Google" is present, check for financial words.
    # This simple count might classify "Google IPO" as Tech if "Google" appears more often?
    # Or Business if "IPO" and "Market" appear.
    # Let's rely on max count.
    
    best_category = max(counts, key=counts.get)
    if counts[best_category] == 0:
        return 'Unclassified' # Or default to World?
    return best_category

df['category'] = df.apply(classify, axis=1)

# Filter for Business
business_df = df[df['category'] == 'Business']

# Count per year
year_counts = business_df.groupby('year').size()

# Ensure all years 2010-2020 are present
all_years = pd.Series(0, index=range(2010, 2021))
year_counts = year_counts.add(all_years, fill_value=0)

average_business = year_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "yearly_counts": year_counts.to_dict(),
    "average": average_business,
    "sample_titles": business_df['title'].head(5).tolist()
}))"""

env_args = {'var_function-call-10515657940082611823': 'file_storage/function-call-10515657940082611823.json', 'var_function-call-9958426536691609633': {'count': 14860, 'query_preview': '{"collection": "articles", "filter": {"article_id": {"$in": [3, 9, 13, 14, 21, 27, 43, 60, 62, 63, 64, 66, 78, 128, 140, 142, 143, 144, 151, 154, 164, 179, 181, 190, 201, 202, 203, 210, 214, 216, 223, 243, 257, 265, 268, 270, 271, 279, 298, 300, 309, 328, 336, 338, 339, 348, 371, 379, 383, 394, 398, 400, 429, 439, 446, 452, 456, 457, 460, 474, 482, 484, 485, 502, 509, 510, 514, 532, 534, 536, 539, 554, 557, 564, 567, 569, 572, 576, 584, 597, 624, 642, 647, 661, 663, 669, 678, 682, 697, 712, 717,'}, 'var_function-call-400928839064045998': [{'_id': '6944cbd736604fe3acbb2149', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cbd736604fe3acbb214a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cbd736604fe3acbb214b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cbd736604fe3acbb214c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cbd736604fe3acbb214d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13455891081347356829': 'Done', 'var_function-call-18393258203316331497': {'type': "<class 'list'>", 'count': 5}, 'var_function-call-6954192202394339732': 'file_storage/function-call-6954192202394339732.json'}

exec(code, env_args)
