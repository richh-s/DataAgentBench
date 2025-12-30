code = """import json

with open(locals()['var_function-call-3133197345042129806'], 'r') as f:
    papers = json.load(f)

target_paper = next(p for p in papers if "A Trip to the Moon" in p['filename'])
print("__RESULT__:")
print(json.dumps(target_paper['text'][:1000]))"""

env_args = {'var_function-call-968771099639512082': 'file_storage/function-call-968771099639512082.json', 'var_function-call-10025871425113369306': 'file_storage/function-call-10025871425113369306.json', 'var_function-call-3133197345042129806': 'file_storage/function-call-3133197345042129806.json', 'var_function-call-14920944781988559493': [], 'var_function-call-6019348044447435505': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'found_years': ['2015'], 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'found_years': [], 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'found_years': [], 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'found_years': [], 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'found_years': [], 'is_empirical': False}]}

exec(code, env_args)
