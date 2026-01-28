code = """import json

# Load all articles data (from MongoDB)
all_articles = var_functions.query_db:2
print(f'Loaded {len(all_articles)} articles from MongoDB')

# Load metadata data from file path
metadata_path = var_functions.query_db:3
print(f'Metadata stored at: {metadata_path}')

with open(metadata_path, 'r') as f:
    metadata_list = json.load(f)
    
print(f'Loaded {len(metadata_list)} metadata records')

# Process 2015 articles
from datetime import datetime
metadata_2015 = [m for m in metadata_list if m.get('publication_date', '').startswith('2015-')]
print(f'Found {len(metadata_2015)} articles from 2015')

# Create article_id to metadata mapping for 2015 articles
metadata_2015_map = {int(m['article_id']): m for m in metadata_2015}
print(f'Created mapping for {len(metadata_2015_map)} 2015 articles')

# Check some sample data
sample_metadata = list(metadata_2015_map.items())[:3]
for aid, meta in sample_metadata:
    print(f'Article {aid}: region={meta.get("region")}, date={meta.get("publication_date")}')

sample_articles = all_articles[:3]
for art in sample_articles:
    print(f'Article data keys: {list(art.keys())}')

print('__RESULT__:')
result = {
    'total_articles': len(all_articles),
    'total_metadata': len(metadata_list),
    'articles_2015': len(metadata_2015),
    'metadata_map_size': len(metadata_2015_map)
}
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e431beeeb5230db76b0e', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e431beeeb5230db76b0f', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e431beeeb5230db76b10', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e431beeeb5230db76b11', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e431beeeb5230db76b12', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json'}

exec(code, env_args)
