code = """import json
import pandas as pd

# Load metadata
path_meta = locals()['var_function-call-6219509864635122554']
with open(path_meta, 'r') as f:
    meta_data = json.load(f)

# Load articles
path_articles = locals()['var_function-call-6391207851705770972']
with open(path_articles, 'r') as f:
    articles_data = json.load(f)

# Convert to DataFrames
df_meta = pd.DataFrame(meta_data)
df_articles = pd.DataFrame(articles_data)

# Ensure article_id is string in both to match
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
# We only care about articles in df_meta (Europe, 2010-2020)
df_merged = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Classification
business_keywords = [
    'business', 'economy', 'economic', 'market', 'stock', 'shares', 'wall st', 
    'invest', 'finance', 'financial', 'trade', 'commerce', 'corporate', 'company', 
    'companies', 'profit', 'loss', 'bank', 'banking', 'dollar', 'euro', 'currency', 
    'oil', 'gold', 'price', 'rates', 'tax', 'deal', 'merger', 'acquisition', 
    'bond', 'recession', 'inflation', 'fed', 'treasury', 'carlyle', 'indus'
]

# Helper function to classify
def is_business(row):
    text = (str(row.get('title', '')) + " " + str(row.get('description', ''))).lower()
    # Check for keywords
    for kw in business_keywords:
        if kw in text:
            return True
    return False

df_merged['is_business'] = df_merged.apply(is_business, axis=1)

# Group by year and count
# Ensure we have all years 2010-2020
years = [str(y) for y in range(2010, 2021)]
yearly_counts = df_merged[df_merged['is_business']].groupby('year').size()

# Reindex to include 0 for missing years
yearly_counts = yearly_counts.reindex(years, fill_value=0)

# Calculate average
average_business = yearly_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "yearly_counts": yearly_counts.to_dict(),
    "average": average_business
}))"""

env_args = {'var_function-call-6219509864635122554': 'file_storage/function-call-6219509864635122554.json', 'var_function-call-11799845015617883549': 14860, 'var_function-call-4236489543979189159': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c5604aa2a519adff7872', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c5604aa2a519adff7873', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c5604aa2a519adff7874', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c5604aa2a519adff7875', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-13155074376232017203': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0'}], 'var_function-call-6391207851705770972': [{'_id': '6944c5604aa2a519adff7871', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944c5604aa2a519adff7872', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944c5604aa2a519adff7873', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944c5604aa2a519adff7874', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944c5604aa2a519adff7875', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
