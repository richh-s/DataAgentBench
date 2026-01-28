code = """import json, re

paper_docs_file = locals()['var_functions.query_db:2']
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

analysis = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '')
    
    # Look for typical publication year patterns in academic papers
    year = None
    
    # Pattern 1: Look for 'UBICOMP '15' style dates
    pub_year_match = re.search(r"UBICOMP\s+'(\d{2})\b", text, re.IGNORECASE)
    if pub_year_match:
        year = 2000 + int(pub_year_match.group(1))
    
    if not year:
        pub_year_match = re.search(r"CHI\s+'(\d{2})\b", text, re.IGNORECASE)
        if pub_year_match:
            year = 2000 + int(pub_year_match.group(1))
    
    if not year:
        pub_year_match = re.search(r"CSCW\s+'(\d{2})\b", text, re.IGNORECASE)
        if pub_year_match:
            year = 2000 + int(pub_year_match.group(1))
    
    if not year:
        year_match = re.search(r"\b(20[0-4][0-9]{1})\b", text)
        if year_match:
            year = int(year_match.group(1))
    
    # Extract domains
    domain_keywords = ['physical activity', 'food', 'sleep', 'mental', 'finances', 'productivity', 'screen time', 'social interactions', 'location', 'chronic', 'diabetes', 'health_behavior']
    domains = []
    for keyword in domain_keywords:
        if keyword in text.lower():
            domains.append(keyword)
    
    analysis.append({
        'title': title,
        'year': year,
        'domains': domains
    })

# Find papers from 2016 in physical activity domain
papers_2016_physical_activity = [p for p in analysis if p['year'] == 2016 and 'physical activity' in p['domains']]

print('__RESULT__:')
print(json.dumps({
    'all_papers': analysis,
    'papers_2016_physical_activity': papers_2016_physical_activity
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:10': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:21': [], 'var_functions.execute_python:18': {'total_papers': 5, 'years_distribution': {}, 'papers_2016_count': 0, 'physical_activity_count': 4, 'physical_activity_2016_count': 0, 'sample_papers_2016_physical_activity': []}, 'var_functions.execute_python:20': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'year_candidates': [], 'domains': ['physical activity', 'finances', 'location']}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_candidates': [], 'domains': []}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_candidates': [], 'domains': ['mental']}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_candidates': [], 'domains': []}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_candidates': [], 'domains': []}]}

exec(code, env_args)
