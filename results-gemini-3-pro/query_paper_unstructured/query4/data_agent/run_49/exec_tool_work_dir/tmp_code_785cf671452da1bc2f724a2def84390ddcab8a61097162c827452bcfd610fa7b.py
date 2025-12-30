code = """import json
import re

file_path = locals()['var_function-call-11172061455759427872']
with open(file_path, 'r') as f:
    papers = json.load(f)

papers_2016 = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Try to find year
    years = []
    
    # 1. Header search
    header = text[:500]
    years_header = re.findall(r'\b(201[0-9])\b', header)
    if years_header:
        years.extend([int(y) for y in years_header])
    
    short_years = re.findall(r"'\d{2}", header)
    if short_years:
        years.extend([int('20' + y[1:]) for y in short_years])
        
    # 2. Copyright search in full text (bottom often has it)
    # "Copyright 2016"
    copyright_years = re.findall(r'Copyright\s+(201[0-9])', text)
    if copyright_years:
        years.extend([int(y) for y in copyright_years])
        
    # 3. ACM string search (e.g. .../15/09...)
    # Regex: /1[0-9]/[0-9]{2}
    acm_years = re.findall(r'/1[0-9]/[0-1][0-9]', text[:1000]) # usually in first page footer
    if acm_years:
        # extract year
        for s in acm_years:
            y = int('20' + s[1:3])
            years.append(y)
            
    # Filter years
    years = [y for y in years if 2010 <= y <= 2020]
    
    # Determine probable year
    # If 2016 is present
    if 2016 in years:
        # Check if 2015 is present (and more prominent?)
        # If 2016 is in Copyright, it's strong.
        # If 2016 is in Header, it's strong.
        papers_2016.append({
            "title": title,
            "years_found": list(set(years)),
            "physical_activity": "physical activity" in text.lower()
        })

print('__RESULT__:')
print(json.dumps(papers_2016))"""

env_args = {'var_function-call-3489125586506889844': 'file_storage/function-call-3489125586506889844.json', 'var_function-call-3489125586506887483': ['Citations', 'sqlite_sequence'], 'var_function-call-13585702268998000327': 'file_storage/function-call-13585702268998000327.json', 'var_function-call-13585702268998000192': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-11172061455759427872': 'file_storage/function-call-11172061455759427872.json', 'var_function-call-12104304543771652425': [], 'var_function-call-12469198988654123846': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'candidates': []}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'candidates': []}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'candidates': []}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'candidates': []}], 'var_function-call-1351698192213324060': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'header': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'years': ['2015']}], 'var_function-call-8254273891371820999': [], 'var_function-call-9585142687352628828': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [2015]}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': []}], 'var_function-call-5890826038591021095': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b'}

exec(code, env_args)
