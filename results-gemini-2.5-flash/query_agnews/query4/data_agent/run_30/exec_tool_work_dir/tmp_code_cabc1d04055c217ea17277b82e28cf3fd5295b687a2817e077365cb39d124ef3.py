code = """import pandas as pd
import json

# Helper function to load data, handling both direct list and file path
def load_data(data_var):
    if isinstance(data_var, str) and data_var.endswith('.json'):
        with open(data_var, 'r') as f:
            return json.load(f)
    else:
        return data_var

articles_data_raw = locals()['var_function-call-1683632755296053516']
metadata_data_raw = locals()['var_function-call-7513958644891186737']

articles_data = load_data(articles_data_raw)
metadata_data = load_data(metadata_data_raw)

articles_df = pd.DataFrame(articles_data)
metadata_df = pd.DataFrame(metadata_data)

# Define broad keywords for 'World' category, including all possible regions and general terms
world_keywords = [
    'world', 'global', 'international', 'foreign', 'country', 'nation',
    'asia', 'europe', 'africa', 'north america', 'south america', 'oceania',
    'middle east', 'latin america', 'pacific', 'atlantic', 'indian ocean',
    'un', 'nato', 'eu', 'g7', 'g20', 'summit', 'treaty', 'diplomacy',
    'war', 'peace', 'conflict', 'crisis', 'refugee', 'migration', 'humanitarian'
]

# Filter for "World" category articles using the broad keyword list
world_articles_df = articles_df[
    articles_df['title'].str.contains('|'.join(world_keywords), case=False, na=False) |
    articles_df['description'].str.contains('|'.join(world_keywords), case=False, na=False)
]

# Filter for articles published in 2015
metadata_df['publication_date'] = pd.to_datetime(metadata_df['publication_date'])
articles_2015_df = metadata_df[metadata_df['publication_date'].dt.year == 2015]

# Convert article_id to common type for merging (ensuring they are integers)
world_articles_df['article_id'] = pd.to_numeric(world_articles_df['article_id'])
articles_2015_df['article_id'] = pd.to_numeric(articles_2015_df['article_id'])

# Merge the two dataframes
merged_df = pd.merge(world_articles_df, articles_2015_df, on='article_id', how='inner')

# Count articles by region
region_counts = merged_df['region'].value_counts().reset_index()
region_counts.columns = ['region', 'article_count']

# Find the region with the largest number of articles
if not region_counts.empty:
    most_articles_region = region_counts.loc[region_counts['article_count'].idxmax()]
    result = most_articles_region.to_dict()
else:
    result = {"region": "No articles found for the 'World' category in 2015 using the defined keywords.", "article_count": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8693865706413765703': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943f9a77be70120c6195407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943f9a77be70120c6195408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943f9a77be70120c6195409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943f9a77be70120c619540a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5296106299331246141': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9755661042273656641': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943f9a77be70120c6195407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943f9a77be70120c6195408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943f9a77be70120c6195409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943f9a77be70120c619540a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7411714914002001774': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943f9a77be70120c6195407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943f9a77be70120c6195408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943f9a77be70120c6195409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943f9a77be70120c619540a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1683632755296053516': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7513958644891186737': 'file_storage/function-call-7513958644891186737.json', 'var_function-call-3272559847496742326': {'region': "No articles found for the 'World' category in 2015.", 'article_count': 0}, 'var_function-call-14411272205554102280': {'region': "No articles found for the 'World' category in 2015 using the defined keywords.", 'article_count': 0}}

exec(code, env_args)
