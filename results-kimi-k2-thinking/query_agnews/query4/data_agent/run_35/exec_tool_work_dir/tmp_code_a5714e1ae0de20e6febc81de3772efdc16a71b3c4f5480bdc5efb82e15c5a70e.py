code = """import json

metadata_2015 = locals()['var_functions.query_db:22']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

region_lookup = {}
for item in metadata_2015:
    article_id = int(item['article_id'])
    region_lookup[article_id] = item['region']

article_ids = list(region_lookup.keys())
article_ids.sort()

world_keywords = [
    'trade', 'deficit', 'international', 'global', 'war', 'peace', 'diplomat',
    'embassy', 'conflict', 'treaty', 'sanction', 'oil', 'energy', 'crisis',
    'refugee', 'aid', 'world', 'abroad', 'overseas', 'foreign', 'nation',
    'europe', 'asia', 'africa', 'america', 'china', 'japan', 'india', 'russia',
    'germany', 'france', 'uk', 'britain', 'afghanistan', 'iraq', 'iran',
    'israel', 'palestine', 'syria', 'climate', 'environment', 'warming',
    'pollution', 'united nations', 'security', 'terror', 'weapon', 'military',
    'defense', 'nuclear', 'korea', 'pakistan', 'disease', 'epidemic', 'aids'
]

def is_world(title, description):
    text = ((title or '') + ' ' + (description or '')).lower()
    for keyword in world_keywords:
        if keyword in text:
            return True
    return False

batch_size = 1000
batches = []
for i in range(0, len(article_ids), batch_size):
    batches.append(article_ids[i:i+batch_size])

result = {
    'total_articles': len(article_ids),
    'batches': len(batches),
    'batch_size': batch_size
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 6696, 'min_id': 13, 'max_id': 127570}, 'var_functions.execute_python:14': {'total_articles': 6696, 'number_of_batches': 14, 'batch_size': 500, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:16': {'total_articles': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_article_id': 127570}, 'var_functions.query_db:18': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:26': {'articles_fetched': 5, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}]}, 'var_functions.execute_python:30': {'world_articles_found': 2, 'total_articles_checked': 5, 'region_counts': {'South America': 2}, 'most_common_region': ['South America', 2]}, 'var_functions.execute_python:32': {'total_article_ids': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_batch_size': 696, 'sample_batch_ids': [13, 18, 26, 51, 52]}}

exec(code, env_args)
