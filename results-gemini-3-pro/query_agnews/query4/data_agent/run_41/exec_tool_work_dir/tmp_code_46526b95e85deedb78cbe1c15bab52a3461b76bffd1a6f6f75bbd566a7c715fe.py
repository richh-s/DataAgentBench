code = """import json
import pandas as pd

# Load articles metadata (2015)
file_path_meta = locals()['var_function-call-1582016694630583511']
with open(file_path_meta, 'r') as f:
    meta_data = json.load(f)
df_meta = pd.DataFrame(meta_data)
df_meta['article_id'] = df_meta['article_id'].astype(int)

# Load articles content
# The result might be a list directly or a file path depending on size.
# The previous output said "The result is stored under key: ... The result is: [...]"
# It didn't say it's in a file. So it's likely a list in the variable.
# But if it's large, the system usually puts it in a file.
# Let's check the type of the variable.
articles_data_var = locals()['var_function-call-607457671861550025']

if isinstance(articles_data_var, str) and (articles_data_var.endswith('.json') or len(articles_data_var) < 200):
    # It might be a file path if it's a string looking like a path
    try:
        with open(articles_data_var, 'r') as f:
            articles_data = json.load(f)
    except:
        # If it's not a file, maybe it's the list itself (but the variable would be the list)
        articles_data = articles_data_var
else:
    articles_data = articles_data_var

# If articles_data is still a string (maybe the preview?), we have a problem. 
# But usually the system ensures if it's large, it's a filepath.
# If it's a list, we are good.

df_articles = pd.DataFrame(articles_data)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge
df_merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Print sample to understand categories
print("__RESULT__:")
print(json.dumps({"sample": df_merged[['title', 'description']].head(10).to_dict(orient='records'), "total_merged": len(df_merged)}))"""

env_args = {'var_function-call-1582016694630583511': 'file_storage/function-call-1582016694630583511.json', 'var_function-call-8744902824758175518': {'count': 6696, 'sample_ids': [13, 18, 26, 51, 52, 67, 70, 74, 86, 97]}, 'var_function-call-607457671861550025': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
