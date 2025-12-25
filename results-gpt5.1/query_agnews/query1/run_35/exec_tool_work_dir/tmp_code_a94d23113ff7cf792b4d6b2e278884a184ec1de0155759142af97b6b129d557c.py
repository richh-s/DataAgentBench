code = """import json
import pandas as pd

path = var_call_dMS6cq3QPt0BXjEmkKPSHttm
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)

sports_keywords = ['game','games','team','teams','win','wins','won','victory','defeat','season','tournament','league','cup','championship','football','soccer','basketball','baseball','tennis','golf','hockey','olympics','athletics','coach','player','players','score','scored','scoring','match']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

is_sports = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[is_sports].copy()

sports_df['desc_len'] = sports_df['description'].fillna('').str.len()

idx = sports_df['desc_len'].idxmax()

title_with_longest_desc = sports_df.loc[idx, 'title'] if pd.notna(idx) else None

result = json.dumps(title_with_longest_desc)

print("__RESULT__:")
print(result)"""

env_args = {'var_call_dMS6cq3QPt0BXjEmkKPSHttm': 'file_storage/call_dMS6cq3QPt0BXjEmkKPSHttm.json'}

exec(code, env_args)
