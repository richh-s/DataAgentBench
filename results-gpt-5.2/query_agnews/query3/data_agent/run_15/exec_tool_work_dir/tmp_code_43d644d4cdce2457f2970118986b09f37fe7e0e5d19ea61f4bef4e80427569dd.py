code = """import json, pandas as pd

meta_path = var_call_2tIK251wfdzAZOVjKA1gemyS
art_path = var_call_zPfOdCOoN3JJu0LeERyfO3pR

with open(meta_path, 'r', encoding='utf-8') as f:
    meta = json.load(f)
with open(art_path, 'r', encoding='utf-8') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# normalize ids
def to_int_series(s):
    return pd.to_numeric(s, errors='coerce').astype('Int64')

meta_df['article_id'] = to_int_series(meta_df['article_id'])
arts_df['article_id'] = to_int_series(arts_df['article_id'])

# join
j = meta_df.merge(arts_df, on='article_id', how='inner')

# classify business using keyword heuristics
text = (j['title'].fillna('') + ' ' + j['description'].fillna('')).str.lower()

biz_kw = [
    'stock','stocks','shares','market','wall st','dow','nasdaq','s&p','ipo','earnings','profit','profits','revenue',
    'economy','economic','gdp','inflation','deficit','trade','bank','banks','fed','central bank','interest rate',
    'currency','dollar','euro','yen','oil','crude','opec','gold','bond','bonds','imf','mortgage','housing',
    'company','companies','business','merger','acquisition','takeover','invest','investment','fund','funds'
]
pattern = '|'.join([pd.re.escape(k) for k in biz_kw])
# pandas doesn't have re.escape; use python re
import re
pattern = '|'.join([re.escape(k) for k in biz_kw])

is_business = text.str.contains(pattern, regex=True)

biz = j[is_business].copy()

# year counts
biz['year'] = pd.to_datetime(biz['publication_date'], errors='coerce').dt.year
biz = biz[(biz['year']>=2010) & (biz['year']<=2020)]
counts = biz.groupby('year').size().reindex(range(2010,2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles_2010_2020': int(counts.sum()),
    'years': 11
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_2tIK251wfdzAZOVjKA1gemyS': 'file_storage/call_2tIK251wfdzAZOVjKA1gemyS.json', 'var_call_zPfOdCOoN3JJu0LeERyfO3pR': 'file_storage/call_zPfOdCOoN3JJu0LeERyfO3pR.json'}

exec(code, env_args)
