code = """import json
import pandas as pd
from datetime import datetime
import re
from collections import Counter

# Load Europe metadata from 2010-2020
europe_metadata_file = locals().get('var_functions.query_db:20')
with open(europe_metadata_file, 'r') as f:
    europe_metadata = json.load(f)

# Load all articles from MongoDB
articles_file = locals().get('var_functions.query_db:30')
with open(articles_file, 'r') as f:
    articles_data = json.load(f)

# Filter for 2010-2020 years and create lookup
target_years = set(range(2010, 2021))
europe_2010_2020_ids = []

for record in europe_metadata:
    date_str = record.get('publication_date', '')
    if date_str:
        try:
            year = int(date_str.split('-')[0])
            if year in target_years:
                europe_2010_2020_ids.append((record['article_id'], year))
        except:
            pass

# Create lookup of articles by ID
articles_dict = {str(art['article_id']): art for art in articles_data}

# Identify business articles
business_keywords = [
    'business', 'stock', 'stocks', 'economy', 'economic', 'market', 'markets',
    'oil', 'profit', 'profits', 'trade', 'trading', 'finance', 'financial',
    'investment', 'investments', 'dollar', 'company', 'companies', 'rate',
    'rates', 'sector', 'bank', 'banks', 'ipo', 'shares', 'fund', 'funds',
    'billion', 'million', 'price', 'prices', 'deficit', 'auction'
]

business_articles = []
missing_articles = []

for article_id, year in europe_2010_2020_ids:
    if article_id in articles_dict:
        article = articles_dict[article_id]
        title = str(article.get('title', '')).lower()
        description = str(article.get('description', '')).lower()
        
        # Check if it's a business article
        for keyword in business_keywords:
            if keyword in title or keyword in description:
                business_articles.append({
                    'article_id': article_id,
                    'year': year,
                    'title': article.get('title', ''),
                    'description': article.get('description', '')
                })
                break
    else:
        missing_articles.append(article_id)

# Count by year
year_counts = Counter()
for article in business_articles:
    year_counts[article['year']] += 1

target_year_counts = {year: year_counts.get(year, 0) for year in target_years}
total_business = len(business_articles)
average_per_year = total_business / len(target_years) if total_business > 0 else 0

print('__RESULT__:')
print(json.dumps({
    "total_business_articles": total_business,
    "year_breakdown": target_year_counts,
    "average_per_year": round(average_per_year, 2),
    "total_europe_articles_checked": len(europe_2010_2020_ids),
    "articles_found": len(articles_dict),
    "missing_articles": len(missing_articles),
    "sample_business_articles": business_articles[:5]
}, default=str))"""

env_args = {'var_functions.list_db:0': ['authors', 'article_metadata'], 'var_functions.query_db:2': [{'_id': '6969c0715ce650d9b2a425cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c0715ce650d9b2a425d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c0715ce650d9b2a425d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c0715ce650d9b2a425d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c0715ce650d9b2a425d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:3': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.execute_python:8': {'articles_type': "<class 'list'>", 'metadata_type': "<class 'list'>", 'articles_sample': [{'_id': '6969c0715ce650d9b2a425cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c0715ce650d9b2a425d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}], 'metadata_sample': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}]}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:11': {'total_metadata_records': 0, 'metadata_sample': []}, 'var_functions.execute_python:14': {'total_metadata_records': 127600, 'total_article_records': 5, 'metadata_sample': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}], 'articles_sample': [{'_id': '6969c0715ce650d9b2a425cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c0715ce650d9b2a425d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c0715ce650d9b2a425d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:17': {'total_articles': 0, 'total_metadata': 127600, 'year_range': '2004 to 2022', 'target_year_counts': {'2016': 6877, '2017': 6610, '2018': 6763, '2019': 6682, '2020': 6848, '2010': 6774, '2011': 6795, '2012': 6676, '2013': 6734, '2014': 6761, '2015': 6696}, 'total_2010_2020': 74216}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:21': {'total_articles': 1000, 'europe_articles_2010_2020': 127600, 'articles_sample': [{'_id': '6969c0715ce650d9b2a425cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c0715ce650d9b2a425d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c0715ce650d9b2a425d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}], 'metadata_sample': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}]}, 'var_functions.execute_python:24': {'total_europe_2010_2020': 14860, 'year_breakdown': {'2016': 1364, '2017': 1391, '2018': 1351, '2019': 1328, '2020': 1366, '2010': 1306, '2011': 1316, '2012': 1355, '2013': 1354, '2014': 1372, '2015': 1357}, 'average_per_year': 1350.909090909091}, 'var_functions.query_db:26': [{'_id': '6969c0715ce650d9b2a425cf', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969c0715ce650d9b2a425d0', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969c0715ce650d9b2a425d1', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969c0715ce650d9b2a425d2', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969c0715ce650d9b2a425d3', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json'}

exec(code, env_args)
