code = """import json
import re

# Load data from storage
citations_path = locals()['var_functions.query_db:5']
papers_path = locals()['var_functions.query_db:6']

with open(citations_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

# Process papers to extract metadata
processed_papers = []

for paper in papers:
    processed = {}
    
    # Extract title from filename
    if 'filename' in paper:
        processed['title'] = paper['filename'].replace('.txt', '')
    else:
        continue
    
    # Extract year from text (look for patterns like 20XX, 'XX, etc.)
    if 'text' in paper:
        text = paper['text']
        
        # Look for year patterns
        year_patterns = [
            r'\b(20\d{2})\b',  # 2015, 2016, etc.
            r"'([0-9]{2})\b",   # '15, '16, etc.
        ]
        
        for pattern in year_patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                if pattern == r"'([0-9]{2})\b":
                    year = 2000 + int(match)
                else:
                    year = int(match)
                
                # Only consider valid conference years (2010-2025)
                if 2010 <= year <= 2025:
                    processed['year'] = year
                    break
            
            if 'year' in processed:
                break
        
        # Extract contribution type
        if re.search(r'empirical', text, re.IGNORECASE):
            processed['contribution'] = ['empirical']
        else:
            processed['contribution'] = []
    
    processed_papers.append(processed)

# Filter papers: empirical contribution and year > 2016
filtered_papers = []
for paper in processed_papers:
    if paper.get('year') and paper['year'] > 2016:
        if 'empirical' in paper.get('contribution', []):
            filtered_papers.append(paper)

# Calculate total citations per paper
total_citations = {}
for cite in citations:
    title = cite['title']
    count = int(cite['citation_count'])
    
    if title not in total_citations:
        total_citations[title] = 0
    total_citations[title] += count

# Get final results
results = []
for paper in filtered_papers:
    title = paper['title']
    citation_count = total_citations.get(title, 0)
    results.append({
        'title': title,
        'total_citation_count': citation_count
    })

# Also check all papers to see what we have for debugging
all_papers_info = []
for paper in processed_papers:
    title = paper['title']
    year = paper.get('year', 'unknown')
    contrib = paper.get('contribution', [])
    citation_count = total_citations.get(title, 0)
    all_papers_info.append({
        'title': title,
        'year': year,
        'contribution': contrib,
        'citations': citation_count
    })

print('__RESULT__:')
print(json.dumps({
    'filtered_results': results,
    'all_papers': all_papers_info
}, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:16': {'num_citations': 1405, 'num_papers': 5}, 'var_functions.execute_python:18': [], 'var_functions.execute_python:20': 'file_storage/functions.execute_python:20.json'}

exec(code, env_args)
