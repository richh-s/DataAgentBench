code = """import json
import re

# Access the MongoDB papers result
papers_result = locals().get('var_functions.query_db:17')

# If it's a file path, load the data
if isinstance(papers_result, str):
    with open(papers_result, 'r') as f:
        papers = json.load(f)
else:
    papers = papers_result

print("Total papers retrieved from MongoDB:", len(papers))

# Extract paper information
paper_metadata = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year - look for patterns
    year = None
    
    # Pattern 1: Look for 4-digit years in 2017-2025 range
    year_match = re.search(r'\b(20(1[7-9]|[2-5]\d))\b', text)
    if year_match:
        year = int(year_match.group(1))
    
    # Pattern 2: Look for venue with 2-digit year
    if not year:
        venue_match = re.search(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})", text, re.IGNORECASE)
        if venue_match:
            year_str = venue_match.group(2)
            year = int('20' + year_str)
    
    # Check for empirical contribution
    contribution = None
    if 'empirical' in text.lower():
        contribution = 'empirical'
    elif 'artifact' in text.lower():
        contribution = 'artifact'
    elif 'theoretical' in text.lower():
        contribution = 'theoretical'
    elif 'survey' in text.lower():
        contribution = 'survey'
    elif 'methodological' in text.lower():
        contribution = 'methodological'
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'original_paper': paper
    })

# Filter empirical papers after 2016
empirical_papers = [p for p in paper_metadata if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016]

print(f"Empirical papers after 2016: {len(empirical_papers)}")
for p in empirical_papers[:5]:
    print(f"  - {p['title']} ({p['year']})")

# Store the empirical papers for next steps
with open('/tmp/empirical_papers.json', 'w') as f:
    json.dump(empirical_papers, f, indent=2)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json'}

exec(code, env_args)
