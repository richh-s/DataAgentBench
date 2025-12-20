code = """import json
import pandas as pd
import re
import os

# Load Metadata
meta_var = locals()['var_function-call-3293774840587708961']
if isinstance(meta_var, str) and os.path.exists(meta_var):
    with open(meta_var, 'r') as f:
        meta_data = json.load(f)
else:
    meta_data = meta_var

# Load Articles
art_var = locals()['var_function-call-6113853128808077927']
if isinstance(art_var, str) and os.path.exists(art_var):
    with open(art_var, 'r') as f:
        art_data = json.load(f)
else:
    art_data = art_var

df_meta = pd.DataFrame(meta_data)
df_art = pd.DataFrame(art_data)

# Ensure types
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_art['article_id'] = df_art['article_id'].astype(int)

# Merge
df = pd.merge(df_meta, df_art, on='article_id', how='left')

# Keywords
# Adding more variations and terms
business_kws = [
    'business', 'economy', 'economic', 'market', 'markets', 'stock', 'stocks', 'trade', 'trading', 
    'finance', 'financial', 'investment', 'investing', 'investor', 'investors', 'money', 'bank', 'banking', 'banks', 
    'dollar', 'euro', 'yen', 'currency', 'forex', 
    'profit', 'profits', 'loss', 'losses', 'quarterly', 'inflation', 'fed', 'central bank', 'rates', 'interest rates', 
    'tax', 'taxes', 'gdp', 'ceo', 'cfo', 'share', 'shares', 'shareholder', 'dividend', 
    'wall st', 'wall street', 'dow', 'dow jones', 'nasdaq', 's&p', 
    'oil', 'crude', 'gas', 'energy', 'pipeline', 'barrel', 'gold', 'price', 'prices', 'commodity', 
    'deal', 'merger', 'acquisition', 'takeover', 'bid', 'ipo', 
    'earnings', 'revenue', 'corporate', 'corporation', 'industry', 'industrial', 
    'company', 'companies', 'firm', 'firms', 
    'deficit', 'budget', 'debt', 'bond', 'bonds', 'loan', 'loans', 'credit', 
    'imf', 'wto', 'world bank', 'treasury', 'retail', 'sales', 'consumer', 'spending', 'shop', 'shopping', 'store', 'stores',
    'employment', 'job', 'jobs', 'unemployment', 'hiring', 'layoff', 'recession', 'growth', 'sector'
]

sports_kws = [
    'sport', 'sports', 'football', 'soccer', 'basketball', 'nba', 'baseball', 'mlb', 'hockey', 'nhl', 
    'tennis', 'golf', 'pga', 'cup', 'world cup', 'game', 'games', 'league', 'premier league', 
    'match', 'matches', 'team', 'teams', 'club', 'player', 'players', 'coach', 'manager', 
    'win', 'won', 'winner', 'winning', 'loss', 'lost', 'loser', 'defeat', 'score', 'scored', 'goal', 'points', 
    'medal', 'olympic', 'olympics', 'championship', 'champion', 'tournament', 'tour', 
    'f1', 'formula 1', 'racing', 'driver', 'athlete', 'athletics', 'stadium', 'season', 'playoff', 'final', 'semi-final'
]

scitech_kws = [
    'technology', 'tech', 'science', 'scientific', 'computer', 'computers', 'computing', 'pc', 
    'software', 'hardware', 'processor', 'chip', 'chips', 'semiconductor', 
    'internet', 'web', 'website', 'online', 'net', 'browser', 'search engine', 
    'google', 'microsoft', 'apple', 'facebook', 'amazon', 'intel', 'ibm', 'linux', 'windows', 
    'virus', 'malware', 'security', 'hacker', 'cyber', 
    'space', 'nasa', 'shuttle', 'station', 'astronaut', 'astronomy', 'planet', 'mars', 'moon', 
    'biology', 'genetics', 'gene', 'genome', 'stem cell', 'cloning', 
    'physics', 'chemist', 'chemistry', 'research', 'study', 'lab', 'laboratory', 
    'mobile', 'phone', 'smartphone', 'wireless', 'network', 'broadband', 'satellite', 'robot', 'robotics', 'digital', 'electronic'
]

world_kws = [
    'world', 'international', 'politics', 'political', 'government', 'governments', 'state', 
    'president', 'presidency', 'minister', 'prime minister', 'chancellor', 'governor', 
    'election', 'elections', 'vote', 'voters', 'poll', 'polls', 
    'parliament', 'congress', 'senate', 'legislature', 'law', 'laws', 'legislation', 'court', 'supreme court', 'judge', 'trial', 
    'war', 'wars', 'military', 'army', 'navy', 'air force', 'troops', 'soldier', 'soldiers', 
    'attack', 'attacks', 'bomb', 'bombing', 'blast', 'explosion', 'terror', 'terrorist', 'terrorism', 'al qaeda', 
    'kill', 'killed', 'killing', 'dead', 'death', 'deaths', 'casualty', 'injury', 
    'police', 'crime', 'criminal', 'arrest', 'prison', 'jail', 
    'treaty', 'agreement', 'negotiation', 'summit', 
    'un', 'united nations', 'eu', 'european union', 'nato', 'diplomat', 'diplomacy', 
    'strike', 'protest', 'demonstration', 'riot', 
    'iraq', 'iraqi', 'iran', 'iranian', 'afghanistan', 'syria', 'israel', 'palestine', 'palestinian', 'gaza', 
    'russia', 'russian', 'china', 'chinese', 'usa', 'us', 'american', 'uk', 'british', 'france', 'french', 'germany', 'german',
    'nuclear', 'weapon', 'arms', 'peace', 'security', 'crisis', 'conflict'
]

keywords = {
    'Business': business_kws,
    'Sports': sports_kws,
    'SciTech': scitech_kws,
    'World': world_kws
}

def classify(row):
    title = str(row['title']) if pd.notnull(row['title']) else ""
    desc = str(row['description']) if pd.notnull(row['description']) else ""
    text = (title + " " + desc).lower()
    
    # Tokenize
    tokens = re.split(r'[^a-z0-9]+', text)
    tokens = set([t for t in tokens if t]) # Use set for presence? Or list for frequency?
    # Frequency is better.
    tokens_list = [t for t in re.split(r'[^a-z0-9]+', text) if t]
    
    scores = {cat: 0 for cat in keywords}
    
    for cat, kws in keywords.items():
        for kw in kws:
            if " " in kw:
                if kw in text:
                    scores[cat] += 1
            else:
                scores[cat] += tokens_list.count(kw)
    
    # Weights?
    # Maybe weight Title matches higher?
    # For now, simple count.
    
    best_cat = max(scores, key=scores.get)
    # If all zero?
    if scores[best_cat] == 0:
        return 'World' # Default
    return best_cat

df['category'] = df.apply(classify, axis=1)

business_df = df[df['category'] == 'Business']
count = len(business_df)

# Check counts per year
yearly = business_df['publication_date'].str[:4].value_counts().sort_index()

print("__RESULT__:")
print(json.dumps({
    "total_business": count,
    "average": count / 11.0,
    "yearly": yearly.to_dict(),
    "preview_ids": business_df['article_id'].head(5).tolist()
}))"""

env_args = {'var_function-call-3293774840587708961': 'file_storage/function-call-3293774840587708961.json', 'var_function-call-16961470035374201743': 14860, 'var_function-call-2984874193688609188': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-389445083591484163': [{'_id': '6944d8dc009828414232b67c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d8dc009828414232b67d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d8dc009828414232b67e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d8dc009828414232b67f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d8dc009828414232b680', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10494170828591850651': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-8997259751239784895': {'total_business': 0, 'average_per_year': 0.0, 'yearly_counts': {}, 'sample_titles': []}, 'var_function-call-6113853128808077927': 'file_storage/function-call-6113853128808077927.json'}

exec(code, env_args)
