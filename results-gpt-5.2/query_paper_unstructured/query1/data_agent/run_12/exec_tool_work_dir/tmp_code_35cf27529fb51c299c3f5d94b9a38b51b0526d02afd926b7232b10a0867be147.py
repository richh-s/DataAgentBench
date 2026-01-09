code = """import json, re
import pandas as pd

docs_path = var_call_aWFXXbvt8ZG9DZdeo3pg48h1
if isinstance(docs_path, str) and docs_path.endswith('.json'):
    with open(docs_path, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_path

# Heuristic: mark as food domain if text contains a standalone domain token 'food' in a domains list section,
# OR if it contains many occurrences of 'food' in keywords/abstract, but to follow hint use contains matching.
# We'll primarily use an explicit metadata pattern 'Domain' 'Domains' 'domain' anywhere, allowing lists.
meta_pat = re.compile(r'\bdomains?\b\s*[:\-]\s*([^\n\r]+)', re.IGNORECASE)
food_titles=set()
for d in docs:
    text = d.get('text','') or ''
    found=False
    for m in meta_pat.finditer(text[:5000]):
        if 'food' in m.group(1).lower():
            found=True
            break
    if not found:
        # fallback: keyword line
        km = re.search(r'\bkeywords?\b\s*[:\-]\s*([^\n\r]+)', text[:5000], re.IGNORECASE)
        if km and 'food' in km.group(1).lower():
            found=True
    if not found:
        # final fallback: phrase 'food journaling' or 'food tracking' in first 5000 chars
        head=text[:5000].lower()
        if ('food journaling' in head) or ('food journal' in head) or ('food tracking' in head) or ('dietary' in head):
            found=True
    if found:
        fn=d.get('filename','') or ''
        title = fn[:-4] if fn.lower().endswith('.txt') else fn
        food_titles.add(title)

print('__RESULT__:')
print(json.dumps({"num_food_titles": len(food_titles), "sample": sorted(list(food_titles))[:20]}))"""

env_args = {'var_call_7CSMavulR5EYTbE2xp0EXyDs': 'file_storage/call_7CSMavulR5EYTbE2xp0EXyDs.json', 'var_call_aWFXXbvt8ZG9DZdeo3pg48h1': 'file_storage/call_aWFXXbvt8ZG9DZdeo3pg48h1.json', 'var_call_rnGisujxXWUhOsQF0cUgpe0v': {'total_citation_count_food_domain': 0, 'num_food_papers_matched': 0, 'num_food_papers_in_docs': 0}}

exec(code, env_args)
