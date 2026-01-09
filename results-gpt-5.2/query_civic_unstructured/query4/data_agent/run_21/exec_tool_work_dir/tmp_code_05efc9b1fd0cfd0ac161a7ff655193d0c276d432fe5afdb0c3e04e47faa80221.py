code = """import json, re
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

texts = [d.get('text','') for d in civic]
all_text = "\n".join(texts)

projects = fund_df['Project_Name'].dropna().astype(str).unique().tolist()

# Spring 2022 start detection: look for project name near a line containing start/begin and 'Spring 2022' or '2022 Spring'
spring_pat = re.compile(r"(?i)\b(?:project schedule|schedule|estimated schedule|timeline|start|begin(?:\s+construction)?|st\b)\b[^\n]{0,120}(?:spring\s*2022|2022\s*[- ]\s*spring)")

started_spring_2022 = []
for name in projects:
    # find occurrences of project name and check window after it for spring 2022 start indicators
    # use escaped name, allow flexible spaces/&
    name_pat = re.escape(name)
    for m in re.finditer(name_pat, all_text, flags=re.IGNORECASE):
        window = all_text[m.start(): min(len(all_text), m.start()+1500)]
        if spring_pat.search(window):
            started_spring_2022.append(name)
            break

started_set = sorted(set(started_spring_2022))
count = len(started_set)

total_funding = int(fund_df[fund_df['Project_Name'].isin(started_set)]['Total_Amount'].sum())

result = {"projects_started_spring_2022_count": count, "total_funding": total_funding, "projects": started_set}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_V2Tw7OZKiywIzEtht4cyQkEK': ['Funding'], 'var_call_m8KW4MH9F5nis5niXr2Mi9vs': 'file_storage/call_m8KW4MH9F5nis5niXr2Mi9vs.json', 'var_call_CxA5tpajKgwluNJXiRKdE6oX': 'file_storage/call_CxA5tpajKgwluNJXiRKdE6oX.json'}

exec(code, env_args)
