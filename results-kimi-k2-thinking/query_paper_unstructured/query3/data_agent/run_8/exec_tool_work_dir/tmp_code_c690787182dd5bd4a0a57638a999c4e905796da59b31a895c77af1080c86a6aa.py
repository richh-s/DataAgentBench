code = """import json
import re

# The result is stored in a file, let's read it
file_path = var_functions.query_db:5

with open(file_path, 'r') as f:
    papers = json.load(f)

# Function to extract paper metadata
paper_data = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for patterns like '2017', '2018', etc.
    year_match = re.search(r'\b(20[0-9]{2})\b', text)
    year = int(year_match.group()) if year_match else None
    
    # Extract contribution type - look for 'empirical', 'artifact', 'theoretical', 'survey', 'methodological'
    contribution = []
    text_lower = text.lower()
    
    if 'empirical' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower or 'methodology' in text_lower:
        contribution.append('methodological')
    
    paper_data.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter papers after 2016 with empirical contribution
empirical_papers_2017_plus = [
    paper for paper in paper_data 
    if paper['year'] and paper['year'] > 2016 and 'empirical' in paper['contribution']
]

print(f"__RESULT__:")
print(json.dumps({
    "total_papers_processed": len(paper_data),
    "empirical_papers_after_2016": len(empirical_papers_2017_plus),
    "sample_empirical_papers": empirical_papers_2017_plus[:5]
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
