code = """import json
import re

file_path = locals()['var_function-call-11757020696500287229']

with open(file_path, 'r') as f:
    papers = json.load(f)

debug_info = []

for paper in papers:
    text = paper['text']
    title = paper['filename']
    
    # Debug extraction
    matches = re.findall(r'20\d\d', text[:1000]) # removed \b
    snippet = text[:200]
    
    debug_info.append({"title": title, "matches": matches, "snippet": snippet})

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-4508703165533921554': ['paper_docs'], 'var_function-call-6558568440617970776': 'file_storage/function-call-6558568440617970776.json', 'var_function-call-12977520170952019892': 'file_storage/function-call-12977520170952019892.json', 'var_function-call-3057315164006980337': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-11757020696500287229': 'file_storage/function-call-11757020696500287229.json', 'var_function-call-14242122036404788287': [], 'var_function-call-7998227982978928728': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'has_empirical': False, 'matches': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False, 'matches': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True, 'matches': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True, 'matches': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False, 'matches': []}]}

exec(code, env_args)
