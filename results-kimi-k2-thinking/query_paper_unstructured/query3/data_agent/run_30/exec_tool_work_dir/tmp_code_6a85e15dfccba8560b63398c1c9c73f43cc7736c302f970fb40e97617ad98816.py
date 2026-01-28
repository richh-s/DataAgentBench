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

# Process first 10 papers to debug
print("=== DEBUG: First 10 papers ===")
for i, doc in enumerate(paper_docs[:10]):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    # Pattern 1: Conference notation like "CHI '17"
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
    text_lower = text.lower()
    if not has_empirical:
        terms = ['we conducted', 'we surveyed', 'we interviewed', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study']
        for term in terms:
            if term in text_lower:
                has_empirical = True
                break
    
    has_citations = title in citations_dict
    
    print(f"{i+1}. {title[:50]}...")
    print(f"   Year: {year}")
    print(f"   Empirical: {has_empirical}")
    print(f"   Has citations: {has_citations}")
    if has_citations:
        print(f"   Citations: {citations_dict[title]}")
    print()

# Summary statistics
has_year_count = 0
has_empirical_count = 0
has_citations_count = 0
after_2016_count = 0

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    match = re.search(r"(?:CHI|UbiComp|DIS|CSCW|WWW|IUI|TEI|AH|OzCHI|PervasiveHealth)\s+'?(\d{2})\b", text)
    if match:
        year_str = match.group(1)
        year_num = int(year_str)
        year = 2000 + year_num if year_num < 50 else 1900 + year_num
    
    if not year:
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    if year:
        has_year_count += 1
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    if not has_empirical:
        terms = ['we conducted', 'we surveyed', 'we interviewed', 'study', 'experiment', 'evaluation', 'participant', 'user study', 'field study']
        text_lower = text.lower()
        for term in terms:
            if term in text_lower:
                has_empirical = True
                break
    
    if has_empirical:
        has_empirical_count += 1
    
    has_citations = title in citations_dict
    if has_citations:
        has_citations_count += 1
    
    if year and year > 2016:
        after_2016_count += 1

print("=== SUMMARY ===")
print(f"Total papers: {len(paper_docs)}")
print(f"Papers with extractable year: {has_year_count}")
print(f"Papers published after 2016: {after_2016_count}")
print(f"Papers with empirical contribution: {has_empirical_count}")
print(f"Papers with citation data: {has_citations_count}")
print(f"Citations records total: {len(citations)}")

# Check for matching titles
matching_titles = 0
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title in citations_dict:
        matching_titles += 1

print(f"Papers with matching titles in citations: {matching_titles}")

print("__RESULT__:")
print(json.dumps({
    "total_papers": len(paper_docs),
    "papers_with_year": has_year_count,
    "papers_after_2016": after_2016_count,
    "papers_with_empirical": has_empirical_count,
    "papers_with_citations": has_citations_count,
    "matching_titles": matching_titles
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:36': 'file_storage/functions.query_db:36.json', 'var_functions.list_db:38': ['Citations', 'sqlite_sequence'], 'var_functions.execute_python:44': []}

exec(code, env_args)
