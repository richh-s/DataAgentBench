code = """import json
import pandas as pd
import re

# Load Metadata
with open(locals()['var_function-call-9284748779350516997'], 'r') as f:
    metadata_list = json.load(f)

# Load Articles
articles_list = locals()['var_function-call-10043856992590760587']

df_meta = pd.DataFrame(metadata_list)
df_articles = pd.DataFrame(articles_list)
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

df = pd.merge(df_meta, df_articles, on='article_id', how='inner')
df['year'] = pd.to_datetime(df['publication_date']).dt.year
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Helper to classify and return scores for debugging
def get_classification_debug(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    # (Same keywords as before)
    business_keywords = {
        'business', 'economy', 'market', 'stock', 'trade', 'finance', 'financial', 'bank', 
        'investment', 'investor', 'profit', 'revenue', 'wall street', 'company', 'shares', 
        'dollar', 'euro', 'oil', 'gas', 'prices', 'rate', 'inflation', 'fed', 'treasury', 
        'acquisition', 'merger', 'ipo', 'ceo', 'earnings', 'dow', 'nasdaq', 's&p', 'bond', 
        'debt', 'crisis', 'funds', 'capital', 'growth', 'sales', 'retail', 'commercial', 'industry'
    }
    sports_keywords = {
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket',
        'game', 'match', 'team', 'player', 'coach', 'league', 'cup', 'championship', 'olympic',
        'win', 'lose', 'score', 'medal', 'tournament', 'club', 'race', 'f1', 'nba', 'nfl', 'mlb',
        'stadium', 'athlete', 'season'
    }
    tech_keywords = {
        'technology', 'tech', 'science', 'computer', 'software', 'hardware', 'internet', 'web',
        'google', 'apple', 'microsoft', 'facebook', 'amazon', 'mobile', 'phone', 'app', 'data',
        'space', 'nasa', 'research', 'study', 'scientist', 'discovery', 'device', 'digital', 'network',
        'server', 'chip', 'processor', 'robot', 'ai', 'cyber', 'online', 'browser', 'cloud'
    }
    world_keywords = {
        'world', 'war', 'peace', 'president', 'minister', 'government', 'politics', 'election',
        'country', 'military', 'army', 'attack', 'bomb', 'kill', 'protest', 'un', 'nato', 'treaty',
        'parliament', 'vote', 'law', 'court', 'police', 'crime', 'region', 'border', 'china', 'russia',
        'europe', 'usa', 'uk', 'france', 'germany', 'syria', 'iraq', 'iran', 'palestine', 'israel', 
        'egypt', 'africa', 'asia', 'official', 'security'
    }
    
    scores = {'Business': 0, 'Sports': 0, 'Sci/Tech': 0, 'World': 0}
    words = re.findall(r'\w+', text)
    for word in words:
        if word in business_keywords: scores['Business'] += 1
        elif word in sports_keywords: scores['Sports'] += 1
        elif word in tech_keywords: scores['Sci/Tech'] += 1
        elif word in world_keywords: scores['World'] += 1
    
    max_score = max(scores.values())
    cat = 'Unknown'
    if max_score > 0:
        best_cats = [k for k, v in scores.items() if v == max_score]
        cat = best_cats[0]
        if 'Business' in best_cats: cat = 'Business'
        
    return cat, text, scores

# Apply and store details
results = df.apply(get_classification_debug, axis=1)
df['category'] = results.apply(lambda x: x[0])
df['text'] = results.apply(lambda x: x[1])
df['scores'] = results.apply(lambda x: x[2])

print("__RESULT__:")
print(json.dumps({
    "total_merged": len(df),
    "category_counts": df['category'].value_counts().to_dict(),
    "sample_non_business": df[df['category'] != 'Business'][['title', 'category', 'scores']].head(5).to_dict(orient='records'),
    "sample_unknown": df[df['category'] == 'Unknown'][['title', 'description']].head(5).to_dict(orient='records')
}))"""

env_args = {'var_function-call-9284748779350516997': 'file_storage/function-call-9284748779350516997.json', 'var_function-call-16724156452483696481': {'count': 14860, 'first_10_ids': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}, 'var_function-call-10043856992590760587': [{'_id': '6944d9cdc5455efc705a86b8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d9cdc5455efc705a86b9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d9cdc5455efc705a86ba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d9cdc5455efc705a86bb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d9cdc5455efc705a86bc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-732580074867003729': {'yearly_counts': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091, 'total_business': 1}}

exec(code, env_args)
