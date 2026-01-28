code = """import json
import re

# Read the citations data from 2020
citations_file = var_functions.query_db:0
with open(citations_file, 'r') as f:
    citations_2020 = json.load(f)

# Read the paper documents
papers_file = var_functions.query_db:5
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Process CHI papers
chi_papers = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Check if this is a CHI paper
    # Look for CHI venue patterns in the text
    if re.search(r'CHI\s+[\'\u2018\u2019]\d{2}|CHI\s+\d{4}|CHI\s+\d{2}', text, re.IGNORECASE):
        # Extract title from filename (remove .txt)
        title = filename.replace('.txt', '')
        
        # Try to extract year from text
        year_match = re.search(r'CHI\s+[\'\u2018\u2019](\d{2})|CHI\s+(\d{4})|CHI\s+(\d{2})', text)
        year = None
        if year_match:
            year_str = year_match.group(1) or year_match.group(2) or year_match.group(3)
            if len(year_str) == 4:
                year = int(year_str)
            elif len(year_str) == 2:
                # Convert 2-digit year to 4-digit (assuming 2000s)
                year = int('20' + year_str)
        
        chi_papers.append({
            'title': title,
            'year': year,
            'filename': filename
        })

print('__RESULT__:')
print(f"Number of CHI papers found: {len(chi_papers)}")
if chi_papers:
    print(f"First few CHI papers: {chi_papers[:3]}")
else:
    print("No CHI papers found with current pattern")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['paper_docs'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
