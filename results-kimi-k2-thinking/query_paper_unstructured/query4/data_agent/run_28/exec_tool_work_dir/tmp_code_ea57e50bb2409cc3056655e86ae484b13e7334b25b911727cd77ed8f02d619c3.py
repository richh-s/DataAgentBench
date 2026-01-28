code = """import json
import re

# Access the stored results
citations = locals()['var_functions.query_db:2']  # From SQLite Citations table
paper_docs = locals()['var_functions.query_db:3']  # From MongoDB paper_docs collection

# If they are file paths, load them
if isinstance(citations, str):
    with open(citations, 'r') as f:
        citations = json.load(f)

if isinstance(paper_docs, str):
    with open(paper_docs, 'r') as f:
        paper_docs = json.load(f)

# Analyze a sample of papers to understand structure
sample_papers = paper_docs[:10]
analysis = []

for i, doc in enumerate(sample_papers):
    filename = doc.get('filename', '')
    text = doc.get('text', '')[:500]  # First 500 chars
    
    # Look for year patterns
    year_patterns = [r"\b201[0-9]\b", r"\b202[0-5]\b"]
    years_found = []
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        years_found.extend(matches)
    
    # Look for venue patterns
    venue_patterns = [r"CHI", r"UbiComp", r"Ubicomp", r"CSCW", r"DIS", r"PervasiveHealth", r"WWW", r"IUI"]
    venues_found = []
    for pattern in venue_patterns:
        if re.search(pattern, text):
            venues_found.append(pattern)
    
    # Check for physical activity keywords
    physical_activity_keywords = ['physical activity', 'fitness', 'exercise', 'activity tracking', 'wearable', 'steps', 'walking', 'running']
    text_lower = text.lower()
    has_physical_activity = any(keyword in text_lower for keyword in physical_activity_keywords)
    
    analysis.append({
        'index': i,
        'filename': filename,
        'years_found': years_found,
        'venues_found': venues_found,
        'has_physical_activity': has_physical_activity,
        'text_preview': text[:200]
    })

print('__RESULT__:')
print(json.dumps(analysis, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_docs_count': 1405, 'citations_count': 5, 'first_paper_keys': ['id', 'title', 'citation_count', 'citation_year'], 'first_citation_keys': ['_id', 'filename', 'text']}, 'var_functions.execute_python:14': 'file_storage/functions.execute_python:14.json', 'var_functions.execute_python:16': []}

exec(code, env_args)
