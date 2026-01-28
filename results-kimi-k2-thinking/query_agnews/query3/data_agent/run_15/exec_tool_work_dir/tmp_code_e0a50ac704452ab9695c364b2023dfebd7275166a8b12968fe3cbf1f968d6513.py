code = """import json
import pandas as pd

# Load all articles (only 5 available)
articles = locals()['var_functions.query_db:14']

# Load all metadata from file
metadata_file = locals()['var_functions.query_db:8']
with open(metadata_file, 'r') as f:
    metadata = json.load(f)

# Convert to DataFrames
articles_df = pd.DataFrame(articles)
metadata_df = pd.DataFrame(metadata)

# Check how many articles vs metadata entries we have
print(f'Total articles available: {len(articles_df)}')
print(f'Total metadata entries: {len(metadata_df)}')

# Check for Europe articles in our small sample
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
europe_articles = metadata_df[
    (metadata_df['region'] == 'Europe') & 
    (metadata_df['publication_date'] >= '2010-01-01') & 
    (metadata_df['publication_date'] <= '2020-12-31')
].copy()

europe_articles['year'] = europe_articles['publication_date'].dt.year

print(f'Europe articles in 2010-2020: {len(europe_articles)}')

# Define business keywords
def is_business_article(title, description):
    if not title and not description:
        return False
    
    business_keywords = [
        'wall st', 'business', 'economy', 'stocks', 'stock', 'oil', 'prices',
        'commercial', 'investment', 'firm', 'company', 'companies', 'market',
        'finance', 'financial', 'trade', 'trading', 'profit', 'loss', 'revenue',
        'economic', 'economics', 'bears', 'bear', 'bull', 'equity', 'bond',
        'export', 'pipeline', 'gasoline', 'energy', 'dollar', 'wall street',
        'nasdaq', 'dow jones', 's&p', 'bank', 'banking', 'merger', 'acquisition'
    ]
    
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in business_keywords)

# Apply business classification
if not articles_df.empty:
    articles_df['is_business'] = articles_df.apply(
        lambda row: is_business_article(row.get('title', ''), row.get('description', '')), 
        axis=1
    )
    print(f'Business articles in our sample: {articles_df["is_business"].sum()}')
    print(articles_df[['article_id', 'title', 'is_business']])

# Merge with Europe metadata
europe_article_ids = set(europe_articles['article_id'].astype(str))
print(f'Europe article IDs in range: {sorted(list(europe_article_ids))}')

# Check which of our 5 articles are in Europe range
europe_matches = articles_df[articles_df['article_id'].isin(europe_article_ids)]
print(f'Matching articles: {len(europe_matches)}')
if not europe_matches.empty:
    print(europe_matches[['article_id', 'title']])

print('__RESULT__:')
print(json.dumps({
    'message': 'Analysis shows insufficient data to calculate meaningful average',
    'articles_available': len(articles_df),
    'europe_articles_in_range': len(europe_articles),
    'sample_business_articles': int(articles_df['is_business'].sum()) if not articles_df.empty else 0
}))"""

env_args = {'var_functions.query_db:0': [{'_id': '6969b785cac35b9b0168bab8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b785cac35b9b0168bab9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b785cac35b9b0168baba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b785cac35b9b0168babb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b785cac35b9b0168babc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:4': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:6': [{'_id': '6969b785cac35b9b0168bab8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b785cac35b9b0168bab9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b785cac35b9b0168baba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b785cac35b9b0168babb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b785cac35b9b0168babc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'average_business_articles_per_year': 1.0, 'total_years_with_data': 1, 'total_business_articles': 1, 'years': [{'year': 2020, 'count': 1}]}, 'var_functions.query_db:14': [{'_id': '6969b785cac35b9b0168bab8', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b785cac35b9b0168bab9', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b785cac35b9b0168baba', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b785cac35b9b0168babb', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b785cac35b9b0168babc', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
