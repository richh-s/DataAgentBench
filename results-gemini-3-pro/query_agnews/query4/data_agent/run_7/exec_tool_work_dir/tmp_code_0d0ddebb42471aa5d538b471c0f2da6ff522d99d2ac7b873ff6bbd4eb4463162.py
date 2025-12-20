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

# Load chunks
chunk1 = load_data(locals().get('var_function-call-3180343222858944713'))
chunk2 = load_data(locals().get('var_function-call-428940154534076718'))
chunk3 = load_data(locals().get('var_function-call-16451314129414624884'))

# Load metadata
meta_list = load_data(locals().get('var_function-call-1113576567256238630'))

# Combine articles
articles_map = {}
for a in chunk1 + chunk2 + chunk3:
    articles_map[str(a['article_id'])] = a

print(f"Total unique articles: {len(articles_map)}")

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

print(f"Total joined: {len(joined_data)} out of {len(meta_list)}")

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
        # Heuristics for ties/zeros
        if 'oil' in t_tokens or 'oil' in d_tokens:
            if 'price' in t_tokens or 'price' in d_tokens:
                return 'Business'
            if 'iraq' in t_tokens or 'iraq' in d_tokens:
                return 'World'
            return 'Business'
        return 'World' # Default
        
    return max(scores, key=scores.get)

world_articles = []
for item in joined_data:
    cat = classify(item['title'], item['description'])
    if cat == 'World':
        world_articles.append(item)

# Count by region
region_counts = collections.Counter(a['region'] for a in world_articles)

result = {
    "top_region": region_counts.most_common(1)[0][0],
    "count": region_counts.most_common(1)[0][1],
    "all_counts": dict(region_counts)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-1113576567256238630': 'file_storage/function-call-1113576567256238630.json', 'var_function-call-4504038018777674965': 6696, 'var_function-call-12536537785643237180': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6757720913690530617': [{'_id': '6944f01c2559a523768b8392', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944f01c2559a523768b8393', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944f01c2559a523768b8394', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944f01c2559a523768b8395', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944f01c2559a523768b8396', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3911136318591709052': {}, 'var_function-call-4960252981226212142': {'meta_count': 6696, 'art_count': 5, 'meta_sample_ids': ['13', '18', '26', '51', '52'], 'art_sample_ids': ['0', '1', '2', '3', '4'], 'art_sample_titles': ['Wall St. Bears Claw Back Into the Black (Reuters)', 'Carlyle Looks Toward Commercial Aerospace (Reuters)', "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'Oil prices soar to all-time record, posing new menace to US economy (AFP)'], 'overlap_count': 0, 'sample_overlap': []}, 'var_function-call-11871230373173193569': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-3180343222858944713': 'file_storage/function-call-3180343222858944713.json', 'var_function-call-428940154534076718': 'file_storage/function-call-428940154534076718.json', 'var_function-call-8439387632348820906': {'top_region': 'North America', 'count': 461, 'all_counts': {'Africa': 459, 'North America': 461, 'Asia': 441, 'Europe': 441, 'South America': 436}, 'total_world_articles': 2238, 'total_joined': 5226, 'missing': 1470}, 'var_function-call-3430246693265726814': {'total_fetched': 150000, 'unique_fetched': 100000, 'missing_count': 1470, 'sample_missing': ['127344', '115070', '125568', '119363', '126562', '108532', '122387', '117220', '123260', '118485'], 'fetched_min': 0, 'fetched_max': 99999, 'missing_min': 100058, 'missing_max': 127570}, 'var_function-call-9722131743788783949': [], 'var_function-call-12225342654463950385': [], 'var_function-call-3177709901536100540': [{'_id': '6944f01e2559a523768d7502', 'article_id': '127344', 'title': 'Briefly: Israel, Egypt and US trade pact', 'description': 'Egypt, Israel and the United States have reached an agreement that allows Egyptian industry to sell products using Israeli parts duty free in America.'}], 'var_function-call-16451314129414624884': 'file_storage/function-call-16451314129414624884.json'}

exec(code, env_args)
