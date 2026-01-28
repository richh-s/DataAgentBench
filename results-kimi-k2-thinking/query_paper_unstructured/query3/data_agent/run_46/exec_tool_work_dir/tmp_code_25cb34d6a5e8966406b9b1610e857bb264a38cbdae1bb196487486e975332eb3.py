code = """import json
import re

# Load paper documents
paper_docs_path = locals()['var_functions.query_db:8']
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

# Load citations data
citations_path = locals()['var_functions.query_db:9']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Parse paper metadata from text
papers = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Try to extract year from text (look for 4-digit year patterns like '2015', "'15", etc.)
    year = None
    year_patterns = [
        r'\b(20\d{2})\b',  # four digit years starting with 20
        r"'\b(\d{2})\b",   # two digit years with apostrophe
    ]
    
    # Look for year in the first 500 characters (usually in header)
    header = text[:1000]
    
    # Try to find four-digit year first
    year_match = re.search(r'\b(20\d{2})\b', header)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Try two-digit format like '17
        year_match = re.search(r"'\s*(\d{2})\b", header)
        if year_match:
            year_num = int(year_match.group(1))
            if year_num < 50:
                year = 2000 + year_num
            else:
                year = 1900 + year_num
    
    # Try to extract contribution types from text
    contribution = []
    # Look for common contribution patterns
    contribution_patterns = [
        r'empirical', r'artifact', r'theoretical', r'survey', r'methodological',
        r'empiric', r'implementation', r'design', r'evaluation', r'study',
        r'case study', r'field study', r'user study'
    ]
    
    # Search in abstract and introduction sections
    lower_text = text.lower()
    
    # Check if 'empirical' appears
    has_empirical = 'empirical' in lower_text
    
    # Also check for study types
    has_study = any(s in lower_text for s in ['study', 'evaluation', 'experiment'])
    
    papers.append({
        'title': title,
        'filename': filename,
        'year': year,
        'text_sample': text[:200],
        'has_empirical': has_empirical,
        'has_study': has_study
    })

# Print the papers info
for p in papers:
    print(f"Title: {p['title']}")
    print(f"Year: {p['year']}")
    print(f"Has Empirical: {p['has_empirical']}")
    print(f"Has Study: {p['has_study']}")
    print("---")

print('__RESULT__:')
print(json.dumps(papers, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:16': 'file_storage/functions.execute_python:16.json'}

exec(code, env_args)
