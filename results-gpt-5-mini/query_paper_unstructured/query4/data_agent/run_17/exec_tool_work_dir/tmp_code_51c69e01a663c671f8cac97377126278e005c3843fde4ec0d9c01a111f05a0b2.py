code = """import json, re
path = var_call_557VZrPhqUrgO6CAofXjAEsq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

venue_keywords = ['CHI','Ubicomp','CSCW','DIS','PervasiveHealth','WWW','IUI','OzCHI','TEI','AH','Proceedings','Proc.','Proc','ACM','IEEE']
results = []
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    if not text:
        continue
    if not re.search(r'\b(physical activity|physical activit|exercise|physical training|physical fitness)\b', text, re.I):
        continue
    # find all occurrences of '2016'
    for m in re.finditer(r'2016', text):
        start = max(0, m.start()-200)
        end = m.end()+200
        context = text[start:end]
        # check if any venue keyword occurs in context
        if any(re.search(r'\b'+re.escape(k)+r'\b', context, re.I) for k in venue_keywords):
            results.append(title)
            break

# deduplicate
results = list(dict.fromkeys(results))
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_VNEvq032PXm1hSsPWSIEbAc4': 'file_storage/call_VNEvq032PXm1hSsPWSIEbAc4.json', 'var_call_VAXyipWQI6VX8cowdguGGkry': [], 'var_call_557VZrPhqUrgO6CAofXjAEsq': 'file_storage/call_557VZrPhqUrgO6CAofXjAEsq.json', 'var_call_cOaf4DkuMvSAPShkJlA1MB3v': []}

exec(code, env_args)
