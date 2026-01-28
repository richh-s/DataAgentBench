code = """import json
import re

# Load paper documents
papers_path = locals()['var_functions.query_db:26']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
citations_path = locals()['var_functions.query_db:27']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Debug: Check what we have
print('Number of papers:', len(papers))
print('Number of citation entries:', len(citations))

# Sample some papers to see structure
sample_papers = papers[:3]
for i, paper in enumerate(sample_papers):
    filename = paper.get('filename', '')
    text_preview = paper.get('text', '')[:500]
    print(f'\nPaper {i+1}:')
    print('Filename:', filename)
    print('Title extracted:', filename.replace('.txt', '') if filename else '')
    
    # Try to find year
    year_match = re.search(r"\b(20(?:1[0-9]|2[0-9]))\b", text_preview)
    year = year_match.group(1) if year_match else 'Not found'
    print('Year found:', year)
    
    # Check for empirical
    has_empirical = 'empirical' in text_preview.lower()
    print('Has empirical:', has_empirical)

# Show some citations
sample_citations = citations[:5]
print('\nSample citations:')
for i, cit in enumerate(sample_citations):
    print(f"{i+1}. Title: {cit.get('title', '')[:60]}... Count: {cit.get('citation_count', 0)}")

result = {'papers_loaded': len(papers), 'citations_loaded': len(citations)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}, 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.execute_python:30': []}

exec(code, env_args)
