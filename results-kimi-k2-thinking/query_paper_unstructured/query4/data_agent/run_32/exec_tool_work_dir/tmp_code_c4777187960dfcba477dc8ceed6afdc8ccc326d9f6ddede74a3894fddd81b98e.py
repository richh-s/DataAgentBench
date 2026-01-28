code = """import json, re

# Load paper documents
paper_docs_file = locals()['var_functions.query_db:2']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

# Let's directly search for 2016 in each text
papers_with_2016 = []
for doc in paper_docs:
    text = doc.get('text', '')
    if '2016' in text and 'physical activity' in text.lower():
        papers_with_2016.append(doc)

analysis = []
for doc in papers_with_2016:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    analysis.append(title)

print('__RESULT__:')
print(json.dumps(analysis))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:21': [], 'var_functions.execute_python:18': {'total_papers': 5, 'years_distribution': {}, 'papers_2016_count': 0, 'physical_activity_count': 4, 'physical_activity_2016_count': 0, 'sample_papers_2016_physical_activity': []}, 'var_functions.execute_python:20': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'year_candidates': [], 'domains': ['physical activity', 'finances', 'location']}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_candidates': [], 'domains': []}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_candidates': [], 'domains': ['mental']}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_candidates': [], 'domains': []}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_candidates': [], 'domains': []}], 'var_functions.execute_python:22': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'domains': ['physical activity', 'food', 'mental', 'finances', 'location', 'chronic']}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'domains': ['physical activity', 'food', 'sleep', 'finances', 'productivity', 'location', 'diabetes']}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'domains': ['physical activity', 'sleep', 'mental', 'social interactions']}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'domains': ['physical activity', 'food', 'mental', 'productivity', 'location', 'chronic']}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'domains': ['sleep', 'mental', 'location', 'chronic']}], 'papers_2016_physical_activity': []}}

exec(code, env_args)
