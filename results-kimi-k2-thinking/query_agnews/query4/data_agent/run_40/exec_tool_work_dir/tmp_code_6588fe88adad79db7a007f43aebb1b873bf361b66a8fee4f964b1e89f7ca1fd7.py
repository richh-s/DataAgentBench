code = """import json
from collections import Counter

# Load all 2015 article IDs from metadata
metadata_file = locals()['var_functions.query_db:2']
with open(metadata_file, 'r') as f:
    metadata_records = json.load(f)

# Create article_id to region mapping
article_regions = {int(rec['article_id']): rec['region'] for rec in metadata_records}
all_article_ids = list(article_regions.keys())

# Load all articles from the database query result
articles_file = locals()['var_functions.query_db:22']
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

print('__RESULT__:')
print(json.dumps({
    'total_2015_articles': len(all_article_ids),
    'total_database_articles': len(all_articles),
    'sample_2015': all_article_ids[:5],
    'sample_db_articles': all_articles[:2]
}))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'count': 6696, 'sample': [{'article_id': '13', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'region': 'Africa', 'publication_date': '2015-08-03'}]}, 'var_functions.execute_python:8': {'total_article_ids': 6696, 'sample_article_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.query_db:10': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:12': {'total_article_ids': 6696, 'min_article_id': 13, 'max_article_id': 127570, 'sample_article_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271]}, 'var_functions.execute_python:14': {'total_articles_2015': 6696, 'regions': ['South America', 'Africa', 'Europe', 'Asia', 'North America']}, 'var_functions.execute_python:16': {'total_batches': 7, 'first_batch_size': 1000, 'last_batch_size': 696}, 'var_functions.execute_python:18': {'total_articles': 6696, 'regions': ['South America', 'Europe', 'Africa', 'Asia', 'North America']}, 'var_functions.execute_python:29': {'total_article_ids': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271]}, 'var_functions.query_db:22': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}]}

exec(code, env_args)
