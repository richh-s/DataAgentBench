code = """import json
import pandas as pd

# Load metadata JSON from file path stored in var_call_5d9g51AKboTVOEsapUiJgD3E
with open(var_call_5d9g51AKboTVOEsapUiJgD3E, 'r') as f:
    metadata = json.load(f)

articles = var_call_Kt0MVezymAoWjg6d1Mfsi3xP

# Create DataFrames
md_df = pd.DataFrame(metadata)
arts_df = pd.DataFrame(articles)

# Merge on article_id
df = md_df.merge(arts_df[['article_id','title','description']], on='article_id', how='left')

# Parse years
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

# Define business-related keywords
biz_kw = [
    'market','markets','stock','stocks','economy','economic','finance','financial',
    'oil','earnings','investment','investor','investors','business','company','companies',
    'commercial','carlyle','wall st','wall street','short-seller','short-sellers','private investment'
]

# Classify as business if any keyword appears in title or description
def is_business(row):
    text = ''
    if isinstance(row.get('title'), str):
        text += ' ' + row['title'].lower()
    if isinstance(row.get('description'), str):
        text += ' ' + row['description'].lower()
    for kw in biz_kw:
        if kw in text:
            return True
    return False

df['is_business'] = df.apply(is_business, axis=1)

# Filter years 2010-2020 inclusive
df_period = df[(df['year'] >= 2010) & (df['year'] <= 2020)]

# Count business articles per year, ensure all years present
years = list(range(2010, 2021))
counts_series = df_period[df_period['is_business']].groupby('year').size()
counts = {year: int(counts_series.get(year, 0)) for year in years}

# Compute average
average = sum(counts.values()) / len(years) if len(years) > 0 else 0.0

result = {
    'counts_per_year': counts,
    'average_per_year': average
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5d9g51AKboTVOEsapUiJgD3E': 'file_storage/call_5d9g51AKboTVOEsapUiJgD3E.json', 'var_call_Kt0MVezymAoWjg6d1Mfsi3xP': [{'_id': '69599c6f02c599526acbc521', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69599c6f02c599526acbc522', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69599c6f02c599526acbc523', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69599c6f02c599526acbc524', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69599c6f02c599526acbc525', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}]}

exec(code, env_args)
