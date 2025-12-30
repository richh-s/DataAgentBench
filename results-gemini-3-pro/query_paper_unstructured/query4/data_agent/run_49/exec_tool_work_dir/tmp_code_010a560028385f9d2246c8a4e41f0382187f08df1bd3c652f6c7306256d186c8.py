code = """import json

file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

titles_2016 = []

for p in papers:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    if 'physical activity' not in text.lower():
        continue

    header = text[:300] 
    
    # Check for 2016 or '16
    has_2016 = '2016' in header or "'16" in header
    
    has_other_year = False
    for y in range(2010, 2021):
        if y == 2016: continue
        # Construct short year string like '15
        y_str = str(y)
        short_y = "'" + y_str[2:]
        if y_str in header or short_y in header:
            has_other_year = True
            break
            
    if has_2016 and not has_other_year:
        titles_2016.append(title)
    elif has_2016 and has_other_year:
        first_line = text.split('\n')[0]
        if '2016' in first_line or "'16" in first_line:
            titles_2016.append(title)

print('__RESULT__:')
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json', 'var_function-call-12104304543771652425': [], 'var_function-call-12469198988654123846': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'candidates': []}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'candidates': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'candidates': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'candidates': []}], 'var_function-call-1351698192213324060': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years': ['2015']}]}

exec(code, env_args)
