code = """import json
import pandas as pd

# Load 2015 metadata
metadata_2015_file = 'file_storage/functions.query_db:18.json'
with open(metadata_2015_file, 'r') as f:
    metadata_2015 = json.load(f)

# Load all articles
articles_file = 'file_storage/functions.query_db:30.json'
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Convert to DataFrames
metadata_df = pd.DataFrame(metadata_2015)
metadata_df['article_id'] = metadata_df['article_id'].astype(str)
articles_df = pd.DataFrame(all_articles)
articles_df['article_id'] = articles_df['article_id'].astype(str)

# Merge to get 2015 articles with full content
merged_df = pd.merge(articles_df, metadata_df, on='article_id', how='inner')

# Combine title and description for analysis
merged_df['combined_text'] = merged_df['title'].fillna('') + ' ' + merged_df['description'].fillna('')

def categorize_article(text):
    lower_text = text.lower()
    
    world_keywords = ['iraq', 'iran', 'israel', 'palestine', 'afghanistan', 'pakistan', 'india', 'china', 'japan', 'korea', 'russia', 'ukraine', 'united nations', 'un', 'refugee', 'global', 'international']
    
    sports_keywords = ['football', 'soccer', 'basketball', 'tennis', 'olympics', 'world cup', 'championship', 'tournament']
    
    business_keywords = ['stock', 'wall street', 'economy', 'market', 'trade', 'oil', 'price', 'company', 'business', 'bank']
    
    science_tech_keywords = ['technology', 'google', 'microsoft', 'software', 'computer', 'internet', 'science']
    
    world_count = sum(1 for keyword in world_keywords if keyword in lower_text)
    sports_count = sum(1 for keyword in sports_keywords if keyword in lower_text)
    business_count = sum(1 for keyword in business_keywords if keyword in lower_text)
    science_tech_count = sum(1 for keyword in science_tech_keywords if keyword in lower_text)
    
    counts = {'World': world_count, 'Sports': sports_count, 'Business': business_count, 'Science/Technology': science_tech_count}
    max_category = max(counts, key=counts.get)
    
    if counts[max_category] <= 1:
        if any(keyword in lower_text for keyword in ['iraq', 'iran', 'israel', 'un', 'refugee']):
            return 'World'
        elif any(keyword in lower_text for keyword in ['stock', 'market', 'economy', 'oil']):
            return 'Business'
        else:
            return 'World'
    
    return max_category

merged_df['category'] = merged_df['combined_text'].apply(categorize_article)

world_2015 = merged_df[merged_df['category'] == 'World']
region_counts = world_2015['region'].value_counts()

top_region = region_counts.idxmax()
top_count = int(region_counts.max())

result = {
    'top_region': top_region,
    'article_count': top_count,
    'region_breakdown': region_counts.to_dict()
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'metadata_count': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:16': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_articles': 5, 'articles_2015': 0, 'sample_data': []}, 'var_functions.query_db:22': [{'total_metadata': '6696'}], 'var_functions.query_db:24': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
