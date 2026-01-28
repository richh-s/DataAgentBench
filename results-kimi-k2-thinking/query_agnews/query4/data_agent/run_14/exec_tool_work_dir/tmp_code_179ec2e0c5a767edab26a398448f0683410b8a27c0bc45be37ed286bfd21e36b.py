code = """import json
import pandas as pd

# Load the small articles list directly
articles_data = locals()['var_functions.query_db:26']

# Load the metadata from the file path
metadata_file = locals()['var_functions.query_db:27']
with open(metadata_file, 'r') as f:
    metadata_2015_data = json.load(f)

# Convert to DataFrames
articles_df = pd.DataFrame(articles_data)
metadata_2015_df = pd.DataFrame(metadata_2015_data)

# Convert article_id to string for consistent merging
articles_df['article_id'] = articles_df['article_id'].astype(str)
metadata_2015_df['article_id'] = metadata_2015_df['article_id'].astype(str)

# Merge - find which of the 5 articles are from 2015
merged_2015 = pd.merge(metadata_2015_df, articles_df, on='article_id', how='inner')

# Categorize articles into World, Sports, Business, Science/Technology
def categorize_article(title, description):
    text = (str(title) + ' ' + str(description)).lower()
    
    # World category - geopolitical, international affairs, countries
    world_keywords = ['iraq', 'iraqi', 'iran', 'iranian', 'war', 'conflict', 'peace', 'united nations', 'un ', 
                     'world', 'global', 'international', 'foreign', 'diplomatic', 'embassy', 'refugee',
                     'africa', 'african', 'asia', 'asian', 'europe', 'european', 'america', 'american',
                     'china', 'chinese', 'japan', 'japanese', 'russia', 'russian', 'ukraine', 'ukrainian',
                     'syria', 'syrian', 'israel', 'israeli', 'palestine', 'palestinian', 'afghanistan', 'afghan']
    
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Business category
    business_keywords = ['stock', 'market', 'economy', 'economic', 'business', 'finance', 'financial',
                        'company', 'investment', 'profit', 'revenue', 'wall street', 'bank', 'dollar']
    
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    
    # Sports category  
    sports_keywords = ['sport', 'game', 'match', 'championship', 'tournament', 'team', 'player',
                      'olympic', 'nba', 'nfl', 'soccer', 'football', 'basketball', 'baseball']
    
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    
    # Science/Technology category
    sci_tech_keywords = ['science', 'technology', 'tech', 'research', 'study', 'computer', 'software',
                        'internet', 'digital', 'mobile', 'artificial intelligence', 'ai', 'robot',
                        'space', 'nasa', 'medical', 'medicine', 'health']
    
    if any(keyword in text for keyword in sci_tech_keywords):
        return 'Science/Technology'
    
    # Default to World for news agency articles (Reuters, AFP, AP)
    if any(agency in text for agency in ['reuters', 'afp', 'ap ', 'associated press']):
        return 'World'
    
    return 'World'  # Default fallback

# Categorize the merged articles
if len(merged_2015) > 0:
    merged_2015['category'] = merged_2015.apply(
        lambda row: categorize_article(row['title'], row['description']), 
        axis=1
    )
    
    # Filter for World category
    world_articles = merged_2015[merged_2015['category'] == 'World']
    
    # Group by region and count
    region_counts = world_articles['region'].value_counts()
    
    if not region_counts.empty:
        top_region = region_counts.idxmax()
        top_count = region_counts.max()
        result = top_region + ' (' + str(top_count) + ' articles)'
    else:
        result = 'No World category articles found'
else:
    result = 'No 2015 articles found in the dataset'

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:10': 'No World category articles found in 2015', 'var_functions.execute_python:12': {'total_2015_articles': 0, 'sample_articles': []}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_articles': 5, 'total_metadata': 127600, 'total_2015_metadata': 6696}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_2015_articles': 6696, 'sample_ids': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97']}, 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:26': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.execute_python:34': {'articles_type': "<class 'list'>", 'metadata_type': "<class 'str'>", 'articles_is_list': True, 'metadata_is_list': False, 'articles_preview': 'Already a list', 'metadata_preview': 'file_storage/functions.query_db:27.json'}}

exec(code, env_args)
