code = """import json, re
# var_call_CGhz2TCzvXvH0HGqonLb9qg7 is a file path to the Mongo query result JSON
path = var_call_CGhz2TCzvXvH0HGqonLb9qg7
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

results = []
year_re = re.compile(r"\b(2017|2018|2019|2020|2021|2022|2023|2024|2025|2026)\b")
for doc in data:
    text = doc.get('text','')
    filename = doc.get('filename','')
    if not filename.endswith('.txt'):
        title = filename
    else:
        title = filename[:-4]
    # ensure 'empirical' appears in text
    if re.search(r'(?i)empirical', text):
        m = year_re.search(text)
        if m:
            year = int(m.group(1))
            if year > 2016:
                results.append({'title': title, 'year': year})

# remove duplicates (keep first occurrence)
seen = set()
unique = []
for r in results:
    t = r['title']
    if t not in seen:
        seen.add(t)
        unique.append(r)

out = json.dumps(unique)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_O6T9ov9jzG5YdiuSjrbbVoPU': ['paper_docs'], 'var_call_CGhz2TCzvXvH0HGqonLb9qg7': 'file_storage/call_CGhz2TCzvXvH0HGqonLb9qg7.json'}

exec(code, env_args)
