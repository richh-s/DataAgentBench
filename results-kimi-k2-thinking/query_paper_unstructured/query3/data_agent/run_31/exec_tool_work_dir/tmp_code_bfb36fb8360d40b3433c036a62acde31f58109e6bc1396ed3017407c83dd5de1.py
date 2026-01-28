code = """import json
import re

# Load the full paper documents data
paper_docs_file = locals()['var_functions.query_db:24']
citations_file = locals()['var_functions.query_db:18']

with open(paper_docs_file, 'r') as f:
    papers_data = json.load(f)

with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Create citation lookup
citation_lookup = {}
for citation in citations_data:
    citation_lookup[citation['title']] = int(citation['total_citations'])

# Extract paper information
results = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Get title
    title = filename.replace('.txt', '')
    
    # Extract year with multiple patterns
    year = None
    # Pattern 1: Look for venue + year (e.g., CHI 2017)
    venue_pattern = r'(CHI|CSCW|Ubicomp|UbiComp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|CHI EA).{0,30}(20\d{2})'
    venue_match = re.search(venue_pattern, text[:5000], re.IGNORECASE)
    if venue_match:
        year = int(venue_match.group(2))
    
    # Pattern 2: Look for standalone 4-digit year
    if not year:
        year_match = re.search(r'\b(20\d{2})\b', text[:5000])
        if year_match:
            year = int(year_match.group(1))
    
    # Only process papers after 2016
    if not year or year <= 2016:
        continue
    
    # Check for empirical contribution
    text_lower = text.lower()
    has_empirical = False
    
    # Broader set of empirical indicators
    empirical_terms = [
        'empirical', 'study', 'survey', 'interview', 'interviews', 
        'experiment', 'experimental', 'user study', 'field study',
        'case study', 'evaluation', 'evaluated', 'participants',
        'participant', 'data collection', 'we conducted', 'we studied',
        'we interviewed', 'ethnographic', 'observation', 'longitudinal'
    ]
    
    for term in empirical_terms:
        if term in text_lower:
            has_empirical = True
            break
    
    if has_empirical:
        total_citations = citation_lookup.get(title, 0)
        results.append({
            'title': title,
            'year': year,
            'total_citations': total_citations
        })

# Sort by title
results.sort(key=lambda x: x['title'])

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': "<class 'str'>", 'var_functions.execute_python:14': 'Loaded 5 papers', 'var_functions.execute_python:16': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': 'empirical,artifact,methodological'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'total_citations': 266}], 'var_functions.execute_python:22': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'total_citations': 265}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'total_citations': 266}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json'}

exec(code, env_args)
