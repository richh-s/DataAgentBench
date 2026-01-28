code = """import json
import pandas as pd

# Load Europe metadata from file
with open(locals()['var_functions.query_db:8'], 'r') as f:
    europe_articles = json.load(f)

# Load all articles from the larger query  
with open(locals()['var_functions.query_db:50'], 'r') as f:
    all_articles = json.load(f)

# Create DataFrames
df_europe = pd.DataFrame(europe_articles)
df_articles = pd.DataFrame(all_articles)

# Filter Europe articles for 2010-2020
df_europe['year'] = pd.to_datetime(df_europe['publication_date']).dt.year
df_europe_filtered = df_europe[(df_europe['year'] >= 2010) & (df_europe['year'] <= 2020)]

# Merge Europe metadata with article content
df_combined = df_europe_filtered.merge(df_articles, on='article_id', how='inner')

# Enhanced business keywords (more comprehensive)
business_keywords = [
    # Financial markets
    'wall st', 'wall street', 'stock', 'stocks', 'stock market', 'shares', 'trading', 'bourse',
    # Economics
    'economy', 'economic', 'economics', 'gdp', 'inflation', 'recession', 'growth', 'economist',
    # Business general
    'business', 'company', 'companies', 'corporate', 'corporation', 'firm', 'enterprise', 'venture',
    # Banking & Finance
    'bank', 'banking', 'banker', 'banks', 'financial', 'finance', 'financing', 'investment', 'investing',
    'investor', 'investors', 'capital', 'fund', 'funds', 'hedge fund', 'private equity', 'venture capital',
    # Markets
    'market', 'markets', 'bull market', 'bear market', 'commodity', 'commodities', 'oil price', 'oil prices',
    # Money & Currency
    'dollar', 'euro', 'yen', 'currency', 'currencies', 'exchange rate', 'interest rate', 'rates',
    # Corporate
    'profit', 'profits', 'revenue', 'earnings', 'quarterly', 'dividend', 'acquisition', 'merger',
    'takeover', 'ipo', 'initial public offering', 'public offering', 'shares', 'earnings report',
    # Trade
    'trade', 'trading', 'imports', 'exports', 'trade deficit', 'trade surplus', 'tariff', 'tariffs',
    # Industry sectors
    'retail', 'industry', 'industrial', 'manufacturing', 'technology', 'tech', 'pharmaceutical', 'automotive',
    # Employment
    'jobs', 'employment', 'unemployment', 'hiring', 'layoffs', 'workforce', 'salary', 'wages'
]

# More comprehensive business check
keywords_set = set(business_keywords)

def is_business_article(title, description):
    if pd.isna(title):
        title = ''
    if pd.isna(description):
        description = ''
    
    text = f"{title} {description}".lower()
    
    # Check for standard business keywords
    for keyword in keywords_set:
        if keyword in text:
            return True
    
    # Additional check for strong financial terms  
    financial_terms = ['$', 'bn', 'million', 'billion', 'earnings', 'revenue']
    title_lower = title.lower()
    desc_lower = description.lower()
    
    if any(term in title_lower or term in desc_lower for term in ['stocks', 'shares', 'trading', 'ipo', 'investment', 'corporate', 'finance']):
        return True
        
    return False

# Apply categorization
business_articles_count = 0
business_counts_by_year = {year: 0 for year in range(2010, 2021)}

for idx, row in df_combined.iterrows():
    if is_business_article(row.get('title', ''), row.get('description', '')):
        business_articles_count += 1
        year = row['year']
        if year in business_counts_by_year:
            business_counts_by_year[year] += 1

# Calculate average
total_years = len(business_counts_by_year)
average_per_year = business_articles_count / total_years if total_years > 0 else 0

result = {
    'business_articles_by_year': business_counts_by_year,
    'total_business_articles': int(business_articles_count),
    'average_business_articles_per_year': round(average_per_year, 2),
    'total_europe_articles_analyzed': len(df_combined)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.list_db:2': ['authors', 'article_metadata'], 'var_functions.query_db:5': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:7': [{'_id': '6969beac5487ab0a07c7ac76', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac77', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969beac5487ab0a07c7ac78', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:16': {'business_counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total_business_articles': 0, 'average_per_year': 0.0}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'europe_articles_2010_2020': 14860, 'total_articles_db': 100, 'sample_europe_article_ids': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63']}, 'var_functions.query_db:22': [{'_id': '6969beac5487ab0a07c7ac76', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac77', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969beac5487ab0a07c7ac78', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:30': {'business_counts_per_year': {'2010': 0, '2011': 0, '2012': 0, '2013': 0, '2014': 0, '2015': 0, '2016': 0, '2017': 0, '2018': 0, '2019': 0, '2020': 0}, 'total_business_articles': 0, 'average_per_year': 0.0}, 'var_functions.query_db:32': [{'_id': '6969beac5487ab0a07c7ac76', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac77', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969beac5487ab0a07c7ac78', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': [{'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7f', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac83', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969beac5487ab0a07c7ac84', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969beac5487ab0a07c7ac8b', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}], 'var_functions.execute_python:40': {'total_europe_articles': 14860, 'sample_europe_article_ids': ['3', '9', '13', '14', '21', '27', '43', '60', '62', '63'], 'sample_actual_articles': [{'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7f', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac83', 'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'_id': '6969beac5487ab0a07c7ac84', 'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'_id': '6969beac5487ab0a07c7ac8b', 'article_id': '21', 'title': 'Eurozone economy keeps growing', 'description': 'Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.'}]}, 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:44': [{'_id': '6969beac5487ab0a07c7ac76', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969beac5487ab0a07c7ac77', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969beac5487ab0a07c7ac78', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969beac5487ab0a07c7ac79', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969beac5487ab0a07c7ac7a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:46': [{'article_id': '3'}, {'article_id': '9'}, {'article_id': '13'}, {'article_id': '14'}, {'article_id': '21'}, {'article_id': '27'}, {'article_id': '43'}, {'article_id': '60'}, {'article_id': '62'}, {'article_id': '63'}, {'article_id': '64'}, {'article_id': '66'}, {'article_id': '78'}, {'article_id': '128'}, {'article_id': '140'}, {'article_id': '142'}, {'article_id': '143'}, {'article_id': '144'}, {'article_id': '151'}, {'article_id': '154'}], 'var_functions.execute_python:48': {'total_europe_articles': 14860, 'total_actual_articles': 5, 'common_article_ids_length': 1, 'europe_sample_ids': ['94322', '100879', '115837', '33095', '60312', '85583', '95144', '34218', '34930', '113414'], 'actual_sample_ids': ['4', '0', '3', '2', '1'], 'common_sample': ['3']}, 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json'}

exec(code, env_args)
