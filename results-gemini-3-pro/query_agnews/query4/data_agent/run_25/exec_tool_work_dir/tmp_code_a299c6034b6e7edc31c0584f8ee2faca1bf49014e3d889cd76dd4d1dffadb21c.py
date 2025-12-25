code = """import json

# Load SQL result
with open(locals()['var_function-call-8192239243877575471'], 'r') as f:
    metadata_list = json.load(f)

# Extract unique IDs
# IDs in metadata are strings (e.g. "13").
# IDs in articles are likely strings too.
ids = list(set(item['article_id'] for item in metadata_list))

# Construct query
query = {
    "collection": "articles",
    "filter": {
        "article_id": {"$in": ids}
    },
    "projection": {
        "article_id": 1,
        "title": 1,
        "description": 1,
        "_id": 0
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-8192239243877575471': 'file_storage/function-call-8192239243877575471.json', 'var_function-call-4285467361081759445': 6696, 'var_function-call-13346176432867388839': [{'_id': '69450821ec4d8e6298d328d7', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69450821ec4d8e6298d328d8', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69450821ec4d8e6298d328d9', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69450821ec4d8e6298d328da', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69450821ec4d8e6298d328db', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-152803809967091269': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13229976580628931333': 'file_storage/function-call-13229976580628931333.json', 'var_function-call-14357045956631284067': {'region': 'Africa', 'count': 27, 'all_counts': {'South America': 23, 'Europe': 21, 'Asia': 22, 'North America': 20, 'Africa': 27}}, 'var_function-call-2003783828452005932': 6696, 'var_function-call-5861112987740130627': {'counts': {'Business': 143, 'Sci_Tech': 57, 'Unknown': 66, 'Sports': 96, 'World': 132}, 'samples': [['Google IPO Auction Off to Rocky Start  WASHINGTON/', 'Business'], ['US trade deficit swells in June The US trade defic', 'Business'], ['Google auction begins on Friday An auction of shar', 'Sci_Tech'], ["Delightful Dell The company's results show that it", 'Business'], ["Chrysler's Bling King After a tough year, Detroit'", 'Unknown'], ['IT Myth 5: Most IT projects fail Do most IT projec', 'Business'], ["U.K.'s NHS taps Gartner to help plan \\$9B IT overh", 'Business'], ['HP to Buy Synstar Hewlett-Packard will pay \\$297 m', 'Business'], ['Oracle Sales Data Seen Being Released (Reuters) Re', 'Business'], ["What's in a Name? Well, Matt Is Sexier Than Paul (", 'Unknown'], ["NASA's Genesis Spacecraft Adjusts Course (AP) AP -", 'Sci_Tech'], ['Earth is Rare, New Study Suggests (SPACE.com) SPAC', 'Sci_Tech'], ['Indictments Using DNA on Rise Nationally (AP) AP -', 'Unknown'], ["Insecurity: (Or Why Americans Aren't Feeling The R", 'Business'], ["Reverse Psychology \\\\I really hope SUN doesn't Ope", 'Business'], ["'Madden,' 'ESPN' Football Score in Different Ways ", 'Sports'], ["News: Climate Change Could Doom Alaska's Tundra In", 'Business'], ['News: Warmer Weather, Human Disturbances Interact ', 'World'], ['Building Dedicated to Space Shuttle Columbia Astro', 'World'], ["Saturn's Moon Titan: Prebiotic Laboratory by Harry", 'Sports']]}}

exec(code, env_args)
