code = """import json
import re

path_papers = locals()['var_function-call-13071401018580020986']
with open(path_papers, 'r') as f:
    papers = json.load(f)

result = {}

p1 = papers[0]
result['title'] = p1['filename']
result['text_start_repr'] = repr(p1.get('text', '')[:200])
match = re.search(r'20\d\d', p1.get('text', '')[:200])
result['match'] = str(match)

# Check 'A Wee Bit More Interaction'
for p in papers:
    if "A Wee Bit More Interaction" in p['filename']:
        result['p4_title'] = p['filename']
        result['p4_text_start'] = repr(p.get('text', '')[:200])
        match4 = re.search(r'20\d\d', p.get('text', '')[:200])
        result['p4_match'] = str(match4)

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json', 'var_function-call-5244719068911348439': {'error': "[Errno 2] No such file or directory: 'var_function-call-13071401018580020986'"}, 'var_function-call-9288955964106777218': 'file_storage/function-call-9288955964106777218.json', 'var_function-call-12503289098151716023': 'file_storage/function-call-12503289098151716023.json', 'var_function-call-12161952385795619877': [], 'var_function-call-18122560194841091265': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 0, 'is_empirical': False, 'years_found': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'is_empirical': False, 'years_found': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'is_empirical': True, 'years_found': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'is_empirical': True, 'years_found': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'is_empirical': False, 'years_found': []}]}

exec(code, env_args)
