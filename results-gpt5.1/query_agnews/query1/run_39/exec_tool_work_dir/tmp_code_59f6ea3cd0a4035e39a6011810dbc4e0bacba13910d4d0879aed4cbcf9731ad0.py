code = """import json, pandas as pd

path = var_call_KujKv8UPnBLXxP19P0PGuLVL
with open(path, 'r') as f:
    data = json.load(f)

sports_keywords = ['game','games','team','teams','season','score','scored','scoring','win','wins','won','lost','loss','coach','player','players','league','cup','tournament','match','matches','goal','goals','basketball','baseball','football','soccer','tennis','golf','olympic','olympics','nfl','nba','nhl','mlb']

max_len = -1
best_title = None
for art in data:
    desc = art.get('description') or ''
    title = art.get('title') or ''
    text = (title + ' ' + desc).lower()
    if any(k in text for k in sports_keywords):
        l = len(desc)
        if l > max_len:
            max_len = l
            best_title = title

result = best_title

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KujKv8UPnBLXxP19P0PGuLVL': 'file_storage/call_KujKv8UPnBLXxP19P0PGuLVL.json'}

exec(code, env_args)
