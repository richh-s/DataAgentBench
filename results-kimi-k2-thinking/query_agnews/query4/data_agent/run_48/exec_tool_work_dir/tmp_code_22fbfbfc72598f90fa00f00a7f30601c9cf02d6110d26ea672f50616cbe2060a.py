code = """import json

# Load metadata and create mapping
metadata_file = locals()['var_functions.query_db:0']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

article_id_to_region = {}
for item in metadata_2015:
    article_id_to_region[int(item['article_id'])] = item['region']

# Process articles in batches and categorize
world_articles_by_region = {}
processed_count = 0

# Keywords for categorization
world_keywords = [
    'iraq', 'iran', 'afghanistan', 'syria', 'israel', 'palestine', 'lebanon', 'jordan', 'egypt', 'saudi', 'yemen',
    'china', 'russia', 'ukraine', 'korea', 'japan', 'india', 'pakistan', 'turkey', 'libya', 'mexico', 'canada',
    'united nations', 'un', 'eu', 'european union', 'nato', 'world bank', 'imf', 'wto', 'africa', 'europe', 'asia',
    'climate change', 'global warming', 'international', 'foreign', 'diplomatic', 'treaty', 'summit', 'global',
    'war', 'peace', 'conflict', 'refugee', 'migrant', 'migration', 'ambassador', 'embassy', 'border', 'overseas'
]

business_keywords = [
    'stock', 'wall st', 'wall street', 'economy', 'economic', 'business', 'company', 'corporate', 'earnings',
    'google', 'microsoft', 'apple', 'ipo', 'investment', 'investors', 'trade', 'deficit', 'oil prices', 'crude',
    'dell', 'chrysler', 'carlyle', 'commercial', 'acquisition', 'merger', 'bank', 'finance', 'financial'
]

sports_keywords = [
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympics', 'world cup', 'team',
    'player', 'coach', 'game', 'match', 'score', 'win', 'championship', 'tournament', 'league', 'sport', 'sports',
    'quarterback', 'touchdown', 'goal', 'record', 'playoff', 'series'
]

scitech_keywords = [
    'scientist', 'research', 'study', 'findings', 'discover', 'discovery', 'technology', 'tech', 'apple', 'iphone',
    'ipad', 'computer', 'software', 'hardware', 'internet', 'space', 'nasa', 'rocket', 'satellite', 'gene', 'dna'
]

def categorize_article(title, description):
    text = (title + ' ' + (description or '')).lower()
    
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    
    if any(keyword in text for keyword in scitech_keywords):
        return 'Science/Technology'
    
    return 'Other'

# We'll need to query the articles in batches - for now, let's prepare the structure
print('__RESULT__:')
print(json.dumps({
    'status': 'ready_to_process',
    'total_articles_to_check': len(article_id_to_region),
    'world_articles_by_region': world_articles_by_region
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'record_count': 6696, 'first_five': [{'article_id': '13', 'region': 'Europe'}, {'article_id': '18', 'region': 'South America'}, {'article_id': '26', 'region': 'Africa'}, {'article_id': '51', 'region': 'South America'}, {'article_id': '52', 'region': 'Africa'}], 'data_type': "<class 'list'>"}, 'var_functions.query_db:6': [{'_id': '6969f6f44ea4ebf2429cc3ba', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969f6f44ea4ebf2429cc3bf', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969f6f44ea4ebf2429cc3c7', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969f6f44ea4ebf2429cc3e0', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969f6f44ea4ebf2429cc3e1', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:12': {'type': "<class 'list'>", 'record_count': 5, 'first_article': {'_id': '6969f6f44ea4ebf2429cc3ba', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}}, 'var_functions.execute_python:14': {'metadata_count': 6696, 'article_id_sample': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97'], 'total_unique_articles': 6696}, 'var_functions.query_db:16': [{'_id': '6969f6f44ea4ebf2429cc3ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f6f44ea4ebf2429cc3ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f6f44ea4ebf2429cc3af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f6f44ea4ebf2429cc3b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f6f44ea4ebf2429cc3b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:18': {'total_articles': 6696, 'region_sample': {'13': 'Europe', '18': 'South America', '26': 'Africa', '51': 'South America', '52': 'Africa'}}, 'var_functions.query_db:20': [{'_id': '6969f6f44ea4ebf2429cc3ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f6f44ea4ebf2429cc3ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f6f44ea4ebf2429cc3af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f6f44ea4ebf2429cc3b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f6f44ea4ebf2429cc3b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:22': {'total_articles_2015': 0, 'sample_articles': []}, 'var_functions.execute_python:24': {'metadata_count': 6696, 'metadata_sample': {'article_id': '13', 'region': 'Europe'}, 'articles_type': "<class 'list'>", 'articles_count': 5}, 'var_functions.execute_python:26': [{'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'category': 'Business'}, {'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'category': 'World'}, {'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'category': 'Business'}, {'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'category': 'World'}, {'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'category': 'Business'}, {'title': 'Google IPO Auction Off to Rocky Start', 'category': 'Business'}, {'title': 'US trade deficit swells in June', 'category': 'Business'}, {'title': 'Google auction begins on Friday', 'category': 'Business'}, {'title': 'Delightful Dell', 'category': 'Business'}, {'title': "Chrysler's Bling King", 'category': 'Business'}, {'title': 'Local Football Team Wins Championship', 'category': 'Sports'}, {'title': 'Scientists Discover New Species in Amazon', 'category': 'Science/Technology'}, {'title': 'Apple Announces New iPhone', 'category': 'Science/Technology'}, {'title': 'EU Leaders Meet to Discuss Climate Change', 'category': 'World'}], 'var_functions.execute_python:28': {'total_ids': 6696, 'batches_count': 14, 'first_batch': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.execute_python:30': {'total_mappings': 6696, 'sample': {'13': 'Europe', '18': 'South America', '26': 'Africa', '51': 'South America', '52': 'Africa'}}, 'var_functions.execute_python:34': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'var_functions.execute_python:36': {'message': 'Setup complete', 'total_articles': 6696, 'sample_regions': {'13': 'Europe', '18': 'South America', '26': 'Africa'}}, 'var_functions.execute_python:38': {'total': 6696, 'batch_size': 1000, 'first_ten': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.execute_python:40': {'query_filter': "{'article_id': {'$in': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97', '116', '117', '141', '165', '179', '203', '240', '243', '266', '271', '309', '314', '364', '365', '369', '379', '408', '429', '488', '498', '501', '509', '519', '534', '606', '652', '698', '743', '745', '879', '885', '902', '907', '924', '932', '935', '941', '970', '987', '993']}}", 'batch_size': 50, 'first_five_ids': [13, 18, 26, 51, 52]}}

exec(code, env_args)
