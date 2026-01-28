code = """import json

# Load all article IDs from the metadata
var_name = 'var_functions.query_db:2'
metadata_path = locals()[var_name]

with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Group articles by year
articles_by_year = {}
for rec in metadata_records:
    year = int(rec['publication_date'][:4])
    if year not in articles_by_year:
        articles_by_year[year] = []
    articles_by_year[year].append(int(rec['article_id']))

print('Articles by year:')
for year in sorted(articles_by_year.keys()):
    print(f"{year}: {len(articles_by_year[year])} articles")

# Save the grouped data
grouped_data = {
    'by_year': articles_by_year,
    'all_ids': [int(rec['article_id']) for rec in metadata_records]
}

print('__RESULT__:')
print(json.dumps(grouped_data, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': '14860', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:18': {'collection': 'articles', 'filter': {'article_id': {'$in': [3, 9, 13, 14, 21, 27, 43, 60, 62, 63]}}, 'projection': {'article_id': 1, 'title': 1, 'description': 1}}, 'var_functions.query_db:20': [{'_id': '6969cf6befa86fa502823d70', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cf6befa86fa502823d76', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969cf6befa86fa502823d7a', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969cf6befa86fa502823d7b', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969cf6befa86fa502823d82', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}]}

exec(code, env_args)
