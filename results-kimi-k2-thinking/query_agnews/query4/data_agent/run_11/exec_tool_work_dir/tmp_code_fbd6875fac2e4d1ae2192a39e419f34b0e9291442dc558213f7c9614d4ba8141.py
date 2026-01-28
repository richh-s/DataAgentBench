code = """import json
import pandas as pd
import re

# Load data
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

articles_file = locals()['var_functions.query_db:24']
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Create DataFrames
df_metadata = pd.DataFrame(metadata_2015)
df_articles = pd.DataFrame(all_articles)

# Merge to get 2015 articles with full data
df_merged = pd.merge(df_metadata, df_articles, on='article_id', how='inner')

# Function to categorize articles
def categorize_article(title, description):
    text = f"{title} {description}".lower()
    
    # World category keywords
    world_keywords = [
        'war', 'conflict', 'iraq', 'afghanistan', 'iran', 'israel', 'palestine', 'lebanon',
        'syria', 'ukraine', 'russia', 'china', 'india', 'pakistan', 'korea', 'japan',
        'europe', 'africa', 'asia', 'america', 'united nations', 'un', 'government',
        'political', 'election', 'president', 'prime minister', 'global', 'international',
        'peace', 'military', 'troops', 'soldiers', 'attack', 'bomb', 'terror', 'diplomat',
        'foreign', 'border', 'crisis', 'refugee', 'diplomatic', 'treaty', 'allies',
        'nuclear', 'embassy', 'consulate', 'ambassador', 'summit', 'conference'
    ]
    
    # Sports category keywords (to exclude from World)
    sports_keywords = [
        'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf',
        'game', 'match', 'team', 'player', 'coach', 'season', 'championship',
        'tournament', 'olympic', 'world cup', 'league', 'score', 'victory', 'defeat'
    ]
    
    # Business category keywords (to exclude from World)
    business_keywords = [
        'stock', 'market', 'economy', 'finance', 'business', 'company', 'corporate',
        'profit', 'loss', 'revenue', 'sales', 'earnings', 'shares', 'trading',
        'wall st', 'nasdaq', 'dow', 'index', 'fund', 'investment', 'investor'
    ]
    
    # Science/Tech category keywords (to exclude from World)
    tech_keywords = [
        'technology', 'tech', 'science', 'research', 'study', 'internet', 'digital',
        'computer', 'software', 'hardware', 'mobile', 'phone', 'data', 'algorithm',
        'ai', 'artificial intelligence', 'robot', 'space', 'satellite', 'rocket'
    ]
    
    # Check if it's World category
    world_score = sum(1 for keyword in world_keywords if keyword in text)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text)
    business_score = sum(1 for keyword in business_keywords if keyword in text)
    tech_score = sum(1 for keyword in tech_keywords if keyword in text)
    
    # If world keywords present and not dominated by other categories
    if world_score > 0:
        max_other = max(sports_score, business_score, tech_score)
        if world_score >= max_other or (world_score > 0 and max_other == 0):
            return 'World'
    
    # Check other categories
    if sports_score > 0 and sports_score >= max(business_score, tech_score):
        return 'Sports'
    
    if business_score > 0 and business_score >= max(sports_score, tech_score):
        return 'Business'
    
    if tech_score > 0 and tech_score >= max(sports_score, business_score):
        return 'Science/Technology'
    
    # Default to World if contains geopolitical terms even without strong scores
    if any(term in text for term in ['iraq', 'afghanistan', 'israel', 'iran', 'korea', 'nuclear', 'war']):
        return 'World'
    
    return 'Other'

# Apply categorization
df_merged['category'] = df_merged.apply(
    lambda row: categorize_article(str(row['title']), str(row['description'])), 
    axis=1
)

# Filter for World category
world_articles = df_merged[df_merged['category'] == 'World']

# Count articles by region
region_counts = world_articles['region'].value_counts()

print('__RESULT__:')
print(json.dumps({
    'total_articles_2015': len(df_merged),
    'world_articles': len(world_articles),
    'region_counts': region_counts.to_dict(),
    'top_region': region_counts.index[0] if not region_counts.empty else None,
    'top_region_count': int(region_counts.iloc[0]) if not region_counts.empty else 0
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 6696, 'sample_article_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:6': [{'_id': '6969d9a5cb04bbc737d88faa', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d9a5cb04bbc737d88fab', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d9a5cb04bbc737d88fac', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d9a5cb04bbc737d88fad', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d9a5cb04bbc737d88fae', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': [{'_id': '6969d9a5cb04bbc737d88faa', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d9a5cb04bbc737d88fab', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d9a5cb04bbc737d88fac', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d9a5cb04bbc737d88fad', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d9a5cb04bbc737d88fae', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'metadata_type': "<class 'str'>", 'metadata_is_str': True, 'articles_type': "<class 'list'>", 'metadata_sample': '[{"article_id": "13", "region": "Europe"}, {"article_id": "18", "region": "South America"}]', 'articles_sample': '[{"_id": "6969d9a5cb04bbc737d88faa", "article_id": "0", "title": "Wall St. Bears Claw Back Into the Black (Reuters)", "description": "Reuters - Short-sellers, Wall Street\'s dwindling\\\\band of ultra-cynics, are seeing green again."}, {"_id": "6969d9a5cb04bbc737d88fab", "article_id": "1", "title": "Carlyle Looks Toward Commercial Aerospace (Reuters)", "description": "Reuters - Private investment firm Carlyle Group,\\\\which has a reputation for making well-timed and occasionally\\\\controversial plays in the defense industry, has quietly placed\\\\its bets on another part of the market."}]'}, 'var_functions.execute_python:14': {'metadata_shape': [6696, 2], 'articles_shape': [5, 4], 'metadata_columns': ['article_id', 'region'], 'articles_columns': ['_id', 'article_id', 'title', 'description'], 'sample_metadata': [{'article_id': '13', 'region': 'Europe'}, {'article_id': '18', 'region': 'South America'}], 'sample_articles': [{'_id': '6969d9a5cb04bbc737d88faa', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d9a5cb04bbc737d88fab', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}, 'var_functions.execute_python:16': {'total_article_ids': 6696, 'sample_ids': ['102395', '51016', '12410', '87211', '42487', '81093', '45816', '71849', '28798', '111235'], 'id_range': 'min: 13, max: 127570'}, 'var_functions.query_db:18': [{'_id': '6969d9a5cb04bbc737d88faa', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d9a5cb04bbc737d88fab', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d9a5cb04bbc737d88fac', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d9a5cb04bbc737d88fad', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d9a5cb04bbc737d88fae', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:20': [{'_id': '6969d9a5cb04bbc737d88faa', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d9a5cb04bbc737d88fab', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d9a5cb04bbc737d88fac', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d9a5cb04bbc737d88fad', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d9a5cb04bbc737d88fae', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:22': {'total_ids': 6696, 'min_id': 13, 'max_id': 127570, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271]}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': {'metadata_articles': 6696, 'all_articles': 127600, 'filtered_2015_articles': 6696, 'metadata_sample': [{'article_id': '13', 'region': 'Europe'}, {'article_id': '18', 'region': 'South America'}], 'sample_2015_article': {'_id': '6969d9a5cb04bbc737d88fb7', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}}, 'var_functions.execute_python:28': {'merged_count': 6696, 'columns': ['article_id', 'region', '_id', 'title', 'description'], 'sample_article': {'article_id': '13', 'region': 'Europe', '_id': '6969d9a5cb04bbc737d88fb7', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}}}

exec(code, env_args)
