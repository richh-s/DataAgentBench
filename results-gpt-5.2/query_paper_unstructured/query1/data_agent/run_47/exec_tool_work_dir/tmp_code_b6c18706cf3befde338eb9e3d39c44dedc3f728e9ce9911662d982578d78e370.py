code = """import json, re
import pandas as pd

# load filenames list
path = var_call_SJofI3R6txRWDXqcqqA60Rmg
with open(path,'r',encoding='utf-8') as f:
    all_files = json.load(f)
all_titles = [r['filename'].removesuffix('.txt') for r in all_files]

# load subset of docs containing 'food'
path2 = var_call_3rlZ2uHOjJikEh9F4DD8CcLJ
with open(path2,'r',encoding='utf-8') as f:
    food_docs = json.load(f)

# heuristic: title is food-domain if filename suggests food OR text has food journaling/dietary etc in first 5k chars
food_title_set = set()
food_keywords = re.compile(r"\b(food|diet|dietary|nutrition|eating|meal|calorie|myfitnesspal|food journal|journaling)\b", re.I)
for d in food_docs:
    title = d.get('filename','').removesuffix('.txt')
    if not title:
        continue
    t = title.lower()
    if any(k in t for k in ['food','diet','nutrition','eating','meal','calorie','myfitnesspal']):
        food_title_set.add(title)
        continue
    txt = (d.get('text') or '')[:5000]
    if food_keywords.search(txt):
        # require multiple hits to reduce false positives
        hits = len(food_keywords.findall(txt))
        if hits >= 3:
            food_title_set.add(title)

result = {
    'food_titles': sorted(food_title_set),
    'food_title_count': len(food_title_set)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_fqyLmqBXi1eSvfzW9Tgq6WNT': ['paper_docs'], 'var_call_OzlqLOMLE4S4spqANwtp7aV3': ['Citations', 'sqlite_sequence'], 'var_call_SJofI3R6txRWDXqcqqA60Rmg': 'file_storage/call_SJofI3R6txRWDXqcqqA60Rmg.json', 'var_call_cLV5oXj5Kzm9iBgbWs7AjebG': [], 'var_call_3rlZ2uHOjJikEh9F4DD8CcLJ': 'file_storage/call_3rlZ2uHOjJikEh9F4DD8CcLJ.json'}

exec(code, env_args)
