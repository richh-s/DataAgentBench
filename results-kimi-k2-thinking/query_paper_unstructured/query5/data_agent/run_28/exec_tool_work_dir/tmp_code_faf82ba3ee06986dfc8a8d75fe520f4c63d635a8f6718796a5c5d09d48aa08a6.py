code = """import json
import re

# Load data from stored file paths
citations_path = var_functions.query_db:0
papers_path = var_functions.query_db:6

with open(citations_path, 'r') as f:
    citations_2020 = json.load(f)

with open(papers_path, 'r') as f:
    paper_docs = json.load(f)

# Build paper info lookup
paper_info = {}
for paper in paper_docs:
    if 'filename' in paper:
        title = paper['filename'].replace('.txt', '')
        text = paper.get('text', '')
        
        # Extract year information
        year = None
        # Look for patterns like CHI'15, CHI 2015, or just 2015
        year_patterns = [
            r"CHI\s*['’]\s*(\d{2})",
            r"\bCHI\s*\d{4}\b",
            r"\b(20|19)\d{2}\b"
        ]
        
        for pattern in year_patterns:
            match = re.search(pattern, text)
            if match:
                matched_text = match.group(0)
                # Extract 4-digit year
                year_match = re.search(r"\d{4}", matched_text)
                if year_match:
                    year = int(year_match.group(0))
                break
        
        # Check if this is a CHI paper
        is_chi = 'CHI' in text or 'chi' in paper['filename'].lower()
        
        paper_info[title] = {
            'venue': 'CHI' if is_chi else 'Other',
            'year': year
        }

# Find CHI papers cited in 2020
chi_citations = []
total_citations = 0

for citation in citations_2020:
    title = citation['title']
    if title in paper_info and paper_info[title]['venue'] == 'CHI':
        count = int(citation['citation_count'])
        chi_citations.append({
            'title': title,
            'citation_count': count,
            'publication_year': paper_info[title]['year']
        })
        total_citations += count

print('__RESULT__:')
result = {
    'total_chi_papers_cited': len(chi_citations),
    'total_citation_count_2020': total_citations,
    'chi_papers_details': chi_citations
}
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:30': {'citations_type': "<class 'str'>", 'citations_preview': 'file_storage/functions.query_db:0.json', 'papers_type': "<class 'str'>", 'papers_preview': 'file_storage/functions.query_db:6.json'}}

exec(code, env_args)
