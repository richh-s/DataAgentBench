code = """import json
import pandas as pd

# The result from query_db is stored as a file path, let's read it
file_path = locals()['var_functions.query_db:8']

# Read the JSON file
with open(file_path, 'r') as f:
    european_articles_raw = json.load(f)

# Convert to DataFrame for easier manipulation
metadata_df = pd.DataFrame(european_articles_raw)
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])

# Filter for 2010-2020
mask = (metadata_df['publication_date'].dt.year >= 2010) & (metadata_df['publication_date'].dt.year <= 2020)
filtered_df = metadata_df[mask]

# Group by year
duplicates_check = filtered_df.groupby('article_id').size().reset_index(name='count')
has_duplicates = (duplicates_check['count'] > 1).any()

print('__RESULT__:')
print(json.dumps({
    'total_european_articles_2010_2020': len(filtered_df),
    'unique_articles': filtered_df['article_id'].nunique(),
    'date_range': {
        'min': filtered_df['publication_date'].min().strftime('%Y-%m-%d'),
        'max': filtered_df['publication_date'].max().strftime('%Y-%m-%d')
    },
    'has_duplicates': has_duplicates,
    'articles_per_year': filtered_df.groupby(filtered_df['publication_date'].dt.year).size().to_dict()
}))"""

env_args = {'var_functions.query_db:0': [{'region': 'Europe', 'count': '25432'}], 'var_functions.query_db:2': [{'_id': '6969b9374839902a6ae6d508', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6969b9374839902a6ae6d509', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969b9374839902a6ae6d50a', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969b9374839902a6ae6d50b', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969b9374839902a6ae6d50c', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969b9374839902a6ae6d50d', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969b9374839902a6ae6d50e', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969b9374839902a6ae6d50f', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969b9374839902a6ae6d510', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969b9374839902a6ae6d511', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}], 'var_functions.execute_python:9': {'european_articles_count': '25432', 'sample_articles_count': 10}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
