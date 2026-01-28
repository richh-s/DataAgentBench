code = """import json
import re

path_papers = locals()['var_function-call-13071401018580020986']
with open(path_papers, 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    years = re.findall(r'\b(20\d{2})\b', text[:2000])
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2030]
    pub_year = valid_years[0] if valid_years else 0
    is_empirical = 'empirical' in text.lower()
    
    debug_info.append({
        'title': title,
        'year': pub_year,
        'is_empirical': is_empirical,
        'years_found': valid_years
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-6267193881023352391': 'file_storage/function-call-6267193881023352391.json', 'var_function-call-6267193881023352398': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-13071401018580018055': ['paper_docs'], 'var_function-call-13071401018580020986': 'file_storage/function-call-13071401018580020986.json', 'var_function-call-5244719068911348439': {'error': "[Errno 2] No such file or directory: 'var_function-call-13071401018580020986'"}, 'var_function-call-9288955964106777218': 'file_storage/function-call-9288955964106777218.json', 'var_function-call-12503289098151716023': 'file_storage/function-call-12503289098151716023.json', 'var_function-call-12161952385795619877': []}

exec(code, env_args)
