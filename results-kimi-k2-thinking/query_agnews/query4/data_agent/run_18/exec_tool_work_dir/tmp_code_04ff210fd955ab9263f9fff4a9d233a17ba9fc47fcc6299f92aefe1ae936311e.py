code = """import json
import re

# Load data
metadata_file_path = locals()['var_functions.query_db:4']
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

articles_file_path = locals()['var_functions.query_db:12']
with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Create lookup dictionaries
metadata_dict = {item['article_id']: item for item in metadata_2015}
articles_dict = {item['article_id']: item for item in all_articles}

# Find World category articles published in 2015
world_articles = []

# Keywords for World category
world_keywords = [
    'iraq', 'iran', 'afghanistan', 'war', 'conflict', 'united nations', 'world', 'global',
    'international', 'peace', 'treaty', 'diplomatic', 'embassy', 'ambassador', 'foreign',
    'abroad', 'overseas', 'europe', 'asia', 'africa', 'south america', 'north america',
    'mideast', 'middle east', 'china', 'japan', 'russia', 'ukraine', 'israel', 'palestine',
    'syria', 'lebanon', 'pakistan', 'india', 'korea', 'afghan', 'taliban', 'al qaeda',
    'terrorist', 'terrorism', 'military', 'pentagon', 'defense', 'security', 'nato'
]

# Process articles
for article in all_articles:
    article_id = str(article['article_id'])
    
    # Check if this article was published in 2015
    if article_id in metadata_dict:
        metadata = metadata_dict[article_id]
        title = article.get('title', '').lower()
        description = article.get('description', '').lower()
        
        # Check if it's World category
        is_world = any(keyword in title or keyword in description for keyword in world_keywords)
        
        if is_world:
            world_articles.append({
                'article_id': article_id,
                'region': metadata['region'],
                'title': article.get('title', ''),
                'description': article.get('description', '')
            })

# Count by region
region_counts = {}
for article in world_articles:
    region = article['region']
    region_counts[region] = region_counts.get(region, 0) + 1

# Sort by count descending
sorted_regions = sorted(region_counts.items(), key=lambda x: x[1], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'world_articles_count': len(world_articles),
    'region_counts': region_counts,
    'top_region': sorted_regions[0] if sorted_regions else None,
    'top_5_regions': sorted_regions[:5]
}, default=str))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.list_db:1': ['articles'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'_id': '6969df3b0f682e5f6f226df5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969df3b0f682e5f6f226df6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969df3b0f682e5f6f226df7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969df3b0f682e5f6f226df8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969df3b0f682e5f6f226df9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:10': {'metadata_2015_count': 6696, 'articles_data_count': 5, 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}], 'sample_articles': [{'_id': '6969df3b0f682e5f6f226df5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969df3b0f682e5f6f226df6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969df3b0f682e5f6f226df7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': {'metadata_2015_count': 6696, 'all_articles_count': 50000, 'sample_metadata': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}], 'sample_articles': [{'_id': '6969df3b0f682e5f6f226df5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969df3b0f682e5f6f226df6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969df3b0f682e5f6f226df7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}}

exec(code, env_args)
