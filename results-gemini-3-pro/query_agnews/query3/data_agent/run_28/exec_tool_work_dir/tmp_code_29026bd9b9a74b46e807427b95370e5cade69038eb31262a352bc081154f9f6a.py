code = """import json
import pandas as pd
import re

# Load Metadata
meta_path = locals()['var_function-call-3293774840587708961']
with open(meta_path, 'r') as f:
    meta_data = json.load(f)

# Load Articles
art_path = locals()['var_function-call-10494170828591850651']
with open(art_path, 'r') as f:
    art_data = json.load(f)

# Convert to DataFrames
df_meta = pd.DataFrame(meta_data)
df_art = pd.DataFrame(art_data)

# Ensure article_id is int
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_art['article_id'] = df_art['article_id'].astype(int)

# Merge
# We only care about articles in metadata (Europe, 2010-2020)
df = pd.merge(df_meta, df_art, on='article_id', how='left')

# Keywords
keywords = {
    'Business': ['business', 'economy', 'market', 'stock', 'trade', 'finance', 'financial', 'investment', 'money', 'bank', 'dollar', 'euro', 'yen', 'profit', 'loss', 'inflation', 'fed', 'rates', 'tax', 'gdp', 'ceo', 'cfo', 'shares', 'wall st', 'dow jones', 'nasdaq', 'oil', 'gold', 'price', 'deal', 'merger', 'acquisition', 'earnings', 'corporate', 'industry', 'company', 'companies', 'deficit', 'budget', 'debt'],
    'Sports': ['sport', 'football', 'soccer', 'basketball', 'baseball', 'hockey', 'tennis', 'golf', 'cup', 'game', 'league', 'match', 'team', 'player', 'coach', 'win', 'won', 'loss', 'lost', 'score', 'medal', 'olympic', 'championship', 'tournament', 'f1', 'racing', 'formula one', 'athlete', 'stadium'],
    'SciTech': ['technology', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'google', 'microsoft', 'apple', 'facebook', 'amazon', 'intel', 'chip', 'virus', 'space', 'nasa', 'astronomy', 'biology', 'physics', 'chemistry', 'research', 'study', 'mobile', 'phone', 'wireless', 'network', 'satellite', 'robot', 'tech', 'digital'],
    'World': ['world', 'politics', 'government', 'president', 'minister', 'prime minister', 'election', 'vote', 'parliament', 'congress', 'senate', 'war', 'military', 'army', 'troops', 'attack', 'bomb', 'blast', 'kill', 'police', 'crime', 'court', 'law', 'treaty', 'un', 'united nations', 'eu', 'european union', 'nato', 'diplomat', 'strike', 'protest', 'iraq', 'iran', 'afghanistan', 'syria', 'israel', 'palestine', 'russia', 'china', 'usa', 'uk', 'france', 'germany', 'spain', 'italy', 'official', 'officials', 'security', 'nuclear', 'peace']
}

def classify(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    scores = {cat: 0 for cat in keywords}
    
    # Simple counting
    # Tokenize by non-alphanumeric to avoid partial matches (e.g. 'win' in 'winter')
    tokens = re.split(r'[^a-z0-9]+', text)
    token_set = set(tokens) # Use set for presence check? Or count? Frequency might matter.
    # Let's use count.
    
    for cat, kws in keywords.items():
        for kw in kws:
            if " " in kw: # Multi-word keyword
                if kw in text:
                    scores[cat] += 1
            else:
                if kw in tokens: # Exact word match
                    scores[cat] += 1
                    
    # Heuristic adjustments
    # "Oil" is heavily Business but appears in World (wars over oil).
    # If Business and World are close, check specific words?
    # For now, just take max.
    
    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'World' # Default fallback? Or maybe Unknown.
    return best_cat

df['category'] = df.apply(classify, axis=1)

# Count Business articles
business_articles = df[df['category'] == 'Business']
total_business = len(business_articles)

# Years 2010-2020 is 11 years.
average = total_business / 11.0

print("__RESULT__:")
print(json.dumps({
    "total_business": total_business,
    "average_per_year": average,
    "yearly_counts": business_articles['publication_date'].str[:4].value_counts().to_dict(),
    "sample_titles": business_articles['title'].head(5).tolist()
}))"""

env_args = {'var_function-call-3293774840587708961': 'file_storage/function-call-3293774840587708961.json', 'var_function-call-16961470035374201743': 14860, 'var_function-call-2984874193688609188': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-389445083591484163': [{'_id': '6944d8dc009828414232b67c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944d8dc009828414232b67d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944d8dc009828414232b67e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944d8dc009828414232b67f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944d8dc009828414232b680', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-10494170828591850651': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
