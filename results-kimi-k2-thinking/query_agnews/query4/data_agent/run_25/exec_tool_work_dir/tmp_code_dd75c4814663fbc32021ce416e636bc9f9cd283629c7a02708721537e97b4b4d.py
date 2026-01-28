code = """import json

# Load all articles and 2015 metadata
articles_file = locals()['var_functions.query_db:24']
with open(articles_file, 'r') as f:
    articles_all = json.load(f)

metadata_file = locals()['var_functions.query_db:10']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Create mapping from article_id to region
article_region_map = {item['article_id']: item['region'] for item in metadata_2015}

# Filter 2015 articles
articles_2015 = [a for a in articles_all if a['article_id'] in article_region_map]

print('All articles:', len(articles_all))
print('2015 articles:', len(articles_2015))
print('Metadata records:', len(metadata_2015))

# Simple categorization function
def get_category(text):
    text_lower = text.lower()
    
    # World keywords
    world_words = ['iraq','iran','china','japan','korea','africa','europe','india','america','canada','australia','war','peace','un','world','international','foreign','disaster','earthquake','hurricane']
    
    # Business keywords
    business_words = ['stock','stocks','dow','nasdaq','economy','economic','oil price','dollar','euro','fed','business','revenue','profit']
    
    # Sports keywords
    sports_words = ['football','soccer','basketball','baseball','hockey','tennis','olympic','championship','tournament']
    
    # Tech keywords
    tech_words = ['google','microsoft','apple','technology','tech','science','internet','computer','software']
    
    # Score
    scores = []
    if any(word in text_lower for word in world_words): scores.append('World')
    if any(word in text_lower for word in business_words): scores.append('Business')
    if any(word in text_lower for word in sports_words): scores.append('Sports')
    if any(word in text_lower for word in tech_words): scores.append('Technology')
    
    return scores[0] if scores else 'World'

# Categorize and count
world_articles_by_region = {}
total_by_region = {}

for article in articles_2015:
    region = article_region_map[article['article_id']]
    title = article['title']
    desc = article['description']
    
    total_by_region[region] = total_by_region.get(region, 0) + 1
    
    # Combine title and description
    text = title + ' ' + desc
    category = get_category(text)
    
    if category == 'World':
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

print('Total 2015 articles by region:', total_by_region)
print('World articles by region:', world_articles_by_region)

# Find region with most World articles
if world_articles_by_region:
    max_region = max(world_articles_by_region, key=world_articles_by_region.get)
    max_count = world_articles_by_region[max_region]
    print(f'Region with most World articles: {max_region} ({max_count} articles)')
else:
    print('No World articles found')

print('__RESULT__:')
print(json.dumps(world_articles_by_region))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e2f52f04fcdaecf22318', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e2f52f04fcdaecf22319', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e2f52f04fcdaecf2231a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e2f52f04fcdaecf2231b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e2f52f04fcdaecf2231c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:4': ['authors', 'article_metadata'], 'var_functions.query_db:6': [{'_id': '6969e2f52f04fcdaecf22318', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e2f52f04fcdaecf22319', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e2f52f04fcdaecf2231a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e2f52f04fcdaecf2231b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e2f52f04fcdaecf2231c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:18': {'total_articles_2015': 6696, 'regions': {'Europe': 1357, 'South America': 1332, 'Africa': 1345, 'Asia': 1333, 'North America': 1329}}, 'var_functions.query_db:20': [{'_id': '6969e2f52f04fcdaecf22318', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e2f52f04fcdaecf22319', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e2f52f04fcdaecf2231a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e2f52f04fcdaecf2231b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e2f52f04fcdaecf2231c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:22': {'total_articles': 5, 'articles_2015_count': 0, 'article_ids_2015_count': 6696}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:28': {'total_articles': 10000, 'articles_2015_count': 494}}

exec(code, env_args)
