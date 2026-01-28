code = """import json
import pandas as pd
import re

# Read the physical activity papers from the query result
with open('var_functions.query_db:5.json', 'r') as f:
    papers = json.load(f)

print(f"Found {len(papers)} potential papers")

# Function to parse paper info
def parse_paper_info(paper):
    text = paper['text']
    filename = paper['filename']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Try to extract year from the text
    year = None
    # Look for patterns like "2016" or "CHI 2016" or similar
    year_matches = re.findall(r'(CHI|UBICOMP|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s*\'?\.?\s*(\d{4})', text, re.IGNORECASE)
    if year_matches:
        # Get the first match which is likely the publication year
        venue, year = year_matches[0]
        year = int(year)
    else:
        # Alternative: look for any four-digit year in the first 1000 chars
        general_year = re.search(r'(\d{4})', text[:1000])
        if general_year:
            potential_year = int(general_year.group(1))
            if 2010 <= potential_year <= 2025:  # reasonable range
                year = potential_year
    
    # Check if physical activity is mentioned in the paper
    domain = 'physical activity' if re.search(r'physical activity', text, re.IGNORECASE) else None
    
    return {
        'title': title,
        'year': year,
        'filename': filename,
        'domain': domain
    }

# Parse all papers
parsed_papers = []
for paper in papers:
    parsed = parse_paper_info(paper)
    if parsed['domain']:  # Only keep papers with physical activity domain
        parsed_papers.append(parsed)

# Filter for 2016 papers
papers_2016 = [p for p in parsed_papers if p['year'] == 2016]

print(f"Found {len(papers_2016)} papers from 2016 in physical activity domain")
for p in papers_2016:
    print(f"  - {p['title']} (Year: {p['year']})")

# Save result
result_json = json.dumps(papers_2016)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
