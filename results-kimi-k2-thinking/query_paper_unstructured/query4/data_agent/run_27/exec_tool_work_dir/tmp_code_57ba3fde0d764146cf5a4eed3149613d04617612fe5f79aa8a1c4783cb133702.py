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
physical_activity_2016 = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Debug: print what we're working with
    print(f"Checking: {title}")
    
    # Check for physical activity domain - look for the phrase or related terms
    text_lower = text.lower()
    is_physical_activity = 'physical activity' in text_lower
    
    if is_physical_activity:
        print(f"  -> Found physical activity domain")
        
        # Try multiple patterns to find year
        year = None
        
        # Pattern 1: Full year like 2016
        year_match = re.search(r'\b(2016)\b', text)
        if year_match:
            year = int(year_match.group(1))
            print(f"  -> Found year: {year}")
        
        # Pattern 2: Conference notation like '16
        conf_match = re.search(r"[A-Z]['’](16)", text)
        if conf_match and not year:
            year = 2016
            print(f"  -> Found conference year: {year}")
        
        # Pattern 3: Look for "2016" specifically in the text
        if '2016' in text:
            year = 2016
            print(f"  -> Found 2016 in text")
        
        if year == 2016:
            total_cites = citation_totals.get(title, 0)
            physical_activity_2016.append({
                'title': title,
                'year': year,
                'total_citations': total_cites
            })
            print(f"  -> ADDED: {title} with {total_cites} citations")

# Also try substring matching - maybe the titles don't match exactly
if not physical_activity_2016:
    print("\nTrying fuzzy matching...")
    
    # Get all physical activity papers regardless of year first
    physical_activity_papers = []
    for doc in papers_data:
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        title = filename.replace('.txt', '') if filename else ''
        
        if 'physical activity' in text.lower():
            # Try to find any year
            year_match = re.search(r'\b(20[12][0-9])\b', text)
            year = int(year_match.group(1)) if year_match else None
            
            physical_activity_papers.append({
                'title': title,
                'year': year
            })
    
    print(f"Found {len(physical_activity_papers)} physical activity papers:")
    for paper in physical_activity_papers:
        print(f"  - {paper['title']} ({paper['year']})")
        
        # Check citations for this paper
        if paper['title'] in citation_totals:
            print(f"    -> Citations: {citation_totals[paper['title']]}")

result = {
    'papers_2016_physical_activity': physical_activity_2016,
    'count': len(physical_activity_2016)
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': {'total_papers_found': 0, 'papers_2016': [], 'count_2016': 0}, 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.execute_python:14': {'year_distribution': {}, 'physical_activity_papers_by_year': {}, 'counts_by_year': {}}, 'var_functions.execute_python:18': {'total_physical_activity_papers': 4, 'papers_2016': [], 'count_2016': 0}, 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.execute_python:26': {'papers_2016': [], 'physical_activity_papers_total': 0}, 'var_functions.execute_python:28': {'physical_activity_papers_by_year': {}, 'papers_2016': [], 'total_2016_papers': 0}, 'var_functions.execute_python:32': {'papers_2016_physical_activity': [], 'count': 0}}

exec(code, env_args)
