code = """import json
import pandas as pd
import re

# Load full articles data
articles_file_path = locals()['var_functions.query_db:14']
metadata_file_path = locals()['var_functions.query_db:3']

# Read both JSON files
if isinstance(articles_file_path, str) and articles_file_path.endswith('.json'):
    with open(articles_file_path, 'r') as f:
        articles_data = json.load(f)
else:
    articles_data = locals()['var_functions.query_db:14']

if isinstance(metadata_file_path, str) and metadata_file_path.endswith('.json'):
    with open(metadata_file_path, 'r') as f:
        metadata_data = json.load(f)
else:
    metadata_data = locals()['var_functions.query_db:3']

# Convert to DataFrames
articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Convert article_id to string for matching
articles_df['article_id'] = articles_df['article_id'].astype(str)
metadata_df['article_id'] = metadata_df['article_id'].astype(str)

# Merge datasets
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')

# Filter for 2015
merged_df['publication_date'] = pd.to_datetime(merged_df['publication_date'])
merged_2015 = merged_df[merged_df['publication_date'].dt.year == 2015]

# Create categorization function
def categorize_article(title, description):
    text = f"{title} {description}".lower()
    
    # Sports indicators
    sports_terms = ['nfl', 'nba', 'mlb', 'nhl', 'football', 'basketball', 'baseball', 'hockey', 'soccer', 'tennis', 'olympic', 'game', 'match', 'player', 'team']
    if any(term in text for term in sports_terms):
        return 'Sports'
    
    # Business indicators  
    business_terms = ['stock', 'market', 'economy', 'business', 'company', 'corporate', 'trade', 'dollar', 'oil price', 'google ipo', 'investment', 'profit', 'revenue']
    if any(term in text for term in business_terms):
        return 'Business'
    
    # Science/Tech indicators
    tech_terms = ['google', 'technology', 'tech', 'internet', 'software', 'hardware', 'scientific', 'research', 'nuclear', 'solar', 'energy technology']
    if any(term in text for term in tech_terms):
        return 'Science/Technology'
    
    # World indicators (geo-political, international affairs, conflicts, etc.)
    world_terms = ['iraq', 'iran', 'afghanistan', 'war', 'conflict', 'united nations', 'peace', 'diplomatic', 'embassy', 'rebel', 'militia', 'pipeline', 'japan', 'china', 'south africa', 'chad', 'refugee', 'israel', 'palestin', 'korea', 'saudi', 'oil export']
    if any(term in text for term in world_terms):
        return 'World'
    
    # Default fallback - analyze content
    # If it mentions countries/regions and political/social issues
    countries = ['usa', 'uk', 'europe', 'asia', 'africa', 'america', 'china', 'japan', 'iraq', 'iran', 'israel', 'russia', 'mexico', 'canada']
    political_terms = ['government', 'president', 'election', 'policy', 'minister', 'senate', 'congress', 'parliament']
    
    country_mentions = sum(1 for country in countries if country in text)
    political_mentions = sum(1 for term in political_terms if term in text)
    
    if country_mentions > 0 or political_mentions > 0:
        return 'World'
    
    # Default to World if uncertain (international news dataset)
    return 'World'

# Apply categorization
merged_2015['category'] = merged_2015.apply(lambda row: categorize_article(row['title'], row['description']), axis=1)

# Filter for World category
world_2015 = merged_2015[merged_2015['category'] == 'World']

# Count by region
region_counts = world_2015['region'].value_counts()

print('__RESULT__:')
print(json.dumps({
    'total_articles_2015': len(merged_2015),
    'world_articles_2015': len(world_2015),
    'region_counts': region_counts.to_dict(),
    'top_region': region_counts.index[0] if len(region_counts) > 0 else None,
    'top_region_count': int(region_counts.iloc[0]) if len(region_counts) > 0 else 0
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:6': {'articles_shape': [5, 4], 'metadata_shape': [6696, 3], 'articles_columns': ['_id', 'article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'region', 'publication_date'], 'articles_head': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'metadata_head': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'region': 'Africa', 'publication_date': '2015-06-02'}]}, 'var_functions.query_db:8': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'articles_count': 5, 'sample_articles': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
