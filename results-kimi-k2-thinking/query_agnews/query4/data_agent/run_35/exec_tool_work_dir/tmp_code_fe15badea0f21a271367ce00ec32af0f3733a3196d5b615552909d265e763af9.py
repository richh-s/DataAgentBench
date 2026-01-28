code = """import json

# Load 2015 metadata
metadata_2015 = locals()['var_functions.query_db:22']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Load articles data
articles_data = locals()['var_functions.query_db:24']
if isinstance(articles_data, str) and articles_data.endswith('.json'):
    with open(articles_data, 'r') as f:
        articles_data = json.load(f)

# Create region lookup
region_lookup = {int(item['article_id']): item['region'] for item in metadata_2015}

# Categorize articles based on title and description
world_keywords = [
    'trade', 'deficit', 'international', 'global', 'war', 'peace', 'diplomat', 
    'embassy', 'conflict', 'treaty', 'sanction', 'oil', 'energy', 'crisis',
    'refugee', 'aid', 'world', 'abroad', 'overseas', 'foreign', 'nation',
    'europe', 'asia', 'africa', 'america', 'china', 'japan', 'india',
    'mexico', 'canada', 'russia', 'germany', 'france', 'uk', 'britain',
    'afghanistan', 'iraq', 'iran', 'israel', 'palestine', 'syria',
    'climate', 'environment', 'warming', 'pollution', 'united nations',
    'security', 'terror', 'weapon', 'military', 'defense', 'atomic',
    'nuclear', 'korea', 'pakistan', 'aids', 'disease', 'epidemic'
]

def is_world_article(title, description):
    text = (title or '').lower() + ' ' + (description or '').lower()
    return any(keyword in text for keyword in world_keywords)

world_articles = []
for article in articles_data:
    article_id = int(article['article_id'])
    if is_world_article(article.get('title', ''), article.get('description', '')):
        region = region_lookup.get(article_id, 'Unknown')
        world_articles.append({
            'article_id': article_id,
            'region': region,
            'title': article.get('title', '')
        })

# Count by region
from collections import Counter
region_counts = Counter([item['region'] for item in world_articles])
most_common_region = region_counts.most_common(1)[0] if region_counts else (None, 0)

result = {
    "world_articles_found": len(world_articles),
    "total_articles_checked": len(articles_data),
    "region_counts": dict(region_counts),
    "most_common_region": most_common_region
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 6696, 'min_id': 13, 'max_id': 127570}, 'var_functions.execute_python:14': {'total_articles': 6696, 'number_of_batches': 14, 'batch_size': 500, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:16': {'total_articles': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_article_id': 127570}, 'var_functions.query_db:18': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:26': {'articles_fetched': 5, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}]}}

exec(code, env_args)
