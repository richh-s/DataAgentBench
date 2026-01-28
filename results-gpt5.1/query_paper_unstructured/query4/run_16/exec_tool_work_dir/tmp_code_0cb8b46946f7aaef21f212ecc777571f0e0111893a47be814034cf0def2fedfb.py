code = """import re, json
from pathlib import Path

# load full mongo results
with open(var_call_MIs4DmmXkPI0SzuvTnJ4XXiG, 'r') as f:
    mongo_docs = json.load(f)

# heuristic extract year and domain from text
papers = []
for d in mongo_docs:
    text = d.get('text','')
    # year: look for 2016
    if '2016' not in text:
        continue
    # domain: require 'physical activity' phrase
    if re.search(r'physical activity', text, re.I):
        title = d.get('filename','').replace('.txt','')
        papers.append(title)

# load citations aggregate
with open(var_call_1EsPnWa4u8ENjF81nOhsxntj, 'r') as f:
    cits = json.load(f)

# map title -> total
cit_map = {c['title'].strip('"'): int(c['total_citations']) for c in cits}

results = []
for t in papers:
    if t in cit_map:
        results.append({'title': t, 'total_citations': cit_map[t]})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_MIs4DmmXkPI0SzuvTnJ4XXiG': 'file_storage/call_MIs4DmmXkPI0SzuvTnJ4XXiG.json', 'var_call_1EsPnWa4u8ENjF81nOhsxntj': 'file_storage/call_1EsPnWa4u8ENjF81nOhsxntj.json'}

exec(code, env_args)
