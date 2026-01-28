code = """import json
import pandas as pd

# Get the file path from storage
file_path = locals()['var_functions.query_db:7']

# Load article metadata from file
with open(file_path, 'r') as f:
    europe_metadata = json.load(f)

# Convert to DataFrame
metadata_df = pd.DataFrame(europe_metadata)

# Extract year from publication_date
metadata_df['year'] = pd.to_datetime(metadata_df['publication_date']).dt.year

# Filter for 2010-2020
metadata_df = metadata_df[(metadata_df['year'] >= 2010) & (metadata_df['year'] <= 2020)]

# Count total articles and group by year
total_articles = len(metadata_df)
year_counts = metadata_df.groupby('year').size().reset_index(name='count')
year_counts = year_counts.sort_values('year')

# Prepare result
result = {
    'total_articles': total_articles,
    'year_range': f"{int(metadata_df['year'].min())}-{int(metadata_df['year'].max())}" if total_articles > 0 else "No articles found",
    'articles_by_year': year_counts.to_dict('records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': [{'_id': '6969c99e58b4f1d48f75d9ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c99e58b4f1d48f75d9ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c99e58b4f1d48f75d9af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c99e58b4f1d48f75d9b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c99e58b4f1d48f75d9b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json'}

exec(code, env_args)
