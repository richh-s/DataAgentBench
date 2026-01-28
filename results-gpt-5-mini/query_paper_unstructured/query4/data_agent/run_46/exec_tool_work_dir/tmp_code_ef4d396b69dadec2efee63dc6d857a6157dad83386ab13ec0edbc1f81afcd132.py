code = """import json, re
# Read the Mongo query result containing docs with 'physical' and 'activity'
path = var_call_zQema5txZszizqodvhPu7Oxr
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

matches = []
for doc in docs:
    filename = doc.get('filename','')
    text = doc.get('text','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    low = text.lower()
    if 'physical' in low and 'activity' in low:
        if re.search(r"\b2016\b", text):
            matches.append(title)
# dedupe
matches = list(dict.fromkeys(matches))
import json
print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_ueY8ny6tvVKcJ9NNvBSzXQv9': 'file_storage/call_ueY8ny6tvVKcJ9NNvBSzXQv9.json', 'var_call_k4guTGoCsoObrR3VeZLLdU84': [], 'var_call_zQema5txZszizqodvhPu7Oxr': 'file_storage/call_zQema5txZszizqodvhPu7Oxr.json', 'var_call_akrROVWBvQUPsCMRHuNVpUJU': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None}], 'var_call_jiSj5ODYQsrRs6zMyYqQsuSt': 'file_storage/call_jiSj5ODYQsrRs6zMyYqQsuSt.json'}

exec(code, env_args)
