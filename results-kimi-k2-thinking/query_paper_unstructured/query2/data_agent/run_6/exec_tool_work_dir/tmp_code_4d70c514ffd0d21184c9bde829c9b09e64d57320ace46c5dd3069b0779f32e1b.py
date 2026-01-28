code = """import json
import re

citations_key = 'var_functions.query_db:0'
papers_key = 'var_functions.query_db:2'

citations_var = locals()[citations_key]
papers_var = locals()[papers_key]

# Load citations data
citations = []
if isinstance(citations_var, str) and citations_var.endswith('.json'):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_var

# Load papers data
papers = []
if isinstance(papers_var, str) and papers_var.endswith('.json'):
    with open(papers_var, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_var

print('Loaded', len(citations), 'citations and', len(papers), 'papers')

# Extract paper metadata
paper_metadata = []
for doc in papers:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    source = None
    text_lower = text.lower()
    if 'acm' in text_lower:
        source = 'ACM'
    elif 'ieee' in text_lower:
        source = 'IEEE'
    elif 'pubmed' in text_lower or 'nih' in text_lower:
        source = 'PubMed'
    
    year = None
    header = text[:1000]
    year_matches = re.findall(r'\b(20\d{2})\b', header)
    if year_matches:
        valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2024]
        if valid_years:
            year = min(valid_years)
    
    if not year:
        patterns = [r'CHI\s*\'?\s*(20\d{2})', r'Ubicomp\s*\'?\s*(20\d{2})', r'CSCW\s*\'?\s*(20\d{2})']
        for pat in patterns:
            match = re.search(pat, text, re.IGNORECASE)
            if match:
                y = int(match.group(1))
                if 2000 <= y <= 2024:
                    year = y
                    break
    
    paper_metadata.append({'title': title.lower().strip(), 'source': source, 'year': year})

print('Extracted metadata for', len(paper_metadata), 'papers')

# Map for lookup
paper_map = {p['title']: p for p in paper_metadata}

# Find ACM papers in 2018 citations
acm_counts = []
matched = 0

for citation in citations:
    cit_title = citation.get('title', '').lower().strip()
    cit_count = int(citation.get('citation_count', 0))
    
    paper = paper_map.get(cit_title)
    if paper:
        matched += 1
        if paper['source'] == 'ACM':
            acm_counts.append(cit_count)

print('Matched', matched, 'citations to papers')
print('Found', len(acm_counts), 'ACM papers with citations')

# Calculate average
if acm_counts:
    avg = sum(acm_counts) / len(acm_counts)
    result_str = f"{avg:.2f}"
else:
    result_str = "0.00"

print("Average citation count:", result_str)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
