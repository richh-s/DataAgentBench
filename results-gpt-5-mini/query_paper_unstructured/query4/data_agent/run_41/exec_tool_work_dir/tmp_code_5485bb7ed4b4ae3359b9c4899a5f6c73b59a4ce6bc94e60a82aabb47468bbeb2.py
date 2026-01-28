code = """import json, re
with open(var_call_touM182CAbPKUSrxioioIRs3, 'r') as f:
    docs = json.load(f)
results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    if re.search(r'physical activity', text, re.I) and re.search(r'2016', text):
        # try to extract publication year near top
        head = text[:400]
        m = re.search(r"\b(19|20)\d{2}\b", head)
        year = int(m.group(0)) if m else 2016
        results.append({'title': title, 'year': year})
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_DI1QgzAvteEOnKUxNEZimjEB': 'file_storage/call_DI1QgzAvteEOnKUxNEZimjEB.json', 'var_call_W1tS2pTBCUpcTDP5CcoLelKQ': [], 'var_call_VqIrqx1xaChgeklSyjGyHB89': 'file_storage/call_VqIrqx1xaChgeklSyjGyHB89.json', 'var_call_aL3WayOSWGUcSYq3Eh7186vj': [], 'var_call_touM182CAbPKUSrxioioIRs3': 'file_storage/call_touM182CAbPKUSrxioioIRs3.json'}

exec(code, env_args)
