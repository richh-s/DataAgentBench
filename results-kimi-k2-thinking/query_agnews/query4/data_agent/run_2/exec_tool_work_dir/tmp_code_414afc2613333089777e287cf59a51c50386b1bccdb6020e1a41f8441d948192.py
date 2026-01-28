code = """import json
import pandas as pd
import re

# Load the data from file paths
metadata_file = locals()['var_functions.query_db:5']
articles_file = locals()['var_functions.query_db:40']

with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Convert to DataFrames
metadata_df = pd.DataFrame(metadata_2015)
articles_df = pd.DataFrame(all_articles)

# Merge on article_id
merged_df = pd.merge(metadata_df, articles_df, on='article_id', how='inner')

# World category keywords
world_keywords = [
    'world', 'global', 'international', 'united nations', 'un', 'eu', 'european union',
    'foreign', 'overseas', 'diplomatic', 'diplomacy', 'war', 'peace', 'conflict',
    'iraq', 'afghanistan', 'iran', 'israel', 'palestine', 'china', 'india', 'russia',
    'europe', 'asia', 'africa', 'america', 'mideast', 'middle east',
    'embassy', 'ambassador', 'treaty', 'sanctions', 'human rights',
    'climate', 'environment', 'pollution', 'carbon', 'emissions'
]

# Check if article is World category
def is_world_category(title, description):
    text = f"{title} {description}".lower()
    
    for keyword in world_keywords:
        if keyword in text:
            return True
    
    world_patterns = [
        r'\b(minister|president|prime minister|government|parliament|senate)\b.*\b(foreign|international|overseas)\b',
        r'\b(eu|un|nato|wto|who|world bank|imf|g8|g20)\b',
        r'\b(global\s+warming|climate\s+change|greenhouse\s+gas)\b',
        r'\b(peace\s+talks|ceasefire|war|conflict|crisis)\b'
    ]
    
    for pattern in world_patterns:
        if re.search(pattern, text):
            return True
    
    return False

# Identify World articles
world_articles = []
for _, row in merged_df.iterrows():
    if is_world_category(row['title'], row['description']):
        world_articles.append({
            'article_id': row['article_id'],
            'region': row['region']
        })

world_df = pd.DataFrame(world_articles)

# Find top region
if not world_df.empty:
    region_counts = world_df['region'].value_counts()
    top_region = region_counts.idxmax()
    top_count = int(region_counts.max())
    
    result = f"{top_region} published the largest number of World category articles in 2015 with {top_count} articles."
else:
    result = "No World category articles found in 2015."

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'_id': '6969d14bc6b861d1fff2ee10', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d14bc6b861d1fff2ee11', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d14bc6b861d1fff2ee12', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d14bc6b861d1fff2ee13', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d14bc6b861d1fff2ee14', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': [{'_id': '6969d14bc6b861d1fff2ee10', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d14bc6b861d1fff2ee11', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d14bc6b861d1fff2ee12', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d14bc6b861d1fff2ee13', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d14bc6b861d1fff2ee14', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:18': 'None', 'var_functions.execute_python:20': ['var_functions.list_db:0', 'var_functions.list_db:2', 'var_functions.query_db:5', 'var_functions.query_db:8', 'var_functions.query_db:10', 'var_functions.query_db:12', 'var_functions.execute_python:18', '__builtins__', 'json'], 'var_functions.execute_python:30': {'metadata_type': "<class 'str'>", 'metadata_length': 38, 'metadata_sample': 'f', 'articles_type': "<class 'list'>", 'articles_length': 5, 'articles_sample': {'_id': '6969d14bc6b861d1fff2ee10', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}}, 'var_functions.execute_python:36': {'metadata_shape': [6696, 2], 'articles_shape': [5, 4], 'metadata_columns': ['article_id', 'region'], 'articles_columns': ['_id', 'article_id', 'title', 'description']}, 'var_functions.query_db:38': [{'_id': '6969d14bc6b861d1fff2ee10', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d14bc6b861d1fff2ee11', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d14bc6b861d1fff2ee12', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d14bc6b861d1fff2ee13', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d14bc6b861d1fff2ee14', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
