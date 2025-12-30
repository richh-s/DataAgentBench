code = """import json
import re

with open(locals()['var_function-call-8978544678357083899'], 'r') as f:
    papers = json.load(f)

# Inspect first paper and "A Wee Bit More Interaction..."
targets = ["A Lived Informatics Model of Personal Informatics.txt", "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"]

results = {}
for p in papers:
    if p['filename'] in targets:
        results[p['filename']] = p['text'][:200]

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-15050569047067534700': 'file_storage/function-call-15050569047067534700.json', 'var_function-call-3142892684795704503': 'file_storage/function-call-3142892684795704503.json', 'var_function-call-8978544678357083899': 'file_storage/function-call-8978544678357083899.json', 'var_function-call-9130584372251179173': 'file_storage/function-call-9130584372251179173.json', 'var_function-call-5001071914055655965': [], 'var_function-call-15001692400345327096': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}]}

exec(code, env_args)
