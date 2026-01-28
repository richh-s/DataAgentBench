code = """import json, re
path = var_call_h8CIT19siyAbgT4EYFNOWynA
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

candidates = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    if not re.search(r"empirical", text, re.I):
        continue
    # find years 2017-2030
    years = [(m.group(0), m.start()) for m in re.finditer(r"\b(20(?:1[7-9]|2\d|30))\b", text)]
    year = None
    if years:
        # choose the year with smallest index (earliest in doc)
        years_sorted = sorted(years, key=lambda x: x[1])
        year = int(years_sorted[0][0])
    # fallback: look for 2017-2025 explicitly
    if year and year > 2016:
        candidates.append({'title': title, 'year': year})

# deduplicate
seen=set()
unique=[]
for c in candidates:
    if c['title'] not in seen:
        seen.add(c['title'])
        unique.append(c)

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_h8CIT19siyAbgT4EYFNOWynA': 'file_storage/call_h8CIT19siyAbgT4EYFNOWynA.json', 'var_call_3dA7kX9PtJ8QLXwxTaRemCVm': [], 'var_call_5RCodw8aYgeDXSEbFmfrMuIY': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'empirical': True}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': [], 'empirical': True}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': [], 'empirical': True}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': [], 'empirical': True}], 'var_call_9NrFBHJVN99IbTavOMcezAFh': {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'digits4_count': 99, 'digits4_sample': ['2018', '2018', '2018', '4503', '5620', '1145', '3173', '3173', '2018', '2018'], 'chi_contexts': [[2513, 'ee. Request permissions from permissions@acm.org.\nCHI 2018, April 21–26, 2018, Montréal, QC, Canada\n'], [5196, 'hat works by parameterizing animations, within a\n\nCHI 2018 Paper CHI 2018, April 21–26, 2018, Montré'], [5211, 'rameterizing animations, within a\n\nCHI 2018 Paper CHI 2018, April 21–26, 2018, Montréal, QC, CanadaP']]}}

exec(code, env_args)
