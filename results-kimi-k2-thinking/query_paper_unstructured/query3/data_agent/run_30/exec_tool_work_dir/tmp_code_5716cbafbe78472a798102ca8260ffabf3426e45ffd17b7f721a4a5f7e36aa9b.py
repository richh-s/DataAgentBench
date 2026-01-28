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
    
    # Extract year using comprehensive patterns
    year = None
    text_to_search = text[:2000]  # Search in first 2000 chars (usually covers header)
    
    # Pattern 1: Conference/journal venue with year like "UBICOMP '15" or "CHI 2017"
    # Match patterns like: UBICOMP '15, CHI 2017, CHI'17, etc.
    venue_pattern = r"\b(?:CHI|UbiComp|UBICOMP|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth|IEEE|ACM)\s*'?(\d{2,4})\b"
    match = re.search(venue_pattern, text_to_search, re.IGNORECASE)
    if match:
        year_str = match.group(1)
        if len(year_str) == 2:
            year_num = int(year_str)
            year = 2000 + year_num if year_num < 50 else 1900 + year_num
        elif len(year_str) == 4:
            year = int(year_str)
    
    # Pattern 2: Copyright year
    if not year:
        copyright_pattern = r"Copyright.*?(\d{4})"
        match = re.search(copyright_pattern, text_to_search)
        if match:
            year_candidate = int(match.group(1))
            if 2010 <= year_candidate <= 2030:
                year = year_candidate
    
    # Pattern 3: Explicit year in text (4-digit)
    if not year:
        year_pattern = r"\b(20\d{2})\b"
        matches = re.findall(year_pattern, text_to_search)
        for match in matches:
            year_candidate = int(match)
            if 2010 <= year_candidate <= 2030:
                year = year_candidate
                break
    
    # Pattern 4: Full date with year
    if not year:
        date_pattern = r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+(\d{4})\b"
        match = re.search(date_pattern, text_to_search)
        if match:
            year_candidate = int(match.group(2))
            if 2010 <= year_candidate <= 2030:
                year = year_candidate
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Check methodology terms if not explicitly empirical
    if not has_empirical:
        terms = ['we conducted', 'we surveyed', 'we interviewed', 'we collected', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study', 'research method']
        text_lower = text.lower()[:5000]
        for term in terms:
            if term in text_lower:
                has_empirical = True
                break
    
    # Filter and collect results
    if has_empirical and year and year > 2016 and title in citations_dict:
        results.append({
            'title': title,
            'total_citations': citations_dict[title]
        })

# Sort by citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Output final results
output = json.dumps(results_sorted, indent=2)
print("__RESULT__:")
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:44': [], 'var_functions.execute_python:46': {'total_papers': 5, 'papers_with_year': 0, 'papers_after_2016': 0, 'papers_with_empirical': 5, 'papers_with_citations': 5, 'matching_titles': 5}, 'var_functions.execute_python:48': [], 'var_functions.execute_python:50': []}

exec(code, env_args)
