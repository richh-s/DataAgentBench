code = """import json
# For debugging, print counts of food_titles and sample titles
with open(var_call_wxSRpCaUQJYsSzxcqKROq0Kr, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

food_titles = []
import re
food_re = re.compile(r"\bfood\b", flags=re.IGNORECASE)
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    text = doc.get('text', '') or ''
    if food_re.search(text) or food_re.search(title):
        food_titles.append(title)

print("__RESULT__:")
print(json.dumps({'num_food_titles': len(food_titles), 'sample_food_titles': food_titles[:20]}))"""

env_args = {'var_call_djzbDlRjiV19N5YcxI0hNWCQ': ['paper_docs'], 'var_call_wxSRpCaUQJYsSzxcqKROq0Kr': 'file_storage/call_wxSRpCaUQJYsSzxcqKROq0Kr.json', 'var_call_rVg4KEByAbVgQ0s0CKONhP8M': 'file_storage/call_rVg4KEByAbVgQ0s0CKONhP8M.json', 'var_call_aLuTZrkvdGa4fE3rOhw30iAQ': 0}

exec(code, env_args)
