code = """import json
import re

# Load all papers from MongoDB
papers_file = locals()['var_functions.query_db:10']
papers = []
with open(papers_file, 'r') as f:
    papers = json.load(f)

# More robust domain extraction
paper_info = {}
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '').lower()
    
    # Initialize with basic info
    info = {
        'title': title,
        'domains': [],
        'venue': None,
        'year': None
    }
    
    # Extract venue - look for patterns like CHI, Ubicomp, CSCW, etc.
    venue_pattern = r"(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH) \\'\d{2}"
    venue_match = re.search(venue_pattern, text)
    if venue_match:
        info['venue'] = venue_match.group(1)
    
    # Extract year - look for 4-digit years
    year_pattern = r"\b(20\d{2})\b"
    year_matches = re.findall(year_pattern, text)
    if year_matches:
        info['year'] = max(year_matches)  # Use the max year found
    
    # Extract domains - more comprehensive search
    domain_keywords = {
        'food': [r'\bfood\b', r'dietar', r'eating', r'nutrition'],
        'physical activity': [r'\bphysical activity\b', r'exercise\b', r'fitness\b'],
        'sleep': [r'\bsleep\b'],
        'mental': [r'\bmental\b', r'anxiety\b', r'depression\b'],
        'finances': [r'\bfinance\b', r'expense\b', r'cost\b'],
        'productivity': [r'\bproductivity\b', r'task\b', r'work\b'],
        'screen time': [r'screen time', r'digital', r'smartphone'],
        'social interactions': [r'social', r'interaction\b'],
        'location': [r'\blocation\b', r'place\b', r'gps\b'],
        'health_behavior': [r'health behavior', r'self-track', r'personal informatics']
    }
    
    domains_found = []
    for domain, patterns in domain_keywords.items():
        for pattern in patterns:
            if re.search(pattern, text):
                domains_found.append(domain)
                break
    
    info['domains'] = list(set(domains_found))  # Remove duplicates
    
    if title:
        paper_info[title] = info

# Find food papers
food_papers = []
for title, info in paper_info.items():
    if 'food' in info['domains']:
        food_papers.append(title)

print('__RESULT__:')
print(json.dumps({
    "paper_analysis": paper_info,
    "food_papers": food_papers
}))"""

env_args = {'var_functions.query_db:0': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'citations_count': 1405, 'papers_count': 5}, 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.execute_python:12': {'total_papers': 5, 'total_citations': 1405}, 'var_functions.execute_python:14': {'total_papers_loaded': 5, 'papers_with_titles': 5, 'food_papers_found': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'food_papers_count': 3}, 'var_functions.execute_python:16': {'food_papers': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'total_food_citations': 876, 'citation_records_found': 17}}

exec(code, env_args)
