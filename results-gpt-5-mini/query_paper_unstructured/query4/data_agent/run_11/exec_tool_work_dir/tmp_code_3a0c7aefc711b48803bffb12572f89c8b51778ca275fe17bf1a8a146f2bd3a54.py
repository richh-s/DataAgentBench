code = """import json
with open(var_call_UiXFAWxlyIWYkqSXdENiIgwM, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_tAhYfbZ5ec3wGmZhugmAT3IR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# build citation lookup
cit_lookup = {c['title']: int(c['total_citations']) for c in citations}

results = []
for doc in docs:
    text = doc.get('text','') or ''
    t_low = text.lower()
    if 'physical activity' in t_low and '2016' in t_low:
        title = doc.get('filename','').replace('.txt','')
        tc = cit_lookup.get(title, 0)
        results.append({'title': title, 'total_citations': tc})

import json as _json
print('__RESULT__:')
print(_json.dumps(results))"""

env_args = {'var_call_xDXDXv7O3Y8IsCnBirJ5usD6': ['paper_docs'], 'var_call_XXKoRyaVMde9ECUXLfDpTQ8d': ['Citations', 'sqlite_sequence'], 'var_call_UiXFAWxlyIWYkqSXdENiIgwM': 'file_storage/call_UiXFAWxlyIWYkqSXdENiIgwM.json', 'var_call_tAhYfbZ5ec3wGmZhugmAT3IR': 'file_storage/call_tAhYfbZ5ec3wGmZhugmAT3IR.json', 'var_call_8lOWLDZODDnFFsHeYPVcUv5P': [], 'var_call_UWlQfXs9zZLRaNbYAwpihdrr': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'pub_year': None, 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'pub_year': None, 'has_physical_activity': True}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'pub_year': None, 'has_physical_activity': True}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'pub_year': None, 'has_physical_activity': True}, {'title': 'Charting Design Preferences on Wellness Wearables', 'pub_year': None, 'has_physical_activity': True}]}

exec(code, env_args)
