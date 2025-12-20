code = """import json
import pandas as pd
import os

# Load SQL results
sql_key = 'var_function-call-1308901072042740489'
# It's a file path
with open(locals()[sql_key], 'r') as f:
    sql_data = json.load(f)

df_meta = pd.DataFrame(sql_data)
# df_meta has 'article_id', 'year'
# article_id might be string or int. In preview it was "3", "9". So string.

# Load Mongo results
mongo_key = 'var_function-call-9429883819834955631'
mongo_val = locals()[mongo_key]

if isinstance(mongo_val, str) and os.path.exists(mongo_val):
    with open(mongo_val, 'r') as f:
        mongo_data = json.load(f)
else:
    mongo_data = mongo_val

df_articles = pd.DataFrame(mongo_data)
# df_articles has 'article_id', 'title', 'description'
# article_id in preview was "0", "1". So string.

# Merge
# Ensure types match
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Classification
business_keywords = [
    'business', 'economy', 'market', 'financial', 'stock', 'trade', 'corporate', 
    'money', 'industry', 'profit', 'investment', 'bank', 'price', 'jobs', 
    'euro', 'dollar', 'fiscal', 'debt', 'oil', 'growth', 'rates', 'inflation', 
    'recession', 'merger', 'acquisition', 'deal', 'shares', 'investors', 'finance',
    'wall st', 'nasdaq', 'dow', 'gold', 'crude', 'imf', 'wto', 'revenue', 'sales'
]

# Negative keywords (to avoid false positives if any, but "Business" usually is distinct)
# "Sports", "Science", "World"
# Let's just stick to positive keywords. If a title contains these, it's likely Business.

def is_business(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter Business
business_articles = merged[merged['is_business']]

# Group by year and count
yearly_counts = business_articles.groupby('year').size()

# Filter years 2010 to 2020 (inclusive) - already done in SQL but good to check
# The SQL filter was `publication_date >= '2010-01-01' AND ...`
# So years should be correct.

# Calculate Average
average_per_year = yearly_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "yearly_counts": yearly_counts.to_dict(),
    "average": average_per_year
}))"""

env_args = {'var_function-call-1308901072042740489': 'file_storage/function-call-1308901072042740489.json', 'var_function-call-11225229030681604654': 14860, 'var_function-call-9429883819834955631': [{'_id': '6944e5dbe888aca5de8a5407', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e5dbe888aca5de8a5408', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e5dbe888aca5de8a5409', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e5dbe888aca5de8a540a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e5dbe888aca5de8a540b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
