code = """import json
import re

# Load the data from the file
file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    papers = json.load(f)

# Function to extract paper information from the text
def extract_paper_info(text, filename):
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Extract year from the text
    year_match = re.search(r'(CHI|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(\d{4})', text)
    if year_match:
        year = int(year_match.group(2))
    else:
        year = 0
    
    # Find contribution types - look for patterns around "contribution"
    contribution_patterns = [
        r'contribution[s]?[^.]{0,200}empirical',
        r'empirical[^.]{0,200}contribution',
        r'empirical\s+understanding',
        r'empirical\s+study',
        r'empirical\s+investigation',
        r've contribution[s]?.*empirical',
    ]
    
    has_empirical = False
    for pattern in contribution_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            has_empirical = True
            break
    
    return {
        'title': title,
        'year': year,
        'has_empirical': has_empirical
    }

# Filter papers that have empirical contribution and are published after 2016
empirical_papers = []
for paper in papers:
    info = extract_paper_info(paper['text'], paper['filename'])
    if info['has_empirical'] and info['year'] > 2016:
        empirical_papers.append(info)

print(f"Found {len(empirical_papers)} empirical papers published after 2016")
print("First few papers:")
for p in empirical_papers[:5]:
    print(f"  - {p['title']} ({p['year']})")

# Save for next step
result = json.dumps(empirical_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
