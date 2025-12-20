code = """import json
import pandas as pd

# Load data (files are already there)
meta_path = locals()['var_function-call-11639742510862021534']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

articles_path = locals()['var_function-call-8302544355556226833']
with open(articles_path, 'r') as f:
    articles_data = json.load(f)

df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)
df = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Expanded Keywords
keywords = {
    'Business': ['business', 'market', 'stock', 'economy', 'financial', 'trade', 'invest', 'bank', 'profit', 'oil', 'price', 'dollar', 'euro', 'gold', 'wall street', 'corp', 'company', 'industry', 'job', 'growth', 'deal', 'sale', 'fed', 'rate', 'revenue', 'share', 'bond', 'exchange', 'tax', 'budget', 'merger', 'acquisition', 'ceo', 'cfo', 'asset', 'fund', 'nasdaq', 'dow jones', 'currency', 'debt', 'loan', 'credit', 'recession', 'inflation', 'capital', 'commercial', 'manufacturing', 'retail', 'earnings', 'dividend', 'ipo', 'quarter', 'loss', 'guidance', 'forecast', 'analyst', 'sector', 'rally', 'slump', 'crisis', 'tariff', 'export', 'import', 'goods', 'service', 'pay', 'salary', 'workforce', 'layoff', 'hiring', 'consumer', 'spending', 'bonds', 'commodity', 'futures', 'treasury', 'yield', 'central bank', 'ecb', 'imf'],
    'Sports': ['sport', 'game', 'team', 'cup', 'match', 'score', 'win', 'player', 'league', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'hockey', 'athlete', 'coach', 'tournament', 'championship', 'medal', 'race', 'nfl', 'nba', 'mlb', 'fifa', 'stadium', 'club', 'golf', 'cricket', 'rugby', 'boxing', 'formula one', 'f1', 'super bowl'],
    'SciTech': ['technology', 'science', 'computer', 'internet', 'web', 'space', 'nasa', 'software', 'google', 'apple', 'microsoft', 'phone', 'research', 'study', 'cell', 'virus', 'biotech', 'chip', 'network', 'data', 'robot', 'mars', 'moon', 'orbit', 'launch', 'server', 'online', 'digital', 'device', 'app', 'browser', 'facebook', 'amazon', 'intel', 'linux', 'windows', 'genetic', 'astronomy', 'physics', 'chemistry', 'biology'],
    'World': ['world', 'war', 'peace', 'president', 'election', 'politic', 'government', 'treaty', 'attack', 'kill', 'bomb', 'police', 'court', 'nation', 'country', 'international', 'military', 'army', 'un', 'united nations', 'security', 'law', 'crime', 'minister', 'official', 'parliament', 'congress', 'senate', 'vote', 'campaign', 'protest', 'diplomat', 'foreign', 'prime minister', 'chancellor', 'terror', 'bombing', 'nuclear', 'state', 'refugee', 'human rights']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    
    best_cat = max(scores, key=scores.get)
    # Tie-breaking: If Business has same score as World, prefer Business (usually economic news involving govt)
    if scores['Business'] > 0 and scores['Business'] == scores[best_cat]:
         return 'Business'
         
    if scores[best_cat] == 0:
        return 'Unclassified'
    return best_cat

df['text'] = df['title'].fillna('') + ' ' + df['description'].fillna('')
df['category'] = df['text'].apply(classify)

df_biz = df[df['category'] == 'Business'].copy()
df_biz['year'] = pd.to_datetime(df_biz['publication_date']).dt.year

years = list(range(2010, 2021))
counts = df_biz['year'].value_counts().reindex(years, fill_value=0)
average = counts.mean()

print("__RESULT__:")
print(json.dumps({
    "counts": counts.to_dict(),
    "average": average,
    "merged_rows": len(df),
    "business_count": len(df_biz),
    "unclassified": len(df[df['category'] == 'Unclassified'])
}))"""

env_args = {'var_function-call-11639742510862021534': 'file_storage/function-call-11639742510862021534.json', 'var_function-call-7912262759371964937': 'file_storage/function-call-7912262759371964937.json', 'var_function-call-7698643900256978742': 14860, 'var_function-call-13170610014898490485': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8382702086317822417': [{'_id': '6944d6a50a99d7e0e8672aa9', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d6a50a99d7e0e8672aaa', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d6a50a99d7e0e8672aab', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d6a50a99d7e0e8672aac', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d6a50a99d7e0e8672aad', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17709649415609663654': {'counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 1}, 'average': 0.09090909090909091, 'total_articles_fetched': 5, 'total_articles_merged': 1}, 'var_function-call-5039010200560302586': 'file_storage/function-call-5039010200560302586.json', 'var_function-call-7485474422923815158': {'missing_count': 12587, 'max_meta_id': 127583, 'max_article_id': 19999}, 'var_function-call-4671565419648004789': 'file_storage/function-call-4671565419648004789.json', 'var_function-call-8302544355556226833': 'file_storage/function-call-8302544355556226833.json', 'var_function-call-8401902750977588758': {'counts': {'2010': 388, '2011': 408, '2012': 417, '2013': 414, '2014': 415, '2015': 399, '2016': 420, '2017': 453, '2018': 441, '2019': 398, '2020': 397}, 'average': 413.6363636363636, 'merged_rows': 14860, 'business_count': 4550, 'unclassified': 728}}

exec(code, env_args)
