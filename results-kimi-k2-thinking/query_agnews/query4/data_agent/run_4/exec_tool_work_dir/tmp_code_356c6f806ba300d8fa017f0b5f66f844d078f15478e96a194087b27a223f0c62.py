code = """import json
import pandas as pd
import re

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

# Combine title and description for text analysis
merged_df['combined_text'] = merged_df['title'].fillna('') + ' ' + merged_df['description'].fillna('')

# Function to categorize articles
def categorize_article(text):
    """
    Categorize articles based on title and description
    Categories: World, Sports, Business, Science/Technology
    """
    lower_text = text.lower()
    
    # Count keywords for each category
    world_keywords = ['iraq', 'iran', 'israel', 'palestine', 'afghanistan', 'pakistan', 'india', 'china', 'japan', 'korea', 'russia', 'ukraine', 'europe', 'asia', 'africa', 'middle east', 'united nations', 'un', 'war', 'peace', 'diplomat', 'embassy', 'world bank', 'imf', 'refugee', 'border', 'conflict', 'crisis', 'global', 'international', 'peacekeeping', 'treaty', 'summit']
    
    sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'olympics', 'world cup', 'championship', 'tournament', 'coach', 'player', 'team', 'league', 'season', 'score', 'game', 'match', 'victory', 'win', 'lose', 'sport', 'sports']
    
    business_keywords = ['stock', 'stocks', 'wall street', 'dow', 'nasdaq', 'economy', 'economic', 'market', 'trade', 'deficit', 'oil', 'price', 'prices', 'company', 'companies', 'profit', 'loss', 'revenue', 'sales', 'business', 'corporate', 'bank', 'investment', 'investor', 'share', 'shares', 'earnings', 'quarter', 'growth', 'gdp', 'unemployment', 'job', 'jobs']
    
    science_tech_keywords = ['technology', 'tech', 'science', 'scientific', 'research', 'google', 'microsoft', 'apple', 'hp', 'intel', 'software', 'hardware', 'computer', 'internet', 'web', 'online', 'digital', 'mobile', 'phone', 'patent', 'innovation', 'ai', 'artificial intelligence', 'chip', 'semiconductor', 'space', 'nasa', 'satellite', 'biotech', 'pharmaceutical']
    
    world_count = sum(1 for keyword in world_keywords if keyword in lower_text)
    sports_count = sum(1 for keyword in sports_keywords if keyword in lower_text)
    business_count = sum(1 for keyword in business_keywords if keyword in lower_text)
    science_tech_count = sum(1 for keyword in science_tech_keywords if keyword in lower_text)
    
    # Determine category
    counts = {
        'World': world_count,
        'Sports': sports_count,
        'Business': business_count,
        'Science/Technology': science_tech_count
    }
    
    # Get category with max count
    max_category = max(counts, key=counts.get)
    
    # If all counts are 0 or very low, use some heuristics
    if counts[max_category] <= 1:
        # Default heuristics
        if any(keyword in lower_text for keyword in ['iraq', 'iran', 'israel', 'un', 'refugee', 'peace', 'summit']):
            return 'World'
        elif any(keyword in lower_text for keyword in ['stock', 'market', 'economy', 'company', 'profit', 'oil', 'google']):
            return 'Business'
        elif any(keyword in lower_text for keyword in ['technology', 'tech', 'software', 'computer', 'internet']):
            return 'Science/Technology'
        else:
            return 'World'  # Default to World
    
    return max_category

# Apply categorization
merged_df['category'] = merged_df['combined_text'].apply(categorize_article)

# Filter for World category in 2015
world_2015 = merged_df[merged_df['category'] == 'World']

# Count articles per region
region_counts = world_2015['region'].value_counts()

# Get top region
top_region = region_counts.idxmax()
top_count = region_counts.max()

print('__RESULT__:')
print(json.dumps({
    'top_region': top_region,
    'article_count': int(top_count),
    'total_world_articles': len(world_2015),
    'region_breakdown': region_counts.to_dict()
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:14': {'metadata_count': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:16': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_articles': 5, 'articles_2015': 0, 'sample_data': []}, 'var_functions.query_db:22': [{'total_metadata': '6696'}], 'var_functions.query_db:24': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': [{'_id': '6969d27ce5ce562e5673a9ed', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d27ce5ce562e5673a9ee', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d27ce5ce562e5673a9ef', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d27ce5ce562e5673a9f0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d27ce5ce562e5673a9f1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
