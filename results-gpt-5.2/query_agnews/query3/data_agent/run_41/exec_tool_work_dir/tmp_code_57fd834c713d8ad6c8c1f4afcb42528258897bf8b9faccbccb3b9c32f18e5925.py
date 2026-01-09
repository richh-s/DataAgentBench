code = """import json, pandas as pd

# load europe metadata
def load_records(var):
    if isinstance(var, str):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

europe = load_records(var_call_HHPUQfayRdEHuu0N84x6TaC5)
arts = load_records(var_call_Ay9oyGAj9QKD2FATjxBcrwK1)

df_eu = pd.DataFrame(europe)
df_a = pd.DataFrame(arts)

# normalize ids
df_eu['article_id'] = df_eu['article_id'].astype(int)
df_a['article_id'] = df_a['article_id'].astype(int)

# merge only needed articles (Europe, 2010-2020)
df = df_eu.merge(df_a, on='article_id', how='inner')

# simple keyword-based classifier for Business
business_kw = [
    'stock','stocks','market','markets','wall st','wall street','ipo','shares','profit','profits','earnings','revenue',
    'economy','economic','trade','deficit','inflation','interest rate','interest rates','fed','central bank','bank',
    'currency','dollar','euro','oil','prices','price','opec','gdp','unemployment','jobs','investment','fund',
    'merger','acquisition','takeover','company','companies','corporate','ceo','industry','financial','finance'
]

def is_business(row):
    text = ((row.get('title') or '') + ' ' + (row.get('description') or '')).lower()
    return any(k in text for k in business_kw)

df['is_business'] = df.apply(is_business, axis=1)
df['year'] = pd.to_datetime(df['publication_date'], errors='coerce').dt.year

df_b = df[(df['is_business']) & (df['year'].between(2010, 2020))]
counts = df_b.groupby('year').size().reindex(range(2010, 2021), fill_value=0)
avg_per_year = counts.mean()

result = {
    'average_business_articles_per_year_europe_2010_2020': float(avg_per_year),
    'total_business_articles': int(counts.sum()),
    'years': {int(y): int(c) for y, c in counts.items()}
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_HHPUQfayRdEHuu0N84x6TaC5': 'file_storage/call_HHPUQfayRdEHuu0N84x6TaC5.json', 'var_call_Ay9oyGAj9QKD2FATjxBcrwK1': 'file_storage/call_Ay9oyGAj9QKD2FATjxBcrwK1.json'}

exec(code, env_args)
