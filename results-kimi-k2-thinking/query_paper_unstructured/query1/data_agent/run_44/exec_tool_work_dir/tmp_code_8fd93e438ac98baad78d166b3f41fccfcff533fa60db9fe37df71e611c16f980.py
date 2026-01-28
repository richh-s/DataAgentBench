code = """import json
import re

# Access the file paths from storage
citations_file_path = locals()['var_functions.query_db:2']
papers_file_path = locals()['var_functions.query_db:5']

# Load the full data
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Process papers to extract domains
paper_domains = {}  # title -> domains list
for paper in papers_data:
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    
    # Extract domain information from text
    text = paper['text'].lower()
    
    domains = []
    
    # Check for food domain (and other common domains mentioned in hints)
    if 'food' in text:
        domains.append('food')
    if 'physical activity' in text:
        domains.append('physical activity')
    if 'sleep' in text:
        domains.append('sleep')
    if 'mental' in text:
        domains.append('mental')
    if 'finances' in text or 'financial' in text:
        domains.append('finances')
    if 'productivity' in text:
        domains.append('productivity')
    if 'screen time' in text:
        domains.append('screen time')
    if 'social interactions' in text:
        domains.append('social interactions')
    if 'location' in text:
        domains.append('location')
    if 'chronic' in text:
        domains.append('chronic')
    if 'diabetes' in text:
        domains.append('diabetes')
    if 'health behavior' in text or 'health_behaviour' in text:
        domains.append('health_behavior')
    
    # Store the domains for this paper
    paper_domains[title] = domains

# Match citations with papers and filter for food domain
total_citations = 0
food_papers_citations = {}

for citation in citations_data:
    title = citation['title']
    
    # Check if this paper is in the food domain
    if title in paper_domains and 'food' in paper_domains[title]:
        citation_count = int(citation['citation_count'])
        total_citations += citation_count
        
        # Track per paper
        if title not in food_papers_citations:
            food_papers_citations[title] = 0
        food_papers_citations[title] += citation_count

# Prepare result
result = {
    'total_citation_count': total_citations,
    'food_papers_count': len(food_papers_citations),
    'food_papers_details': food_papers_citations
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'citations_records': 100, 'paper_documents': 5}}

exec(code, env_args)
