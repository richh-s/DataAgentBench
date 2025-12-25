code = """import json
import re

# Helper to load data
def load_data(var_val):
    if isinstance(var_val, str):
        # Assume it's a file path
        with open(var_val, 'r') as f:
            return json.load(f)
    else:
        # Assume it's the data list
        return var_val

# Load metadata
meta_var = locals()['var_function-call-12987280970809318212']
meta_list = load_data(meta_var)

# Load articles
art_var = locals()['var_function-call-1079264442624552925']
art_list = load_data(art_var)

# Create a mapping from article_id to year
# Filter for 2010-2020
id_to_year = {}
for m in meta_list:
    # article_id might be str or int in metadata
    aid = int(m['article_id'])
    date = m['publication_date'] # "YYYY-MM-DD"
    year = int(date[:4])
    if 2010 <= year <= 2020:
        id_to_year[aid] = year

# Categories keywords
categories = {
    'Business': ['business', 'economy', 'market', 'financial', 'stock', 'share', 'trade', 'investment', 'bank', 'money', 'price', 'profit', 'loss', 'corp', 'tax', 'rate', 'dollar', 'euro', 'yen', 'budget', 'debt', 'inflation', 'recession', 'growth', 'sale', 'deal', 'merger', 'acquisition', 'industry', 'commercial', 'wall street', 'dow', 'nasdaq', 'oil', 'gas', 'energy', 'bonds', 'futures', 'forex', 'ceo', 'cfo', 'fed', 'treasury'],
    'Sports': ['sport', 'game', 'team', 'cup', 'league', 'player', 'match', 'win', 'score', 'olympic', 'football', 'soccer', 'baseball', 'basketball', 'tennis', 'golf', 'coach', 'champion', 'tournament', 'medal', 'athlete', 'race', 'f1', 'nfl', 'nba', 'mlb', 'nhl'],
    'SciTech': ['science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'space', 'nasa', 'study', 'research', 'virus', 'phone', 'mobile', 'apple', 'google', 'microsoft', 'biotech', 'robot', 'astronomy', 'physics', 'biology', 'experiment', 'discovery', 'launch', 'orbit', 'mars', 'moon', 'online', 'data', 'cyber'],
    'World': ['world', 'war', 'peace', 'election', 'president', 'minister', 'attack', 'bomb', 'kill', 'government', 'police', 'court', 'law', 'china', 'russia', 'iran', 'iraq', 'uk', 'france', 'germany', 'eu', 'un', 'nation', 'military', 'army', 'conflict', 'treaty', 'protest', 'vote', 'parliament', 'official', 'state', 'security', 'terror']
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    for cat, kws in categories.items():
        for kw in kws:
            # Word boundary check is better
            # \bkw\b
            if re.search(r'\b' + re.escape(kw) + r'\b', text):
                scores[cat] += 1
    
    # Get max score
    max_cat = max(scores, key=scores.get)
    if scores[max_cat] == 0:
        return 'World' # Default
    return max_cat

# Count business articles per year
year_counts = {y: 0 for y in range(2010, 2021)}

business_count = 0
processed_count = 0

for art in art_list:
    # article_id might be str in articles
    aid = int(art['article_id'])
    if aid in id_to_year:
        title = art.get('title', '')
        desc = art.get('description', '')
        full_text = title + " " + desc
        
        cat = classify(full_text)
        if cat == 'Business':
            y = id_to_year[aid]
            year_counts[y] += 1
            business_count += 1
        processed_count += 1

print("__RESULT__:")
print(json.dumps({"year_counts": year_counts, "processed": processed_count, "total_business": business_count}))"""

env_args = {'var_function-call-12987280970809318212': 'file_storage/function-call-12987280970809318212.json', 'var_function-call-3327544021322435934': 'file_storage/function-call-3327544021322435934.json', 'var_function-call-5544368014430609247': {'min': 3, 'max': 127583, 'count': 14860}, 'var_function-call-11134278749745899859': [{'_id': '6944cce21659048c9db08bdd', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944cce21659048c9db08bde', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944cce21659048c9db08bdf', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944cce21659048c9db08be0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944cce21659048c9db08be1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1079264442624552925': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
