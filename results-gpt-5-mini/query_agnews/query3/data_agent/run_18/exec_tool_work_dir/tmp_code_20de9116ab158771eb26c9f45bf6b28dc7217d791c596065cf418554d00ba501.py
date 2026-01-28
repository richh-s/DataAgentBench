code = """import json
import pandas as pd

# Load data from storage variables
# var_call_zUT3sUHsknIKciDT4w49V4Iv is a path to a JSON file (large result)
metadata_path = var_call_zUT3sUHsknIKciDT4w49V4Iv
with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

articles = var_call_aBLbtiJ0qJ9R6al400pP25Cu

# Create DataFrames
mdf = pd.DataFrame(metadata)
adf = pd.DataFrame(articles)

# Ensure article_id is string
mdf['article_id'] = mdf['article_id'].astype(str)
adf['article_id'] = adf['article_id'].astype(str)

# Merge
df = pd.merge(mdf, adf, on='article_id', how='left')

# Extract year
df['year'] = df['publication_date'].str.slice(0,4).astype(int)

# Define business-related keywords
keywords = [
    'business', 'market', 'markets', 'stock', 'stocks', 'shares', 'share', 'earnings', 'profit', 'profits',
    'revenue', 'investment', 'investor', 'investors', 'oil prices', 'oil price', 'oil', 'economy', 'economic',
    'wall st', 'wall street', 'carlyle', 'private investment', 'commercial', 'company', 'companies', 'firm', 'firms',
    'bank', 'banks', 'finance', 'financial'
]

# Function to classify
def is_business_article(title, desc):
    text = ''
    if isinstance(title, str):
        text += title.lower() + ' '
    if isinstance(desc, str):
        text += desc.lower()
    for kw in keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_business'] = df.apply(lambda row: is_business_article(row.get('title',''), row.get('description','')), axis=1)

# Filter years 2010-2020 inclusive
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Count per year
years = list(range(2010, 2021))
counts = df.groupby('year')['is_business'].sum().reindex(years, fill_value=0).to_dict()

total_business = int(sum(counts.values()))
num_years = len(years)
avg = total_business / num_years if num_years>0 else 0.0

result = {
    'average_business_articles_per_year': avg,
    'total_business_articles': total_business,
    'years_counted': num_years,
    'yearly_counts': counts
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_zUT3sUHsknIKciDT4w49V4Iv': 'file_storage/call_zUT3sUHsknIKciDT4w49V4Iv.json', 'var_call_aBLbtiJ0qJ9R6al400pP25Cu': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
