code = """import json
import re
from collections import Counter

c_path = locals()['var_function-call-15796312403929804430']
p_path = locals()['var_function-call-93104423649467143']

with open(c_path, 'r') as f:
    c_data = json.load(f)

with open(p_path, 'r') as f:
    p_data = json.load(f)

c_map = {}
for x in c_data:
    t = x['title']
    c_val = int(x['citation_count'])
    c_map[t] = c_map.get(t, 0) + c_val

results = []

for p in p_data:
    text = p['text']
    fname = p['filename']
    title = fname.replace('.txt', '')
    
    # Extract Year
    # Strategy: Find most frequent year (2010-2025) in the text
    years = re.findall(r'20\d\d', text)
    valid_years = [int(y) for y in years if 2010 <= int(y) <= 2025]
    
    pub_year = 0
    if valid_years:
        # Most common year is likely the pub year (appearing in footers etc)
        pub_year = Counter(valid_years).most_common(1)[0][0]
    
    # Fallback: if no years found, maybe '19 format? 
    # But usually 2019 appears.
    
    if pub_year > 2016:
        # Check empirical
        if 'empirical' in text.lower():
            total_citations = c_map.get(title, 0)
            results.append({
                "title": title,
                "citation_count": total_citations,
                "year": pub_year
            })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7844967085086575341': 'file_storage/function-call-7844967085086575341.json', 'var_function-call-7844967085086573572': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-12278789652942674597': 'file_storage/function-call-12278789652942674597.json', 'var_function-call-15796312403929804430': 'file_storage/function-call-15796312403929804430.json', 'var_function-call-14593713414867433848': [], 'var_function-call-13454756578952752926': {'total_papers': 5, 'year_gt_2016': 0, 'empirical_in_text': 2, 'both': 0}, 'var_function-call-93104423649467143': 'file_storage/function-call-93104423649467143.json', 'var_function-call-16161007735834324086': [], 'var_function-call-8573954616140981769': {'gt_2016': 0, 'empirical': 0}, 'var_function-call-15695848446438165967': 'Done', 'var_function-call-13234309845643690303': {'found_target': False, 'target_header': '', 'first_filenames': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt']}, 'var_function-call-10959156238210617065': {'total_papers': 99, 'found_target': True, 'header': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith', 'has_empirical': True, 'years_found': []}, 'var_function-call-17098856828547943896': {'all_years': ['2019', '2019', '2019', '2019', '2019', '2019', '2019', '2018', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019', '2019'], 'copyright_years': []}}

exec(code, env_args)
