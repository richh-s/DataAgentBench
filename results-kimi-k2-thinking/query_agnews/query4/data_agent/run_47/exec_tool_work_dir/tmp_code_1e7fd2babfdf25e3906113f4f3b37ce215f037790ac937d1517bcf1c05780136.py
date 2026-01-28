code = """import json
from collections import Counter

# Load existing results
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

article_ids = [int(item['article_id']) for item in metadata_2015]
region_map = {int(item['article_id']): item['region'] for item in metadata_2015}

# Batch processing in batches of 400 to avoid query size limits
batches = [article_ids[i:i+400] for i in range(0, len(article_ids), 400)]
remaining = len(batches)

print('__RESULT__:')
print(json.dumps({'total_batches': len(batches), 'total_articles': len(article_ids)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 6696, 'article_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:6': [{'_id': '6969f57701dd4ba30fe36693', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969f57701dd4ba30fe36698', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969f57701dd4ba30fe366a0', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969f57701dd4ba30fe366b9', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969f57701dd4ba30fe366ba', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:8': {'total_articles': 6696, 'first_10': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'last_10': [127433, 127438, 127440, 127445, 127479, 127481, 127486, 127511, 127569, 127570]}}

exec(code, env_args)
