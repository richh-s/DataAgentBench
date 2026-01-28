code = """import json
from collections import Counter

# Load 2015 metadata
metadata_2015 = locals()['var_functions.query_db:22']
if isinstance(metadata_2015, str) and metadata_2015.endswith('.json'):
    with open(metadata_2015, 'r') as f:
        metadata_2015 = json.load(f)

# Create region lookup
region_lookup = {}
for item in metadata_2015:
    article_id = int(item['article_id'])
    region_lookup[article_id] = item['region']

# World category keywords
world_keywords = [
    'trade', 'deficit', 'international', 'global', 'war', 'peace', 'diplomat',
    'embassy', 'conflict', 'treaty', 'sanction', 'oil', 'energy', 'crisis',
    'refugee', 'aid', 'world', 'abroad', 'overseas', 'foreign', 'nation',
    'europe', 'asia', 'africa', 'america', 'china', 'japan', 'india', 'russia',
    'germany', 'france', 'uk', 'britain', 'afghanistan', 'iraq', 'iran',
    'israel', 'palestine', 'syria', 'climate', 'environment', 'warming',
    'pollution', 'security', 'terror', 'military', 'nuclear', 'korea', 'pakistan',
    'disease', 'epidemic', 'aids', 'refugees', 'diplomacy', 'negotiation'
]

def is_world_article(title, description):
    text = ((title or '') + ' ' + (description or '')).lower()
    return any(keyword in text for keyword in world_keywords)

# Get articles data (this is the full dataset from query_db:42)
articles_data = locals()['var_functions.query_db:42']
if isinstance(articles_data, str) and articles_data.endswith('.json'):
    with open(articles_data, 'r') as f:
        articles_data = json.load(f)

# Process articles
world_articles_by_region = Counter()
global_article_count = 0

for article in articles_data:
    article_id = int(article['article_id'])
    
    # Only process 2015 articles
    if article_id in region_lookup:
        global_article_count += 1
        title = article.get('title', '')
        description = article.get('description', '')
        
        if is_world_article(title, description):
            region = region_lookup[article_id]
            world_articles_by_region[region] += 1

# Find region with most World articles
if world_articles_by_region:
    most_common = world_articles_by_region.most_common(1)[0]
    result = {
        'total_2015_articles_processed': global_article_count,
        'world_articles_found': sum(world_articles_by_region.values()),
        'region_with_most_world': most_common[0],
        'world_articles_count': most_common[1],
        'all_regions': dict(world_articles_by_region)
    }
else:
    result = {'error': 'No World articles found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:8': {'total_articles_2015': 6696, 'unique_article_ids': 6696, 'sample_article_ids': [13, 18, 26]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_articles': 6696, 'min_id': 13, 'max_id': 127570}, 'var_functions.execute_python:14': {'total_articles': 6696, 'number_of_batches': 14, 'batch_size': 500, 'first_batch_sample': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:16': {'total_articles': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_article_id': 127570}, 'var_functions.query_db:18': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:26': {'articles_fetched': 5, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}]}, 'var_functions.execute_python:30': {'world_articles_found': 2, 'total_articles_checked': 5, 'region_counts': {'South America': 2}, 'most_common_region': ['South America', 2]}, 'var_functions.execute_python:32': {'total_article_ids': 6696, 'number_of_batches': 7, 'first_batch_size': 1000, 'last_batch_size': 696, 'sample_batch_ids': [13, 18, 26, 51, 52]}, 'var_functions.execute_python:36': {'total_articles': 6696, 'batches': 7, 'batch_size': 1000}, 'var_functions.query_db:42': [{'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}]}

exec(code, env_args)
