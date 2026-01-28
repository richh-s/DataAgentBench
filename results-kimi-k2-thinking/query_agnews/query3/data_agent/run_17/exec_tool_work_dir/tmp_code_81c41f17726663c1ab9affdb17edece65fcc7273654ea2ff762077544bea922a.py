code = """import json
import pandas as pd

# Load articles (this is actually a list, not a file path)
all_articles = locals()['var_functions.query_db:20']

# Load European articles metadata
metadata_file = locals()['var_functions.query_db:8']
with open(metadata_file, 'r') as f:
    european_articles_raw = json.load(f)

# Set up data
articles_df = pd.DataFrame(all_articles)
metadata_df = pd.DataFrame(european_articles_raw)

# Create business keywords list
business_keywords = [
    'stock', 'stocks', 'wall st', 'wall street', 'economy', 'economic', 
    'oil', 'price', 'prices', 'market', 'markets', 'investment', 'investing',
    'business', 'company', 'companies', 'bank', 'banks', 'financial', 'finance',
    'profit', 'loss', 'revenue', 'sales', 'trading', 'fund', 'funds'
]

# Check if the sample articles are business articles
def is_business_article(title, description):
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in business_keywords)

# Analyze the sample articles
sample_results = []
for _, article in articles_df.iterrows():
    is_business = is_business_article(article['title'], article['description'])
    sample_results.append({
        'article_id': article['article_id'],
        'title': article['title'],
        'is_business': is_business
    })

# Get European articles IDs for 2010-2020
european_ids = set(metadata_df['article_id'].astype(str).tolist())

# Check which of our sample articles are European
for result in sample_results:
    result['is_european'] = result['article_id'] in european_ids

print('__RESULT__:')
print(json.dumps({
    'sample_articles_analysis': sample_results,
    'european_articles_count': len(metadata_df),
    'sample_articles_count': len(articles_df)
}, default=str))"""

env_args = {'var_functions.query_db:0': [{'region': 'Europe', 'count': '25432'}], 'var_functions.query_db:2': [{'_id': '6969b9374839902a6ae6d508', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9374839902a6ae6d509', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9374839902a6ae6d50a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9374839902a6ae6d50b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9374839902a6ae6d50c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969b9374839902a6ae6d50d', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969b9374839902a6ae6d50e', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969b9374839902a6ae6d50f', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969b9374839902a6ae6d510', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969b9374839902a6ae6d511', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.execute_python:9': {'european_articles_count': '25432', 'sample_articles_count': 10}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_european_articles_2010_2020': 14860, 'unique_articles': 14860, 'date_range_min': '2010-01-01', 'date_range_max': '2020-12-30', 'articles_per_year': {'2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357, '2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366}}, 'var_functions.query_db:14': [{'_id': '6969b9374839902a6ae6d508', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9374839902a6ae6d509', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9374839902a6ae6d50a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9374839902a6ae6d50b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9374839902a6ae6d50c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:18': {'total_articles': 5, 'total_european_cases': 14860, 'european_id_sample': ['82482', '37248', '49844', '84537', '89140'], 'article_columns': ['_id', 'article_id', 'title', 'description'], 'sample_article': {'_id': '6969b9374839902a6ae6d508', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}}, 'var_functions.query_db:20': [{'_id': '6969b9374839902a6ae6d508', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9374839902a6ae6d509', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9374839902a6ae6d50a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9374839902a6ae6d50b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9374839902a6ae6d50c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
