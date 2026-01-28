code = """import json
import pandas as pd

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

civic = load_json_maybe(var_call_m8KW4MH9F5nis5niXr2Mi9vs)
fund = load_json_maybe(var_call_CxA5tpajKgwluNJXiRKdE6oX)

fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)

all_text = "\n".join([d.get('text','') for d in civic]).lower()
projects = fund_df['Project_Name'].dropna().astype(str).unique().tolist()

started_set = []
for name in projects:
    n = name.lower()
    if n in all_text:
        idx = all_text.find(n)
        window = all_text[idx: min(len(all_text), idx+2000)]
        if ('spring 2022' in window or '2022-spring' in window or '2022 spring' in window) and (
            'begin' in window or 'start' in window or 'st:' in window or 'begin construction' in window
        ):
            started_set.append(name)

started_set = sorted(set(started_set))
count = len(started_set)

total_funding = int(fund_df[fund_df['Project_Name'].isin(started_set)]['Total_Amount'].sum())

result = {"projects_started_spring_2022_count": count, "total_funding": total_funding, "projects": started_set}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_V2Tw7OZKiywIzEtht4cyQkEK': ['Funding'], 'var_call_m8KW4MH9F5nis5niXr2Mi9vs': 'file_storage/call_m8KW4MH9F5nis5niXr2Mi9vs.json', 'var_call_CxA5tpajKgwluNJXiRKdE6oX': 'file_storage/call_CxA5tpajKgwluNJXiRKdE6oX.json'}

exec(code, env_args)
