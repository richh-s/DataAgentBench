code = """import json, re
# load the paper_docs query result from the stored .json file
path = var_call_HWIzGp9Q8Mszq8gzqBmGqkfc
with open(path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

selected = []
for p in papers:
    filename = p.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = p.get('text','')
    if not text:
        continue
    # find first 4-digit year between 2000 and 2029
    m = re.search(r'\b(20[0-2][0-9])\b', text)
    year = int(m.group(1)) if m else None
    if year and year > 2016 and 'empirical' in text.lower():
        selected.append({'title': title, 'year': year})

# produce JSON string
result = json.dumps(selected)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_nRINhIm1ITwxpdsbY9l1GZUf': ['paper_docs'], 'var_call_yCC4E8r7SIzhVgHbHKsaG3oC': ['Citations', 'sqlite_sequence'], 'var_call_HWIzGp9Q8Mszq8gzqBmGqkfc': 'file_storage/call_HWIzGp9Q8Mszq8gzqBmGqkfc.json'}

exec(code, env_args)
