code = """import json

# Get all 2015 article_ids from the metadata file
file_path = locals()['var_functions.query_db:0']
with open(file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Process in batches to avoid query size limits
def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]

# Get article_ids from metadata
article_ids = [int(item['article_id']) for item in metadata_2015]
print('__RESULT__:')
print(json.dumps({
    'total_articles': len(article_ids),
    'first_10': article_ids[:10],
    'last_10': article_ids[-10:]
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'count': 6696, 'article_ids': ['13', '18', '26', '51', '52']}, 'var_functions.query_db:6': [{'_id': '6969f57701dd4ba30fe36693', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969f57701dd4ba30fe36698', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969f57701dd4ba30fe366a0', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969f57701dd4ba30fe366b9', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969f57701dd4ba30fe366ba', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}]}

exec(code, env_args)
