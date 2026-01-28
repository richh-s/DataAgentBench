code = """import json
import pandas as pd

articles_data = var_functions.query_db:0
metadata_data = var_functions.query_db:2

if type(articles_data) is str and '.json' in articles_data:
    articles_raw = open(articles_data, 'r').read()
    articles_list = json.loads(articles_raw)
else:
    articles_list = articles_data

if type(metadata_data) is str and '.json' in metadata_data:
    metadata_raw = open(metadata_data, 'r').read()
    metadata_list = json.loads(metadata_raw)
else:
    metadata_list = metadata_data

df_art = pd.DataFrame(articles_list)
df_meta = pd.DataFrame(metadata_list)

df_art['article_id'] = df_art['article_id'].astype(str)
df_meta['article_id'] = df_meta['article_id'].astype(str)

df = pd.merge(df_art, df_meta, on='article_id', how='inner')

biz_words = ['business', 'economy', 'stock', 'stocks', 'wall st', 'wall street', 'company', 'companies', 'corporate', 'investment', 'investing', 'market', 'markets', 'trade', 'trading', 'finance', 'financial', 'profit', 'revenue', 'sales', 'oil', 'energy', 'bank', 'banking', 'job', 'jobs', 'dollar', 'euro']

def check_biz(title, desc):
    t = (str(title) + ' ' + str(desc)).lower()
    return any(w in t for w in biz_words)

df['biz'] = df.apply(lambda x: check_biz(x['title'], x['description']), axis=1)

df_biz = df[df['biz'] == True].copy()
df_biz['year'] = pd.to_datetime(df_biz['publication_date']).dt.year
df_biz = df_biz[(df_biz['year'] >= 2010) & (df_biz['year'] <= 2020)]

year_counts = df_biz.groupby('year').size().reset_index(name='count')
avg = year_counts['count'].mean() if len(year_counts) > 0 else 0

result = {
    'average_business_articles_per_year': round(float(avg), 2),
    'total_business_articles': int(year_counts['count'].sum()) if len(year_counts) > 0 else 0,
    'years_covered': len(year_counts)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
