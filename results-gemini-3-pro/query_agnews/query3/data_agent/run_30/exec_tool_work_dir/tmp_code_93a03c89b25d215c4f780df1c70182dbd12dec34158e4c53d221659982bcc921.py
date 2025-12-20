code = """import json
import pandas as pd
import re

# Load Data
with open(locals()['var_function-call-9284748779350516997'], 'r') as f:
    metadata_list = json.load(f)
with open(locals()['var_function-call-16732576443780575921'], 'r') as f:
    batch1 = json.load(f)
with open(locals()['var_function-call-11422003096982108356'], 'r') as f:
    batch2 = json.load(f)
with open(locals()['var_function-call-12106970953398615057'], 'r') as f:
    batch3 = json.load(f)

# Combine and Deduplicate Articles
articles_list = batch1 + batch2 + batch3
df_articles = pd.DataFrame(articles_list)
df_articles['article_id'] = df_articles['article_id'].astype(int)
df_articles = df_articles.drop_duplicates(subset=['article_id'])

# Metadata
df_meta = pd.DataFrame(metadata_list)
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_meta = df_meta.drop_duplicates(subset=['article_id']) # Ensure metadata unique

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Filter Years
df['year'] = pd.to_datetime(df['publication_date']).dt.year
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Classification
def classify_article(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    
    # Same keywords...
    business_keywords = {
        'business', 'economy', 'market', 'stock', 'trade', 'finance', 'financial', 'bank', 
        'investment', 'investor', 'profit', 'revenue', 'wall street', 'company', 'shares', 
        'dollar', 'euro', 'oil', 'gas', 'prices', 'rate', 'inflation', 'fed', 'treasury', 
        'acquisition', 'merger', 'ipo', 'ceo', 'earnings', 'dow', 'nasdaq', 's&p', 'bond', 
        'debt', 'crisis', 'funds', 'capital', 'growth', 'sales', 'retail', 'commercial', 'industry',
        'imf', 'wto', 'ecb', 'central bank', 'currency', 'exchange', 'dividend', 'shareholder',
        'manufacturing', 'jobs', 'unemployment', 'recession', 'tariff', 'budget', 'deficit', 'surplus'
    }
    sports_keywords = {
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket',
        'game', 'match', 'team', 'player', 'coach', 'league', 'cup', 'championship', 'olympic',
        'win', 'lose', 'score', 'medal', 'tournament', 'club', 'race', 'f1', 'nba', 'nfl', 'mlb',
        'stadium', 'athlete', 'season', 'fifa', 'uefa', 'boxing', 'hockey', 'rugby'
    }
    tech_keywords = {
        'technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web',
        'google', 'apple', 'microsoft', 'facebook', 'amazon', 'mobile', 'phone', 'app', 'data',
        'space', 'nasa', 'research', 'study', 'scientist', 'discovery', 'device', 'digital', 'network',
        'server', 'chip', 'processor', 'robot', 'ai', 'cyber', 'online', 'browser', 'cloud', 'ibm', 'intel',
        'astronomy', 'biology', 'physics', 'chemistry', 'medical', 'virus', 'cancer', 'health'
    }
    world_keywords = {
        'world', 'war', 'peace', 'president', 'minister', 'government', 'politics', 'election',
        'country', 'military', 'army', 'attack', 'bomb', 'kill', 'protest', 'un', 'nato', 'treaty',
        'parliament', 'vote', 'law', 'court', 'police', 'crime', 'region', 'border', 'china', 'russia',
        'europe', 'usa', 'uk', 'france', 'germany', 'syria', 'iraq', 'iran', 'palestine', 'israel', 
        'egypt', 'africa', 'asia', 'official', 'security', 'prime minister', 'senate', 'congress',
        'terrorist', 'rebel', 'diplomat', 'ambassador', 'sanctions'
    }
    
    scores = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
    words = re.findall(r'\w+', text)
    for word in words:
        if word in business_keywords: scores['Business'] += 1
        elif word in sports_keywords: scores['Sports'] += 1
        elif word in tech_keywords: scores['Sci/Tech'] += 1
        elif word in world_keywords: scores['World'] += 1
            
    if 'wall street' in text: scores['Business'] += 2
    if 'central bank' in text: scores['Business'] += 2
    if 'prime minister' in text: scores['World'] += 2
    
    max_score = max(scores.values())
    if max_score == 0: return 'Unknown'
    best_cats = [k for k, v in scores.items() if v == max_score]
    if 'Business' in best_cats: return 'Business'
    return best_cats[0]

df['category'] = df.apply(classify_article, axis=1)

business_df = df[df['category'] == 'Business']
yearly_counts = business_df.groupby('year').size()
all_years = pd.Index(range(2010, 2021), name='year')
yearly_counts = yearly_counts.reindex(all_years, fill_value=0)

print("__RESULT__:")
print(json.dumps({
    "yearly_counts": yearly_counts.to_dict(),
    "average": yearly_counts.mean(),
    "total_business": int(yearly_counts.sum()),
    "total_merged": len(df)
}))"""

env_args = {'var_function-call-9284748779350516997': 'file_storage/function-call-9284748779350516997.json', 'var_function-call-16724156452483696481': {'count': 14860, 'first_10_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_function-call-10043856992590760587': [{'_id': '6944d9cdc5455efc705a86b8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d9cdc5455efc705a86b9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d9cdc5455efc705a86ba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d9cdc5455efc705a86bb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d9cdc5455efc705a86bc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-732580074867003729': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091, 'total_business': 1}, 'var_function-call-8949601244673809398': {'total_merged': 1, 'category_counts': {'Business': 1}, 'sample_non_business': [], 'sample_unknown': []}, 'var_function-call-16732576443780575921': 'file_storage/function-call-16732576443780575921.json', 'var_function-call-2263675403483438088': {'yearly_counts': {'2010': 88, '2011': 117, '2012': 116, '2013': 122, '2014': 113, '2015': 119, '2016': 113, '2017': 131, '2018': 124, '2019': 123, '2020': 122}, 'average': 117.0909090909091, 'total_business': 1288, 'total_articles_merged': 5762}, 'var_function-call-2624805255953775997': {'meta_min_id': 3, 'meta_max_id': 127583, 'articles_min_id': 0, 'articles_max_id': 49999, 'articles_count': 50000}, 'var_function-call-11422003096982108356': 'file_storage/function-call-11422003096982108356.json', 'var_function-call-12106970953398615057': 'file_storage/function-call-12106970953398615057.json', 'var_function-call-10466209198604847285': {'yearly_counts': {'2010': 282, '2011': 360, '2012': 354, '2013': 381, '2014': 345, '2015': 360, '2016': 348, '2017': 396, '2018': 381, '2019': 384, '2020': 375}, 'average': 360.54545454545456, 'total_business': 3966, 'total_articles_merged': 17286, 'total_metadata': 14860, 'match_rate': 1.163257065948856}}

exec(code, env_args)
