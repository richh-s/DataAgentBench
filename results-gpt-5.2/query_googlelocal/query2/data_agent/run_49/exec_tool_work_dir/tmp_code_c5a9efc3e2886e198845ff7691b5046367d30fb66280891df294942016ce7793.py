code = """import json, pandas as pd

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str):
        with open(maybe_path_or_list, 'r') as f:
            return json.load(f)
    return maybe_path_or_list

reviews = load_records(var_call_2KHuMQWfJ8kzobnDcLb696UX)

rdf = pd.DataFrame(reviews)
rdf['rating'] = pd.to_numeric(rdf['rating'], errors='coerce')
avg = rdf.groupby('gmap_id', as_index=False)['rating'].mean().rename(columns={'rating':'avg_rating'})
avg = avg[avg['avg_rating'] >= 4.0]

print('__RESULT__:')
print(avg.sort_values(['avg_rating','gmap_id'], ascending=[False, True]).to_json(orient='records'))"""

env_args = {'var_call_ZV98RAEAkWXKV0Va4Pkgat7b': [], 'var_call_2KHuMQWfJ8kzobnDcLb696UX': 'file_storage/call_2KHuMQWfJ8kzobnDcLb696UX.json', 'var_call_N9iho3YJpTSSnxaMKIyHwOn6': []}

exec(code, env_args)
