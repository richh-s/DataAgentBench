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

# Define explicit keywords for each category
world_specific_keywords = [
    'world', 'global', 'international', 'foreign affairs', 'geopolitics', 'diplomacy',
    'united nations', 'un', 'eu', 'nato', 'g7', 'g20', 'summit', 'treaty',
    'conflict', 'war', 'peace', 'crisis', 'refugee', 'migration', 'humanitarian',
    'asia', 'europe', 'africa', 'north america', 'south america', 'oceania',
    'middle east', 'latin america', 'pacific', 'atlantic', 'arctic', 'antarctic'
]
sports_keywords = [
    'sport', 'sports', 'game', 'match', 'league', 'cup', 'season', 'tournament', 'athlete', 'team',
    'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'rugby', 'cricket', 'olympic', 'super bowl', 'world series'
]
business_keywords = [
    'business', 'economy', 'economic', 'finance', 'financial', 'market', 'stock', 'stocks', 'shares',
    'company', 'companies', 'firm', 'investment', 'investor', 'profit', 'loss', 'revenue', 'ceo', 'bank',
    'trade', 'merger', 'acquisition', 'inflation', 'recession', 'currency', 'dollar', 'euro', 'yen', 'gdp',
    'oil prices', 'gas prices', 'commodities', 'tech companies'
]
science_tech_keywords = [
    'science', 'scientific', 'technology', 'tech', 'research', 'study', 'discovery', 'innovation',
    'computer', 'software', 'internet', 'digital', 'ai', 'artificial intelligence', 'robot', 'robotics',
    'space', 'nasa', 'galaxy', 'universe', 'planet', 'medicine', 'health', 'medical', 'vaccine', 'drug',
    'engineering', 'data', 'cybersecurity', 'biotechnology', 'genetics', 'physics', 'chemistry', 'biology', 'astronomy'
]

# Convert article_id to common type for merging (ensuring they are integers)
articles_df['article_id'] = pd.to_numeric(articles_df['article_id'])
metadata_df['article_id'] = pd.to_numeric(metadata_df['article_id'])

# Merge articles and metadata
combined_df = pd.merge(articles_df, metadata_df, on='article_id', how='inner')

# Filter for articles published in 2015
combined_df['publication_date'] = pd.to_datetime(combined_df['publication_date'])
articles_2015_df = combined_df[combined_df['publication_date'].dt.year == 2015].copy()

# Function to check if keywords are present in title or description (case-insensitive)
def contains_keywords(text, keywords):
    if pd.isna(text):
        return False
    return any(keyword.lower() in text.lower() for keyword in keywords)

# Categorize articles with a priority order
articles_2015_df['category'] = None

# Assign 'Sports' category (highest priority)
articles_2015_df.loc[
    articles_2015_df.apply(lambda row: contains_keywords(row['title'], sports_keywords) or contains_keywords(row['description'], sports_keywords), axis=1),
    'category'
] = 'Sports'

# Assign 'Business' category
articles_2015_df.loc[
    articles_2015_df.apply(lambda row: contains_keywords(row['title'], business_keywords) or contains_keywords(row['description'], business_keywords), axis=1) & (articles_2015_df['category'].isna()),
    'category'
] = 'Business'

# Assign 'Science/Technology' category
articles_2015_df.loc[
    articles_2015_df.apply(lambda row: contains_keywords(row['title'], science_tech_keywords) or contains_keywords(row['description'], science_tech_keywords), axis=1) & (articles_2015_df['category'].isna()),
    'category'
] = 'Science/Technology'

# Assign 'World' category to articles containing world-specific keywords AND not categorized yet
articles_2015_df.loc[
    articles_2015_df.apply(lambda row: contains_keywords(row['title'], world_specific_keywords) or contains_keywords(row['description'], world_specific_keywords), axis=1) & (articles_2015_df['category'].isna()),
    'category'
] = 'World'

# For any remaining articles that are still uncategorized, we will assign them to World as well, as a fallback.
# This assumes any article not explicitly classified into other categories might be general 'World' news.
articles_2015_df['category'].fillna('World', inplace=True)

# Filter for 'World' category articles
world_articles_2015_df = articles_2015_df[articles_2015_df['category'] == 'World']

# Count articles by region for 'World' category
region_counts = world_articles_2015_df['region'].value_counts().reset_index()
region_counts.columns = ['region', 'article_count']

# Find the region with the largest number of 'World' articles
if not region_counts.empty:
    most_articles_region = region_counts.loc[region_counts['article_count'].idxmax()]
    result = most_articles_region.to_dict()
else:
    result = {"region": "No articles found for the 'World' category in 2015 with current keyword definitions.", "article_count": 0}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-8693865706413765703': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943f9a77be70120c6195407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943f9a77be70120c6195408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943f9a77be70120c6195409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943f9a77be70120c619540a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-5296106299331246141': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}], 'var_function-call-9755661042273656641': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943f9a77be70120c6195407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943f9a77be70120c6195408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943f9a77be70120c6195409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943f9a77be70120c619540a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7411714914002001774': [{'_id': '6943f9a77be70120c6195406', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943f9a77be70120c6195407', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943f9a77be70120c6195408', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943f9a77be70120c6195409', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943f9a77be70120c619540a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1683632755296053516': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-7513958644891186737': 'file_storage/function-call-7513958644891186737.json', 'var_function-call-3272559847496742326': {'region': "No articles found for the 'World' category in 2015.", 'article_count': 0}, 'var_function-call-14411272205554102280': {'region': "No articles found for the 'World' category in 2015 using the defined keywords.", 'article_count': 0}, 'var_function-call-14101817405882675055': {'region': "No articles found for the 'World' category in 2015 using the defined keywords.", 'article_count': 0}, 'var_function-call-12275809478551427769': {'region': "No articles found for the 'World' category in 2015 using the defined keywords.", 'article_count': 0}, 'var_function-call-15427678944212785435': {'region': "No articles found for the 'World' category in 2015 using the defined keywords.", 'article_count': 0}, 'var_function-call-8245432365330884141': {'region': "No articles found for the 'World' category in 2015 using the simplified keywords.", 'article_count': 0}, 'var_function-call-13835359626394647657': {'region': "No articles found for the 'World' category in 2015.", 'article_count': 0}, 'var_function-call-16566821860631559129': {'region': "No articles found for the 'World' category in 2015.", 'article_count': 0}, 'var_function-call-1140607788361555103': {'region': "No articles found for the 'World' category in 2015 using the defined categorization logic.", 'article_count': 0}, 'var_function-call-1800949751574783874': {'region': "No articles found for the 'World' category in 2015.", 'article_count': 0}}

exec(code, env_args)
