code = """import json
import re

meta_path = locals()['var_functions.query_db:2']
arts_path = locals()['var_functions.query_db:44']

with open(meta_path, 'r') as f:
    metadata_2015 = json.load(f)

with open(arts_path, 'r') as f:
    articles_all = json.load(f)

# Create mappings
region_map = {int(rec['article_id']): rec['region'] for rec in metadata_2015}
art_map = {int(rec['article_id']): rec for rec in articles_all}

# Get common articles
common_ids = set(region_map.keys()) & set(art_map.keys())

# Keyword lists
world_words = ['world', 'global', 'international', 'united nations', 'un', 'war', 'conflict', 'peace', 'diplomat', 'embassy', 'crisis', 'foreign']
sports_words = ['sports', 'game', 'match', 'player', 'coach', 'league', 'tournament']
business_words = ['business', 'economy', 'stock', 'market', 'company', 'investment', 'finance']
scitech_words = ['science', 'technology', 'research', 'study', 'scientist', 'tech', 'computer']

def get_category(title, desc):
    text = (title + ' ' + desc).lower()
    
    if any(w in text for w in sports_words):
        return 'Sports'
    if any(w in text for w in business_words):
        return 'Business'
    if any(w in text for w in scitech_words):
        return 'Science/Technology'
    if any(w in text for w in world_words):
        return 'World'
    
    return 'Other'

# Count World articles by region
world_counts = {}
checked = 0

for aid in common_ids:
    a = art_map[aid]
    cat = get_category(a.get('title',''), a.get('description',''))
    checked += 1
    
    if cat == 'World':
        reg = region_map[aid]
        world_counts[reg] = world_counts.get(reg, 0) + 1

print('Checked', checked, 'articles')
print('World articles by region:', world_counts)

if world_counts:
    top = max(world_counts, key=world_counts.get)
    print('Top region:', top, world_counts[top])

result = {'checked': checked, 'world_counts': world_counts, 'top': max(world_counts, key=world_counts.get) if world_counts else None}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'metadata_count': 6696, 'articles_count': 5}, 'var_functions.query_db:16': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:28': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:42': [{'_id': '6969e07c5660b390b4e04a79', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e07c5660b390b4e04a7a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e07c5660b390b4e04a7b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e07c5660b390b4e04a7c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e07c5660b390b4e04a7d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.execute_python:48': {'metadata_2015_count': 6696, 'articles_all_count': 50000, 'common_ids_count': 2606}, 'var_functions.execute_python:50': {'total_2015_articles': 2606, 'region_counts': {'Asia': 517, 'North America': 489, 'South America': 529, 'Europe': 535, 'Africa': 536}}}

exec(code, env_args)
