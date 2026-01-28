code = """import json, re
# Load the Mongo query result from storage
path = var_call_w2Nv7UgCjiHN6I6HYUjZ4I6P
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles = []
records = []
for d in docs:
    filename = d.get('filename','')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = d.get('text','')
    # check if 'physical activity' appears
    if re.search(r'physical activity', text, re.IGNORECASE):
        # try to extract publication year: look in first 800 chars, then whole text
        head = text[:800]
        m = re.search(r'\b(20\d{2})\b', head)
        year = None
        if m:
            year = int(m.group(1))
        else:
            m2 = re.search(r'\b(20\d{2})\b', text)
            if m2:
                year = int(m2.group(1))
        if year == 2016:
            titles.append(title)
            records.append({'title': title, 'year': year})

# deduplicate while preserving order
seen = set()
unique_titles = []
for t in titles:
    if t not in seen:
        seen.add(t)
        unique_titles.append(t)

output = {'titles': unique_titles, 'count': len(unique_titles)}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_H8MR8XiAJQcwfwjUzIUnvAZp': ['paper_docs'], 'var_call_abt9r2WlD9FlUNBcOscHzbCD': ['Citations', 'sqlite_sequence'], 'var_call_w2Nv7UgCjiHN6I6HYUjZ4I6P': 'file_storage/call_w2Nv7UgCjiHN6I6HYUjZ4I6P.json'}

exec(code, env_args)
