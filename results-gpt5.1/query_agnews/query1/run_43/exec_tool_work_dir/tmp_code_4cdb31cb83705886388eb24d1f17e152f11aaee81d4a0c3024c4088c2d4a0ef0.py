code = """import json, pandas as pd
from pathlib import Path

path = var_call_rGncF69I04fmwgOVJqzcZJUQ
with open(path, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
# simple sports classifier
sports_keywords = ['football','soccer','nba','nfl','mlb','nhl','olympic','tennis','golf','cricket','baseball','basketball','hockey','athletics','racing','grand prix','fifa','uefa','olympics','world cup','rugby','motorsport','motogp']

text = (df['title'].fillna('') + ' ' + df['description'].fillna('')).str.lower()

is_sports = text.apply(lambda t: any(k in t for k in sports_keywords))

sports_df = df[is_sports].copy()

sports_df['desc_len'] = sports_df['description'].fillna('').str.len()

idx = sports_df['desc_len'].idxmax()

title = None if pd.isna(idx) else sports_df.loc[idx, 'title']

result = json.dumps(title)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_rGncF69I04fmwgOVJqzcZJUQ': 'file_storage/call_rGncF69I04fmwgOVJqzcZJUQ.json'}

exec(code, env_args)
