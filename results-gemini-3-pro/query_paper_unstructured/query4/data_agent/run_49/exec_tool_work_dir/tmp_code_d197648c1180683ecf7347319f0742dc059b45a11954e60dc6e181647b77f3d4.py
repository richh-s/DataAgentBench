code = """import json

file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

for p in papers:
    if "Stage-based Model" in p['filename']:
        print('__RESULT__:')
        print(json.dumps(p['text'][:1000]))
        break"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json', 'var_function-call-12104304543771652425': [], 'var_function-call-12469198988654123846': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'candidates': []}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'candidates': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'candidates': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'candidates': []}], 'var_function-call-1351698192213324060': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years': ['2015']}], 'var_function-call-8254273891371820999': [], 'var_function-call-9585142687352628828': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [2015]}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': []}]}

exec(code, env_args)
