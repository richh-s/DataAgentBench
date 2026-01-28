code = """import json
import pandas as pd

# Load the large metadata result from file path variable
metadata_path = var_call_qFYCEPNcC5i9kNKLbffrXMPd
with open(metadata_path, 'r', encoding='utf-8') as f:
    metadata = json.load(f)

articles = var_call_V43WsOO5iwJXHAOaEVfYO6kV

# Create DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure article_id types align
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge metadata for Europe with article content
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Consider years 2010 through 2020 inclusive
years = list(range(2010, 2021))

# Define a simple keyword-based classifier for Business
business_keywords = [
    'market','economy','stock','stocks','wall st','wall street','investment','investor','investors',
    'finance','financial','bank','banks','company','companies','business','commercial','merger','acquisition',
    'ipo','earnings','profit','profits','revenue','tax','interest rate','inflation','oil prices','oil','crude',
    'shares','billion','million'
]

def is_business(row):
    text = ''
    if isinstance(row.get('title'), str):
        text += row['title'] + ' '
    if isinstance(row.get('description'), str):
        text += row['description']
    text = text.lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_business'] = df.apply(is_business, axis=1)

# Extract year from publication_date
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

# Count business articles per year within target range
counts = {}
for y in years:
    cnt = int(df[(df['year'] == y) & (df['is_business'] == True)].shape[0])
    counts[str(y)] = cnt

# Compute average over 11 years
total_business = sum(counts.values())
average_per_year = total_business / len(years)

result = {
    'counts_per_year': counts,
    'total_business_articles_2010_2020': total_business,
    'average_per_year': round(average_per_year, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qFYCEPNcC5i9kNKLbffrXMPd': 'file_storage/call_qFYCEPNcC5i9kNKLbffrXMPd.json', 'var_call_V43WsOO5iwJXHAOaEVfYO6kV': [{'_id': '6959a003b2043ec31e4bb146', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6959a003b2043ec31e4bb147', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6959a003b2043ec31e4bb148', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6959a003b2043ec31e4bb149', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6959a003b2043ec31e4bb14a', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
