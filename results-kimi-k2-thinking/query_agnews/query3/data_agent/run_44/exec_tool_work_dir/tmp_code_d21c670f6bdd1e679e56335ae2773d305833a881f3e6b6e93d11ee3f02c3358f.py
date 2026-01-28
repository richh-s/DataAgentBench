code = """import json

# Read the full metadata database results
metadata_path = var_functions.query_db:12
with open(metadata_path, 'r') as f:
    metadata_records = json.load(f)

# Read the full articles database results
articles_path = var_functions.query_db:14
with open(articles_path, 'r') as f:
    articles_records = json.load(f)

# Convert to DataFrames for analysis
import pandas as pd

articles_df = pd.DataFrame(articles_records)
metadata_df = pd.DataFrame(metadata_records)

# Show basic info
print("Number of articles:", len(articles_df))
print("Number of metadata records:", len(metadata_df))
print("\nArticles columns:", articles_df.columns.tolist())
print("Metadata columns:", metadata_df.columns.tolist())

# Show unique years in metadata
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
print("\nYear range:", metadata_df['publication_date'].dt.year.min(), "to", metadata_df['publication_date'].dt.year.max())
print("\nEurope articles by year:")
europe_metadata = metadata_df[metadata_df['region'] == 'Europe']
print(europe_metadata['publication_date'].dt.year.value_counts().sort_index())

# Check for business articles based on keywords
business_keywords = ['business', 'economy', 'stock', 'market', 'oil', 'price', 'wall', 'carlyle', 'firm', 'company', 'financial']
articles_df['title_lower'] = articles_df['title'].str.lower()
articles_df['desc_lower'] = articles_df['description'].str.lower()

# Filter business articles
business_articles = articles_df[
    articles_df['title_lower'].str.contains('|'.join(business_keywords)) | 
    articles_df['desc_lower'].str.contains('|'.join(business_keywords))
]

print("\nBusiness articles found:", len(business_articles))
print(business_articles[['title']].head())

# Merge with metadata
merged = business_articles.merge(metadata_df, on='article_id', how='inner')
print("\nMerged business articles:", len(merged))

# Filter for Europe and 2010-2020
europe_business = merged[
    (merged['region'] == 'Europe') & 
    (merged['publication_date'].dt.year >= 2010) & 
    (merged['publication_date'].dt.year <= 2020)
]

print("Europe business articles 2010-2020:", len(europe_business))

if len(europe_business) > 0:
    # Count by year
    europe_business['year'] = europe_business['publication_date'].dt.year
    yearly_counts = europe_business['year'].value_counts().sort_index()
    print("\nYearly counts:")
    print(yearly_counts)
    print("\nAverage per year:", yearly_counts.mean())
    
    result = {
        'total_articles': len(europe_business),
        'average_per_year': float(yearly_counts.mean()),
        'years_covered': yearly_counts.index.tolist(),
        'yearly_counts': yearly_counts.to_dict()
    }
else:
    result = {'message': 'No Europe business articles found for 2010-2020'}

print("\n__RESULT__:")
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'_id': '6969cbf1495113a7f4a675c1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cbf1495113a7f4a675c2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cbf1495113a7f4a675c3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cbf1495113a7f4a675c4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cbf1495113a7f4a675c5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969cbf1495113a7f4a675c6', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969cbf1495113a7f4a675c7', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969cbf1495113a7f4a675c8', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969cbf1495113a7f4a675c9', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969cbf1495113a7f4a675ca', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.list_db:5': ['authors', 'article_metadata'], 'var_functions.query_db:6': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}, {'article_id': '5', 'author_id': '802', 'region': 'Africa', 'publication_date': '2011-02-21'}, {'article_id': '6', 'author_id': '156', 'region': 'North America', 'publication_date': '2017-09-20'}, {'article_id': '7', 'author_id': '570', 'region': 'Europe', 'publication_date': '2022-12-23'}, {'article_id': '8', 'author_id': '272', 'region': 'Africa', 'publication_date': '2011-03-30'}, {'article_id': '9', 'author_id': '399', 'region': 'Europe', 'publication_date': '2016-05-24'}], 'var_functions.query_db:10': [{'_id': '6969cbf1495113a7f4a675c1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cbf1495113a7f4a675c2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cbf1495113a7f4a675c3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cbf1495113a7f4a675c4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cbf1495113a7f4a675c5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': [{'_id': '6969cbf1495113a7f4a675c1', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969cbf1495113a7f4a675c2', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969cbf1495113a7f4a675c3', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969cbf1495113a7f4a675c4', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969cbf1495113a7f4a675c5', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
