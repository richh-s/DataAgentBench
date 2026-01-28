code = """import json
import pandas as pd
# file paths from previous tool results
meta_path = var_call_2rQ9dGfrtFxHN8lzY23MYLjM
biz_path = var_call_PNlUxUjTdWCn1JUKhdhWRawg
# load
with open(meta_path, 'r') as f:
    meta = json.load(f)
with open(biz_path, 'r') as f:
    biz = json.load(f)
# DataFrames
df_meta = pd.DataFrame(meta)
df_biz = pd.DataFrame(biz)
# ensure article_id int
df_meta['article_id'] = df_meta['article_id'].astype(int)
df_biz['article_id'] = df_biz['article_id'].astype(int)
# extract year
df_meta['year'] = pd.to_datetime(df_meta['publication_date']).dt.year
# filter years 2010-2020
df_meta = df_meta[(df_meta['year'] >= 2010) & (df_meta['year'] <= 2020)]
# merge to get business articles in Europe
df_merged = pd.merge(df_meta, df_biz[['article_id','title','description']], on='article_id', how='inner')
# count per year
years = list(range(2010,2021))
counts = {str(y): int(df_merged[df_merged['year']==y].shape[0]) for y in years}
total = sum(counts.values())
avg = total / len(years) if len(years)>0 else 0
# prepare result
result = {"year_counts": counts, "total_business_articles": int(total), "average_per_year": avg}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_YqinKIOyfwVYtDOpsyk3NNHW': ['articles'], 'var_call_e07lyV9DBwFNuOU5bvSqKSUM': ['authors', 'article_metadata'], 'var_call_2rQ9dGfrtFxHN8lzY23MYLjM': 'file_storage/call_2rQ9dGfrtFxHN8lzY23MYLjM.json', 'var_call_4xCvV4636mjDMlS8xaYZRLGY': 'file_storage/call_4xCvV4636mjDMlS8xaYZRLGY.json', 'var_call_PNlUxUjTdWCn1JUKhdhWRawg': 'file_storage/call_PNlUxUjTdWCn1JUKhdhWRawg.json'}

exec(code, env_args)
