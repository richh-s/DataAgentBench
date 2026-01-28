code = """import json
mongo_path = var_call_lw1BDdON2qA81FPDZcOaeCQD
cite_path = var_call_4r8mPtyhh6ISyuNbudo6maG5
with open(mongo_path, 'r', encoding='utf-8') as f:
    mongo_records = json.load(f)
with open(cite_path, 'r', encoding='utf-8') as f:
    cite_records = json.load(f)
cite_map = {r['title']: int(r['total_citations']) for r in cite_records}

results = []
for rec in mongo_records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','') or ''
    lt = text.lower()
    if 'empirical' not in lt:
        continue
    # find year by scanning for years strings
    found_year = None
    found_idx = None
    for y in range(1900, 2031):
        ys = str(y)
        idx = lt.find(ys)
        if idx != -1:
            if found_idx is None or idx < found_idx:
                found_year = y
                found_idx = idx
    if found_year is None:
        continue
    if found_year <= 2016:
        continue
    if title in cite_map:
        results.append({'title': title, 'year': found_year, 'total_citations': cite_map[title]})

# deduplicate
seen = {}
for r in results:
    seen[r['title']] = r
final = list(seen.values())

print('__RESULT__:')
print(json.dumps(final))"""

env_args = {'var_call_hltMAjoVg8naiJZY0LKIVF1Z': ['paper_docs'], 'var_call_koRdw2k2stIYQakj58C4PrJM': 'file_storage/call_koRdw2k2stIYQakj58C4PrJM.json', 'var_call_mDVYpWfH8X4FYBQecWRWGXE3': {'titles': [], 'records': []}, 'var_call_lw1BDdON2qA81FPDZcOaeCQD': 'file_storage/call_lw1BDdON2qA81FPDZcOaeCQD.json', 'var_call_Di7ndayXtIPTIhPU9cPRRx29': ['Citations', 'sqlite_sequence'], 'var_call_4r8mPtyhh6ISyuNbudo6maG5': 'file_storage/call_4r8mPtyhh6ISyuNbudo6maG5.json', 'var_call_ieeomIwXK05iYLcRbonPlVy9': [], 'var_call_x539M77kazg0nyaya4dw4lK6': 'file_storage/call_x539M77kazg0nyaya4dw4lK6.json', 'var_call_ZZhGyxAvergo37bP7b8NIkcx': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 266}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 270}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 269}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'year': None, 'empirical': True, 'in_citations': True, 'citations': 466}], 'var_call_szlZPF63YcZtSdRDDuoZbJHZ': {'found_years': [], 'snippet': 'CHI 2018, April 21–26, 2018, Montréal, QC, Canada\n© 2018 Copyright held by the owner/author(s). Publication rights licensed to ACM.\nISBN 978-1-4503-5620-6/18/04. . . $15.00\nDOI: http://dx.doi.org/10.1'}}

exec(code, env_args)
