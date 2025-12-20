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
    return []

# Load metadata
meta_var = locals().get('var_function-call-1113576567256238630')
metadata_list = load_data(meta_var)

# Load articles chunk 1
chunk1_var = locals().get('var_function-call-3180343222858944713')
articles_list1 = load_data(chunk1_var)

# Load articles chunk 2
chunk2_var = locals().get('var_function-call-428940154534076718')
articles_list2 = load_data(chunk2_var)

# Combine articles
# Use dictionary for fast lookup
articles_map = {}
for a in articles_list1:
    articles_map[str(a['article_id'])] = a
for a in articles_list2:
    articles_map[str(a['article_id'])] = a

# Join
joined_data = []
missing_count = 0
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
    else:
        missing_count += 1

# Keywords
keywords = {
    'Sports': ['sport', 'game', 'team', 'match', 'cup', 'league', 'win', 'loss', 'score', 'player', 'olympic', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'nfl', 'nba', 'mlb', 'nhl', 'champion', 'medal', 'coach', 'stadium', 'race', 'f1', 'golf', 'hockey', 'cricket', 'rugby', 'tournament', 'athens', 'sox', 'yankees', 'reds', 'bulls', 'lakers', 'final', 'semi-final'],
    'Business': ['business', 'company', 'market', 'stock', 'share', 'trade', 'economy', 'profit', 'loss', 'revenue', 'invest', 'bank', 'dollar', 'euro', 'yen', 'oil', 'price', 'corp', 'inc', 'ltd', 'wall st', 'nasdaq', 'dow jones', 'ceo', 'cfo', 'merger', 'acquisition', 'deal', 'sale', 'fed', 'inflation', 'rates', 'earnings', 'quarter', 'growth', 'airbus', 'boeing', 'oracle', 'google', 'microsoft', 'ibm'],
    'Sci/Tech': ['technology', 'science', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'google', 'microsoft', 'apple', 'intel', 'ibm', 'virus', 'space', 'nasa', 'orbit', 'moon', 'mars', 'research', 'study', 'cell', 'phone', 'mobile', 'wireless', 'network', 'chip', 'processor', 'linux', 'windows', 'browser', 'server', 'satellite', 'biotech', 'robot', 'spam', 'hacker', 'blog', 'ipod'],
    'World': ['world', 'international', 'war', 'peace', 'conflict', 'military', 'army', 'navy', 'president', 'minister', 'parliament', 'election', 'vote', 'government', 'treaty', 'un', 'united nations', 'security council', 'bomb', 'blast', 'attack', 'kill', 'hostage', 'terror', 'iraq', 'iran', 'israel', 'palestine', 'gaza', 'syria', 'afghanistan', 'russia', 'china', 'usa', 'bush', 'kerry', 'putin', 'blair', 'uk', 'france', 'germany', 'eu', 'europe', 'africa', 'asia', 'darfur', 'sudan', 'hurricane', 'typhoon', 'quake', 'tsunami', 'storm', 'police', 'crash', 'court', 'trial', 'judge', 'prison', 'jail', 'law', 'legal', 'protest', 'riot', 'rebel', 'troop', 'soldier', 'baghdad', 'kabul', 'tehran', 'jerusalem']
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
                
    if all(s == 0 for s in scores.values()):
        # Fallback: maybe specific check for common words?
        # "oil" -> Business or World?
        # If ambiguous, maybe Business if price mentioned, World if Iraq?
        if 'oil' in t_tokens or 'oil' in d_tokens:
            if 'price' in t_tokens or 'price' in d_tokens:
                return 'Business'
            if 'iraq' in t_tokens or 'iraq' in d_tokens:
                return 'World'
            return 'Business' # Default oil to Business
        return 'World' # Default to World if unknown (risky but "largest number" implies many)
        
    return max(scores, key=scores.get)

world_articles = []
for item in joined_data:
    cat = classify(item['title'], item['description'])
    if cat == 'World':
        world_articles.append(item)

# Count by region
region_counts = collections.Counter(a['region'] for a in world_articles)

# Find largest
if region_counts:
    top_region = region_counts.most_common(1)[0]
    result = {
        "top_region": top_region[0],
        "count": top_region[1],
        "all_counts": dict(region_counts),
        "total_world_articles": len(world_articles),
        "total_joined": len(joined_data),
        "missing": missing_count
    }
else:
    result = {"error": "No world articles found", "missing": missing_count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1113576567256238630': 'file_storage/function-call-1113576567256238630.json', 'var_function-call-4504038018777674965': 6696, 'var_function-call-12536537785643237180': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6757720913690530617': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3911136318591709052': {}, 'var_function-call-4960252981226212142': {'meta_count': 6696, 'art_count': 5, 'meta_sample_ids': ['13', '18', '26', '51', '52'], 'art_sample_ids': ['0', '1', '2', '3', '4'], 'art_sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)'], 'overlap_count': 0, 'sample_overlap': []}, 'var_function-call-11871230373173193569': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-3180343222858944713': 'file_storage/function-call-3180343222858944713.json', 'var_function-call-428940154534076718': 'file_storage/function-call-428940154534076718.json'}

exec(code, env_args)
