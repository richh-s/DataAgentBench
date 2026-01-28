code = """import json
import re

# Get file paths
mongo_file = locals()['var_functions.query_db:2']
citations_file = locals()['var_functions.query_db:22']

# Load MongoDB data
with open(mongo_file, 'r') as f:
    papers_data = json.load(f)

# Load citations data
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create a dict of titles to total citations
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_totals[title] = citation_totals.get(title, 0) + count

# Find all papers and extract physical activity domain
physical_activity_papers = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Try to find year - look for conference years like '16 or 2016
    # Check first lines, copyright, and conference headers
    text_lower = text.lower()
    
    # Check for physical activity domain
    is_physical_activity = 'physical activity' in text_lower
    
    if title and is_physical_activity:
        # Try multiple patterns to find year
        year = None
        
        # Pattern 1: Full year like 2016
        year_match = re.search(r'\b(20[12][0-9])\b', text)
        if year_match:
            year = int(year_match.group(1))
        
        # Pattern 2: Conference notation like '16
        conf_match = re.search(r"[A-Z][a-z]+\s+'([0-9]{2}),", text)
        if conf_match and not year:
            year_str = conf_match.group(1)
            if year_str.startswith(('1', '2')):
                year = int('20' + year_str)
        
        # Pattern 3: Look in first 500 chars for year
        first_part = text[:500]
        first_year = re.search(r'\b(20[12][0-9])\b', first_part)
        if first_year and not year:
            year = int(first_year.group(1))
        
        if year == 2016:
            physical_activity_papers.append({
                'title': title,
                'year': year,
                'total_citations': citation_totals.get(title, 0)
            })

result = {
    'papers_2016_physical_activity': physical_activity_papers,
    'count': len(physical_activity_papers)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:14': {'year_distribution': {}, 'physical_activity_papers_by_year': {}, 'counts_by_year': {}}, 'var_functions.execute_python:18': {'total_physical_activity_papers': 4, 'papers_2016': [], 'count_2016': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'papers_2016': [], 'physical_activity_papers_total': 0}, 'var_functions.execute_python:28': {'physical_activity_papers_by_year': {}, 'papers_2016': [], 'total_2016_papers': 0}}

exec(code, env_args)
