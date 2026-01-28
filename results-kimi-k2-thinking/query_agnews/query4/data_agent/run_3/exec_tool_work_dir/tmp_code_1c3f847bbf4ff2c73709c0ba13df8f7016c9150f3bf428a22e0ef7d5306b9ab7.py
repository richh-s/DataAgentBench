code = """import json

# Get file paths from the variables
metadata_file_path = locals()['var_functions.query_db:2']
articles_file_path = locals()['var_functions.query_db:12']

# Load the actual data from files
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Process the data
metadata_dict = {item['article_id']: item for item in metadata_2015}
articles_dict = {str(article['article_id']): article for article in all_articles}

# Keywords for categorization
world_keywords = ['world', 'global', 'international', 'war', 'iraq', 'iran', 'russia', 'china', 'military', 'diplomatic', 'un', 'united nations', 'peace', 'conflict', 'crisis', 'treaty']
sports_keywords = ['game', 'olympic', 'football', 'soccer', 'basketball', 'tennis', 'match']
business_keywords = ['stock', 'business', 'finance', 'economic', 'market', 'company', 'wall street']
scitech_keywords = ['science', 'technology', 'research', 'computer', 'software', 'medical', 'health']

def get_category(title, desc):
    text = (title + ' ' + desc).lower()
    
    for kw in sports_keywords:
        if kw in text:
            return 'Sports'
    
    for kw in business_keywords:
        if kw in text:
            return 'Business'
    
    for kw in scitech_keywords:
        if kw in text:
            return 'Science/Technology'
    
    for kw in world_keywords:
        if kw in text:
            return 'World'
    
    return 'World'  # Default for international news

# Count World articles by region
region_counts = {}
processed = 0
for aid in metadata_dict:
    if aid in articles_dict:
        processed += 1
        article = articles_dict[aid]
        cat = get_category(article.get('title',''), article.get('description',''))
        if cat == 'World':
            region = metadata_dict[aid]['region']
            region_counts[region] = region_counts.get(region, 0) + 1

# Find region with most World articles
top_region = max(region_counts.items(), key=lambda x: x[1]) if region_counts else ('None', 0)

print('__RESULT__:')
print(json.dumps({
    'total_processed': processed,
    'world_articles_by_region': region_counts,
    'top_region': top_region[0],
    'top_count': top_region[1]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:8': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:12': [{'_id': '6969d1d05681768c0793155f', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d1d05681768c07931560', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d1d05681768c07931561', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d1d05681768c07931562', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d1d05681768c07931563', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': 6696, 'var_functions.execute_python:16': 6696, 'var_functions.list_db:24': ['authors', 'article_metadata'], 'var_functions.execute_python:32': {'count': 6696}, 'var_functions.execute_python:38': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:8', 'var_functions.query_db:12', 'var_functions.execute_python:14', 'var_functions.execute_python:16', 'var_functions.list_db:24', 'var_functions.execute_python:32', '__builtins__', 'json'], 'var_functions.execute_python:44': {'type': "<class 'str'>", 'length': 38, 'sample': 'file_storage/functions.query_db:2.json'}}

exec(code, env_args)
