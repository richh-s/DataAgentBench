code = """import json

file_path = locals()['var_function-call-17774907068370160114']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles = [p['filename'].replace('.txt', '') for p in papers]

print("__RESULT__:")
print(json.dumps({"count": len(titles), "titles": titles[:20]}))"""

env_args = {'var_function-call-2991259327904718266': ['paper_docs'], 'var_function-call-2991259327904718481': ['Citations', 'sqlite_sequence'], 'var_function-call-10512507186521432510': 'file_storage/function-call-10512507186521432510.json', 'var_function-call-12545833755252698609': 'file_storage/function-call-12545833755252698609.json', 'var_function-call-10414038178410062022': [], 'var_function-call-9109714520814129217': {'total_papers': 5, 'titles_preview': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'food_in_text_count': 3, 'food_in_text_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-8738282695325536530': [{'count(*)': '1405'}], 'var_function-call-17774907068370160114': 'file_storage/function-call-17774907068370160114.json'}

exec(code, env_args)
