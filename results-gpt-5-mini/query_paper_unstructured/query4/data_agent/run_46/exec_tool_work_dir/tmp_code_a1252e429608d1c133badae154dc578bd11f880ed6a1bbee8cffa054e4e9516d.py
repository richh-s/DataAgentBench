code = """import json, re

# Load the second Mongo query result
path = var_call_zQema5txZszizqodvhPu7Oxr
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract titles where document contains 'physical' and 'activity'
candidates = []
for doc in docs:
    filename = doc.get('filename', '')
    text = doc.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    low = text.lower()
    if 'physical' in low and 'activity' in low:
        # attempt to find publication year in header lines - look for patterns like 'CHI 2016' or '2016' near top
        header = text[:1000]
        years = re.findall(r"\b(19[5-9][0-9]|20[0-2][0-9]|2026)\b", header)
        year = int(years[0]) if years else None
        candidates.append({'title': title, 'year': year})

# Deduplicate by title
seen=set(); unique=[]
for c in candidates:
    if c['title'] not in seen:
        unique.append(c); seen.add(c['title'])

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_ueY8ny6tvVKcJ9NNvBSzXQv9': 'file_storage/call_ueY8ny6tvVKcJ9NNvBSzXQv9.json', 'var_call_k4guTGoCsoObrR3VeZLLdU84': [], 'var_call_zQema5txZszizqodvhPu7Oxr': 'file_storage/call_zQema5txZszizqodvhPu7Oxr.json'}

exec(code, env_args)
