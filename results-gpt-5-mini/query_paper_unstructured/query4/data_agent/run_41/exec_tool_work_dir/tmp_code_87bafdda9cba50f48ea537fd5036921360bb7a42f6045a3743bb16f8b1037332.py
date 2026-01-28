code = """import json, re
with open(var_call_VqIrqx1xaChgeklSyjGyHB89, 'r') as f:
    docs = json.load(f)
results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    if re.search(r'physical activity', text, re.I):
        # find first 4-digit year in the first 600 chars
        head = text[:800]
        m = re.search(r"\b(19|20)\d{2}\b", head)
        year = int(m.group(0)) if m else None
        # If not found in head, search entire text for first occurrence
        if not year:
            m2 = re.search(r"\b(19|20)\d{2}\b", text)
            year = int(m2.group(0)) if m2 else None
        if year==2016:
            results.append({'title': title, 'year': year})
# print per required format
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_DI1QgzAvteEOnKUxNEZimjEB': 'file_storage/call_DI1QgzAvteEOnKUxNEZimjEB.json', 'var_call_W1tS2pTBCUpcTDP5CcoLelKQ': [], 'var_call_VqIrqx1xaChgeklSyjGyHB89': 'file_storage/call_VqIrqx1xaChgeklSyjGyHB89.json'}

exec(code, env_args)
