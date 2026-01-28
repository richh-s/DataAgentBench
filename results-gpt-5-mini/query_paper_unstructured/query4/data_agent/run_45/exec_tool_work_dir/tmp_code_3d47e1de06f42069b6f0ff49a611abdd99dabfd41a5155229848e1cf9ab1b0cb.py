code = """import json, re
path = var_call_YsLRlcU3h7irQLHPdx5tyH09
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)
results = []
for d in docs:
    filename = d.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = d.get('text','')
    has_phys_act = bool(re.search(r'physical\s+activity', text, re.IGNORECASE))
    has_2016 = bool(re.search(r'\b2016\b', text))
    snippets_2016 = re.findall(r'.{0,40}2016.{0,40}', text)
    snippets_phys = re.findall(r'.{0,40}physical\s+activity.{0,40}', text, re.IGNORECASE)
    results.append({'title': title, 'has_physical_activity': has_phys_act, 'has_2016': has_2016, 'snippets_2016': snippets_2016[:5], 'snippets_phys': snippets_phys[:5]})
print('__RESULT__:')
import json
print(json.dumps(results))"""

env_args = {'var_call_H8MR8XiAJQcwfwjUzIUnvAZp': ['paper_docs'], 'var_call_abt9r2WlD9FlUNBcOscHzbCD': ['Citations', 'sqlite_sequence'], 'var_call_w2Nv7UgCjiHN6I6HYUjZ4I6P': 'file_storage/call_w2Nv7UgCjiHN6I6HYUjZ4I6P.json', 'var_call_riAVJQvz9VqLp676ohi9NTRg': {'titles': [], 'count': 0}, 'var_call_YsLRlcU3h7irQLHPdx5tyH09': 'file_storage/call_YsLRlcU3h7irQLHPdx5tyH09.json', 'var_call_5mYX0mpwlu8bYcXV637tyzmA': {'total_docs_returned': 5, 'filtered_count': 5, 'examples': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'has_physical': True, 'has_activity': True, 'years_found': []}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'has_physical': True, 'has_activity': True, 'years_found': []}]}}

exec(code, env_args)
