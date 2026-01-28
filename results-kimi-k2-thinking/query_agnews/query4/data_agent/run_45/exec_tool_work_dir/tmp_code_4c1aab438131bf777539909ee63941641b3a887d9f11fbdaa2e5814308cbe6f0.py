code = """import json
import pandas as pd

# The query result for articles is stored as a list
articles_data = var_functions.query_db:4
print(f"Articles data type: {type(articles_data)}")
print(f"Articles count: {len(articles_data)}")

# The query result for metadata is stored as a file path
metadata_file_path = var_functions.query_db:5
print(f"Metadata file path: {metadata_file_path}")

# Open and read the full metadata file
with open(metadata_file_path, 'r') as f:
    metadata_data = json.load(f)

print(f"Metadata data type: {type(metadata_data)}")
print(f"Metadata count: {len(metadata_data)}")

# Convert to DataFrame and filter for 2015
metadata_df = pd.DataFrame(metadata_data)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
metadata_2015 = metadata_df[metadata_df['publication_date'].dt.year == 2015]

print(f"2015 articles count: {len(metadata_2015)}")
print("\n__RESULT__:")
print(json.dumps({
    'total_articles': len(articles_data),
    'total_metadata': len(metadata_data),
    'metadata_2015_count': len(metadata_2015)
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'_id': '6969f2d0c3421cbf4230d3d6', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f2d0c3421cbf4230d3d7', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f2d0c3421cbf4230d3d8', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f2d0c3421cbf4230d3d9', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f2d0c3421cbf4230d3da', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
