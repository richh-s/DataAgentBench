code = """import json
import re

citations_result = locals()['var_functions.query_db:0']
papers_result = locals()['var_functions.query_db:2']

citations_data = json.load(open(citations_result)) if isinstance(citations_result, str) else citations_result
papers_data = json.load(open(papers_result)) if isinstance(papers_result, str) else papers_result

# Extract paper info
papers = []
for doc in papers_data:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.endswith('.txt') else filename
    
    source = None
    t = text.lower()
    if 'acm' in t and 'association for computing machinery' in t:
        source = 'ACM'
    elif 'acm' in t:
        source = 'ACM'
    elif 'ieee' in t:
        source = 'IEEE'
    elif 'pubmed' in t or 'nih' in t:
        source = 'PubMed'
    
    year = None
    h = text[:1000]
    m = re.findall(r'\b(20\d{2})\b', h)
    if m:
        valid = [int(y) for y in m if 2000 <= int(y) <= 2024]
        if valid:
            year = min(valid)
    
    if not year:
        patterns = [r'CHI\s*\'?\s*(20\d{2})', r'Ubicomp\s*\'?\s*(20\d{2})', r'CSCW\s*\'?\s*(20\d{2})', r'DIS\s*\'?\s*(20\d{2})']
        for p in patterns:
            match = re.search(p, text, re.I)
            if match:
                y = int(match.group(1))
                if 2000 <= y <= 2024:
                    year = y
                    break
    
    papers.append({'title': title.lower(), 'source': source, 'year': year})

# Map titles to papers
paper_map = {p['title']: p for p in papers}

# Find ACM papers in citations
acm_counts = []
total_matched = 0

for citation in citations_data:
    title = citation.get('title', '').lower()
    count = int(citation.get('citation_count', 0))
    
    paper = paper_map.get(title)
    if paper:
        total_matched += 1
        if paper['source'] == 'ACM':
            acm_counts.append(count)

avg = sum(acm_counts) / len(acm_counts) if acm_counts else 0
result = '%.2f' % avg

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
