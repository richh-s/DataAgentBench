code = """import json
import re

p_path = locals()['var_function-call-12278789652942674597']
with open(p_path, 'r') as f:
    p_data = json.load(f)

count_year_gt_2016 = 0
count_empirical = 0
count_both = 0

sample_year_text = ""

for p in p_data:
    text = p['text']
    header = text[:1000]
    years = re.findall(r'20\d\d', header)
    pub_year = 0
    if years:
        y_ints = [int(y) for y in years]
        valid_years = [y for y in y_ints if 2000 <= y <= 2025]
        if valid_years:
            pub_year = min(valid_years)
    
    if pub_year > 2016:
        count_year_gt_2016 += 1
        if 'empirical' in text.lower():
            count_both += 1
        else:
            # Check if there's a contribution line
            pass
            
    if 'empirical' in text.lower():
        count_empirical += 1

print('__RESULT__:')
print(json.dumps({
    "total_papers": len(p_data),
    "year_gt_2016": count_year_gt_2016,
    "empirical_in_text": count_empirical,
    "both": count_both
}))"""

env_args = {'var_function-call-7844967085086575341': 'file_storage/function-call-7844967085086575341.json', 'var_function-call-7844967085086573572': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-12278789652942674597': 'file_storage/function-call-12278789652942674597.json', 'var_function-call-15796312403929804430': 'file_storage/function-call-15796312403929804430.json', 'var_function-call-14593713414867433848': []}

exec(code, env_args)
