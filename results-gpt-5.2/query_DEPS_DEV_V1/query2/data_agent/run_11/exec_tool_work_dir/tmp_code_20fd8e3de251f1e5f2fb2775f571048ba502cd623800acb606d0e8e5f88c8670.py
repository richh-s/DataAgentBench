code = """import json, pandas as pd, pathlib

def load_records(v):
    if isinstance(v, str):
        p = pathlib.Path(v)
        if p.exists() and p.suffix=='.json':
            with p.open('r', encoding='utf-8') as f:
                return json.load(f)
        return json.loads(v)
    return v

ppv = load_records(var_call_IuAYwMo2wMfOj8TtUKynhrKs)
df_ppv = pd.DataFrame(ppv)
print('__RESULT__:')
print(json.dumps({'columns': df_ppv.columns.tolist(), 'head': df_ppv.head(3).to_dict(orient='records')}))"""

env_args = {'var_call_IuAYwMo2wMfOj8TtUKynhrKs': 'file_storage/call_IuAYwMo2wMfOj8TtUKynhrKs.json', 'var_call_R8wNQRAU5G8Qt5kBBovoIdMC': 'file_storage/call_R8wNQRAU5G8Qt5kBBovoIdMC.json', 'var_call_b9RPK28tm89a5M6HY0n5I7fy': 'file_storage/call_b9RPK28tm89a5M6HY0n5I7fy.json'}

exec(code, env_args)
