code = """import json
import re

# Access the result from the storage variable
papers = locals().get('var_functions.query_db:5', [])

if isinstance(papers, str):
    # If it's a file path
    with open(papers, 'r') as f:
        papers = json.load(f)

print(f"Total papers retrieved: {len(papers)}")

# Process papers to extract metadata
empirical_papers_after_2016 = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year
    year = None
    year_patterns = [
        r'\b(20(1[7-9]|[2-9]\d))\b',  # Years 2017-2099
        r'CHI\s+\'?(\d{2})',  # CHI '18
        r'UbiComp\s+\'?(\d{2})',  # UbiComp '17
        r'CSCW\s+\'?(\d{2})',  # CSCW '16
    ]
    
    for pattern in year_patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = int('20' + year_str)
            else:
                year = int(year_str)
            break
    
    # Check for empirical contribution
    if 'empirical' in text.lower():
        contribution = 'empirical'
    else:
        contribution = None
    
    # Filter papers
    if contribution == 'empirical' and year and year > 2016:
        empirical_papers_after_2016.append({
            'title': title,
            'year': year
        })

print(f"Empirical papers after 2016: {len(empirical_papers_after_2016)}")

# Print first few papers for verification
for i, paper in enumerate(empirical_papers_after_2016[:5]):
    print(f"{i+1}. {paper['title']} ({paper['year']})")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
