code = """import json
import re

# Load all papers again
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Load citations data
citations_file_path = locals()['var_functions.query_db:18']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Extract paper information more comprehensively
papers_info = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - multiple patterns
    year = None
    
    # Pattern 1: Look for 20XX in first 3000 chars
    year_match = re.search(r'\b(20\d{2})\b', text[:3000])
    if year_match:
        year = int(year_match.group(1))
    
    # Pattern 2: Look for venue + year
    if not year:
        venue_pattern = r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp).{0,20}(20\d{2})'
        venue_match = re.search(venue_pattern, text[:3000], re.IGNORECASE)
        if venue_match:
            year = int(venue_match.group(2))
            
    # Pattern 3: Look for year in parentheses
    if not year:
        paren_year = re.search(r'\((20\d{2})\)', text[:3000])
        if paren_year:
            year = int(paren_year.group(1))
    
    # Check for empirical contribution
    has_empirical = False
    text_lower = text.lower()
    
    # Look for empirical indicators (more comprehensive)
    empirical_indicators = [
        'empirical', 'user study', 'field study', 'interview', 'interviews',
        'survey', 'experiment', 'experimental', 'case study', 'evaluation',
        'evaluated', 'participants', 'participant', 'we conducted', 
        'we studied', 'we interviewed', 'data collection', 'we surveyed',
        'user research', 'fieldwork', 'ethnographic', 'observation',
        'longitudinal study', 'controlled study'
    ]
    
    for indicator in empirical_indicators:
        if indicator in text_lower:
            has_empirical = True
            break
    
    if has_empirical:
        papers_info.append({
            'title': title,
            'year': year
        })

# Filter papers published after 2016
filtered_papers = [p for p in papers_info if p['year'] and p['year'] > 2016]

# Create citation lookup
citation_dict = {}
for citation in citations_data:
    citation_dict[citation.get('title', '')] = int(citation.get('total_citations', 0))

# Get results
results = []
for paper in filtered_papers:
    title = paper['title']
    if title in citation_dict:
        results.append({
            'title': title,
            'year': paper['year'],
            'total_citations': citation_dict[title]
        })

# Sort by year then citations
results.sort(key=lambda x: (x['year'], -x['total_citations']))

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': "<class 'str'>", 'var_functions.execute_python:14': 'Loaded 5 papers', 'var_functions.execute_python:16': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': 'empirical,artifact,methodological'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'total_citations': 266}]}

exec(code, env_args)
