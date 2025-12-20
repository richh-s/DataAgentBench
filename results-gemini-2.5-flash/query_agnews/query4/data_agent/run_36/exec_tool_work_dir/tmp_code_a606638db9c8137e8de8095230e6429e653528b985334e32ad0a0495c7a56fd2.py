code = """import pandas as pd
import json

# Access the list of JSON-serializable records directly from the tool output variable.
# According to the tool description, query_db returns a list of records directly.
articles_content = locals()['var_function-call-7469951950047165371']

# Load metadata for 2015 from the file path provided by the second tool call.
with open(locals()['var_function-call-14478801640615115315'], 'r') as f:
    metadata_2015 = json.load(f)

# Create Pandas DataFrames from the parsed data.
df_content = pd.DataFrame(articles_content)
df_metadata_2015 = pd.DataFrame(metadata_2015)

# Ensure 'article_id' columns are of string type for a proper merge.
df_content['article_id'] = df_content['article_id'].astype(str)
df_metadata_2015['article_id'] = df_metadata_2015['article_id'].astype(str)

# Merge the two DataFrames on the 'article_id' column using an inner join.
merged_df = pd.merge(df_metadata_2015, df_content, on='article_id', how='inner')

# Filter for articles that belong to the 'World' category.
world_articles = merged_df[
    merged_df['title'].astype(str).str.contains('World|world|Global|global', na=False) |
    merged_df['description'].astype(str).str.contains('World|world|Global|global', na=False)
]

# Initialize result_json with a default message.
result_json = json.dumps({"message": "No 'World' category articles found for 2015 or merge resulted in empty DataFrame."})

# Check if the 'world_articles' DataFrame is not empty.
if not world_articles.empty:
    # Count the number of 'World' articles for each unique region.
    region_counts = world_articles['region'].value_counts().reset_index()
    region_counts.columns = ['region', 'article_count']

    # Check if 'region_counts' DataFrame is not empty.
    if not region_counts.empty:
        # Find the region with the maximum 'article_count'.
        most_articles_region = region_counts.loc[region_counts['article_count'].idxmax()]
        result_json = most_articles_region.to_json()
    else:
        result_json = json.dumps({"message": "No regions found for 'World' category articles in 2015."})

print('__RESULT__:')
print(result_json)"""

env_args = {'var_function-call-7469951950047165371': [{'_id': '6943fb1946347c06cbdb2856', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6943fb1946347c06cbdb2857', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6943fb1946347c06cbdb2858', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6943fb1946347c06cbdb2859', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6943fb1946347c06cbdb285a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-14478801640615115315': 'file_storage/function-call-14478801640615115315.json'}

exec(code, env_args)
