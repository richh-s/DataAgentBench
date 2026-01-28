code = """import json
import re

# Load data
mongo_file = locals()['var_functions.query_db:38']
citations_file = locals()['var_functions.query_db:22']

with open(mongo_file, 'r') as f:
    papers_data = json.load(f)

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Build citation totals map
citation_totals = {}
for citation in citations_data:
    title = citation.get('title', '')
    count = int(citation.get('citation_count', 0))
    citation_totals[title] = citation_totals.get(title, 0) + count

def extract_year(text):
    # Try multiple patterns in order of preference
    patterns = [
        r'\b(2016)\b',  # Explicit 2016
        r"[A-Z]['’](16)\b",  # CHI '16 format
        r'Copyright\s+(20[12][0-9])',  # Copyright year
        r'\b(20[12][0-9])\b',  # Any year
        r'20[12][0-9]',  # Any year pattern
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(0)
            if len(year_str) == 2:  # Handle '16 format
                return int('20' + year_str)
            elif len(year_str) == 4:
                return int(year_str)
    return None

def check_physical_activity_domain(text):
    text_lower = text.lower()
    indicators = ['physical activity', 'activity tracking', 'fitness', 
                  'exercise', 'steps', 'walking', 'running', 'workout']
    return any(indicator in text_lower for indicator in indicators)

# Find 2016 physical activity papers
papers_2016 = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Skip if no title
    if not title:
        continue
    
    # Check domain
    is_pa = check_physical_activity_domain(text)
    
    # Extract year
    year = extract_year(text)
    
    # If it's physical activity and 2016, add to results
    if is_pa and year == 2016:
        total_cites = citation_totals.get(title, 0)
        papers_2016.append({
            'title': title,
            'year': year,
            'total_citations': total_cites
        })

# Result preparation
result = {
    'papers_2016_physical_activity': papers_2016,
    'total_count': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:14': {'year_distribution': {}, 'physical_activity_papers_by_year': {}, 'counts_by_year': {}}, 'var_functions.execute_python:18': {'total_physical_activity_papers': 4, 'papers_2016': [], 'count_2016': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'papers_2016': [], 'physical_activity_papers_total': 0}, 'var_functions.execute_python:28': {'physical_activity_papers_by_year': {}, 'papers_2016': [], 'total_2016_papers': 0}, 'var_functions.execute_python:32': {'papers_2016_physical_activity': [], 'count': 0}, 'var_functions.execute_python:36': {'papers': [], 'total_papers': 0}, 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.execute_python:40': 'file_storage/functions.execute_python:40.json'}

exec(code, env_args)
