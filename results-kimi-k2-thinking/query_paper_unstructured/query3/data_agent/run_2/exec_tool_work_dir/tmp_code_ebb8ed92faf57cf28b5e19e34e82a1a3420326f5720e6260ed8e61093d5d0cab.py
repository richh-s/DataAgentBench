code = """import json
import re
from collections import defaultdict

# Load data
paper_docs_path = var_functions.query_db:2
citations_data = var_functions.query_db:5

with open(paper_docs_path, 'r') as f:
    paper_docs = json.load(f)

citations = citations_data

# Extract paper information
papers_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Extract year
    year_match = re.search(r'(20[0-2][0-9])', text[:1000])
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue
    venue = None
    venue_patterns = [
        r'CHI\s*\'?\d{2}', r'Ubicomp\s*\'?\d{2}', r'UbiComp\s*\'?\d{2}',
        r'CSCW\s*\'?\d{2}', r'DIS\s*\'?\d{2}', r'PervasiveHealth',
        r'WWW', r'IUI', r'OzCHI', r'TEI', r'AH', r'UIST', r'MobileHCI', r'ISS'
    ]
    
    for pattern in venue_patterns:
        match = re.search(pattern, text[:2000], re.IGNORECASE)
        if match:
            venue_match = match.group(0)
            venue = re.sub(r"\'?\d{2}$", "", venue_match).upper()
            break
    
    # Extract contributions
    contribution_patterns = {
        'empirical': r'\b(empirical|study|survey|interview|experiment|evaluation|user study|field study|case study)\b',
        'artifact': r'\b(artifact|system|prototype|tool|application|app|design|implementation)\b',
        'theoretical': r'\b(theoretical|theory|model|framework|conceptual|concept)\b',
        'survey': r'\b(survey|literature review|systematic review|meta-analysis)\b',
        'methodological': r'\b(methodological|method|methodology|approach|technique)\b'
    }
    
    contributions = []
    text_lower = text.lower()
    for contrib_name, pattern in contribution_patterns.items():
        if re.search(pattern, text_lower):
            contributions.append(contrib_name)
    
    papers_info.append({
        'title': title,
        'year': year,
        'contributions': contributions
    })

# Group citations
citations_by_title = defaultdict(list)
for citation in citations:
    cit_title = citation.get('title', '').lower()
    citations_by_title[cit_title].append({
        'citation_count': int(citation.get('citation_count', 0)),
        'citation_year': int(citation.get('citation_year', 0))
    })

# Find papers with empirical contribution after 2016
result = []
for paper in papers_info:
    if paper.get('year') and paper['year'] > 2016:
        if 'empirical' in paper.get('contributions', []):
            title_lower = paper['title'].lower()
            total_citations = 0
            
            if title_lower in citations_by_title:
                for citation in citations_by_title[title_lower]:
                    total_citations += citation['citation_count']
            
            result.append({
                'title': paper['title'],
                'total_citations': total_citations
            })

# Sort by citations
result.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
