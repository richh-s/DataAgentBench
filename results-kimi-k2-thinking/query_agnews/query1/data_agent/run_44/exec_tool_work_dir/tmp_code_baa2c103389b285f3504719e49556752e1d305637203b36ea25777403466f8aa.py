code = """import json, os, sys
# Load the full result from the JSON file path stored in var_functions.query_db:4
file_path = locals().get('var_functions.query_db:4')
print('File path:', file_path)
if not file_path or not os.path.exists(file_path):
    raise FileNotFoundError('File not found')
with open(file_path, 'r') as f:
    articles = json.load(f)
print('Number of articles:', len(articles))
# Show a few sample articles
for i, a in enumerate(articles[:10]):
    print(i, a.get('title'))
# Define sports keywords list
sports_keywords = ['football','basketball','baseball','soccer','hockey','tennis','golf','cricket','rugby','volleyball','olympics','world cup','coach','player','team','league','sport','sports','game','match','champion','title','final','cup','race','athlete','win','lose','defeat','victory','stadium','arena','record','points','score','goal','run','hit','bat','ball','field','court','playoffs','semifinal','quarterfinal','season']
# Function to check if a text is sports-related
import re

def is_sports(text):
    lower = text.lower()
    return any(kw in lower for kw in sports_keywords)
# Filter sports articles
sports_articles = []
for a in articles:
    combined = a.get('title','') + ' ' + a.get('description','')
    if is_sports(combined):
        sports_articles.append(a)
print('Number of sports articles (heuristic):', len(sports_articles))
# Compute description lengths for sports articles and find max
max_len = -1
max_article = None
for a in sports_articles:
    desc_len = len(a.get('description',''))
    if desc_len > max_len:
        max_len = desc_len
        max_article = a
print('Longest description length among sports:', max_len)
print('Title of that article:', max_article.get('title') if max_article else None)
# Output details about the article
if max_article:
    print('Full article:', max_article)
# For completeness, also see if there are any ties
max_articles = [a for a in sports_articles if len(a.get('description','')) == max_len]
print('Number of articles tied for max length:', len(max_articles))
for a in max_articles:
    print('Tied max article title:', a.get('title'))

print('__RESULT__:')
print(json.dumps(max_article.get('title') if max_article else None))"""

env_args = {'var_functions.query_db:0': [{'_id': '69697f31f785858cca58a7cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697f31f785858cca58a7d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697f31f785858cca58a7d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697f31f785858cca58a7d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697f31f785858cca58a7d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '69697f31f785858cca58a7d4', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '69697f31f785858cca58a7d5', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '69697f31f785858cca58a7d6', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '69697f31f785858cca58a7d7', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '69697f31f785858cca58a7d8', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.query_db:2': [{'_id': '69697f31f785858cca58a7cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69697f31f785858cca58a7d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69697f31f785858cca58a7d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69697f31f785858cca58a7d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69697f31f785858cca58a7d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json'}

exec(code, env_args)
