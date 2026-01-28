code = """import json

p_path = locals()['var_function-call-93104423649467143']
with open(p_path, 'r') as f:
    p_data = json.load(f)

target_title = "A Quantified-Self Framework for Exploring and Enhancing Personal Productivity"
found_target = False
target_header = ""

filenames = [p['filename'] for p in p_data[:5]]

for p in p_data:
    if target_title in p['filename']:
        found_target = True
        target_header = p['text'][:500]
        break

result = {
    "found_target": found_target,
    "target_header": target_header,
    "first_filenames": filenames
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-7844967085086575341': 'file_storage/function-call-7844967085086575341.json', 'var_function-call-7844967085086573572': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-12278789652942674597': 'file_storage/function-call-12278789652942674597.json', 'var_function-call-15796312403929804430': 'file_storage/function-call-15796312403929804430.json', 'var_function-call-14593713414867433848': [], 'var_function-call-13454756578952752926': {'total_papers': 5, 'year_gt_2016': 0, 'empirical_in_text': 2, 'both': 0}, 'var_function-call-93104423649467143': 'file_storage/function-call-93104423649467143.json', 'var_function-call-16161007735834324086': [], 'var_function-call-8573954616140981769': {'gt_2016': 0, 'empirical': 0}, 'var_function-call-15695848446438165967': 'Done'}

exec(code, env_args)
