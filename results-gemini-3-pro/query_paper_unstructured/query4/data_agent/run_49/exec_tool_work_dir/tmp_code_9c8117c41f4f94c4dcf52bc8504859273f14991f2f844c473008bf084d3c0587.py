code = """import json
import re

file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

res = []
for p in papers:
    if "Lived Informatics" in p['filename']:
        text = p['text']
        header = text[:200]
        years = re.findall(r'201[0-9]', header)
        res.append({
            'filename': p['filename'],
            'header': header,
            'years': years
        })
        break

print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json', 'var_function-call-12104304543771652425': [], 'var_function-call-12469198988654123846': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'candidates': []}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'candidates': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'candidates': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'candidates': []}]}

exec(code, env_args)
