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

print("=== PROCESSING ALL PAPERS ===")
results = []

for i, doc in enumerate(paper_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    print(f"Paper {i+1}: {title}")
    print(f"Text preview: {text[:200]}...")
    
    # Extract year - more thorough search
    year = None
    
    # Pattern 1: Conference notation like "CHI '17" or "UbiComp '15"
    conf_pattern = r"(?:CHI|UbiComp|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b"
    match = re.search(conf_pattern, text)
    if match:
        year_str = match.group(1)
        year_num = int(year_str)
        year = 2000 + year_num if year_num < 50 else 1900 + year_num
        print(f"Found conference year: {year}")
    
    # Pattern 2: Explicit year like "2015" or "2017" or "2018"
    if not year:
        year_pattern = r"\b(20\d{2})\b"
        match = re.search(year_pattern, text)
        if match:
            year = int(match.group(1))
            print(f"Found explicit year: {year}")
    
    # Pattern 3: Look for "Copyright 2015" or similar
    if not year:
        copyright_pattern = r"Copyright\s+(20\d{2})\b"
        match = re.search(copyright_pattern, text)
        if match:
            year = int(match.group(1))
            print(f"Found copyright year: {year}")
    
    print(f"Final extracted year: {year}")
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    print(f"Has 'empirical' keyword: {has_empirical}")
    
    if not has_empirical:
        terms = ['we conducted', 'we surveyed', 'we interviewed', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study', 'research']
        text_lower = text.lower()
        for term in terms:
            if term in text_lower:
                has_empirical = True
                print(f"Found methodology term: {term}")
                break
    
    print(f"Has empirical contribution: {has_empirical}")
    
    # Check citations
    has_citations = title in citations_dict
    print(f"Has citations in DB: {has_citations}")
    if has_citations:
        print(f"Total citations: {citations_dict[title]}")
    
    print("-" * 50)
    
    # Add to results if matches criteria
    if has_empirical and year and year > 2016 and has_citations:
        results.append({
            'title': title,
            'year': year,
            'total_citations': citations_dict[title]
        })

print("=== FINAL RESULTS ===")
print(f"Total papers matching criteria: {len(results)}")
for r in results:
    print(f"Title: {r['title']}")
    print(f"Year: {r['year']}")
    print(f"Citations: {r['total_citations']}")
    print()

# Format final output
output = json.dumps(results, indent=2)
print("__RESULT__:")
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:44': [], 'var_functions.execute_python:46': {'total_papers': 5, 'papers_with_year': 0, 'papers_after_2016': 0, 'papers_with_empirical': 5, 'papers_with_citations': 5, 'matching_titles': 5}}

exec(code, env_args)
