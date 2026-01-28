code = """import json, re
# Load Mongo query results
mongo_path = var_call_h8CIT19siyAbgT4EYFNOWynA
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Load citations aggregated
citations_path = var_call_UMh8lmhI1ewZ4MZ1iltSYYfN
with open(citations_path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build dict for citations by title
cit_dict = {c['title']: int(c['total_citations']) for c in citations}

results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    if not re.search(r"empirical", text, re.I):
        continue
    # find all 4-digit years 1990-2030 with positions
    years = [(int(m.group(0)), m.start()) for m in re.finditer(r"\b(?:19|20)\d{2}\b", text)]
    pub_year = None
    if years:
        # choose the year that appears earliest in the document
        years_sorted = sorted(years, key=lambda x: x[1])
        pub_year = years_sorted[0][0]
    # additional heuristics: look for patterns like 'CHI 2018'
    if pub_year is None:
        m = re.search(r"(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[\s,\-]*(?:'|’)?\s*(20\d{2})", text, re.I)
        if m:
            pub_year = int(m.group(1))
    if pub_year and pub_year > 2016:
        total_cites = cit_dict.get(title)
        results.append({'title': title, 'year': pub_year, 'total_citations': total_cites if total_cites is not None else None})

# deduplicate by title
seen=set(); unique=[]
for r in results:
    if r['title'] not in seen:
        seen.add(r['title'])
        unique.append(r)

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_h8CIT19siyAbgT4EYFNOWynA': 'file_storage/call_h8CIT19siyAbgT4EYFNOWynA.json', 'var_call_3dA7kX9PtJ8QLXwxTaRemCVm': [], 'var_call_5RCodw8aYgeDXSEbFmfrMuIY': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'empirical': True}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': [], 'empirical': True}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': [], 'empirical': True}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': [], 'empirical': True}], 'var_call_9NrFBHJVN99IbTavOMcezAFh': {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'digits4_count': 99, 'digits4_sample': ['2018', '2018', '2018', '4503', '5620', '1145', '3173', '3173', '2018', '2018'], 'chi_contexts': [[2513, 'ee. Request permissions from permissions@acm.org.\nCHI 2018, April 21–26, 2018, Montréal, QC, Canada\n'], [5196, 'hat works by parameterizing animations, within a\n\nCHI 2018 Paper CHI 2018, April 21–26, 2018, Montré'], [5211, 'rameterizing animations, within a\n\nCHI 2018 Paper CHI 2018, April 21–26, 2018, Montréal, QC, CanadaP']]}, 'var_call_ZyMJjRuBTJsjw8JaDWagKovB': [], 'var_call_JCktTUuk2DUkm8Tn7CXpFySG': [], 'var_call_UMh8lmhI1ewZ4MZ1iltSYYfN': 'file_storage/call_UMh8lmhI1ewZ4MZ1iltSYYfN.json', 'var_call_vc6nvk5OC6enCq0gLDOFksVP': []}

exec(code, env_args)
