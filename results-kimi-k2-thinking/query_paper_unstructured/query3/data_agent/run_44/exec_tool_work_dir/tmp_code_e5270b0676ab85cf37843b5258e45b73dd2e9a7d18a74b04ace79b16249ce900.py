code = """import json
import re

papers_path = locals()['var_functions.query_db:6']
with open(papers_path, 'r') as f:
    papers = json.load(f)

output = []

for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    paper_info = {'title': title}
    
    # Try various year patterns
    year = None
    
    # Pattern 1: UbiComp 'XX, CHI 'XX etc.
    match = re.search(r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'(\d{2})", text, re.IGNORECASE)
    if match:
        year = 2000 + int(match.group(2))
        paper_info['year_found'] = 'venue_pattern'
    
    # Pattern 2: Full year 20XX
    if not year:
        match = re.search(r'\b(20\d{2})\b', text)
        if match:
            year = int(match.group(1))
            paper_info['year_found'] = 'full_pattern'
    
    # Pattern 3: Copyright year
    if not year:
        match = re.search(r'Copyright\s+(\d{4})', text)
        if match:
            year = int(match.group(1))
            paper_info['year_found'] = 'copyright'
    
    paper_info['year'] = year
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    paper_info['has_empirical'] = has_empirical
    paper_info['meets_criteria'] = (year is not None and year > 2016 and has_empirical)
    
    output.append(paper_info)

print('__RESULT__:')
print(json.dumps(output, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'num_citations': 1405, 'num_papers': 5}, 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json', 'var_functions.execute_python:22': {'filtered_results': [], 'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 'unknown', 'contribution': [], 'citations': 390}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 'unknown', 'contribution': [], 'citations': 220}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 'unknown', 'contribution': ['empirical'], 'citations': 266}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 'unknown', 'contribution': [], 'citations': 452}]}, 'var_functions.execute_python:28': [], 'var_functions.execute_python:30': 'file_storage/functions.execute_python:30.json'}

exec(code, env_args)
