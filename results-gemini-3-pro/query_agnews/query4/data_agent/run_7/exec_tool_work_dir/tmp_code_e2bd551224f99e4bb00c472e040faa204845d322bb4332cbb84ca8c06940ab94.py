code = """import json
import collections
import re
import os

# Helper to load data
def load_data(var_value):
    if isinstance(var_value, str) and os.path.exists(var_value):
        with open(var_value, 'r') as f:
            return json.load(f)
    elif isinstance(var_value, list):
        return var_value
    else:
        # It might be a string but not a path? Or something else.
        return var_value

# Load metadata (2015 articles)
# Previous message said it's a file path
meta_var = locals().get('var_function-call-1113576567256238630')
metadata_list = load_data(meta_var)

# Load articles (all articles)
# Previous message showed a list preview but it might be a list or a file path depending on size
articles_var = locals().get('var_function-call-6757720913690530617')
articles_list = load_data(articles_var)

print(f"Metadata count: {len(metadata_list)}")
print(f"Articles count: {len(articles_list)}")

# Index articles by ID
articles_map = {str(a['article_id']): a for a in articles_list}

# Join
joined_data = []
for m in metadata_list:
    aid = str(m['article_id'])
    if aid in articles_map:
        art = articles_map[aid]
        joined_data.append({
            'article_id': aid,
            'region': m['region'],
            'title': art.get('title', ''),
            'description': art.get('description', '')
        })

# Define keywords (same as before)
keywords = {
    'Sports': ['sport', 'game', 'team', 'match', 'cup', 'league', 'win', 'loss', 'score', 'player', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'nfl', 'nba', 'mlb', 'nhl', 'champion', 'medal', 'coach', 'stadium', 'race', 'f1', 'golf', 'hockey', 'cricket', 'rugby', 'tournament', 'athens', 'sox', 'yankees', 'reds', 'bulls', 'lakers', 'final', 'semi-final'],
    'Business': ['business', 'company', 'market', 'stock', 'share', 'trade', 'economy', 'profit', 'loss', 'revenue', 'invest', 'bank', 'dollar', 'euro', 'yen', 'oil', 'price', 'corp', 'inc', 'ltd', 'wall st', 'nasdaq', 'dow jones', 'ceo', 'cfo', 'merger', 'acquisition', 'deal', 'sale', 'fed', 'inflation', 'rates', 'earnings', 'quarter', 'growth', 'airbus', 'boeing', 'oracle', 'google', 'microsoft', 'ibm'],
    'Sci/Tech': ['technology', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'google', 'microsoft', 'apple', 'intel', 'ibm', 'virus', 'space', 'nasa', 'orbit', 'moon', 'mars', 'research', 'study', 'cell', 'phone', 'mobile', 'wireless', 'network', 'chip', 'processor', 'linux', 'windows', 'browser', 'server', 'satellite', 'biotech', 'robot', 'spam', 'hacker', 'blog', 'ipod'],
    'World': ['world', 'international', 'war', 'peace', 'conflict', 'military', 'army', 'navy', 'president', 'minister', 'parliament', 'election', 'vote', 'government', 'treaty', 'un', 'united nations', 'security council', 'bomb', 'blast', 'attack', 'kill', 'hostage', 'terror', 'iraq', 'iran', 'israel', 'palestine', 'gaza', 'syria', 'afghanistan', 'russia', 'china', 'usa', 'bush', 'kerry', 'putin', 'blair', 'uk', 'france', 'germany', 'eu', 'europe', 'africa', 'asia', 'darfur', 'sudan', 'hurricane', 'typhoon', 'quake', 'tsunami', 'storm', 'police', 'crash', 'court', 'trial', 'judge', 'prison', 'jail', 'law', 'legal', 'protest', 'riot', 'rebel', 'troop', 'soldier']
}

def classify(title, desc):
    t_tokens = re.findall(r'\w+', title.lower())
    d_tokens = re.findall(r'\w+', desc.lower())
    
    scores = {cat: 0 for cat in keywords}
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in t_tokens:
                scores[cat] += 2
            if kw in d_tokens:
                scores[cat] += 1
                
    # If all scores are 0, what to do?
    # Maybe check for 'world' in region name? No, region is separate.
    if all(s == 0 for s in scores.values()):
        return None # Unclassified
        
    return max(scores, key=scores.get)

world_articles = []
for item in joined_data:
    cat = classify(item['title'], item['description'])
    if cat == 'World':
        world_articles.append(item)

# Count by region
region_counts = collections.Counter(a['region'] for a in world_articles)

print("__RESULT__:")
print(json.dumps(region_counts))"""

env_args = {'var_function-call-1113576567256238630': 'file_storage/function-call-1113576567256238630.json', 'var_function-call-4504038018777674965': 6696, 'var_function-call-12536537785643237180': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6757720913690530617': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
