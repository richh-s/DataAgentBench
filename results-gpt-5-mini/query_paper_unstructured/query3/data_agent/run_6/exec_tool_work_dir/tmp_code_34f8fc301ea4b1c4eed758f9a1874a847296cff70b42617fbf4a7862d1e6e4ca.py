code = """import json
path = var_call_UMh8lmhI1ewZ4MZ1iltSYYfN
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# load earlier Mongo results
mongo_path = var_call_h8CIT19siyAbgT4EYFNOWynA
with open(mongo_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build set of titles from docs that contain 'empirical' and have year >2016
import re
emp_titles = set()
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','') or ''
    if not re.search(r"empirical", text, re.I):
        continue
    m = re.search(r"\b20(?:1[7-9]|2\d|30)\b", text)
    if m:
        year = int(m.group(0))
        if year > 2016:
            emp_titles.add(title)

# Now filter citations for those titles
results = []
for c in citations:
    t = c.get('title')
    if t in emp_titles:
        results.append({'title': t, 'total_citations': int(c.get('total_citations'))})

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_call_h8CIT19siyAbgT4EYFNOWynA': 'file_storage/call_h8CIT19siyAbgT4EYFNOWynA.json', 'var_call_3dA7kX9PtJ8QLXwxTaRemCVm': [], 'var_call_5RCodw8aYgeDXSEbFmfrMuIY': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'empirical': True}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': [], 'empirical': True}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': [], 'empirical': True}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': [], 'empirical': True}], 'var_call_9NrFBHJVN99IbTavOMcezAFh': {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'digits4_count': 99, 'digits4_sample': ['2018', '2018', '2018', '4503', '5620', '1145', '3173', '3173', '2018', '2018'], 'chi_contexts': [[2513, 'ee. Request permissions from permissions@acm.org.\nCHI 2018, April 21–26, 2018, Montréal, QC, Canada\n'], [5196, 'hat works by parameterizing animations, within a\n\nCHI 2018 Paper CHI 2018, April 21–26, 2018, Montré'], [5211, 'rameterizing animations, within a\n\nCHI 2018 Paper CHI 2018, April 21–26, 2018, Montréal, QC, CanadaP']]}, 'var_call_ZyMJjRuBTJsjw8JaDWagKovB': [], 'var_call_JCktTUuk2DUkm8Tn7CXpFySG': [], 'var_call_UMh8lmhI1ewZ4MZ1iltSYYfN': 'file_storage/call_UMh8lmhI1ewZ4MZ1iltSYYfN.json'}

exec(code, env_args)
