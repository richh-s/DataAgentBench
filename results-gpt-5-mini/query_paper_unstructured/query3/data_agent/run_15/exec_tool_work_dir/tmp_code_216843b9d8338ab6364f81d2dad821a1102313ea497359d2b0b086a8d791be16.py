code = """import json, re
mongo_path = var_call_lw1BDdON2qA81FPDZcOaeCQD
with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)
cite_path = var_call_4r8mPtyhh6ISyuNbudo6maG5
with open(cite_path, 'r', encoding='utf-8') as f:
    cite_records = json.load(f)
cite_map = {r['title']: int(r['total_citations']) for r in cite_records}

out = []
for rec in mongo_records[:200]:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','') or ''
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    year = None
    for y in years:
        yi = int(y)
        if 1900 <= yi <= 2030:
            year = yi
            break
    empirical = 'empirical' in text.lower()
    in_cite = title in cite_map
    out.append({'title': title, 'year': year, 'empirical': empirical, 'in_citations': in_cite, 'citations': cite_map.get(title)})

# limit output
print('__RESULT__:')
print(json.dumps(out[:50]))"""

env_args = {'var_call_hltMAjoVg8naiJZY0LKIVF1Z': ['paper_docs'], 'var_call_koRdw2k2stIYQakj58C4PrJM': 'file_storage/call_koRdw2k2stIYQakj58C4PrJM.json', 'var_call_mDVYpWfH8X4FYBQecWRWGXE3': {'titles': [], 'records': []}, 'var_call_lw1BDdON2qA81FPDZcOaeCQD': 'file_storage/call_lw1BDdON2qA81FPDZcOaeCQD.json', 'var_call_Di7ndayXtIPTIhPU9cPRRx29': ['Citations', 'sqlite_sequence'], 'var_call_4r8mPtyhh6ISyuNbudo6maG5': 'file_storage/call_4r8mPtyhh6ISyuNbudo6maG5.json', 'var_call_ieeomIwXK05iYLcRbonPlVy9': [], 'var_call_x539M77kazg0nyaya4dw4lK6': 'file_storage/call_x539M77kazg0nyaya4dw4lK6.json'}

exec(code, env_args)
