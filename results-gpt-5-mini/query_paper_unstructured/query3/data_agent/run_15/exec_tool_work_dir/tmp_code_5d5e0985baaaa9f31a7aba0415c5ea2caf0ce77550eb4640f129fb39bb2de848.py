code = """import json, re
# Load the Mongo regex 'empirical' query results
mongo_path = var_call_lw1BDdON2qA81FPDZcOaeCQD
with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)
# Load the citations aggregated results
cite_path = var_call_4r8mPtyhh6ISyuNbudo6maG5
with open(cite_path, 'r', encoding='utf-8') as f:
    cite_records = json.load(f)

# Build citation map
cite_map = {}
for r in cite_records:
    title = r.get('title')
    tc = r.get('total_citations')
    try:
        tc_int = int(tc)
    except:
        try:
            tc_int = int(float(tc))
        except:
            tc_int = None
    cite_map[title] = tc_int

results = []
for rec in mongo_records:
    filename = rec.get('filename','')
    if filename.lower().endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    text = rec.get('text','') or ''
    # find year
    years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
    year = None
    for y in years:
        yi = int(y)
        if 1900 <= yi <= 2030:
            year = yi
            break
    empirical = 'empirical' in text.lower()
    if empirical and year is not None and year > 2016 and title in cite_map:
        results.append({'title': title, 'year': year, 'total_citations': cite_map[title]})

# Remove duplicates by title, keep one
seen = {}
for r in results:
    seen[r['title']] = r
final = list(seen.values())

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_hltMAjoVg8naiJZY0LKIVF1Z': ['paper_docs'], 'var_call_koRdw2k2stIYQakj58C4PrJM': 'file_storage/call_koRdw2k2stIYQakj58C4PrJM.json', 'var_call_mDVYpWfH8X4FYBQecWRWGXE3': {'titles': [], 'records': []}, 'var_call_lw1BDdON2qA81FPDZcOaeCQD': 'file_storage/call_lw1BDdON2qA81FPDZcOaeCQD.json', 'var_call_Di7ndayXtIPTIhPU9cPRRx29': ['Citations', 'sqlite_sequence'], 'var_call_4r8mPtyhh6ISyuNbudo6maG5': 'file_storage/call_4r8mPtyhh6ISyuNbudo6maG5.json'}

exec(code, env_args)
