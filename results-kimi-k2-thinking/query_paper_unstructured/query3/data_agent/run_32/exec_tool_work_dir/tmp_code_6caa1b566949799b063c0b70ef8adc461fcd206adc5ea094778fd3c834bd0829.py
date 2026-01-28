code = """import json
import re

# Load MongoDB data
storage_key = 'var_functions.query_db:24'
mongo_result = locals()[storage_key]

if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r', encoding='utf-8') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

print('MongoDB total papers: ' + str(len(all_papers)))

# Process each paper to extract structured data
papers_by_title = {}

for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - try multiple patterns
    year = None
    
    # Pattern 1: CHI '17, UbiComp '15 format
    match = re.search(r"[A-Z][a-zA-Z]*\s+'(\d{2})\b", text)
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Pattern 2: Full year like 2017
        match = re.search(r"\b(20\d{2})\b", text)
        if match:
            year = int(match.group(1))
    
    # Check for empirical contribution (both direct and indirect indicators)
    text_lower = text.lower()
    has_empirical = False
    
    # Direct mention
    if 'empirical' in text_lower:
        has_empirical = True
    elif 'empirically' in text_lower:
        has_empirical = True
    else:
        # Check for research indicators in abstract/intro (first 2000 chars)
        intro_section = text_lower[:2000]
        indicators = ['we conducted', 'we performed', 'experiment', 'user study', 'field study', 'participants', 'subjects', 'data collection', 'interview', 'survey']
        count = sum(1 for ind in indicators if ind in intro_section)
        if count >= 2:
            has_empirical = True
    
    if title:
        papers_by_title[title] = {
            'year': year,
            'has_empirical': has_empirical,
            'filename': filename
        }

print('Processed papers: ' + str(len(papers_by_title)))

# Load citation data
storage_key = 'var_functions.query_db:26'
citation_result = locals()[storage_key]

if isinstance(citation_result, str) and citation_result.endswith('.json'):
    with open(citation_result, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = citation_result

print('Citations loaded: ' + str(len(citations)))

# Create a mapping of title to total citations
citation_map = {}
for cit in citations:
    citation_map[cit['title']] = int(cit['total_citations'])

print('Citation map size: ' + str(len(citation_map)))

# Now join and filter
result = []
for title, paper_info in papers_by_title.items():
    year = paper_info['year']
    has_empirical = paper_info['has_empirical']
    
    if year and year > 2016 and has_empirical:
        total_citations = citation_map.get(title, 0)
        result.append({
            'title': title,
            'year': year,
            'total_citations': total_citations
        })

# Sort by citations descending
result_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

print('Matching papers: ' + str(len(result_sorted)))

# Show top 10
print('\nTop papers:')
for i, paper in enumerate(result_sorted[:10]):
    print(str(i+1) + '. ' + paper['title'] + ' (' + str(paper['year']) + ') - ' + str(paper['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(result_sorted))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
