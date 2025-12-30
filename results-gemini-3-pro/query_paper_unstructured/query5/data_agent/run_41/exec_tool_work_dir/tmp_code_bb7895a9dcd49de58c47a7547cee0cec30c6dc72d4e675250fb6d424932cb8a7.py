code = """import json
import re

# Access file paths from storage
citations_file = locals()['var_function-call-31182004423683262']
papers_file = locals()['var_function-call-15517411522846928457']

# Load data
with open(citations_file, 'r') as f:
    citations = json.load(f)

with open(papers_file, 'r') as f:
    papers = json.load(f)

chi_titles = set()
chi_patterns = [
    r"CHI\s+'\d{2}",          # Matches CHI '15, CHI '99
    r"CHI\s+20\d{2}",        # Matches CHI 2015
    r"Conference on Human Factors in Computing Systems"
]

for p in papers:
    text = p.get('text', '')
    if not text:
        continue
        
    # Check the first 1000 characters (header usually)
    header = text[:1000]
    
    is_chi = False
    for pattern in chi_patterns:
        if re.search(pattern, header, re.IGNORECASE):
            is_chi = True
            break
            
    if is_chi:
        # Extract title from filename
        title = p['filename'].replace('.txt', '')
        chi_titles.add(title)

# Sum citation counts for CHI papers
total_citations = 0
for c in citations:
    # Ensure citation record is for 2020 (already filtered in SQL query but good to be safe if I used a different query)
    # The SQL query was: SELECT title, citation_count FROM Citations WHERE citation_year = 2020
    if c['title'] in chi_titles:
        total_citations += int(c['citation_count'])

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-31182004423683262': 'file_storage/function-call-31182004423683262.json', 'var_function-call-31182004423683057': 'file_storage/function-call-31182004423683057.json', 'var_function-call-15517411522846928457': 'file_storage/function-call-15517411522846928457.json'}

exec(code, env_args)
