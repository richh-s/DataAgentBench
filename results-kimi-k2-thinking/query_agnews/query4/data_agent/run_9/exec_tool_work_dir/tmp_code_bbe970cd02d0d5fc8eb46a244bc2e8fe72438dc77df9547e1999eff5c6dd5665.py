code = """import json
import pandas as pd

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

# Create enhanced categorization function
def categorize_article(title, description):
    text = (f"{title or ''} {description or ''}").lower()
    
    # Check for Sports first (most distinct)
    sports_indicators = [
        'game', 'match', 'player', 'team', 'season', 'coach',
        'football', 'basketball', 'baseball', 'hockey', 'soccer', 'tennis',
        'olympic', 'nfl', 'nba', 'mlb', 'nhl', 'world cup', 'championship'
    ]
    if any(indicator in text for indicator in sports_indicators):
        # Make sure it's not just a business metaphor
        if 'stock market game' not in text and 'investment strategy' not in text:
            return 'Sports'
    
    # Check for Science/Technology
    tech_indicators = [
        'technology', 'tech', 'software', 'hardware', 'internet', 'digital',
        'computer', 'scientific', 'research', 'discovery', 'innovation',
        'google', 'microsoft', 'apple', 'ibm', 'intel', 'nasa', 'space'
    ]
    if any(indicator in text for indicator in tech_indicators):
        # Exclude business news about tech companies
        if 'stock' not in text and 'profit' not in text and 'ip' not in text:
            return 'Science/Technology'
    
    # Check for Business (strong business context)
    business_indicators = [
        'stock market', 'stocks', 'wall street', 'economy', 'economic',
        'trade deficit', 'interest rates', 'investment', 'profit', 'revenue',
        'earnings', 'financial', 'business', 'corporate', 'dollar falls',
        'dollar tumbles', 'oil prices', 'crude prices'
    ]
    if any(indicator in text for indicator in business_indicators):
        return 'Business'
    
    # Check for World (international affairs, politics, conflicts)
    world_indicators = [
        'war', 'peace', 'conflict', 'diplomatic', 'embassy', 'rebel',
        'militia', 'refugee', 'united nations', 'president', 'government',
        'minister', 'iraq', 'iran', 'afghanistan', 'israel', 'palestin',
        'korea', 'saudi', 'arabia', 'africa', 'europe crisis', 'china',
        'japan', 'south africa', 'india', 'pakistan', 'syria'
    ]
    if any(indicator in text for indicator in world_indicators):
        return 'World'
    
    # Default scoring if no clear match
    categories = {'Sports': 0, 'Business': 0, 'Science/Technology': 0, 'World': 0}
    
    # Score based on term frequency
    for term in sports_indicators:
        if term in text:
            categories['Sports'] += 1
    for term in tech_indicators:
        if term in text:
            categories['Science/Technology'] += 1
    for term in business_indicators:
        if term in text:
            categories['Business'] += 1
    for term in world_indicators:
        if term in text:
            categories['World'] += 1
    
    # Assign to category with highest score, or World as default
    max_cat = max(categories, key=categories.get)
    if categories[max_cat] > 0:
        return max_cat
    
    # Default to World for international news context
    return 'World'

# Apply categorization
merged_2015['category'] = merged_2015.apply(lambda row: categorize_article(row['title'], row['description']), axis=1)

# Filter for World category
world_2015 = merged_2015[merged_2015['category'] == 'World']

# Count by region
region_counts = world_2015['region'].value_counts()

# Verify samples
world_samples = world_2015.sample(min(10, len(world_2015)))[['title', 'description', 'region']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps({
    'total_articles_2015': len(merged_2015),
    'world_articles_2015': len(world_2015),
    'category_breakdown': merged_2015['category'].value_counts().to_dict(),
    'region_counts': region_counts.to_dict(),
    'top_region': region_counts.index[0] if len(region_counts) > 0 else None,
    'top_region_count': int(region_counts.iloc[0]) if len(region_counts) > 0 else 0
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:6': {'articles_shape': [5, 4], 'metadata_shape': [6696, 3], 'articles_columns': ['_id', 'article_id', 'title', 'description'], 'metadata_columns': ['article_id', 'region', 'publication_date'], 'articles_head': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'metadata_head': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'region': 'Africa', 'publication_date': '2015-06-02'}]}, 'var_functions.query_db:8': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d83e5cd4154b38acdae4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d83e5cd4154b38acdae5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:12': {'articles_count': 5, 'sample_articles': [{'_id': '6969d83e5cd4154b38acdae1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d83e5cd4154b38acdae2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d83e5cd4154b38acdae3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_articles_2015': 494, 'world_articles_2015': 258, 'region_counts': {'Africa': 62, 'North America': 50, 'Asia': 50, 'Europe': 49, 'South America': 47}, 'top_region': 'Africa', 'top_region_count': 62}, 'var_functions.execute_python:20': {'total_articles_2015': 494, 'world_articles_2015': 110, 'category_breakdown': {'Sports': 232, 'Business': 110, 'World': 110, 'Science/Technology': 42}, 'region_counts': {'South America': 28, 'Africa': 24, 'Europe': 22, 'Asia': 19, 'North America': 17}, 'top_region': 'South America', 'top_region_count': 28}}

exec(code, env_args)
