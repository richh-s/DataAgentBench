code = """import json
import pandas as pd
import re

# Load metadata
meta_path = locals()['var_function-call-11639742510862021534']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

# Load articles
articles_res = locals()['var_function-call-8382702086317822417']
if isinstance(articles_res, str) and (articles_res.endswith('.json') or '/' in articles_res):
    with open(articles_res, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = articles_res

# Convert to DataFrames
df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

# Ensure article_id types match
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Define keywords
keywords = {
    'Business': ['business', 'market', 'stock', 'economy', 'financial', 'trade', 'invest', 'bank', 'profit', 'oil', 'price', 'dollar', 'euro', 'gold', 'wall street', 'corp', 'company', 'industry', 'job', 'growth', 'deal', 'sale', 'fed', 'rate', 'revenue', 'share', 'bond', 'exchange', 'tax', 'budget', 'merger', 'acquisition', 'ceo', 'cfo', 'shares', 'stocks', 'asset', 'fund'],
    'Sports': ['sport', 'game', 'team', 'cup', 'match', 'score', 'win', 'player', 'league', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'hockey', 'athlete', 'coach', 'tournament', 'championship', 'medal', 'race'],
    'SciTech': ['technology', 'science', 'computer', 'internet', 'web', 'space', 'nasa', 'software', 'google', 'apple', 'microsoft', 'phone', 'research', 'study', 'cell', 'virus', 'biotech', 'chip', 'network', 'data', 'robot', 'mars', 'moon', 'orbit', 'launch', 'server', 'online'],
    'World': ['world', 'war', 'peace', 'president', 'election', 'politic', 'government', 'treaty', 'attack', 'kill', 'bomb', 'police', 'court', 'nation', 'country', 'international', 'military', 'army', 'un', 'united nations', 'security', 'law', 'crime', 'minister', 'official', 'parliament']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    
    # Priority handling or default
    # If tie or 0, what?
    # Hint: "Oil prices soar..." is business. "Iraq Halts Oil Exports..." -> "oil" is business, "iraq" (world?). "official" (world).
    # Let's trust the dominant count.
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unclassified'
    return best_cat

# Combine title and description
df['text'] = df['title'].fillna('') + ' ' + df['description'].fillna('')
df['category'] = df['text'].apply(classify)

# Filter for Business
df_biz = df[df['category'] == 'Business'].copy()

# Extract year
df_biz['year'] = pd.to_datetime(df_biz['publication_date']).dt.year

# Count per year (2010-2020)
# Ensure we include all years in the range even if count is 0?
# The question asks for average number per year from 2010 to 2020.
years = list(range(2010, 2021))
counts = df_biz['year'].value_counts().reindex(years, fill_value=0)

average = counts.mean()

print("__RESULT__:")
print(json.dumps({
    "counts_per_year": counts.to_dict(),
    "average": average,
    "total_articles_fetched": len(df_articles),
    "total_articles_merged": len(df)
}))"""

env_args = {'var_function-call-11639742510862021534': 'file_storage/function-call-11639742510862021534.json', 'var_function-call-7912262759371964937': 'file_storage/function-call-7912262759371964937.json', 'var_function-call-7698643900256978742': 14860, 'var_function-call-13170610014898490485': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8382702086317822417': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
