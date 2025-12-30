code = """import json
import re

p_path = locals()['var_function-call-93104423649467143']
with open(p_path, 'r') as f:
    p_data = json.load(f)

count_gt_2016 = 0
count_empirical = 0

for p in p_data:
    text = p['text']
    header = text[:1000]
    
    # improved year extraction
    pub_year = 0
    # 4 digit
    years_4d = re.findall(r'20\d\d', header)
    # 2 digit with apostrophe
    years_2d = re.findall(r"'\d\d", header)
    
    candidates = []
    if years_4d:
        candidates.extend([int(y) for y in years_4d])
    if years_2d:
        candidates.extend([2000 + int(y[1:]) for y in years_2d])
    
    valid_candidates = [y for y in candidates if 2010 <= y <= 2025]
    if valid_candidates:
        pub_year = min(valid_candidates)
        
    if pub_year > 2016:
        count_gt_2016 += 1
        if 'empirical' in text.lower():
            count_empirical += 1

print("__RESULT__:")
print(json.dumps({"gt_2016": count_gt_2016, "empirical": count_empirical}))"""

env_args = {'var_function-call-7844967085086575341': 'file_storage/function-call-7844967085086575341.json', 'var_function-call-7844967085086573572': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-12278789652942674597': 'file_storage/function-call-12278789652942674597.json', 'var_function-call-15796312403929804430': 'file_storage/function-call-15796312403929804430.json', 'var_function-call-14593713414867433848': [], 'var_function-call-13454756578952752926': {'total_papers': 5, 'year_gt_2016': 0, 'empirical_in_text': 2, 'both': 0}, 'var_function-call-93104423649467143': 'file_storage/function-call-93104423649467143.json', 'var_function-call-16161007735834324086': []}

exec(code, env_args)
