code = """import json
import pandas as pd

# Load the two stored query results. The storage variables were provided by previous tool calls.
data_path_meta = var_call_mR3JAxXxHbxfJaNdCFRWQBOU
data_path_articles = var_call_N392kOSF8AnecUccLeLNtg6Q

# If the variables are file paths (strings), load the JSON from them; otherwise assume they are already lists.
if isinstance(data_path_meta, str):
    with open(data_path_meta, 'r', encoding='utf-8') as f:
        meta = json.load(f)
else:
    meta = data_path_meta

if isinstance(data_path_articles, str):
    with open(data_path_articles, 'r', encoding='utf-8') as f:
        articles = json.load(f)
else:
    articles = data_path_articles

# Create DataFrames
df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id types align
df_meta['article_id'] = df_meta['article_id'].astype(str)
df_articles['article_id'] = df_articles['article_id'].astype(str)

# Merge on article_id
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Extract year
df['year'] = df['publication_date'].str.slice(0,4).astype(int)

# Filter years 2010-2020 inclusive
df = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Classification: identify Business articles using keyword matching in title+description
business_keywords = [
    'economy','economic','economics','stocks','stock','shares','market','investment','investor','invest',
    'bank','banks','firm','company','companies','ipo','profit','profits','merger','acquisition','revenue',
    'earnings','financial','finance','trade deficit','trade','business','retail','billion','million','oil prices',
    'oil prices','oil','commodity','currenc','currency','eurozone','euro zone'
]

def is_business(row):
    text = ''
    if pd.notnull(row.get('title')):
        text += str(row.get('title')) + ' '
    if pd.notnull(row.get('description')):
        text += str(row.get('description'))
    text = text.lower()
    for kw in business_keywords:
        if kw in text:
            return True
    return False

# Apply classification
df['is_business'] = df.apply(is_business, axis=1)

# Count business articles per year
counts = df[df['is_business']].groupby('year').size().to_dict()

# Ensure all years 2010-2020 present
years = list(range(2010, 2021))
counts_full = {str(y): int(counts.get(y, 0)) for y in years}

# Compute average over 11 years
total_business = sum(counts_full[str(y)] for y in years)
average = total_business / len(years)

result = {
    'counts_per_year': counts_full,
    'total_business_articles': int(total_business),
    'years_considered': [str(y) for y in years],
    'average_per_year': average
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_mR3JAxXxHbxfJaNdCFRWQBOU': 'file_storage/call_mR3JAxXxHbxfJaNdCFRWQBOU.json', 'var_call_N392kOSF8AnecUccLeLNtg6Q': 'file_storage/call_N392kOSF8AnecUccLeLNtg6Q.json'}

exec(code, env_args)
