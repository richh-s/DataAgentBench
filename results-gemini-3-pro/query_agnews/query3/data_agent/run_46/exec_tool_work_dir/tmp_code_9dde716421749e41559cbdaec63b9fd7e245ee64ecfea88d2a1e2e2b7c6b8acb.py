code = """import json
import pandas as pd
import os

# Load SQL results
sql_key = 'var_function-call-1308901072042740489'
with open(locals()[sql_key], 'r') as f:
    sql_data = json.load(f)

df_meta = pd.DataFrame(sql_data)
# Ensure article_id is string for merging
df_meta['article_id'] = df_meta['article_id'].astype(str)

# Load Mongo results
mongo_key = 'var_function-call-17194694678475492943'
mongo_val = locals()[mongo_key]
if isinstance(mongo_val, str) and os.path.exists(mongo_val):
    with open(mongo_val, 'r') as f:
        mongo_data = json.load(f)
else:
    mongo_data = mongo_val

df_articles = pd.DataFrame(mongo_data)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge
merged = pd.merge(df_meta, df_articles, on='article_id', how='inner')

# Classification
# Extended keywords for Business
business_keywords = [
    'business', 'economy', 'market', 'financial', 'stock', 'trade', 'corporate', 
    'money', 'industry', 'profit', 'investment', 'bank', 'price', 'jobs', 
    'euro', 'dollar', 'fiscal', 'debt', 'oil', 'growth', 'rates', 'inflation', 
    'recession', 'merger', 'acquisition', 'deal', 'shares', 'investors', 'finance',
    'wall st', 'nasdaq', 'dow', 'gold', 'crude', 'imf', 'wto', 'revenue', 'sales',
    'ipo', 'earnings', 'dividend', 'fed', 'central bank', 'bond', 'fund', 'tax', 
    'budget', 'deficit', 'currency', 'consumer', 'retail', 'spending', 'sector', 
    'company', 'firm', 'ceo', 'cfo', 'executive', 'employment', 'unemployment', 
    'layoff', 'hiring', 'wage', 'salary', 'bonus', 'telecom', 'airline', 'automaker',
    'manufacturer', 'supplier', 'production', 'export', 'import'
]

def is_business(row):
    # Check title and description
    text = (str(row.get('title', '')) + " " + str(row.get('description', ''))).lower()
    
    # Simple check: if any keyword is in text
    # Note: simple substring match might have false positives (e.g. "fed" in "fed up")
    # But for this task, it's a reasonable approximation without NLP models.
    # To improve, we could check word boundaries, but let's start simple.
    
    for kw in business_keywords:
        if kw in text:
            return True
    return False

merged['is_business'] = merged.apply(is_business, axis=1)

# Filter Business
business_articles = merged[merged['is_business']]

# Group by year
# Ensure year is valid
# SQL result had 'year' column
business_counts = business_articles.groupby('year').size()

# Fill missing years with 0
all_years = [str(y) for y in range(2010, 2021)]
for y in all_years:
    if y not in business_counts:
        business_counts[y] = 0

# Sort by year for display (optional)
business_counts = business_counts.sort_index()

# Filter only 2010-2020 (though SQL already did this, just ensuring)
business_counts = business_counts[business_counts.index.isin(all_years)]

# Calculate Average
average = business_counts.mean()

print("__RESULT__:")
print(json.dumps({
    "merged_total": len(merged),
    "business_total": len(business_articles),
    "yearly_counts": business_counts.to_dict(),
    "average": average
}))"""

env_args = {'var_function-call-1308901072042740489': 'file_storage/function-call-1308901072042740489.json', 'var_function-call-11225229030681604654': 14860, 'var_function-call-9429883819834955631': [{'_id': '6944e5dbe888aca5de8a5407', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944e5dbe888aca5de8a5408', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944e5dbe888aca5de8a5409', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944e5dbe888aca5de8a540a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944e5dbe888aca5de8a540b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17437920335912610625': {'yearly_counts': {'2020': 1}, 'average': 1.0}, 'var_function-call-16316254877249595399': {'meta_rows': 14860, 'articles_rows': 5, 'merged_rows': 1, 'sample_titles': ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)'], 'business_kw_hits': 0}, 'var_function-call-7789543498600455310': 127583, 'var_function-call-17194694678475492943': 'file_storage/function-call-17194694678475492943.json'}

exec(code, env_args)
