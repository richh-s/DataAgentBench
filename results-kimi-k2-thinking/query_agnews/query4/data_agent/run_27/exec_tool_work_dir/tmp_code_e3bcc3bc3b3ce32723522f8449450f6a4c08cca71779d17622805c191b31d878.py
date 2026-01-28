code = """import json

# Get the stored variables
articles_result = locals().get('var_functions.query_db:18')
metadata_result = locals().get('var_functions.query_db:3')

# Load data from file paths
with open(articles_result, 'r') as f:
    all_articles = json.load(f)

with open(metadata_result, 'r') as f:
    all_metadata = json.load(f)

# Filter for 2015 articles
metadata_2015 = [m for m in all_metadata if m.get('publication_date', '').startswith('2015-')]

print(f'Total articles: {len(all_articles)}')
print(f'2015 articles: {len(metadata_2015)}')

# Find World category articles
world_articles = []
for article in all_articles:
    article_id = article['article_id']
    # Check if this article was published in 2015
    metadata_2015_for_article = [m for m in metadata_2015 if m['article_id'] == article_id]
    if metadata_2015_for_article:
        # Simple heuristic for World category
        title_desc = (article['title'] + ' ' + article['description']).lower()
        
        world_indicators = ['iraq', 'iran', 'iraqi', 'iranian', 'asia', 'europe', 'africa', 
                           'south america', 'north america', 'japan', 'china', 'india', 'korea',
                           'saudi', 'afghanistan', 'sudan', 'chad', 'nigeria', 'mexico', 'canada',
                           'eurozone', 'euro', 'opec', 'oil export', 'oil pipeline', 'dollar',
                           'trade deficit', 'global', 'international', 'refugee', 'militia']
        
        sports_indicators = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'olympic', 'game']
        
        if any(indicator in title_desc for indicator in world_indicators) and not any(sport in title_desc for sport in sports_indicators):
            metadata = metadata_2015_for_article[0]
            world_articles.append({
                'article_id': article_id,
                'region': metadata['region'],
                'title': article['title'][:50] + '...'
            })

print(f'World articles: {len(world_articles)}')

# Count by region
region_counts = {}
for article in world_articles:
    region = article['region']
    region_counts[region] = region_counts.get(region, 0) + 1

print(f'Region counts: {region_counts}')

# Find top region
top_region = max(region_counts.items(), key=lambda x: x[1]) if region_counts else None
print(f'Top region: {top_region}')

# Return result
result = {
    'top_region': top_region[0] if top_region else None,
    'count': top_region[1] if top_region else 0,
    'all_counts': region_counts
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e431beeeb5230db76b0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e431beeeb5230db76b0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e431beeeb5230db76b10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e431beeeb5230db76b11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e431beeeb5230db76b12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:16': {'articles_type': "<class 'list'>", 'articles_length': 5, 'metadata_type': "<class 'str'>", 'metadata_is_str': True}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
