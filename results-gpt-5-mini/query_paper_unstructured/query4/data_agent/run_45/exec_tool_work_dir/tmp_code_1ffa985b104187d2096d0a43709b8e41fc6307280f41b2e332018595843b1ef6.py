code = """import json, re
path = var_call_YsLRlcU3h7irQLHPdx5tyH09
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

out = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    has_physical = bool(re.search(r'physical', text, re.IGNORECASE))
    has_activity = bool(re.search(r'activity', text, re.IGNORECASE))
    yrs = re.findall(r"\b(19|20)\d{2}\b", text)
    # The regex finds first two digits; to get full years, find full 4-digit
    yrs_full = re.findall(r"\b(19|20)\d{2}\b", text)
    # better find 4-digit years
    yrs4 = re.findall(r"\b(20\d{2}|19\d{2})\b", text)
    out.append({'title': title, 'has_physical': has_physical, 'has_activity': has_activity, 'years_found': yrs4[:5]})

# filter those that have both physical and activity
filtered = [o for o in out if o['has_physical'] and o['has_activity']]
print("__RESULT__:")
import json
print(json.dumps({'total_docs_returned': len(docs), 'filtered_count': len(filtered), 'examples': filtered[:30]}))"""

env_args = {'var_call_H8MR8XiAJQcwfwjUzIUnvAZp': ['paper_docs'], 'var_call_abt9r2WlD9FlUNBcOscHzbCD': ['Citations', 'sqlite_sequence'], 'var_call_w2Nv7UgCjiHN6I6HYUjZ4I6P': 'file_storage/call_w2Nv7UgCjiHN6I6HYUjZ4I6P.json', 'var_call_riAVJQvz9VqLp676ohi9NTRg': {'titles': [], 'count': 0}, 'var_call_YsLRlcU3h7irQLHPdx5tyH09': 'file_storage/call_YsLRlcU3h7irQLHPdx5tyH09.json'}

exec(code, env_args)
