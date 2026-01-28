code = """import json, re
mongo_path = var_call_lw1BDdON2qA81FPDZcOaeCQD
with open(mongo_path, 'r', encoding='utf-8') as f:
    records = json.load(f)
# find record
for rec in records:
    if rec.get('filename','').startswith('A Trip to the Moon'):
        text = rec.get('text','') or ''
        # find years
        years = re.findall(r"\b(19\d{2}|20\d{2})\b", text)
        # find 'CHI' line
        chi_idx = text.find('CHI')
        snippet = text[chi_idx:chi_idx+200]
        out = {'found_years': years[:10], 'snippet': snippet}
        break
else:
    out = {'error': 'not found'}
print('__RESULT__:')
import json
print(json.dumps(out))"""

env_args = {'var_call_hltMAjoVg8naiJZY0LKIVF1Z': ['paper_docs'], 'var_call_koRdw2k2stIYQakj58C4PrJM': 'file_storage/call_koRdw2k2stIYQakj58C4PrJM.json', 'var_call_mDVYpWfH8X4FYBQecWRWGXE3': {'titles': [], 'records': []}, 'var_call_lw1BDdON2qA81FPDZcOaeCQD': 'file_storage/call_lw1BDdON2qA81FPDZcOaeCQD.json', 'var_call_Di7ndayXtIPTIhPU9cPRRx29': ['Citations', 'sqlite_sequence'], 'var_call_4r8mPtyhh6ISyuNbudo6maG5': 'file_storage/call_4r8mPtyhh6ISyuNbudo6maG5.json', 'var_call_ieeomIwXK05iYLcRbonPlVy9': [], 'var_call_x539M77kazg0nyaya4dw4lK6': 'file_storage/call_x539M77kazg0nyaya4dw4lK6.json', 'var_call_ZZhGyxAvergo37bP7b8NIkcx': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 266}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 270}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': None, 'empirical': True, 'in_citations': True, 'citations': 269}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'year': None, 'empirical': True, 'in_citations': True, 'citations': 466}]}

exec(code, env_args)
