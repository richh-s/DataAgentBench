code = """import json
import pandas as pd

# Load metadata for 2015
metadata_file_path = globals()['var_functions.query_db:2']
articles_file_path = globals()['var_functions.query_db:14']

with open(metadata_file_path, 'r') as f:
    metadata_2015 = json.load(f)

with open(articles_file_path, 'r') as f:
    all_articles = json.load(f)

# Create dataframes and convert article_id to int
metadata_df = pd.DataFrame(metadata_2015)
metadata_df['article_id'] = metadata_df['article_id'].astype(int)

articles_df = pd.DataFrame(all_articles)
articles_df['article_id'] = articles_df['article_id'].astype(int)

# Merge to combine article content with region info
merged_df = pd.merge(articles_df, metadata_df, on='article_id', how='inner')

# World news categorization function
world_keywords = {
    'war', 'peace', 'conflict', 'military', 'diplomat', 'diplomacy', 'treaty', 'united nations', 'un', 'global', 'world', 'international', 'foreign', 'crisis', 'iraq', 'iran', 'afghanistan', 'syria', 'israel', 'palestine', 'north korea', 'lebanon', 'pakistan', 'india', 'china', 'russia', 'terror', 'terrorist', 'attack', 'bomb', 'violence', 'killed', 'death', 'hostage', 'kidnap', 'election', 'president', 'government', 'political', 'protest', 'humanitarian', 'aid', 'embassy'
}

def is_world_news(title, description):
    text = f"{title} {description}".lower()
    return any(keyword in text for keyword in world_keywords)

# Categorize articles
merged_df['is_world'] = merged_df.apply(lambda row: is_world_news(row['title'], row['description']), axis=1)

# Filter for World category
world_articles = merged_df[merged_df['is_world'] == True]

# Count by region
region_counts = world_articles['region'].value_counts()

top_region = region_counts.index[0] if len(region_counts) > 0 else None
top_region_count = int(region_counts.iloc[0]) if len(region_counts) > 0 else 0

print('__RESULT__:')
print(json.dumps({
    'total_world_articles_2015': len(world_articles),
    'top_region': top_region,
    'top_region_count': top_region_count,
    'region_breakdown': region_counts.to_dict()
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': {'message': 'testing variable access'}, 'var_functions.query_db:14': [{'_id': '6969e4a77dc683d979b3844a', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6969e4a77dc683d979b3844b', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6969e4a77dc683d979b3844c', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6969e4a77dc683d979b3844d', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}, {'_id': '6969e4a77dc683d979b3844e', 'article_id': '5', 'title': 'Stocks End Up, But Near Year Lows (Reuters)', 'description': 'Reuters - Stocks ended slightly higher on Friday\\but stayed near lows for the year as oil prices surged past  #36;46\\a barrel, offsetting a positive outlook from computer maker\\Dell Inc. (DELL.O)'}, {'_id': '6969e4a77dc683d979b3844f', 'article_id': '6', 'title': 'Money Funds Fell in Latest Week (AP)', 'description': "AP - Assets of the nation's retail money market mutual funds fell by  #36;1.17 billion in the latest week to  #36;849.98 trillion, the Investment Company Institute said Thursday."}, {'_id': '6969e4a77dc683d979b38450', 'article_id': '7', 'title': 'Fed minutes show dissent over inflation (USATODAY.com)', 'description': 'USATODAY.com - Retail sales bounced back a bit in July, and new claims for jobless benefits fell last week, the government said Thursday, indicating the economy is improving from a midsummer slump.'}, {'_id': '6969e4a77dc683d979b38451', 'article_id': '8', 'title': 'Safety Net (Forbes.com)', 'description': 'Forbes.com - After earning a PH.D. in Sociology, Danny Bazil Riley started to work as the general manager at a commercial real estate firm at an annual base salary of  #36;70,000. Soon after, a financial planner stopped by his desk to drop off brochures about insurance benefits available through his employer. But, at 32, "buying insurance was the furthest thing from my mind," says Riley.'}, {'_id': '6969e4a77dc683d979b38452', 'article_id': '9', 'title': 'Wall St. Bears Claw Back Into the Black', 'description': " NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again."}, {'_id': '6969e4a77dc683d979b38453', 'article_id': '10', 'title': "Oil and Economy Cloud Stocks' Outlook", 'description': ' NEW YORK (Reuters) - Soaring crude prices plus worries  about the economy and the outlook for earnings are expected to  hang over the stock market next week during the depth of the  summer doldrums.'}], 'var_functions.execute_python:16': ['var_functions.query_db:2', 'var_functions.query_db:14'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.execute_python:28': ['var_functions.query_db:14', 'var_functions.query_db:2', 'var_functions.query_db:20', 'var_functions.query_db:22'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:36': {'var_name': 'var_functions.query_db:2', 'var_value': 'file_storage/functions.query_db:2.json', 'type': "<class 'str'>", 'exists': True}}

exec(code, env_args)
