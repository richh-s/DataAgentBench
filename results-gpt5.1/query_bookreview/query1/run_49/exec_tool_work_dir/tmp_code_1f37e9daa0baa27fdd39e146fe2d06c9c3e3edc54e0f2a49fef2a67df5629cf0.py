code = """import json, re, pandas as pd

with open(var_call_bSPqq6wJ4Cavp1Y3brdNCRhh, 'r') as f:
    books = json.load(f)

reviews = var_call_gb2F2vsaEGOWSWXzLtRvzPrv

# reviews is already a list of dicts with keys 'purchase_id' and 'rating'
rev_df = pd.DataFrame(reviews)
print('__RESULT__:')
print(json.dumps({'cols': list(rev_df.columns), 'sample': rev_df.head(5).to_dict(orient='records')}))"""

env_args = {'var_call_bSPqq6wJ4Cavp1Y3brdNCRhh': 'file_storage/call_bSPqq6wJ4Cavp1Y3brdNCRhh.json', 'var_call_VqPFUDO7mxMhfHDB3mtnrEZR': ['books_info'], 'var_call_fnlaCJJsfM9DgceTkvaytbNx': ['review'], 'var_call_gb2F2vsaEGOWSWXzLtRvzPrv': 'file_storage/call_gb2F2vsaEGOWSWXzLtRvzPrv.json'}

exec(code, env_args)
