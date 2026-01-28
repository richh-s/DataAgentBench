code = """import json

# Get file path from previous MongoDB query
all_articles_file = locals()['var_functions.query_db:24']
with open(all_articles_file, 'r') as f:
    all_articles = json.load(f)

# Get 2015 metadata from file
metadata_file = locals()['var_functions.query_db:4']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Build region map
region_map = {}
for item in metadata_2015:
    region_map[int(item['article_id'])] = item['region']

# Filter to 2015 articles and add region
articles_2015 = []
for article in all_articles:
    article_id = int(article['article_id'])
    if article_id in region_map:
        article_copy = dict(article)
        article_copy['region'] = region_map[article_id]
        article_copy['article_id'] = article_id
        articles_2015.append(article_copy)

print(f'Total 2015 articles: {len(articles_2015)}')
print(f'First article: {articles_2015[0]}')

# Classify articles into categories
world_articles = []
sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'olympic', 'super bowl', 'world cup', 'champion', 'gold medal', 'coach', 'player', 'team', 'game', 'sport']
business_keywords = ['wall st', 'wall street', 'stock', 'dow jones', 'nasdaq', 'company', 'business', 'economic', 'economy', 'market', 'profit', 'bank', 'investment', 'stock market', 'shares', 'trading']
science_tech_keywords = ['scientist', 'technology', 'tech', 'computer', 'internet', 'software', 'hardware', 'research', 'study', 'nasa', 'space', 'satellite', 'laboratory', 'digital', 'robot', 'genetic']
world_keywords = ['iraq', 'afghanistan', 'war', 'peace', 'united nations', 'un', 'eu', 'european union', 'world bank', 'diplomat', 'embassy', 'consulate', 'treaty', 'alliance', 'border', 'conflict', 'military', 'terrorist', 'terrorism', 'nuclear', 'weapon']

for article in articles_2015:
    title = article['title'].lower()
    desc = article['description'].lower()
    text = title + ' ' + desc
    
    is_sports = any(kw in text for kw in sports_keywords)
    is_business = any(kw in text for kw in business_keywords)
    is_science_tech = any(kw in text for kw in science_tech_keywords)
    is_world = any(kw in text for kw in world_keywords)
    
    # Priority: if it matches World keywords, classify as World
    # Otherwise, use other categories
    if is_world:
        article_copy = dict(article)
        article_copy['category'] = 'World'
        world_articles.append(article_copy)
    elif is_sports and not (is_business or is_science_tech):
        continue  # Sports
    elif is_business and not (is_sports or is_science_tech):
        continue  # Business
    elif is_science_tech and not (is_sports or is_business):
        continue  # Science/Technology
    else:
        # Check if it might be World based on broader context
        # Look for country names, international relations
        if any(x in text for x in ['china', 'russia', 'iran', 'israel', 'palestine', 'syria', 'lebanon', 'pakistan', 'india', 'korea', 'japan', 'china', 'afghanistan', 'iraq', 'turkey', 'saudi', 'egypt', 'jordan', 'libya', 'yemen']):
            article_copy = dict(article)
            article_copy['category'] = 'World'
            world_articles.append(article_copy)

print(f'World articles found: {len(world_articles)}')
if world_articles:
    print('Sample World article:', world_articles[0])

# Count by region
from collections import Counter
region_counts = Counter([a['region'] for a in world_articles])
print('Region counts:', dict(region_counts))

most_common_region = region_counts.most_common(1)
if most_common_region:
    result = {
        'most_common_region': most_common_region[0][0],
        'count': most_common_region[0][1],
        'total_world_articles': len(world_articles)
    }
else:
    result = {'most_common_region': None, 'count': 0, 'total_world_articles': 0}

result['all_counts'] = dict(region_counts)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'region_map_size': 6696, 'metadata_count': 6696, 'first_article_id': '13', 'first_region': 'Europe'}, 'var_functions.query_db:24': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
