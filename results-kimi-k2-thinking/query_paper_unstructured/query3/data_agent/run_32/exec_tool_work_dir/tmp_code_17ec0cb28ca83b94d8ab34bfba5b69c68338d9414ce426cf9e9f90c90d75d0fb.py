code = """import json
import re

# Step 1: Process MongoDB papers
storage_key_mongo = 'var_functions.query_db:34'
mongo_result = locals()[storage_key_mongo]

if isinstance(mongo_result, str) and mongo_result.endswith('.json'):
    with open(mongo_result, 'r') as f:
        all_papers = json.load(f)
else:
    all_papers = mongo_result

papers_info = {}

# Extract year and check for empirical contribution
for paper in all_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    # Extract year from text
    year = None
    patterns = [
        r"[A-Z][a-zA-Z]*\s+'(\d{2})\b",
        r"\b(20\d{2})\b"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = 2000 + int(year_str)
            else:
                year = int(year_str)
            break
    
    # Check if paper has empirical contribution
    text_lower = text.lower()
    has_empirical = False
    
    if 'empirical' in text_lower or 'empirically' in text_lower:
        has_empirical = True
    else:
        # Look for research methodology indicators in first part of text
        intro_section = text_lower[:1500]
        research_indicators = [
            'we conducted', 'we performed', 'we studied', 'we surveyed',
            'experiment', 'user study', 'field study', 'case study',
            'participants', 'subjects', 'interview', 'survey'
        ]
        count = sum(1 for indicator in research_indicators if indicator in intro_section)
        if count >= 2:
            has_empirical = True
    
    papers_info[title.lower()] = {
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    }

print('Processed papers: ' + str(len(papers_info)))

# Step 2: Process citation data
storage_key_citations = 'var_functions.query_db:35'
citation_result = locals()[storage_key_citations]

if isinstance(citation_result, str) and citation_result.endswith('.json'):
    with open(citation_result, 'r') as f:
        citations = json.load(f)
else:
    citations = citation_result

citation_map = {}
for cit in citations:
    citation_title = cit['title']
    total_citations = int(cit['total_citations'])
    citation_map[citation_title.lower()] = {
        'original_title': citation_title,
        'total_citations': total_citations
    }

print('Citation map size: ' + str(len(citation_map)))

# Step 3: Find matches - empirical papers after 2016 with citations
result = []

for paper_lower, paper_info in papers_info.items():
    year = paper_info['year']
    has_empirical = paper_info['has_empirical']
    
    if year and year > 2016 and has_empirical:
        if paper_lower in citation_map:
            citation_data = citation_map[paper_lower]
            result.append({
                'title': citation_data['original_title'],
                'year': year,
                'total_citations': citation_data['total_citations']
            })

# Sort by citations
result_sorted = sorted(result, key=lambda x: x['total_citations'], reverse=True)

print('Matching papers found: ' + str(len(result_sorted)))

# Save full results
output = {
    'papers': result_sorted,
    'count': len(result_sorted)
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:10': [], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:14': [], 'var_functions.execute_python:22': [], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:30': [], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:35': 'file_storage/functions.query_db:35.json'}

exec(code, env_args)
