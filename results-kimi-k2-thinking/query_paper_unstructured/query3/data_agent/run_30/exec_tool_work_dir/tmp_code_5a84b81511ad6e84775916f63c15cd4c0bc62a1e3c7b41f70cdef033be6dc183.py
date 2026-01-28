code = """import json
import re

# Get the file paths from storage
paper_docs_path = var_functions.query_db:34
citations_path = var_functions.query_db:36

# Load and process the data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

print("Paper documents: %d" % len(paper_docs))
print("Citation records: %d" % len(citations))

# Process paper documents to extract title, year, and check for empirical contribution
def extract_paper_info(doc):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text using multiple patterns
    year = None
    
    # Pattern 1: Look for conference notation like "CHI '17" or "UbiComp '16"
    conf_pattern = r"(?:CHI|UbiComp|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b"
    match = re.search(conf_pattern, text)
    if match:
        year_str = match.group(1)
        year_num = int(year_str)
        year = 2000 + year_num if year_num < 50 else 1900 + year_num
    
    # Pattern 2: Look for explicit years like "2017" or "2018"
    if not year:
        year_pattern = r"\b(20\d{2})\b"
        match = re.search(year_pattern, text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical contribution - look for the word "empirical"
    has_empirical = 'empirical' in text.lower()
    
    # If not explicitly mentioned, check for research methodology indicators
    if not has_empirical:
        methodology_terms = ['we conducted', 'we surveyed', 'we interviewed', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study']
        text_lower = text.lower()
        for term in methodology_terms:
            if term in text_lower:
                has_empirical = True
                break
    
    return {
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    }

# Process all papers
papers = [extract_paper_info(doc) for doc in paper_docs]

# Create a dictionary of citations for easy lookup
citations_dict = {c['title']: int(c['total_citations']) for c in citations}

# Filter papers: empirical contribution AND published after 2016 AND has citations
results = []
for paper in papers:
    if paper['has_empirical'] and paper['year'] and paper['year'] > 2016:
        total_citations = citations_dict.get(paper['title'], 0)
        if total_citations > 0:
            results.append({
                'title': paper['title'],
                'total_citations': total_citations
            })

# Sort by citation count descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Print results following the required format
result_json = json.dumps(results_sorted, indent=2)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
