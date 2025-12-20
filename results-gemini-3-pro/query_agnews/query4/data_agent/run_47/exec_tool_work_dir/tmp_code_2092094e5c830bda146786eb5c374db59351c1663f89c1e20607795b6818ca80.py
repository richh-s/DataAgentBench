code = """import json
import re

# Load metadata (2015)
path_meta = locals()['var_function-call-1094897247215011109']
with open(path_meta, 'r') as f:
    metadata_list = json.load(f)

# Create a map of article_id -> region for 2015 articles
# Ensure article_id is string for matching
meta_map = {str(x['article_id']): x['region'] for x in metadata_list}

# Load fetched articles (potential World candidates)
path_articles = locals()['var_function-call-10903002743850873654']
with open(path_articles, 'r') as f:
    article_list = json.load(f)

# Filter articles that are in 2015 metadata
# article_id in Mongo result might be int or string. Let's normalize to string.
valid_articles = []
for a in article_list:
    aid = str(a.get('article_id', ''))
    if aid in meta_map:
        # Attach region
        a['region'] = meta_map[aid]
        valid_articles.append(a)

# Define exclusion keywords (lowercase)
business_kw = ["stock", "market", "economy", "profit", "earnings", "share", "trade", "rate", "bank", "company", "corp", "inc", "ceo", "sale", "price", "dollar", "euro", "yen", "wall st", "nasdaq", "dow", "invest", "revenue", "fiscal", "deficit", "inflation"]
sports_kw = ["cup", "game", "match", "score", "win", "loss", "team", "player", "coach", "season", "league", "olympic", "champion", "race", "medal", "club", "football", "soccer", "basketball", "tennis", "golf", "baseball", "hockey", "cricket", "rugby", "sport", "athlete"]
tech_kw = ["google", "apple", "microsoft", "intel", "ibm", "software", "computer", "internet", "web", "system", "device", "phone", "mobile", "nasa", "space", "galaxy", "star", "planet", "study", "research", "science", "tech", "biology", "physics", "chemistry", "linux", "windows", "server", "chip"]

# Helper to check keywords
def has_kw(text, keywords):
    text = text.lower()
    for k in keywords:
        if k in text: # simple substring match
            return True
    return False

# Categorize
world_articles = []
for a in valid_articles:
    title = a.get('title', '')
    # We already filtered by "World" regex in query, but that was broad.
    # Now exclude other categories.
    if has_kw(title, business_kw):
        continue
    if has_kw(title, sports_kw):
        continue
    if has_kw(title, tech_kw):
        continue
    
    # If passed exclusions, consider it World
    world_articles.append(a)

# Count by region
region_counts = {}
for a in world_articles:
    r = a['region']
    region_counts[r] = region_counts.get(r, 0) + 1

# Find max
max_region = None
max_count = -1
for r, c in region_counts.items():
    if c > max_count:
        max_count = c
        max_region = r

result = {
    "region_counts": region_counts,
    "max_region": max_region
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6982124256931612734': ['authors', 'article_metadata'], 'var_function-call-6982124256931612959': ['articles'], 'var_function-call-1094897247215011109': 'file_storage/function-call-1094897247215011109.json', 'var_function-call-1808453290574413428': 6696, 'var_function-call-9634656923083955930': [{'_id': '694525f5404bb9b431eed7be', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '694525f5404bb9b431eed7bf', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '694525f5404bb9b431eed7c0', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '694525f5404bb9b431eed7c1', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '694525f5404bb9b431eed7c2', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-16498854364098799837': {'collection': 'articles', 'filter': {'article_id': {'$in': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97, 116, 117, 141, 165, 179, 203, 240, 243, 266, 271, 309, 314, 364, 365, 369, 379, 408, 429, 488, 498, 501, 509, 519, 534, 606, 652, 698, 743, 745, 879, 885, 902, 907, 924, 932, 935, 941, 970, 987, 993]}}}, 'var_function-call-18334592742465536293': [{'_id': '694525f5404bb9b431eed7cb', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '694525f5404bb9b431eed7d0', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '694525f5404bb9b431eed7d8', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '694525f5404bb9b431eed7f1', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '694525f5404bb9b431eed7f2', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_function-call-6831987041074012427': ['Google IPO Auction Off to Rocky Start', 'US trade deficit swells in June', 'Google auction begins on Friday', 'Delightful Dell', "Chrysler's Bling King"], 'var_function-call-14075185667020531607': {'collection': 'articles', 'filter': {'article_id': {'$in': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97', '116', '117', '141', '165', '179', '203', '240', '243', '266', '271', '309', '314', '364', '365', '369', '379', '408', '429', '488', '498', '501', '509', '519', '534', '606', '652', '698', '743', '745', '879', '885', '902', '907', '924', '932', '935', '941', '970', '987', '993']}}}, 'var_function-call-8107396132798164973': [], 'var_function-call-3307744655709430956': [], 'var_function-call-3307744655709432253': [{'_id': '694525f5404bb9b431eed801', 'article_id': '67', 'title': 'IT Myth 5: Most IT projects fail', 'description': 'Do most IT projects fail? Some point to the number of giant consultancies such as IBM Global Services, Capgemini, and Sapient, who feed off bad experiences encountered by enterprises. Sapient is a company founded on the realization that IT projects are not successful, says Sapient CTO Ben Gaucherin.'}], 'var_function-call-4638770951100367012': [{'_id': '694525f5404bb9b431eed801', 'article_id': '67', 'title': 'IT Myth 5: Most IT projects fail', 'description': 'Do most IT projects fail? Some point to the number of giant consultancies such as IBM Global Services, Capgemini, and Sapient, who feed off bad experiences encountered by enterprises. Sapient is a company founded on the realization that IT projects are not successful, says Sapient CTO Ben Gaucherin.'}, {'_id': '694525f5404bb9b431eed804', 'article_id': '70', 'title': "U.K.'s NHS taps Gartner to help plan \\$9B IT overhaul", 'description': "LONDON -- The U.K.'s National Health Service (NHS) has tapped IT researcher Gartner Inc. to provide market intelligence services as the health organization forges ahead with a mammoth, 5 billion (\\$9.2 billion) project to upgrade its information technology infrastructure."}], 'var_function-call-193538430455494723': 'file_storage/function-call-193538430455494723.json', 'var_function-call-12980097274707660876': 'file_storage/function-call-12980097274707660876.json', 'var_function-call-10903002743850873654': 'file_storage/function-call-10903002743850873654.json'}

exec(code, env_args)
