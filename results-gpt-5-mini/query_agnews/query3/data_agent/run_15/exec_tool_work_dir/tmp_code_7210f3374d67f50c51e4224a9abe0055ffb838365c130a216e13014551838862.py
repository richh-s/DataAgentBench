code = """import json
import pandas as pd
import re

# Load metadata results from the file path provided by the previous query
with open(var_call_q78PEAHtaO6IWgEBR2JqPc9H, 'r') as f:
    metadata = json.load(f)

articles = var_call_R2Cql4qQiXuGYOMBW1s4Dzcy

# Create DataFrames
df_meta = pd.DataFrame(metadata)
df_articles = pd.DataFrame(articles)

# Ensure correct types
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_meta['publication_date'] = pd.to_datetime(df_meta['publication_date'], errors='coerce')

df_articles['article_id'] = df_articles['article_id'].astype(int)
# Some descriptions/titles might be missing; fill with empty strings
df_articles['title'] = df_articles['title'].fillna('')
df_articles['description'] = df_articles['description'].fillna('')

# Merge metadata with article content
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Define business-related keywords
keywords = [
    'business', 'economy', 'economic', 'market', 'markets', 'stock', 'stocks', 'wall st', 'wall street',
    'finance', 'financial', 'investment', 'investor', 'company', 'companies', 'firm', 'billion', 'million',
    'dollar', 'oil prices', 'oil', 'bank', 'banks', 'interest rate', 'unemployment', 'revenue', 'profit', 'profits',
    'merger', 'acquisition', 'acquisitions', 'ipo', 'dividend'
]

# Function to detect business category
def is_business(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    for kw in keywords:
        if kw in text:
            return True
    return False

# Apply detection
df['is_business'] = df.apply(is_business, axis=1)

# Consider years 2010 through 2020 inclusive
df['year'] = df['publication_date'].dt.year
mask = (df['year'] >= 2010) & (df['year'] <= 2020)
df_period = df[mask]

# Count business articles per year
counts_series = df_period[df_period['is_business']].groupby('year').size()

# Ensure all years present
years = list(range(2010, 2021))
counts_dict = {str(y): int(counts_series.get(y, 0)) for y in years}

total_business = sum(counts_dict.values())
num_years = len(years)
average = total_business / num_years if num_years > 0 else 0.0

result = {
    'average_business_articles_per_year': round(average, 2),
    'total_business_articles_2010_2020': int(total_business),
    'years_considered': years,
    'counts_by_year': counts_dict
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_JCaa3ZWg4dLWdpaLItmQtTlw': ['articles'], 'var_call_09FevAZYdkloxPmZEdozjs1C': ['authors', 'article_metadata'], 'var_call_q78PEAHtaO6IWgEBR2JqPc9H': 'file_storage/call_q78PEAHtaO6IWgEBR2JqPc9H.json', 'var_call_R2Cql4qQiXuGYOMBW1s4Dzcy': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
