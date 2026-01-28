code = """import json
import re

# Access stored variables
paper_docs_path = locals()['var_functions.query_db:34']
citations_path = locals()['var_functions.query_db:36']

# Load data
with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

with open(citations_path, 'r') as f:
    citations = json.load(f)

# Create citations dictionary
citations_dict = {}
for c in citations:
    citations_dict[c['title']] = int(c['total_citations'])

# Process papers
results = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    # Pattern 1: Conference notation like "CHI '17"
    import re
    match = re.search(r"(?:CHI|UbiComp|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b", text)
    if match:
        year_str = match.group(1)
        year_num = int(year_str)
        year = 2000 + year_num if year_num < 50 else 1900 + year_num
    
    # Pattern 2: Explicit year like "2017"
    if not year:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Check methodology terms if not explicitly empirical
    if not has_empirical:
        terms = ['we conducted', 'we surveyed', 'we interviewed', 'study', 'experiment', 'evaluation', 'participant', 'user study']
        text_lower = text.lower()
        for term in terms:
            if term in text_lower:
                has_empirical = True
                break
    
    # Filter and collect results
    if has_empirical and year and year > 2016:
        total_citations = citations_dict.get(title, 0)
        if total_citations > 0:
            results.append({'title': title, 'total_citations': total_citations})

# Sort by citations
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

output = json.dumps(results_sorted, indent=2)
print("__RESULT__:")
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
