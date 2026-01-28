code = """import re, json, pandas as pd

# Load full paper_docs result
with open(var_call_1h4LE8DEnYNNspVQzmSd25aO, 'r') as f:
    papers = json.load(f)

# Identify food-domain papers by searching for 'food' or related phrases in context
food_titles = set()
for doc in papers:
    text = doc.get('text', '').lower()
    # simple heuristic: mention of food tracking/eating/diet
    if ' food ' in text or 'food journal' in text or 'tracking food' in text or 'diet ' in text:
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        food_titles.add(title)

# Load citations
with open(var_call_9R5Xl13EoLVEeTifPdsZvNM9, 'r') as f:
    cits = json.load(f)

# Sum citation counts for titles in food_titles

total_citations = 0
for row in cits:
    title = row.get('title', '')
    if title in food_titles:
        try:
            total_citations += int(row.get('citation_count', 0))
        except ValueError:
            continue

result = json.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_1h4LE8DEnYNNspVQzmSd25aO': 'file_storage/call_1h4LE8DEnYNNspVQzmSd25aO.json', 'var_call_9R5Xl13EoLVEeTifPdsZvNM9': 'file_storage/call_9R5Xl13EoLVEeTifPdsZvNM9.json'}

exec(code, env_args)
