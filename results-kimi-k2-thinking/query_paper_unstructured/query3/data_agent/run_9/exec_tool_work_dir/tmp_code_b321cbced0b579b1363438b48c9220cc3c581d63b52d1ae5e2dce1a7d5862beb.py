code = """import json
import re

mongo_file_path = locals()['var_functions.query_db:5']
with open(mongo_file_path, 'r') as f:
    papers = json.load(f)

print('MongoDB papers loaded:', len(papers))

# Process papers to extract metadata
result_empirical = []

for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # Find year (4-digit numbers 2000-2025)
    year_match = re.search(r20[0-2][0-9], text)
    year = int(year_match.group()) if year_match else None
    
    # Check if empirical contribution
    is_empirical = 'empirical' in text.lower()
    
    if is_empirical and year and year > 2016:
        result_empirical.append({
            'title': title,
            'year': year
        })

print('Found empirical papers after 2016:', len(result_empirical))
if result_empirical:
    print('Sample:', result_empirical[:3])

result_dict = {'papers': result_empirical, 'count': len(result_empirical)}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:12': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': None, 'venue': 'CHI', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': None, 'venue': 'CHI', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': None, 'venue': 'CHI', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'contribution': None, 'venue': 'CHI', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': None, 'venue': 'CHI', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'empirical_papers_2017_plus': []}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
