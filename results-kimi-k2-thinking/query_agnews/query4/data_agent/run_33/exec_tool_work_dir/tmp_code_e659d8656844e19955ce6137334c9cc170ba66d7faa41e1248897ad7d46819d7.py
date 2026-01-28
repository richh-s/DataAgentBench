code = """import json
import re

# Get file paths
metadata_2015_file = locals()['var_functions.query_db:8']
articles_all_file = locals()['var_functions.query_db:34']

# Load full data
with open(metadata_2015_file, 'r') as f:
    metadata_2015_full = json.load(f)

with open(articles_all_file, 'r') as f:
    articles_all_full = json.load(f)

# Create article dictionary for fast lookup
articles_dict = {art['article_id']: art for art in articles_all_full}

# Combine articles with their 2015 metadata
articles_2015_full = []
for meta in metadata_2015_full:
    article_id = meta['article_id']
    if article_id in articles_dict:
        article = articles_dict[article_id]
        articles_2015_full.append({
            'article_id': article_id,
            'title': article.get('title', '').lower(),
            'description': article.get('description', '').lower(),
            'region': meta['region'],
            'publication_date': meta['publication_date']
        })

# Classify articles into categories
world_keywords = [
    'iraq', 'iraqi', 'iran', 'iranian', 'afghanistan', 'afghan',
    'war', 'conflict', 'military', 'peace', 'diplomatic', 
    'united nations', 'un', 'israel', 'palestin', 'global',
    'world', 'international', 'foreign', 'abroad', 'embassy',
    'consulate', 'diplomat', 'treaty', 'sanctions', 'border'
]

sports_keywords = [
    'olympic', 'olympics', 'football', 'soccer', 'basketball', 'baseball',
    'tennis', 'golf', 'hockey', 'nfl', 'nba', 'mlb', 'nhl', 'fifa',
    'world cup', 'championship', 'tournament', 'coach', 'player',
    'team', 'game', 'match', 'score', 'victory', 'defeat', 'athlete'
]

business_keywords = [
    'stock', 'stocks', 'market', 'economy', 'economic', 'business',
    'company', 'companies', 'corporate', 'profit', 'loss', 'earnings',
    'revenue', 'sales', 'wall st', 'wall street', 'nasdaq', 'dow',
    'investment', 'investing', 'investor', 'bank', 'banking',
    'fed', 'federal reserve', 'interest rate', 'ipo', 'shares',
    'trading', 'trade', 'dollar', 'oil', 'crude', 'price', 'prices'
]

science_tech_keywords = [
    'technology', 'tech', 'internet', 'google', 'microsoft', 'apple',
    'software', 'hardware', 'computer', 'computing', 'digital',
    'science', 'scientific', 'research', 'study', 'researchers',
    'scientists', 'discovery', 'breakthrough', 'innovation',
    'mobile', 'phone', 'smartphone', 'chip', 'semiconductor',
    'ai', 'artificial intelligence', 'robot', 'robotics'
]

def classify_article(title, description):
    # Combine title and description for classification
    text = title + ' ' + description
    
    # Count matches for each category
    world_count = sum(1 for kw in world_keywords if kw in text)
    sports_count = sum(1 for kw in sports_keywords if kw in text)
    business_count = sum(1 for kw in business_keywords if kw in text)
    science_tech_count = sum(1 for kw in science_tech_keywords if kw in text)
    
    # Find the category with the most matches
    counts = {
        'World': world_count,
        'Sports': sports_count,
        'Business': business_count,
        'Science/Technology': science_tech_count
    }
    
    # Return the category with highest count, or 'Other' if all zero
    max_category = max(counts, key=counts.get)
    return max_category if counts[max_category] > 0 else 'Other'

# Classify all 2015 articles and count by region for World category
world_articles_by_region = {}

for article in articles_2015_full:
    category = classify_article(article['title'], article['description'])
    if category == 'World':
        region = article['region']
        world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

# Prepare results
result = {
    'total_2015_articles_analyzed': len(articles_2015_full),
    'world_articles_by_region': world_articles_by_region,
    'number_of_world_articles': sum(world_articles_by_region.values())
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969eac1caf2607f9f0fc78c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969eac1caf2607f9f0fc78d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969eac1caf2607f9f0fc78e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969eac1caf2607f9f0fc78f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969eac1caf2607f9f0fc790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:7': [{'_id': '6969eac1caf2607f9f0fc78c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969eac1caf2607f9f0fc78d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969eac1caf2607f9f0fc78e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969eac1caf2607f9f0fc78f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969eac1caf2607f9f0fc790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': [{'_id': '6969eac1caf2607f9f0fc78c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969eac1caf2607f9f0fc78d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969eac1caf2607f9f0fc78e', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969eac1caf2607f9f0fc78f', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969eac1caf2607f9f0fc790', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:24': {'available_vars': ['var_functions.list_db:0', 'var_functions.query_db:2', 'var_functions.query_db:3', 'var_functions.query_db:7', 'var_functions.query_db:8', 'var_functions.query_db:14'], 'sample_data': {'articles': [{'_id': '6969eac1caf2607f9f0fc78c', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969eac1caf2607f9f0fc78d', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}]}}, 'var_functions.execute_python:32': {'total_2015_metadata': 6696, 'total_articles_all': 5, 'articles_2015_count': 0, 'sample_article': None}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:36': {'total_2015_articles': 6696, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.', 'region': 'Africa', 'publication_date': '2015-08-03'}]}}

exec(code, env_args)
