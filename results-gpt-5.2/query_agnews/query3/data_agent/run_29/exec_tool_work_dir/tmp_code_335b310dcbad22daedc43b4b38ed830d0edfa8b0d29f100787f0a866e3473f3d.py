code = """import json, pandas as pd

# Load metadata (Europe, 2010-2020)
meta_src = var_call_NcfJxWcdQXW4TjvEfptxU4jd
if isinstance(meta_src, str):
    with open(meta_src, 'r') as f:
        meta = json.load(f)
else:
    meta = meta_src

art_src = var_call_Hmph8e4ZDVytShlj7EdEEckd
if isinstance(art_src, str):
    with open(art_src, 'r') as f:
        arts = json.load(f)
else:
    arts = art_src

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

# Normalize types
meta_df['article_id'] = meta_df['article_id'].astype(int)
meta_df['publication_date'] = pd.to_datetime(meta_df['publication_date'], errors='coerce')
meta_df = meta_df.dropna(subset=['publication_date'])
meta_df['year'] = meta_df['publication_date'].dt.year

arts_df['article_id'] = arts_df['article_id'].astype(int)
arts_df['title'] = arts_df['title'].fillna('')
arts_df['description'] = arts_df['description'].fillna('')
arts_df['text'] = (arts_df['title'] + ' ' + arts_df['description']).str.lower()

# Simple keyword-based business classifier
biz_kw = [
    'stock','stocks','wall st','wall street','nasdaq','dow','s&p','index','shares','share','equity','bond','bonds',
    'ipo','earnings','profit','revenue','quarter','q1','q2','q3','q4','forecast','guidance','dividend',
    'economy','economic','gdp','inflation','deficit','trade','export','imports','unemployment','jobless',
    'bank','banks','banking','central bank','fed','ecb','interest rate','rates','loan','credit',
    'oil','crude','opec','barrel','gas','energy','market','markets','currency','dollar','euro','yen','pound',
    'company','companies','firm','investment','investor','merger','acquisition','takeover','stake','fund','funds',
    'retail','sales','sector','industry','manufacturing','startup','aerospace','commercial'
]

def is_business(text: str) -> bool:
    for kw in biz_kw:
        if kw in text:
            return True
    return False

arts_df['is_business'] = arts_df['text'].map(is_business)

# Join Europe subset to articles, filter business
joined = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='inner')
biz = joined[joined['is_business']]

# Count per year 2010-2020 inclusive, include years with zero
years = list(range(2010, 2021))
counts = biz.groupby('year').size().reindex(years, fill_value=0)
avg_per_year = counts.mean()

out = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'counts_by_year': {str(int(y)): int(c) for y,c in counts.items()},
    'total_business_articles': int(counts.sum()),
    'years': years
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_NcfJxWcdQXW4TjvEfptxU4jd': 'file_storage/call_NcfJxWcdQXW4TjvEfptxU4jd.json', 'var_call_Hmph8e4ZDVytShlj7EdEEckd': 'file_storage/call_Hmph8e4ZDVytShlj7EdEEckd.json'}

exec(code, env_args)
