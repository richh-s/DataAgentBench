code = """import json, pandas as pd

with open(var_call_szvJ2OMgXUzg7zpZ2jLIP3vY, 'r') as f:
    meta = json.load(f)
with open(var_call_yhGMibaPrd4ZrdhnjvAFGqZP, 'r') as f:
    arts = json.load(f)

meta_df = pd.DataFrame(meta)
arts_df = pd.DataFrame(arts)

meta_df['article_id'] = meta_df['article_id'].astype(int)
arts_df['article_id'] = arts_df['article_id'].astype(int)

business_keywords = ['stock','stocks','market','markets','trade','trading','ipo','merger','acquisition','profit','profits','losses','revenue','sales','economy','economic','business','company','companies','shares','oil','price','prices','fund','funds','bank','banks','investment','investors','bond','bonds','currency','currencies','finance','financial','loan','loans','deal','deals','earnings']

bk = set(business_keywords)

def is_business(title, desc):
    text = (str(title) + ' ' + str(desc)).lower()
    tokens = []
    for t in text.split():
        tokens.append(t.strip(".,!?:;()[]{}\"'`"))
    return any(tok in bk for tok in tokens)

arts_df['is_business'] = arts_df.apply(lambda r: is_business(r.get('title',''), r.get('description','')), axis=1)

merged = meta_df.merge(arts_df[['article_id','is_business']], on='article_id', how='left')

biz = merged[merged['is_business']]

biz['year'] = biz['publication_date'].str.slice(0,4).astype(int)

counts = biz.groupby('year')['article_id'].nunique().reindex(range(2010,2021), fill_value=0)

avg_per_year = float(counts.mean())

result = json.dumps({'average_business_articles_per_year_europe_2010_2020': avg_per_year, 'counts_by_year': {str(k): int(v) for k,v in counts.to_dict().items()}})

print("__RESULT__:")
print(result)"""

env_args = {'var_call_szvJ2OMgXUzg7zpZ2jLIP3vY': 'file_storage/call_szvJ2OMgXUzg7zpZ2jLIP3vY.json', 'var_call_yhGMibaPrd4ZrdhnjvAFGqZP': 'file_storage/call_yhGMibaPrd4ZrdhnjvAFGqZP.json'}

exec(code, env_args)
