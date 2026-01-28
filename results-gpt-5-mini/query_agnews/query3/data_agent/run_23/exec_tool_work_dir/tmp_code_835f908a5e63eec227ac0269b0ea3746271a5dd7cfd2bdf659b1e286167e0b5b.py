code = """import pandas as pd
import json
import re

# Load data from storage file paths
meta_path = var_call_CGCBBhBfzybdf4Zfxhj40TX1
articles_path = var_call_VA1uuuIu8nx0F9ZslM0P1GYS

with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(articles_path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

df_meta = pd.DataFrame(meta)
df_articles = pd.DataFrame(articles)

# Ensure article_id is integer for proper join
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_articles['article_id'] = df_articles['article_id'].astype(int)

# Merge metadata (filtered to Europe & date range by earlier query) with article content
df = pd.merge(df_meta, df_articles, on='article_id', how='left')

# Prepare classification keywords
business_kw = [
    'stock','stocks','market','markets','dollar','economy','economical','economic','business','bank','banks',
    'shares','ipo','investment','investor','oil','oil prices','profit','profits','money','trade','retail','commerce',
    'funds','mutual','financial','finance','company','companies','commercial','reuters -','forbes','wall st','wall street',
    'fed','opec','interest rates','interest rate','trade deficit','inflation'
]
sports_kw = ['match','goal','soccer','football','basketball','baseball','tennis','cricket','rugby','fifa','olympic','season']
sci_kw = ['research','scientists','technology','computer','software','internet','google','ibm','email','e-mail','nuclear','scientific','researchers','tech']

# Lowercase combined text
def classify_text(title, desc):
    text = (' '.join(filter(None, [str(title), str(desc)]))).lower()
    # simple token search
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in sci_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Apply classification
df['category'] = df.apply(lambda r: classify_text(r.get('title',''), r.get('description','')), axis=1)

# Extract year
df['publication_date'] = pd.to_datetime(df['publication_date'], errors='coerce')
df['year'] = df['publication_date'].dt.year

# Focus on years 2010-2020 inclusive
years = list(range(2010, 2021))

counts_by_year = df[df['category']=='Business'].groupby('year').size().to_dict()
# Ensure all years present
counts_complete = {str(y): int(counts_by_year.get(y, 0)) for y in years}

total_business = sum(counts_complete.values())
average_per_year = total_business / len(years) if len(years)>0 else 0.0

result = {
    'counts_by_year': counts_complete,
    'total_business_articles_2010_2020': int(total_business),
    'years_considered': years,
    'average_business_articles_per_year': average_per_year
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VA1uuuIu8nx0F9ZslM0P1GYS': 'file_storage/call_VA1uuuIu8nx0F9ZslM0P1GYS.json', 'var_call_CGCBBhBfzybdf4Zfxhj40TX1': 'file_storage/call_CGCBBhBfzybdf4Zfxhj40TX1.json'}

exec(code, env_args)
