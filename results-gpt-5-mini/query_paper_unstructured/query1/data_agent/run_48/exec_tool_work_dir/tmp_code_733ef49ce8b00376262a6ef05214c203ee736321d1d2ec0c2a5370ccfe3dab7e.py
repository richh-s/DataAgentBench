code = """import json
import re

# Load the paper documents result (stored as a JSON file path)
with open(var_call_wxSRpCaUQJYsSzxcqKROq0Kr, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Load the citations result (stored as a JSON file path)
with open(var_call_rVg4KEByAbVgQ0s0CKONhP8M, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Identify papers in the 'food' domain by searching for the word 'food' in the text
food_titles = set()
food_re = re.compile(r"\bfood\b", flags=re.IGNORECASE)
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.rsplit('.txt', 1)[0]
    text = doc.get('text', '') or ''
    if food_re.search(text) or food_re.search(title):
        food_titles.add(title)

# Sum citation_count for all citation records whose title matches a food-domain paper
total_citations = 0
for rec in citations:
    rec_title = rec.get('title')
    try:
        cc = int(rec.get('citation_count', 0))
    except:
        # handle non-int by converting if possible
        try:
            cc = int(float(rec.get('citation_count', 0)))
        except:
            cc = 0
    if rec_title in food_titles:
        total_citations += cc

import json
print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_call_djzbDlRjiV19N5YcxI0hNWCQ': ['paper_docs'], 'var_call_wxSRpCaUQJYsSzxcqKROq0Kr': 'file_storage/call_wxSRpCaUQJYsSzxcqKROq0Kr.json', 'var_call_rVg4KEByAbVgQ0s0CKONhP8M': 'file_storage/call_rVg4KEByAbVgQ0s0CKONhP8M.json'}

exec(code, env_args)
