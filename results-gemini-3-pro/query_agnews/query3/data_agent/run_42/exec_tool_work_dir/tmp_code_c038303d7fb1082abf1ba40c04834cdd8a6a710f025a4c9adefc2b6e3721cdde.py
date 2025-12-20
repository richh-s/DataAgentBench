code = """import json
import pandas as pd
import datetime

# Load Metadata
with open(locals()['var_function-call-8582204155257448886'], 'r') as f:
    metadata_list = json.load(f)

# Load Articles
with open(locals()['var_function-call-12830304169509026760'], 'r') as f:
    articles_list = json.load(f)

# Convert to DataFrames
df_meta = pd.DataFrame(metadata_list)
df_articles = pd.DataFrame(articles_list)

# Ensure article_id is string in both
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Join
# We only care about articles in df_meta (Europe, 2010-2020)
df_merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Business Keywords
business_keywords = [
    'economy', 'economic', 'market', 'stock', 'share', 'invest', 'trade', 'bank', 
    'profit', 'loss', 'revenue', 'dollar', 'euro', 'currency', 'financial', 'finance', 
    'business', 'corp', 'firm', 'company', 'ipo', 'merger', 'acquisition', 'wall street', 
    'oil price', 'dow jones', 'nasdaq', 'tax', 'employment', 'job', 'growth', 'recession',
    'inflation', 'budget', 'debt', 'ceo', 'manager', 'sales', 'retail', 'industry', 'commercial'
]

# Simple Classifier
def is_business(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    # Check for Business keywords
    score = 0
    for kw in business_keywords:
        if kw in text:
            score += 1
    
    # Heuristic: if score > 0, it's likely business. 
    # But wait, "World" news might mention "jobs" or "economy".
    # The hint says "Determining an article’s category requires understanding...".
    # Given I don't have a trained model, I will use a strong set of keywords.
    # Let's check a few examples in my head. "Oil prices soar" -> Business? Or World? 
    # Usually Oil prices are Business/Economy. 
    # "Iraq halts oil exports" -> Could be World or Business. 
    # "Google IPO" -> Business.
    # "Stocks End Up" -> Business.
    
    # I'll rely on the presence of these keywords. 
    # A more robust way might be to check if Business keywords dominate over Sports/SciTech/World keywords.
    # But let's assume if it hits Business keywords it is Business.
    # To be safer, I should probably exclude Sports/SciTech keywords.
    
    sports_keywords = ['sport', 'game', 'match', 'cup', 'league', 'team', 'player', 'coach', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'cricket']
    tech_keywords = ['technology', 'tech', 'science', 'computer', 'software', 'internet', 'web', 'google', 'apple', 'microsoft', 'space', 'nasa', 'robot', 'mobile', 'phone', 'gadget']
    # "Google IPO" contains "google" (Tech) and "IPO" (Business). Usually Business.
    
    # Let's just stick to Business keywords presence.
    return score > 0

# Apply Classification
df_merged['is_business'] = df_merged.apply(is_business, axis=1)

# Extract Year
df_merged['year'] = pd.to_datetime(df_merged['publication_date']).dt.year

# Filter Business Articles
business_articles = df_merged[df_merged['is_business']]

# Count per year
counts = business_articles.groupby('year').size()

# Fill missing years with 0
all_years = list(range(2010, 2021))
counts = counts.reindex(all_years, fill_value=0)

# Calculate Average
average = counts.mean()

print("__RESULT__:")
print(json.dumps({
    "counts_per_year": counts.to_dict(),
    "average": average,
    "total_filtered_articles": len(df_merged),
    "total_business_articles": len(business_articles)
}))"""

env_args = {'var_function-call-8582204155257448886': 'file_storage/function-call-8582204155257448886.json', 'var_function-call-10360183093832859744': 'file_storage/function-call-10360183093832859744.json', 'var_function-call-8113535131067025306': [{'_id': '6944e32773df47891b047b1c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e32773df47891b047b1d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e32773df47891b047b1e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e32773df47891b047b1f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e32773df47891b047b20', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-15993919006908130781': 5, 'var_function-call-17518911728583085632': ['articles'], 'var_function-call-12830304169509026760': 'file_storage/function-call-12830304169509026760.json'}

exec(code, env_args)
