code = """import json, pandas as pd

# Read the 2015 article metadata from file
file_path = var_functions.query_db:4
with open(file_path, 'r') as f:
    articles_2015_metadata = json.load(f)

# Convert to DataFrame
df_metadata = pd.DataFrame(articles_2015_metadata)
article_ids_2015 = df_metadata['article_id'].tolist()

print('Total 2015 articles:', len(article_ids_2015))

# Read the articles from MongoDB (from previous query)
mongo_articles = var_functions.query_db:10

# Convert MongoDB result
if isinstance(mongo_articles, str):
    # It's a file path
    with open(mongo_articles, 'r') as f:
        all_articles = json.load(f)
else:
    all_articles = mongo_articles

# Filter to only 2015 articles
articles_2015 = [a for a in all_articles if str(a['article_id']) in article_ids_2015]

print('Found 2015 articles in MongoDB:', len(articles_2015))

# Create a mapping from article_id to region
region_map = dict(zip(df_metadata['article_id'], df_metadata['region']))

# Add region to each article
for article in articles_2015:
    article_id = str(article['article_id'])
    article['region'] = region_map.get(article_id, 'Unknown')

# Show first few
pd.set_option('display.max_columns', None)
df_articles = pd.DataFrame(articles_2015)
print(df_articles.head())

# Save for next step
print('__RESULT__:')
print(json.dumps({
    'count': len(articles_2015),
    'articles_preview': articles_2015[:5]
}))"""

env_args = {'var_functions.list_db:0': ['articles'], 'var_functions.query_db:2': [{'article_id': '13', 'author_id': '921', 'region': 'Europe', 'publication_date': '2015-10-17'}, {'article_id': '18', 'author_id': '268', 'region': 'South America', 'publication_date': '2015-08-15'}, {'article_id': '26', 'author_id': '470', 'region': 'Africa', 'publication_date': '2015-08-03'}, {'article_id': '51', 'author_id': '387', 'region': 'South America', 'publication_date': '2015-06-14'}, {'article_id': '52', 'author_id': '684', 'region': 'Africa', 'publication_date': '2015-06-02'}], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:10': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
