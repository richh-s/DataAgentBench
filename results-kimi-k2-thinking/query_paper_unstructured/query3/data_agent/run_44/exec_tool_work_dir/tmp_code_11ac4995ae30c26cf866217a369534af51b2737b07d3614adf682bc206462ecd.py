code = """import json
import re

papers_path = locals()['var_functions.query_db:6']
with open(papers_path, 'r') as f:
    papers = json.load(f)

citations_path = locals()['var_functions.query_db:5']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Process each paper
results = []

for paper in papers:
    # Get title from filename
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Get text
    text = paper.get('text', '')
    
    # Extract year - look for patterns like 20XX or 'XX or conference years
    year = None
    
    # Pattern 1: Four digit year 20XX
    match1 = re.search(r'\b(20\d{2})\b', text)
    if match1:
        year = int(match1.group(1))
    else:
        # Pattern 2: 'XX format
        match2 = re.search(r"'([0-9]{2})\b", text)
        if match2:
            year = 2000 + int(match2.group(1))
    
    # Check if empirical (case-insensitive match for 'empirical')
    is_empirical = bool(re.search(r'empirical', text, re.IGNORECASE))
    
    # Skip if not after 2016 or not empirical
    if not (year and year > 2016 and is_empirical):
        continue
    
    # Calculate total citations
    total_citations = 0
    for cite in citations:
        if cite['title'] == title:
            total_citations += int(cite['citation_count'])
    
    results.append({
        'title': title,
        'year': year,
        'total_citation_count': total_citations
    })

# Return results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'num_citations': 1405, 'num_papers': 5}, 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'filtered_results': [], 'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 'unknown', 'contribution': [], 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 'unknown', 'contribution': [], 'citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 'unknown', 'contribution': [], 'citations': 452}]}}

exec(code, env_args)
