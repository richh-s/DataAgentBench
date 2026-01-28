code = """import json, pandas as pd

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

cit_recs = load_maybe_path(var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S)
df=pd.DataFrame(cit_recs)
print('__RESULT__:')
print(json.dumps({'columns': list(df.columns), 'head': df.head(3).to_dict(orient='records')}, ensure_ascii=False))"""

env_args = {'var_call_8AQzsnVK3pjf8qv96fVixUDd': 'file_storage/call_8AQzsnVK3pjf8qv96fVixUDd.json', 'var_call_Gcy9OwZ4BPgbXR3BKg8KmU3S': 'file_storage/call_Gcy9OwZ4BPgbXR3BKg8KmU3S.json', 'var_call_CuwislDkhq3PJKeBDgFmstlY': [], 'var_call_sTOTPpLvdzZRAbkte2NRypwi': 'file_storage/call_sTOTPpLvdzZRAbkte2NRypwi.json', 'var_call_53iSUuuy40M0TesDhNqEkEr4': [{'cid': '0', 'name': 'id', 'type': 'INTEGER', 'notnull': '0', 'dflt_value': 'None', 'pk': '1'}, {'cid': '1', 'name': 'title', 'type': 'TEXT', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '2', 'name': 'citation_count', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}, {'cid': '3', 'name': 'citation_year', 'type': 'INTEGER', 'notnull': '1', 'dflt_value': 'None', 'pk': '0'}]}

exec(code, env_args)
