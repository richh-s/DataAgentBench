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

print("=== PROCESSING PAPERS WITH IMPROVED YEAR EXTRACTION ===")
results = []

for i, doc in enumerate(paper_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    print(f"Paper {i+1}: {title}")
    
    # Extract year - case-insensitive and more patterns
    year = None
    
    # Pattern 1: Conference notation like "UBICOMP '15" or "CHI '17" - case insensitive
    conf_pattern = r"(?:CHI|UbiComp|UBICOMP|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b"
    match = re.search(conf_pattern, text, re.IGNORECASE)
    if match:
        year_str = match.group(1)
        year_num = int(year_str)
        year = 2000 + year_num if year_num < 50 else 1900 + year_num
        print(f"  Found conference year: {year}")
    
    # Pattern 2: Copyright year like "Copyright 2015" or "Copyright 2017"
    if not year:
        copyright_pattern = r"Copyright\s+(20\d{2})\b"
        match = re.search(copyright_pattern, text)
        if match:
            year = int(match.group(1))
            print(f"  Found copyright year: {year}")
    
    # Pattern 3: Explicit year in text like "2017" or "2018" (but not part of citations/years)
    if not year:
        # Look for year patterns near conference/venue mentions
        year_context_pattern = r"(?:20\d{2})\b"
        matches = re.findall(year_context_pattern, text)
        for match in matches:
            year_candidate = int(match)
            if 2010 <= year_candidate <= 2030:  # Reasonable range
                year = year_candidate
                print(f"  Found explicit year: {year}")
                break
    
    print(f"  Final extracted year: {year}")
    
    # Check for empirical contribution (same as before)
    has_empirical = 'empirical' in text.lower()
    
    if not has_empirical:
        terms = ['we conducted', 'we surveyed', 'we interviewed', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study', 'research']
        text_lower = text.lower()
        for term in terms:
            if term in text_lower:
                has_empirical = True
                break
    
    print(f"  Has empirical contribution: {has_empirical}")
    print(f"  Has citations in DB: {title in citations_dict}")
    if title in citations_dict:
        print(f"  Total citations: {citations_dict[title]}")
    
    # Add to results if matches criteria
    if has_empirical and year and year > 2016 and title in citations_dict:
        results.append({
            'title': title,
            'year': year,
            'total_citations': citations_dict[title]
        })
        print(f"  *** MATCHED CRITERIA - Added to results ***")
    
    print()

print("=== SUMMARY ===")
print(f"Total papers processed: {len(paper_docs)}")
print(f"Papers matching criteria (empirical + after 2016 + has citations): {len(results)}")

# Sort by citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Output final results
output = json.dumps(results_sorted, indent=2)
print("__RESULT__:")
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:44': [], 'var_functions.execute_python:46': {'total_papers': 5, 'papers_with_year': 0, 'papers_after_2016': 0, 'papers_with_empirical': 5, 'papers_with_citations': 5, 'matching_titles': 5}, 'var_functions.execute_python:48': []}

exec(code, env_args)
