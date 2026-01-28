code = """import json
import re

# Read the papers data from file
file_path = locals()['var_functions.query_db:4']
with open(file_path, 'r') as f:
    papers_data = json.load(f)

# Read the citations data from file
citations_file_path = locals()['var_functions.query_db:18']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Extract paper information
papers_info = []
for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year - look for 4-digit year patterns
    year = None
    # Search in first part of text for year
    year_match = re.search(r'\b(20\d{2})\b', text[:2000])
    if year_match:
        year = int(year_match.group(1))
    
    # If not found, look for venue year pattern
    if not year:
        venue_pattern = r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).{0,10}(20\d{2})'
        venue_match = re.search(venue_pattern, text[:2000], re.IGNORECASE)
        if venue_match:
            year = int(venue_match.group(2))
    
    # Check for empirical contribution
    has_empirical = False
    text_lower = text.lower()
    
    # Look for empirical indicators
    empirical_indicators = [
        'empirical', 'user study', 'field study', 'interview', 'interviews',
        'survey', 'experiment', 'experimental', 'case study', 'evaluation',
        'evaluated', 'participants', 'participant'
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

# Create a dictionary for easy lookup
titles_to_find = [p['title'] for p in filtered_papers]

# Get citation counts for these papers
paper_citations = {}
for citation in citations_data:
    cite_title = citation.get('title', '')
    if cite_title in titles_to_find:
        if cite_title not in paper_citations:
            paper_citations[cite_title] = int(citation.get('total_citations', 0))

# Combine results
results = []
for paper in filtered_papers:
    title = paper['title']
    total_citations = paper_citations.get(title, 0)
    results.append({
        'title': title,
        'year': paper['year'],
        'total_citations': total_citations
    })

# Sort by citations (descending)
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': "<class 'str'>", 'var_functions.execute_python:14': 'Loaded 5 papers', 'var_functions.execute_python:16': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'contribution': 'empirical,artifact,methodological'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'contribution': 'empirical,theoretical,artifact,methodological'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'contribution': 'empirical,artifact,methodological'}], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
