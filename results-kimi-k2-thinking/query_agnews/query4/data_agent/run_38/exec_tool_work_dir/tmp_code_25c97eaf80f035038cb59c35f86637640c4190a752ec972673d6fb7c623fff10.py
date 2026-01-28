code = """import json

# Load all 2015 article metadata from file
with open('file_storage/functions.query_db:14.json', 'r') as f:
    metadata = json.load(f)

# Create lookup for region by article_id
region_lookup = {}
for item in metadata:
    region_lookup[int(item['article_id'])] = item['region']

# Load a subset of articles
with open('file_storage/functions.query_db:34.json', 'r') as f:
    sample_articles = json.load(f)

# Simple World category detection
def detect_world_category(title, description):
    if not title or not description:
        return False
    
    text = (title + ' ' + description).lower()
    
    world_terms = [
        'world', 'global', 'international', 'nation', 'country', 'countries',
        'conflict', 'war', 'peace', 'treaty', 'united nations', 'eu', 'nato',
        'diplomatic', 'diplomacy', 'foreign', 'abroad', 'embassy', 'terrorist',
        'refugee', 'migrant', 'immigration', 'border', 'sanction', 'summit'
    ]
    
    for term in world_terms:
        if term in text:
            return True
    return False

# Process loaded articles
world_articles_by_region = {'Europe': 0, 'South America': 0, 'Africa': 0, 'Asia': 0, 'North America': 0}
total_loaded = 0

for article in sample_articles:
    article_id = int(article['article_id'])
    if article_id in region_lookup:
        total_loaded += 1
        # Check if article belongs to World category based on title/description
        if detect_world_category(article.get('title', ''), article.get('description', '')):
            region = region_lookup[article_id]
            if region in world_articles_by_region:
                world_articles_by_region[region] += 1

# Output results
result = {
    'total_articles': len(metadata),
    'sample_articles_checked': total_loaded,
    'world_articles_by_region': world_articles_by_region
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'type': 'str', 'value': 'file_storage/functions.query_db:2.json'}, 'var_functions.execute_python:8': {'count_2015': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_functions.query_db:12': [{'_id': '6969ee90d879a09892c35643', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969ee90d879a09892c35648', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969ee90d879a09892c35650', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969ee90d879a09892c35669', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969ee90d879a09892c3566a', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_articles': 6696, 'num_batches': 7, 'batch_size': 1000}, 'var_functions.execute_python:22': {'Europe': 1357, 'South America': 1332, 'Africa': 1345, 'Asia': 1333, 'North America': 1329}, 'var_functions.query_db:24': [{'_id': '6969ee90d879a09892c35643', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969ee90d879a09892c35648', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969ee90d879a09892c35650', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969ee90d879a09892c35669', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969ee90d879a09892c3566a', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}, {'_id': '6969ee90d879a09892c35679', 'article_id': '67', 'title': 'IT Myth 5: Most IT projects fail', 'description': 'Do most IT projects fail? Some point to the number of giant consultancies such as IBM Global Services, Capgemini, and Sapient, who feed off bad experiences encountered by enterprises. Sapient is a company founded on the realization that IT projects are not successful, says Sapient CTO Ben Gaucherin.'}, {'_id': '6969ee90d879a09892c3567c', 'article_id': '70', 'title': "U.K.'s NHS taps Gartner to help plan \\$9B IT overhaul", 'description': "LONDON -- The U.K.'s National Health Service (NHS) has tapped IT researcher Gartner Inc. to provide market intelligence services as the health organization forges ahead with a mammoth, 5 billion (\\$9.2 billion) project to upgrade its information technology infrastructure."}, {'_id': '6969ee90d879a09892c35680', 'article_id': '74', 'title': 'HP to Buy Synstar', 'description': 'Hewlett-Packard will pay \\$297 million for the British company. Also: TiVo goes all out to attract customers   hellip;. Sprint offers service guarantees for business wireless subscribers   hellip;. and more.'}], 'var_functions.execute_python:26': {'status': 'ready_to_process', 'total_articles': 6696, 'region_counts_preliminary': {'Europe': 0, 'South America': 0, 'Africa': 0, 'Asia': 0, 'North America': 0}}, 'var_functions.execute_python:28': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97], 'var_functions.query_db:34': [{'_id': '6969ee90d879a09892c35637', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969ee90d879a09892c35638', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969ee90d879a09892c35639', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969ee90d879a09892c3563a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969ee90d879a09892c3563b', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}]}

exec(code, env_args)
