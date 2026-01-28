code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_9DH6aKujlvf58acomXd5FTzI, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(var_call_XHhfnaYrn8yg07BODDIuzIrK, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Create DataFrames
df_meta = pd.DataFrame(meta)
# Ensure article_id types align
if df_meta['article_id'].dtype == object:
    df_meta['article_id'] = df_meta['article_id'].astype(int)

df_articles = pd.DataFrame(articles)
if df_articles['article_id'].dtype == object:
    df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata for 2015 (meta already filtered) with articles
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Fill NaNs for title/description
df['title'] = df['title'].fillna('')
df['description'] = df['description'].fillna('')

# Simple rule-based classifier
sports_kw = ['match','tournament','goal','scored','season','football','soccer','basketball','baseball','tennis','golf','olympic','coach','team','league','nba','mlb','nfl','fifa','cup','race','boxing','athlete','athletes','score','draw']
business_kw = ['stock','stocks','market','economy','bank','banks','profit','profits','shares','invest','investment','oil','barrel','billion','trade deficit','trade','revenue','financial','finance','dollar','$','interest rate','ipo','merger','acquisition','company','firm']
sci_kw = ['research','scientist','scientists','science','technology','tech','nasa','nuclear','drug','drugs','medical','study','studies','computer','internet','software','ph.d','researchers','experiment','clinical']

def categorize(row):
    text = (str(row.get('title','')) + ' ' + str(row.get('description',''))).lower()
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply
df['category'] = df.apply(categorize, axis=1)

# Count World articles by region
world_df = df[df['category'] == 'World']
counts = world_df['region'].value_counts().to_dict()

# Determine top region
if counts:
    top_region = max(counts.items(), key=lambda x: x[1])[0]
    top_count = counts[top_region]
else:
    top_region = None
    top_count = 0

result = {'top_region': top_region, 'count': int(top_count), 'counts': counts}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_9DH6aKujlvf58acomXd5FTzI': 'file_storage/call_9DH6aKujlvf58acomXd5FTzI.json', 'var_call_XHhfnaYrn8yg07BODDIuzIrK': 'file_storage/call_XHhfnaYrn8yg07BODDIuzIrK.json'}

exec(code, env_args)
