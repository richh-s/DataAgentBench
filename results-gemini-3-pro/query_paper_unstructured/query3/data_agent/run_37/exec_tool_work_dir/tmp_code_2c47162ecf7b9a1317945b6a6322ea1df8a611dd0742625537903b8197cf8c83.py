code = """import json
import re

with open(locals()['var_function-call-1188879216130437550'], 'r') as f:
    papers = json.load(f)

results = []
for i, p in enumerate(papers[:5]):
    text = p.get('text', '')
    # simple regex for 20xx
    matches = re.findall(r'20\d{2}', text[:1000])
    results.append(f"Paper {i}: matches={matches}")

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-563988683724796528': 'file_storage/function-call-563988683724796528.json', 'var_function-call-1188879216130437550': 'file_storage/function-call-1188879216130437550.json', 'var_function-call-6926115911538441459': 'file_storage/function-call-6926115911538441459.json', 'var_function-call-11700601508177380664': [], 'var_function-call-15227438266193405659': [{'title': 'A Lived Informatics Model of Personal Informatics', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'extracted_year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'extracted_year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'extracted_year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'extracted_year': None, 'has_empirical': False}]}

exec(code, env_args)
