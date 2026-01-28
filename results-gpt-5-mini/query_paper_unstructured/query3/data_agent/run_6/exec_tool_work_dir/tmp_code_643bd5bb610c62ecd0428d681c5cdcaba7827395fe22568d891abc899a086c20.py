code = """import json, re
path = var_call_h8CIT19siyAbgT4EYFNOWynA
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

d = docs[0]
text = d.get('text','')
# find all digit sequences of length 4
digits4 = re.findall(r"\d{4}", text)
# find 'CHI' occurrences with surrounding context
chi_matches = [(m.start(), text[max(0,m.start()-50):m.start()+50]) for m in re.finditer(r"CHI", text)]

import json
print('__RESULT__:')
print(json.dumps({'filename': d.get('filename'), 'digits4_count': len(digits4), 'digits4_sample': digits4[:10], 'chi_contexts': chi_matches[:3]}))"""

env_args = {'var_call_h8CIT19siyAbgT4EYFNOWynA': 'file_storage/call_h8CIT19siyAbgT4EYFNOWynA.json', 'var_call_3dA7kX9PtJ8QLXwxTaRemCVm': [], 'var_call_5RCodw8aYgeDXSEbFmfrMuIY': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'empirical': True}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years_found': [], 'empirical': True}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt', 'years_found': [], 'empirical': True}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt', 'years_found': [], 'empirical': True}, {'filename': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'years_found': [], 'empirical': True}]}

exec(code, env_args)
