code = """import json
import pandas as pd

# Load metadata results from file path provided by previous query
with open(var_call_rKCzsemTQCcxwjqubUs6ZOnf, 'r') as f:
    meta = json.load(f)

# Articles results are directly available as var_call_l9hzgeW95RusCTbO9vDkkIev
arts = var_call_l9hzgeW95RusCTbO9vDkkIev

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_arts = pd.DataFrame(arts)

# Ensure article_id are strings for proper merging
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_arts['article_id'] = df_arts['article_id'].astype(str)

# Merge metadata with article content
df = df_meta.merge(df_arts, on='article_id', how='left')

# Extract year from publication_date
df['year'] = df['publication_date'].str.slice(0,4)

# Define business-related keywords (heuristic)
keywords = [
    'economy','economic','market','markets','stock','stocks','wall st','wall street',
    'investment','investor','shares','share','bank','finance','financial','earnings',
    'business','company','companies','merger','acquisition','ipo','revenue','oil prices','oil',
    'carlyle','aerospace','commercial aerospace'
]

# Classification function
def is_business(title, description):
    text = ''
    if title and not pd.isna(title):
        text += str(title) + ' '
    if description and not pd.isna(description):
        text += str(description)
    t = text.lower()
    return any(k in t for k in keywords)

# Apply classification
df['is_business'] = df.apply(lambda r: is_business(r.get('title',''), r.get('description','')), axis=1)

# Compute counts per year for 2010-2020 inclusive
years = [str(y) for y in range(2010, 2021)]
counts = {year: int(df[df['year']==year]['is_business'].sum()) for year in years}

total_business = sum(counts.values())
avg_per_year = total_business / len(years)

result = {
    'counts_per_year': counts,
    'total_business_articles': int(total_business),
    'average_per_year': round(avg_per_year, 2)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_rKCzsemTQCcxwjqubUs6ZOnf': 'file_storage/call_rKCzsemTQCcxwjqubUs6ZOnf.json', 'var_call_ZJre6Bqzg372vXtx1TKT3Dea': ['articles'], 'var_call_l9hzgeW95RusCTbO9vDkkIev': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
