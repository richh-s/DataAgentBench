code = """import json
from collections import Counter

# Load metadata and create region lookup
meta_path = locals()['var_functions.query_db:0']
with open(meta_path, 'r') as f:
    metas = json.load(f)

regions_by_id = {int(m['article_id']): m['region'] for m in metas}

# Process first batch of 100 articles to test
article_ids = [item['article_id'] for item in metas[:100]]

print('__RESULT__:')
print(json.dumps({
    'total_articles_from_2015': len(metas),
    'test_batch_size': len(article_ids),
    'sample_regions': {article_ids[i]: regions_by_id[int(article_ids[i])] for i in range(5)}
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 6696, 'article_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:6': [{'_id': '6969f57701dd4ba30fe36693', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969f57701dd4ba30fe36698', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969f57701dd4ba30fe366a0', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969f57701dd4ba30fe366b9', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969f57701dd4ba30fe366ba', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:8': {'total_articles': 6696, 'first_10': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'last_10': [127433, 127438, 127440, 127445, 127479, 127481, 127486, 127511, 127569, 127570]}, 'var_functions.execute_python:10': {'total_batches': 17, 'total_articles': 6696}, 'var_functions.query_db:12': [{'_id': '6969f57701dd4ba30fe36693', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969f57701dd4ba30fe36698', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969f57701dd4ba30fe366a0', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969f57701dd4ba30fe366b9', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969f57701dd4ba30fe366ba', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:14': {'total_articles': 6696, 'num_batches': 67}}

exec(code, env_args)
