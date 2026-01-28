code = """import json
import re

# Get the paper data file path
paper_data_path = locals()['var_functions.query_db:14']

# Load all papers from MongoDB
with open(paper_data_path, 'r') as f:
    all_papers = json.load(f)

print(f"Total papers loaded: {len(all_papers)}")

# Initialize list for processed papers
processed_papers = []

for paper in all_papers[:50]:  # Process first 50 for now
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    year_match = re.search(r"(20\d{2})", text)
    year = int(year_match.group(1)) if year_match else None
    
    # Extract venue from text (look for common conference/journal patterns)
    venue_patterns = [
        r"CHI\s*'?(\d{2}|\d{4})?", r"UbiComp\s*'?(\d{2}|\d{4})?", 
        r"CSCW\s*'?(\d{2}|\d{4})?", r"DIS\s*'?(\d{2}|\d{4})?",
        r"PervasiveHealth\s*'?(\d{2}|\d{4})?", r"WWW\s*'?(\d{2}|\d{4})?",
        r"IUI\s*'?(\d{2}|\d{4})?", r"OzCHI\s*'?(\d{2}|\d{4})?",
        r"TEI\s*'?(\d{2}|\d{4})?", r"AH\s*'?(\d{2}|\d{4})?"
    ]
    
    venue = None
    for pattern in venue_patterns:
        venue_match = re.search(pattern, text, re.IGNORECASE)
        if venue_match:
            venue_upper = venue_match.group(0).split()[0].upper()
            venue = venue_upper.strip("'-")
            break
    
    # Extract source from text (look for publisher patterns)
    source = None
    if 'ACM' in text or 'Association for Computing Machinery' in text:
        source = 'ACM'
    elif 'IEEE' in text:
        source = 'IEEE'
    elif 'PubMed' in text or 'pubmed' in text:
        source = 'PubMed'
    
    # Extract domain from text (look for physical activity specifically)
    domain = None
    if 'physical activity' in text.lower() or 'physical' in text.lower():
        if 'mental' in text.lower() and 'physical' in text.lower():
            domain = ['physical activity', 'mental']
        else:
            domain = ['physical activity']
    elif 'mental' in text.lower():
        domain = ['mental']
    
    # Extract contribution type
    contribution = None
    if 'empirical' in text.lower():
        contribution = ['empirical']
    elif 'artifact' in text.lower() or 'prototype' in text.lower():
        contribution = ['artifact']
    elif 'theoretical' in text.lower():
        contribution = ['theoretical']
    elif 'survey' in text.lower():
        contribution = ['survey']
    
    processed_papers.append({
        'title': title,
        'year': year,
        'venue': venue,
        'source': source,
        'domain': domain,
        'contribution': contribution,
        'text_length': len(text)
    })

# Show summary
papers_2016_pa = [p for p in processed_papers if p['year'] == 2016 and p['domain'] and 'physical activity' in p['domain']]

print(f"\nFound {len(papers_2016_pa)} papers from 2016 in physical activity domain")
for paper in papers_2016_pa:
    print(f"- {paper['title']}")

result = json.dumps(processed_papers[:10], indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
