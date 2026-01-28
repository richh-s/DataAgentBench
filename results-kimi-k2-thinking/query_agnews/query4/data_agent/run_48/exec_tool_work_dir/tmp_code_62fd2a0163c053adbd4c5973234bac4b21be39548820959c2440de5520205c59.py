code = """import json

# Test categorization with sample articles
sample_titles = [
    "Wall St. Bears Claw Back Into the Black (Reuters)",
    "Carlyle Looks Toward Commercial Aerospace (Reuters)",
    "Oil and Economy Cloud Stocks' Outlook (Reuters)",
    "Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)",
    "Oil prices soar to all-time record, posing new menace to US economy (AFP)",
    "Google IPO Auction Off to Rocky Start",
    "US trade deficit swells in June",
    "Google auction begins on Friday",
    "Delightful Dell",
    "Chrysler's Bling King",
    "Local Football Team Wins Championship",
    "Scientists Discover New Species in Amazon",
    "Apple Announces New iPhone",
    "EU Leaders Meet to Discuss Climate Change"
]

# Identify keywords for World category
world_keywords = ['iraq', 'war', 'presidential', 'election', 'united nations', 'eu leaders', 'climate change', 'international', 'global', 'world', 'foreign', 'diplomatic', 'treaty', 'summit']

business_keywords = ['google', 'wall st', 'stock', 'economy', 'trade deficit', 'ipo', 'dell', 'chrysler', 'carlyle', 'commercial', 'oil prices', 'crude prices', 'earnings']

sports_keywords = ['football', 'team', 'wins', 'championship', 'score', 'game', 'player', 'coach', 'tournament', 'world cup']

scitech_keywords = ['scientists', 'discover', 'new species', 'apple', 'iphone', 'technology', 'research', 'study', 'findings', 'scientist']

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    # Check for World category
    if any(keyword in text for keyword in world_keywords):
        return 'World'
    
    # Check for Business category
    if any(keyword in text for keyword in business_keywords):
        return 'Business'
    
    # Check for Sports category
    if any(keyword in text for keyword in sports_keywords):
        return 'Sports'
    
    # Check for Science/Technology category
    if any(keyword in text for keyword in scitech_keywords):
        return 'Science/Technology'
    
    return 'Uncategorized'

# Test the categorization
results = []
for title in sample_titles:
    category = categorize_article(title, "")
    results.append({'title': title, 'category': category})

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:5': {'record_count': 6696, 'first_five': [{'article_id': '13', 'region': 'Europe'}, {'article_id': '18', 'region': 'South America'}, {'article_id': '26', 'region': 'Africa'}, {'article_id': '51', 'region': 'South America'}, {'article_id': '52', 'region': 'Africa'}], 'data_type': "<class 'list'>"}, 'var_functions.query_db:6': [{'_id': '6969f6f44ea4ebf2429cc3ba', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969f6f44ea4ebf2429cc3bf', 'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.'}, {'_id': '6969f6f44ea4ebf2429cc3c7', 'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.'}, {'_id': '6969f6f44ea4ebf2429cc3e0', 'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell."}, {'_id': '6969f6f44ea4ebf2429cc3e1', 'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd"}], 'var_functions.execute_python:12': {'type': "<class 'list'>", 'record_count': 5, 'first_article': {'_id': '6969f6f44ea4ebf2429cc3ba', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}}, 'var_functions.execute_python:14': {'metadata_count': 6696, 'article_id_sample': ['13', '18', '26', '51', '52', '67', '70', '74', '86', '97'], 'total_unique_articles': 6696}, 'var_functions.query_db:16': [{'_id': '6969f6f44ea4ebf2429cc3ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f6f44ea4ebf2429cc3ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f6f44ea4ebf2429cc3af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f6f44ea4ebf2429cc3b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f6f44ea4ebf2429cc3b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:18': {'total_articles': 6696, 'region_sample': {'13': 'Europe', '18': 'South America', '26': 'Africa', '51': 'South America', '52': 'Africa'}}, 'var_functions.query_db:20': [{'_id': '6969f6f44ea4ebf2429cc3ad', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969f6f44ea4ebf2429cc3ae', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969f6f44ea4ebf2429cc3af', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969f6f44ea4ebf2429cc3b0', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969f6f44ea4ebf2429cc3b1', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:22': {'total_articles_2015': 0, 'sample_articles': []}, 'var_functions.execute_python:24': {'metadata_count': 6696, 'metadata_sample': {'article_id': '13', 'region': 'Europe'}, 'articles_type': "<class 'list'>", 'articles_count': 5}}

exec(code, env_args)
