code = """import json, pandas as pd

# load reviews (large)
path = var_call_9RofuNWl3PIy2JtrLJbA0HEz
with open(path, 'r') as f:
    reviews = json.load(f)

df_rev = pd.DataFrame(reviews)
df_rev['rating'] = pd.to_numeric(df_rev['rating'], errors='coerce')

# businesses filtered to massage therapy-related via description heuristic
biz = pd.DataFrame(var_call_Dgb4IxkGF794V7b6JtQdRP0V)

avg = df_rev.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
res = biz.merge(avg, on='gmap_id', how='left')
res = res[res['avg_rating'].notna() & (res['avg_rating']>=4.0)][['name','avg_rating']]
res = res.sort_values(['avg_rating','name'], ascending=[False, True])
res['avg_rating'] = res['avg_rating'].round(3)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_60FiJNo10KBAAt21D3ah1mGp': [], 'var_call_9RofuNWl3PIy2JtrLJbA0HEz': 'file_storage/call_9RofuNWl3PIy2JtrLJbA0HEz.json', 'var_call_wxfUeP9JGuIgPDtIrc7izMQM': [], 'var_call_Dgb4IxkGF794V7b6JtQdRP0V': [{'gmap_id': 'gmap_22', 'name': 'Angel-A Massage', 'description': ' Experience relaxation and rejuvenation at this wellness retreat in Fair Oaks, CA 95628, where skilled therapists offer soothing treatments designed to relieve stress and promote overall well-being.'}, {'gmap_id': 'gmap_24', 'name': 'SUSY massage', 'description': ' Offering a range of therapeutic bodywork services, this wellness center in Carmichael, CA 95608 helps clients relax and rejuvenate for overall well-being.'}, {'gmap_id': 'gmap_32', 'name': 'J B Oriental Inc', 'description': ' Experience rejuvenating therapies and soothing body treatments designed to enhance relaxation and well-being in Roseville, CA 95747.'}]}

exec(code, env_args)
