code = """import json

# Get the file path from storage
file_path = locals()['var_functions.query_db:7']

# Load article metadata from file
with open(file_path, 'r') as f:
    metadata = json.load(f)

# Count total and per year
total_articles = len(metadata)
years = [int(item['publication_date'][:4]) for item in metadata]
years_2010_2020 = [y for y in years if 2010 <= y <= 2020]

print('__RESULT__:')
print(json.dumps({
    'total_articles_in_file': total_articles,
    'articles_2010_2020': len(years_2010_2020),
    'year_range': f"{min(years_2010_2020)}-{max(years_2010_2020)}" if years_2010_2020 else None
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': [{'_id': '6969c99e58b4f1d48f75d9ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c99e58b4f1d48f75d9ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c99e58b4f1d48f75d9af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c99e58b4f1d48f75d9b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c99e58b4f1d48f75d9b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'total_articles': 14860, 'year_range': '2010-2020', 'articles_by_year': [{'year': 2010, 'count': 1306}, {'year': 2011, 'count': 1316}, {'year': 2012, 'count': 1355}, {'year': 2013, 'count': 1354}, {'year': 2014, 'count': 1372}, {'year': 2015, 'count': 1357}, {'year': 2016, 'count': 1364}, {'year': 2017, 'count': 1391}, {'year': 2018, 'count': 1351}, {'year': 2019, 'count': 1328}, {'year': 2020, 'count': 1366}]}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json'}

exec(code, env_args)
