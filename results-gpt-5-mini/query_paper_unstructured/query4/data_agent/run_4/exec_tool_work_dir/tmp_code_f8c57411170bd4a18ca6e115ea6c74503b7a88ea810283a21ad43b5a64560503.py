code = """import json, re
p = var_call_40G8suqyORvGvH2VqbbBEhkO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build set of titles that contain 'physical activity' domain from paper_docs results
titles_with_domain = set()
for rec in data:
    filename = rec.get('filename','')
    text = rec.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    if 'physical activity' in text.lower() or 'physical activity' in title.lower():
        titles_with_domain.add(title)

# load citation totals
p2 = var_call_xQdYTsepG8F9TC14yLse3ody
with open(p2, 'r', encoding='utf-8') as f:
    cit = json.load(f)

# Now find titles from cit that match titles_with_domain
matches = []
for t in cit:
    # normalize by removing .txt? titles in cit likely match filenames without .txt
    norm = t
    if norm in titles_with_domain:
        matches.append({'title': norm, 'total_citations': cit[t]})

# also try substring matching: if any title in titles_with_domain is substring of cit title or vice versa
for td in titles_with_domain:
    for t in cit:
        if td.lower() in t.lower() or t.lower() in td.lower():
            if not any(m['title']==t for m in matches):
                matches.append({'title': t, 'total_citations': cit[t]})

print('__RESULT__:')
print(json.dumps(sorted(matches, key=lambda x: x['title'])))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json', 'var_call_jokn9ejj3SySQh0YVLoqQrID': [], 'var_call_GCWkR1OFB2vPEOsJxlXZD4wx': [], 'var_call_On7oCux1AjpCpaT2jkfydY5j': 'file_storage/call_On7oCux1AjpCpaT2jkfydY5j.json', 'var_call_z3BmMZCV2zNwBJd3OBhZLJql': ['paper_docs'], 'var_call_9PGGGyYeJkpVGL7Mt4nLr2dm': ['Citations', 'sqlite_sequence'], 'var_call_BQYWUevYFUky85OvPZGvHJRC': 'file_storage/call_BQYWUevYFUky85OvPZGvHJRC.json', 'var_call_xQdYTsepG8F9TC14yLse3ody': 'file_storage/call_xQdYTsepG8F9TC14yLse3ody.json'}

exec(code, env_args)
