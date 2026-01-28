code = """import json, os
import pandas as pd

# Load full results from files
with open(var_call_0N2UENKk8v33ZJH5bFXftHAV, 'r') as f:
    papers = json.load(f)
with open(var_call_zlhh4uPHs57hXIQj2Q72o8Fe, 'r') as f:
    citations = json.load(f)

# Extract titles (filenames without .txt) for papers whose text suggests food domain
food_titles = []
for doc in papers:
    fname = doc.get('filename', '')
    title = os.path.splitext(fname)[0]
    text = (doc.get('text') or '').lower()
    if ' food ' in text or 'foods ' in text or ' food.' in text or 'diet' in text or 'dietary' in text or 'eating' in text or 'meal' in text or 'calorie' in text:
        food_titles.append(title)

food_titles = sorted(set(food_titles))

# Sum citation_count for citations whose title matches any of the food_titles
food_set = set(food_titles)

total_citations = 0
for row in citations:
    title = row.get('title')
    if title in food_set:
        try:
            c = int(row.get('citation_count') or 0)
        except ValueError:
            c = 0
        total_citations += c

result = {"food_titles": food_titles, "total_citations": total_citations}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_0N2UENKk8v33ZJH5bFXftHAV': 'file_storage/call_0N2UENKk8v33ZJH5bFXftHAV.json', 'var_call_zlhh4uPHs57hXIQj2Q72o8Fe': 'file_storage/call_zlhh4uPHs57hXIQj2Q72o8Fe.json'}

exec(code, env_args)
