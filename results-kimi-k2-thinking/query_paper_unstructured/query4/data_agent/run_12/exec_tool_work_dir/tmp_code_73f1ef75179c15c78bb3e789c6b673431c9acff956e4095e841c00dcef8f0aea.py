code = """import json
import re

# Load full papers data from MongoDB
mongo_key = 'var_functions.query_db:16'
papers_data = locals().get(mongo_key)

if isinstance(papers_data, str) and papers_data.endswith('.json'):
    with open(papers_data, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_data

# Load full citations data from SQLite
citations_key = 'var_functions.query_db:14'
citations_data = locals().get(citations_key)

if isinstance(citations_data, str) and citations_data.endswith('.json'):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

# Parse paper information
paper_info = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for year in text (common patterns like '2016' or 'CHI 2016')
    year_match = re.search(r'\b(20\d{2})\b', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check if paper is in 'physical activity' domain
    # Look for keywords in text
    domain_keywords = ['physical activity', 'physical activities', 'fitness', 'exercise', 'activity tracking']
    text_lower = text.lower()
    is_physical_activity = any(keyword in text_lower for keyword in domain_keywords)
    
    paper_info.append({
        'title': title,
        'year': year,
        'is_physical_activity': is_physical_activity,
        'filename': filename
    })

# Filter papers from 2016 in physical activity domain
papers_2016_pa = [p for p in paper_info if p['year'] == 2016 and p['is_physical_activity']]

print('__RESULT__:')
print(json.dumps({
    'total_papers': len(papers),
    'total_citations': len(citations),
    'papers_2016_pa': papers_2016_pa,
    'all_papers_info': paper_info
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:12': {'total_papers': 99, 'first_paper_sample': {'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}}, 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'total_papers_loaded': 5}}

exec(code, env_args)
