code = """import json, os
from pathlib import Path

path = var_call_4bSVMiSFwCy5WALrws6x23wZ
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['football','soccer','tennis','basketball','olympics','nfl','nhl','mlb','nba','golf','cricket','baseball','hockey','athletics','racing','motorsport','nascar','fifa','uefa','grand prix','marathon','rugby']

max_len = -1
max_title = None

for doc in data:
    desc = doc.get('description') or ''
    text = (doc.get('title','') + ' ' + desc).lower()
    if any(k in text for k in sports_keywords):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_title = doc.get('title')

result = max_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4bSVMiSFwCy5WALrws6x23wZ': 'file_storage/call_4bSVMiSFwCy5WALrws6x23wZ.json'}

exec(code, env_args)
