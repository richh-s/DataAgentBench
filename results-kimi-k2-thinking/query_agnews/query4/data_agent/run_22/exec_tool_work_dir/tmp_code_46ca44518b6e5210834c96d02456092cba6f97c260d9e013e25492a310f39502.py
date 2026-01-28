code = """import json

# Load metadata for 2015
metadata_file = locals()['var_functions.query_db:20']
with open(metadata_file, 'r') as f:
    metadata_2015 = json.load(f)

# Load all articles
articles_file = locals()['var_functions.query_db:16']
with open(articles_file, 'r') as f:
    articles = json.load(f)

# Create article_id to article mapping
articles_dict = {article['article_id']: article for article in articles}

# Categorization rules based on keywords
world_keywords = ['war', 'conflict', 'peace', 'diplomat', 'embassy', 'united nations', 'un', 'treaty', 'terror', 'military', 'iraq', 'iran', 'afghanistan', 'israel', 'palestin', 'korea', 'china', 'united states', 'russia', 'ukraine', 'syria', 'refugee', 'border', 'immigration', 'diplomatic']

sports_keywords = ['football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'olympic', 'world cup', 'championship', 'tournament', 'match', 'game', 'score', 'team', 'player', 'coach', 'league', 'sport', 'sporting', 'athlete']

business_keywords = ['stock', 'market', 'economy', 'company', 'business', 'finance', 'bank', 'investment', 'trade', 'profit', 'revenue', 'sales', 'corporation', 'ipo', 'share', 'dollar', 'euro', 'oil', 'price', 'growth', 'job', 'employment', 'unemployment', 'retail', 'housing']

science_tech_keywords = ['technology', 'scientific', 'research', 'internet', 'computer', 'software', 'hardware', 'digital', 'tech', 'innovation', 'discovery', 'space', 'nasa', 'rocket', 'satellite', 'genetic', 'medical', 'disease', 'cure', 'vaccine', 'climate', 'environment', 'google', 'microsoft', 'apple', 'ibm']

def categorize_article(title, description):
    text = (title + ' ' + description).lower()
    
    cat_scores = {
        'World': 0,
        'Sports': 0,
        'Business': 0,
        'Science/Technology': 0
    }
    
    # Count keyword matches for each category
    for word in world_keywords:
        if word in text:
            cat_scores['World'] += 1
    
    for word in sports_keywords:
        if word in text:
            cat_scores['Sports'] += 1
    
    for word in business_keywords:
        if word in text:
            cat_scores['Business'] += 1
    
    for word in science_tech_keywords:
        if word in text:
            cat_scores['Science/Technology'] += 1
    
    # Return category with highest score, default to 'World' if tie or no matches
    max_score = max(cat_scores.values())
    if max_score == 0:
        return 'World'  # Default category
    
    max_categories = [cat for cat, score in cat_scores.items() if score == max_score]
    return max_categories[0]  # Return first category if tie

# Process 2015 articles
world_articles_by_region = {}

for meta in metadata_2015:
    article_id = meta['article_id']
    if article_id in articles_dict:
        article = articles_dict[article_id]
        title = article['title']
        description = article['description']
        
        # Categorize article
        category = categorize_article(title, description)
        
        if category == 'World':
            region = meta['region']
            if region not in world_articles_by_region:
                world_articles_by_region[region] = 0
            world_articles_by_region[region] += 1

# Find region with most World articles
if world_articles_by_region:
    top_region = max(world_articles_by_region, key=world_articles_by_region.get)
    top_count = world_articles_by_region[top_region]
else:
    top_region = None
    top_count = 0

print('__RESULT__:')
print(json.dumps({
    "top_region": top_region,
    "world_articles_count": top_count,
    "world_articles_by_region": world_articles_by_region,
    "total_world_articles": sum(world_articles_by_region.values())
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969e166554525264c42cef5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e166554525264c42cef6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e166554525264c42cef7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e166554525264c42cef8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e166554525264c42cef9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969e166554525264c42cefa', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969e166554525264c42cefb', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969e166554525264c42cefc', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969e166554525264c42cefd', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969e166554525264c42cefe', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.list_db:5': ['authors', 'article_metadata'], 'var_functions.query_db:6': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': [{'_id': '6969e166554525264c42cef5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e166554525264c42cef6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e166554525264c42cef7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e166554525264c42cef8', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e166554525264c42cef9', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:14': {'metadata_count': 127600, 'articles_count': 5, 'sample_metadata': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}], 'sample_articles': [{'_id': '6969e166554525264c42cef5', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969e166554525264c42cef6', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e166554525264c42cef7', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'metadata_loaded': 127600, 'articles_loaded': 127600}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'total_2015_articles': 6696, 'sample_articles': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'title': 'US trade deficit swells in June', 'description': 'The US trade deficit has exploded 19 to a record \\$55.8bn as oil costs drove imports higher, according to a latest figures.', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'title': 'Google auction begins on Friday', 'description': 'An auction of shares in Google, the web search engine which could be floated for as much as \\$36bn, takes place on Friday.', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'title': 'Delightful Dell', 'description': "The company's results show that it's not grim all over tech world. Just all of it that isn't Dell.", 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'title': "Chrysler's Bling King", 'description': "After a tough year, Detroit's troubled carmaker is back -- thanks to a maverick designer and a car that is dazzling the hip-hop crowd", 'region': 'Africa', 'publication_date': '2015-06-02'}]}}

exec(code, env_args)
