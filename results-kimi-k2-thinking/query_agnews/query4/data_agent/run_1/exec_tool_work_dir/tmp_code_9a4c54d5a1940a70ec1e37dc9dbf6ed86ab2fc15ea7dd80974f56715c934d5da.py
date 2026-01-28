code = """import json
import re

# Load 2015 metadata
metadata_file_path = locals()['var_functions.query_db:6']
with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

# Load all articles
articles_file_path = locals()['var_functions.query_db:30']
with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Create a dictionary for quick lookup of articles by article_id
articles_dict = {str(article['article_id']): article for article in all_articles}

# Merge metadata with articles for 2015 entries
merged_2015 = []
for meta in metadata_2015:
    article_id = meta['article_id']
    if article_id in articles_dict:
        merged_entry = {
            'article_id': article_id,
            'region': meta['region'],
            'title': articles_dict[article_id]['title'],
            'description': articles_dict[article_id]['description']
        }
        merged_2015.append(merged_entry)

# More refined World news classification
world_indicators = [
    # Geographic and political entities
    'iraq', 'iran', 'japan', 'korea', 'china', 'india', 'africa', 'europe', 
    'afghanistan', 'pakistan', 'israel', 'palestine', 'syria', 'lebanon', 
    'saudi arabia', 'mexico', 'canada', 'australia', 'germany', 'france', 
    'britain', 'russia', 'ukraine', 'south africa', 'north korea', 'south korea',
    
    # International relations and events
    'world', 'global', 'international', 'nuclear', 'war', 'peace', 'conflict', 
    'terror', 'embassy', 'refugee', 'united nations', 'security council', 'diplomatic',
    'ambassador', 'consulate', 'treaty', 'sanctions', 'foreign', 'border', 'military',
    
    # International economic/political issues
    'trade deficit', 'oil exports', 'pipeline', 'central bank', 'currency',
    'economic growth', 'imports', 'exports', 'aid', 'imf', 'world bank'
]

# Clear exclusions (these are definitely NOT world news)
exclusions = {
    'sports': ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 
               'hockey', 'olympic', 'world cup', 'fifa', 'nfl', 'nba', 'mlb', 'nhl'],
    
    'technology': ['software', 'computer', 'internet', 'technology', 'tech', 'science',
                   'research', 'microsoft', 'apple', 'intel', 'google', 'genesis spacecraft',
                   'nasa', 'spacecraft', 'IT ', 'IT'],  # Note: IT with space or caps
    
    'business': ['stock', 'shares', 'earnings', 'profit', 'IPO', 'investment', 
                 'merger', 'acquisition', 'corporate', 'quarterly', 'index'],
    
    'entertainment': ['sexier', 'hollywood', 'movie', 'film', 'music', 'celebrity',
                      'entertainment'],
    
    'domestic_us': ['americans aren\'t feeling', 'u.s. economy', 'us economy',
                    'american', 'washington/']  # Domestic US issues
}

world_articles_by_region = {}

for article in merged_2015:
    title = article['title'].lower()
    desc = article['description'].lower()
    text = f"{title} {desc}"
    
    # Skip if matches any exclusion categories
    is_excluded = False
    for category, keywords in exclusions.items():
        if any(keyword.lower() in text for keyword in keywords):
            is_excluded = True
            break
    
    if not is_excluded:
        # Check if it has world indicators
        has_world_indicator = any(indicator in text for indicator in world_indicators)
        
        if has_world_indicator:
            region = article['region']
            world_articles_by_region[region] = world_articles_by_region.get(region, 0) + 1

# Find region with most world articles
if world_articles_by_region:
    max_region = max(world_articles_by_region.items(), key=lambda x: x[1])
else:
    max_region = (None, 0)

print("__RESULT__:")
result = {
    "top_region": max_region[0],
    "article_count": max_region[1],
    "all_regions": world_articles_by_region,
    "total_world_articles": sum(world_articles_by_region.values())
}
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969d08d05c8c827384383ef', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d08d05c8c827384383f0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d08d05c8c827384383f1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d08d05c8c827384383f2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d08d05c8c827384383f3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969d08d05c8c827384383f4', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969d08d05c8c827384383f5', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969d08d05c8c827384383f6', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969d08d05c8c827384383f7', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969d08d05c8c827384383f8', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:2': [{'_id': '6969d08d05c8c827384383ef', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d08d05c8c827384383f0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d08d05c8c827384383f1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d08d05c8c827384383f2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d08d05c8c827384383f3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:5': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}, {'article_id': '67', 'author_id': '344', 'region': 'Asia', 'publication_date': '2015-07-16'}, {'article_id': '70', 'author_id': '914', 'region': 'Asia', 'publication_date': '2015-03-21'}, {'article_id': '74', 'author_id': '251', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '86', 'author_id': '942', 'region': 'Asia', 'publication_date': '2015-05-11'}, {'article_id': '97', 'author_id': '664', 'region': 'North America', 'publication_date': '2015-09-16'}, {'article_id': '116', 'author_id': '950', 'region': 'Asia', 'publication_date': '2015-07-15'}, {'article_id': '117', 'author_id': '734', 'region': 'Africa', 'publication_date': '2015-09-26'}, {'article_id': '141', 'author_id': '760', 'region': 'Asia', 'publication_date': '2015-11-12'}, {'article_id': '165', 'author_id': '95', 'region': 'North America', 'publication_date': '2015-03-05'}, {'article_id': '179', 'author_id': '971', 'region': 'Europe', 'publication_date': '2015-04-27'}, {'article_id': '203', 'author_id': '322', 'region': 'Europe', 'publication_date': '2015-05-13'}, {'article_id': '240', 'author_id': '331', 'region': 'South America', 'publication_date': '2015-07-21'}, {'article_id': '243', 'author_id': '930', 'region': 'Europe', 'publication_date': '2015-04-12'}, {'article_id': '266', 'author_id': '703', 'region': 'South America', 'publication_date': '2015-01-17'}, {'article_id': '271', 'author_id': '494', 'region': 'Europe', 'publication_date': '2015-06-24'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': [{'_id': '6969d08d05c8c827384383ef', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d08d05c8c827384383f0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d08d05c8c827384383f1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969d08d05c8c827384383f2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969d08d05c8c827384383f3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:22': ["var_functions.query_db:0: <class 'list'>", "var_functions.query_db:12: <class 'list'>", "var_functions.query_db:2: <class 'list'>", "var_functions.query_db:5: <class 'list'>", "var_functions.query_db:6: <class 'str'>"], 'var_functions.execute_python:26': {'num_2015_articles': 6696, 'num_total_articles': 5, 'sample_metadata': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}], 'sample_articles': [{'_id': '6969d08d05c8c827384383ef', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969d08d05c8c827384383f0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969d08d05c8c827384383f1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.execute_python:36': {'world_articles_by_region': {'South America': 35, 'Asia': 23, 'North America': 27, 'Africa': 35, 'Europe': 30}, 'max_region': 'South America', 'max_count': 35, 'total_world_articles': 150}, 'var_functions.execute_python:38': {'world_articles_by_region': {'South America': 39, 'Asia': 31, 'North America': 33, 'Europe': 31, 'Africa': 41}, 'sorted_regions': [['Africa', 41], ['South America', 39], ['North America', 33], ['Asia', 31], ['Europe', 31]], 'total_world_articles': 175, 'sample_classifications': [{'article_id': '18', 'region': 'South America', 'title': 'US trade deficit swells in June', 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '67', 'region': 'Asia', 'title': 'IT Myth 5: Most IT projects fail', 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '74', 'region': 'South America', 'title': 'HP to Buy Synstar', 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '97', 'region': 'North America', 'title': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '116', 'region': 'Asia', 'title': "NASA's Genesis Spacecraft Adjusts Course (AP)", 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '165', 'region': 'North America', 'title': "Insecurity: (Or Why Americans Aren't Feeling The Recovery)", 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '240', 'region': 'South America', 'title': "News: Climate Change Could Doom Alaska's Tundra", 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '243', 'region': 'Europe', 'title': 'News: Warmer Weather, Human Disturbances Interact to Change ...', 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '498', 'region': 'North America', 'title': 'Bomb at India Independence Parade Kills 15 (AP)', 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}, {'article_id': '501', 'region': 'Asia', 'title': 'Edwards Calls for Changes to Drug Plans (AP)', 'is_world': True, 'is_business': False, 'is_sports': False, 'is_scitech': False}]}, 'var_functions.execute_python:40': {'top_region': 'South America', 'article_count': 50, 'all_regions': {'South America': 50, 'Asia': 37, 'North America': 43, 'Europe': 41, 'Africa': 46}, 'total_world_articles': 217, 'sample_classified': [{'article_id': '18', 'region': 'South America', 'title': 'US trade deficit swells in June', 'world_matches': 3, 'is_sports': False, 'is_scitech': False}, {'article_id': '67', 'region': 'Asia', 'title': 'IT Myth 5: Most IT projects fail', 'world_matches': 1, 'is_sports': False, 'is_scitech': False}, {'article_id': '74', 'region': 'South America', 'title': 'HP to Buy Synstar', 'world_matches': 1, 'is_sports': False, 'is_scitech': False}, {'article_id': '97', 'region': 'North America', 'title': "What's in a Name? Well, Matt Is Sexier Than Paul (Reuters)", 'world_matches': 1, 'is_sports': False, 'is_scitech': False}, {'article_id': '165', 'region': 'North America', 'title': "Insecurity: (Or Why Americans Aren't Feeling The Recovery)", 'world_matches': 4, 'is_sports': False, 'is_scitech': False}]}}

exec(code, env_args)
