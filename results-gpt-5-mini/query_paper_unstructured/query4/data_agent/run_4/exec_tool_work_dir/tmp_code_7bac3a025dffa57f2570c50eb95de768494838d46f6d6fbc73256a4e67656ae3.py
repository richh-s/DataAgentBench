code = """import json, re
p = var_call_40G8suqyORvGvH2VqbbBEhkO
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

p2 = var_call_xQdYTsepG8F9TC14yLse3ody
with open(p2, 'r', encoding='utf-8') as f:
    cit = json.load(f)

candidates = []
for rec in data:
    filename = rec.get('filename','')
    text = rec.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    if 'physical activity' not in text.lower() and 'physical activity' not in title.lower():
        continue
    # search for any 4-digit year between 1990 and 2025 anywhere in text
    years = re.findall(r"\b(19[9][0-9]|20[0-2][0-9]|2025)\b", text)
    years_full = re.findall(r"\b(19[9][0-9]|20[0-2][0-9]|2025)\b", text)
    # years is list of tuples? due to groups; better find all via another pattern
    years2 = re.findall(r"\b(19\d\d|20\d\d)\b", text)
    years_int = []
    for y in years2:
        try:
            yi = int(y)
            if 1990 <= yi <= 2025:
                years_int.append(yi)
        except:
            pass
    year = years_int[0] if years_int else None
    is2016 = 2016 in years_int
    candidates.append({'title': title, 'detected_year': year, 'is2016': is2016})

# filter for is2016
c2016 = [c for c in candidates if c['is2016']]

# If none found, also try to detect year from filename patterns like 'CHI 2016' present in text header lines
if not c2016:
    for rec in data:
        filename = rec.get('filename','')
        text = rec.get('text','')
        title = filename[:-4] if filename.lower().endswith('.txt') else filename
        if 'physical activity' not in text.lower() and 'physical activity' not in title.lower():
            continue
        # look for venue lines like 'CHI 2016'
        if re.search(r"\bCHI\s*2016\b", text) or re.search(r"\bUbicomp\s*2016\b", text, re.I) or re.search(r"\b2016,", text):
            c2016.append({'title': title, 'detected_year': 2016, 'is2016': True})

# Prepare final matches with citation totals
matches = []
for c in c2016:
    t = c['title']
    # find in cit mapping: exact or substring
    found = False
    for ct in cit:
        if ct.strip().lower() == t.strip().lower():
            matches.append({'title': ct, 'total_citations': cit[ct]})
            found = True
            break
    if not found:
        for ct in cit:
            if t.strip().lower() in ct.strip().lower() or ct.strip().lower() in t.strip().lower():
                matches.append({'title': ct, 'total_citations': cit[ct]})
                found = True
                break
    if not found:
        matches.append({'title': t, 'total_citations': None})

print('__RESULT__:')
print(json.dumps({'candidates_count': len(candidates), 'c2016_count': len(c2016), 'c2016': c2016, 'matches': matches}))"""

env_args = {'var_call_UeAwGvyL4BRgCq5TsBDxPehn': 'file_storage/call_UeAwGvyL4BRgCq5TsBDxPehn.json', 'var_call_dtnwJdFJIovt8fdBMoCOC9Z5': [], 'var_call_40G8suqyORvGvH2VqbbBEhkO': 'file_storage/call_40G8suqyORvGvH2VqbbBEhkO.json', 'var_call_jokn9ejj3SySQh0YVLoqQrID': [], 'var_call_GCWkR1OFB2vPEOsJxlXZD4wx': [], 'var_call_On7oCux1AjpCpaT2jkfydY5j': 'file_storage/call_On7oCux1AjpCpaT2jkfydY5j.json', 'var_call_z3BmMZCV2zNwBJd3OBhZLJql': ['paper_docs'], 'var_call_9PGGGyYeJkpVGL7Mt4nLr2dm': ['Citations', 'sqlite_sequence'], 'var_call_BQYWUevYFUky85OvPZGvHJRC': 'file_storage/call_BQYWUevYFUky85OvPZGvHJRC.json', 'var_call_xQdYTsepG8F9TC14yLse3ody': 'file_storage/call_xQdYTsepG8F9TC14yLse3ody.json', 'var_call_k69zPsARtimNXJyEpFOK96WM': [{'title': 'A Lived Informatics Model of Personal Informatics', 'total_citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'total_citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'total_citations': 266}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'total_citations': 306}]}

exec(code, env_args)
