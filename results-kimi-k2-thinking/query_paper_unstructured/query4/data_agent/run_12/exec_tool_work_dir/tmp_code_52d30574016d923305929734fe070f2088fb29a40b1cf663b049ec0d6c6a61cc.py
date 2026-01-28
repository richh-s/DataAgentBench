code = """import json
import re

# Load papers data from MongoDB
mongo_key = 'var_functions.query_db:16'
papers_data = locals().get(mongo_key)

if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_data

# More flexible year extraction
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for year patterns: '15, 2015, CHI '16, etc.
    year_patterns = [
        r'\b(20\d{2})\b',  # 2015, 2016, etc.
        r"\b'(\d{2})\b",   # '15, '16, etc. - assume 2000s
        r'\b(19\d{2})\b'   # 1990s just in case
    ]
    
    year = None
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 4:
                year = int(year_str)
            elif len(year_str) == 2:
                # Convert '15 to 2015
                year = 2000 + int(year_str)
            break
    
    # Domain detection
    text_lower = text.lower()
    domain_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking']
    is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
    
    paper_info.append({
        'title': title,
        'year': year,
        'is_physical_activity': is_physical_activity,
        'filename': filename
    })

papers_2016_pa = [p for p in paper_info if p['year'] == 2016 and p['is_physical_activity']]

print('__RESULT__:')
print(json.dumps({
    'all_papers': paper_info,
    'papers_2016_pa': papers_2016_pa,
    'summary': {
        'total_papers': len(papers),
        'physical_activity_papers': len([p for p in paper_info if p['is_physical_activity']]),
        'papers_2016_pa_count': len(papers_2016_pa)
    }
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_papers': 99, 'first_paper_sample': {'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_papers_loaded': 5}, 'var_functions.execute_python:20': {'total_papers': 5, 'total_citations': 1405, 'papers_2016_pa': [], 'all_papers_info': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_physical_activity': True, 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_physical_activity': True, 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_physical_activity': True, 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_physical_activity': True, 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_physical_activity': True, 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}, 'var_functions.execute_python:22': {'has_sample_paper': True, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'year_candidates': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}}

exec(code, env_args)
