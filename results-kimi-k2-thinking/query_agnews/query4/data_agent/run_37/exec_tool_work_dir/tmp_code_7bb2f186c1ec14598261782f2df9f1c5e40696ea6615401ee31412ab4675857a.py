code = """import json

# Access variables from storage
metadata_2015 = locals()['var_functions.query_db:10']
articles = locals()['var_functions.query_db:11']

# Rest of the code
article_ids_2015 = set([str(m['article_id']) for m in metadata_2015])
articles_2015 = [a for a in articles if a['article_id'] in article_ids_2015]

world_keywords = ['world', 'global', 'international', 'united nations', 'un', 'war', 'peace', 'diplomatic', 'diplomacy', 'treaty', 'africa', 'europe', 'asia', 'america', 'country', 'countries', 'foreign', 'abroad', 'overseas', 'embassy', 'ambassador', 'border', 'migration', 'refugee', 'crisis']

sports_keywords = ['sports', 'game', 'games', 'olympic', 'olympics', 'tournament', 'championship', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'race', 'racing', 'team', 'player', 'athlete', 'medal', 'score', 'victory', 'win', 'lose', 'match']

business_keywords = ['business', 'economy', 'economic', 'market', 'markets', 'stock', 'stocks', 'wall st', 'wall street', 'investment', 'investing', 'company', 'companies', 'corporate', 'trade', 'trading', 'finance', 'financial', 'bank', 'banks', 'banking', 'profit', 'loss', 'revenue', 'earnings', 'federal reserve', 'fed']

science_tech_keywords = ['science', 'technology', 'tech', 'scientific', 'research', 'study', 'studies', 'researchers', 'scientists', 'discovery', 'breakthrough', 'digital', 'internet', 'computer', 'computers', 'software', 'hardware', 'algorithm', 'data', 'ai', 'artificial intelligence', 'robot', 'robots', 'space', 'nasa', 'astronomy', 'physics', 'chemistry', 'biology', 'medical', 'medicine', 'health', 'disease', 'vaccine', 'treatment']

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    world_score = sum(1 for keyword in world_keywords if keyword in text)
    sports_score = sum(1 for keyword in sports_keywords if keyword in text)
    business_score = sum(1 for keyword in business_keywords if keyword in text)
    science_tech_score = sum(1 for keyword in science_tech_keywords if keyword in text)
    scores = {'World': world_score, 'Sports': sports_score, 'Business': business_score, 'Science/Technology': science_tech_score}
    max_score = max(scores.values())
    if max_score == 0:
        return 'Unknown'
    max_categories = [cat for cat, score in scores.items() if score == max_score]
    return max_categories[0]

categorized_articles = []
for article in articles_2015:
    category = categorize_article(article['title'], article['description'])
    categorized_articles.append({'article_id': article['article_id'], 'category': category})

world_article_ids = set([a['article_id'] for a in categorized_articles if a['category'] == 'World'])

region_counts = {}
for meta in metadata_2015:
    if str(meta['article_id']) in world_article_ids:
        region = meta['region']
        region_counts[region] = region_counts.get(region, 0) + 1

max_region = None
max_count = 0
if region_counts:
    max_region = max(region_counts, key=region_counts.get)
    max_count = region_counts[max_region]

result = {'top_region': max_region, 'top_region_count': max_count, 'all_region_counts': region_counts}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:1': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}, {'article_id': '67', 'author_id': '344', 'region': 'Asia', 'publication_date': '2015-07-16'}, {'article_id': '70', 'author_id': '914', 'region': 'Asia', 'publication_date': '2015-03-21'}, {'article_id': '74', 'author_id': '251', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '86', 'author_id': '942', 'region': 'Asia', 'publication_date': '2015-05-11'}, {'article_id': '97', 'author_id': '664', 'region': 'North America', 'publication_date': '2015-09-16'}], 'var_functions.query_db:5': [{'_id': '6969edc28522fa4b10aeeb75', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969edc28522fa4b10aeeb76', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969edc28522fa4b10aeeb77', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969edc28522fa4b10aeeb78', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969edc28522fa4b10aeeb79', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969edc28522fa4b10aeeb7a', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969edc28522fa4b10aeeb7b', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969edc28522fa4b10aeeb7c', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969edc28522fa4b10aeeb7d', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969edc28522fa4b10aeeb7e', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': [{'_id': '6969edc28522fa4b10aeeb75', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969edc28522fa4b10aeeb76', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969edc28522fa4b10aeeb77', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969edc28522fa4b10aeeb78', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969edc28522fa4b10aeeb79', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
