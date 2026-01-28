code = """import json
import pandas as pd

# Load the large metadata result from the provided file path variable
with open(var_call_z3xJbeTuPuxCLBbKQ0l7jYbZ, 'r') as f:
    metadata = json.load(f)

articles = var_call_GQYFzRKbE7YNTmFH5UHdDDYX

# Create DataFrames
df_meta = pd.DataFrame(metadata)
# Ensure article_id is string for safe merge
df_meta['article_id'] = df_meta['article_id'].astype(str)
# Extract year
df_meta['year'] = pd.to_datetime(df_meta['publication_date'], errors='coerce').dt.year

df_articles = pd.DataFrame(articles)
if not df_articles.empty:
    df_articles['article_id'] = df_articles['article_id'].astype(str)
else:
    df_articles = pd.DataFrame(columns=['article_id','title','description'])

# Merge metadata (Europe, 2010-2020 already filtered in query) with articles content
df_merged = df_meta.merge(df_articles, on='article_id', how='left')

# Simple keyword-based classifier for Business
business_keywords = [
    'market','markets','stock','stocks','economy','economic','business','company','companies',
    'finance','financial','invest','investment','revenue','profit','merger','acquisition',
    'wall st','wall street','shares','bonds','oil prices','oil prices','oil','bank','banks',
    'aerospace','private investment','carlyle','corporate', 'retail'
]

def is_business(row):
    title = (row.get('title') or '')
    desc = (row.get('description') or '')
    text = (title + ' ' + desc).lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classifier only where we have some text; if no text, we'll mark as False (cannot determine)
df_merged['is_business'] = df_merged.apply(is_business, axis=1)

# Consider years 2010 through 2020 inclusive
years = list(range(2010, 2021))
counts_by_year = {str(y): 0 for y in years}

# Count business articles per year only for years in range
for y in years:
    counts_by_year[str(y)] = int(((df_merged['year'] == y) & (df_merged['is_business'])).sum())

total_business = sum(counts_by_year.values())
average_business_per_year = total_business / len(years)

# Count how many metadata rows lacked matching article text
unmatched = int(df_merged['title'].isna().sum())

result = {
    'counts_by_year': counts_by_year,
    'total_business_articles': int(total_business),
    'years_considered': len(years),
    'average_business_articles_per_year': round(float(average_business_per_year), 2),
    'unmatched_metadata_rows_without_article_text': unmatched
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_z3xJbeTuPuxCLBbKQ0l7jYbZ': 'file_storage/call_z3xJbeTuPuxCLBbKQ0l7jYbZ.json', 'var_call_GQYFzRKbE7YNTmFH5UHdDDYX': [{'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
