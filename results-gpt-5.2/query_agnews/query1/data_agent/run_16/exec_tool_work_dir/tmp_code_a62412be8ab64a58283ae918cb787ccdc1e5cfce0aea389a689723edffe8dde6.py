code = """import json, pandas as pd

path = var_call_GefB5SQGwUvBzQPf6UAQ160r
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

def is_sports(title, desc):
    t = (title or '').lower()
    d = (desc or '').lower()
    text = t + ' ' + d
    sports_keywords = [
        'nba','nfl','mlb','nhl','soccer','football','basketball','baseball','hockey','tennis','golf','olympic','olympics',
        'fifa','uefa','premier league','la liga','serie a','bundesliga','champions league','world cup',
        'coach','coaching','quarterback','touchdown','home run','pitcher','inning','goal','assist','penalty','tournament',
        'match','season','playoff','playoffs','championship','final','semifinal','rankings','athlete','stadium','league',
        'yankees','red sox','lakers','celtics','warriors','cowboys','patriots','giants','packers','manchester','barcelona',
        'real madrid','arsenal','chelsea','liverpool'
    ]
    return any(k in text for k in sports_keywords)

best = None
best_len = -1
for r in data:
    title = r.get('title')
    desc = r.get('description')
    if desc is None:
        continue
    if is_sports(title, desc):
        l = len(desc)
        if l > best_len:
            best_len = l
            best = title

result = {"title": best, "description_length": best_len}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GefB5SQGwUvBzQPf6UAQ160r': 'file_storage/call_GefB5SQGwUvBzQPf6UAQ160r.json'}

exec(code, env_args)
