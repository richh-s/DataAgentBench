code = """import json
import re

# Read the full paper docs data
paper_docs_file = var_functions.query_db:2
if isinstance(paper_docs_file, str) and paper_docs_file.endswith('.json'):
    with open(paper_docs_file, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = var_functions.query_db:2

print(f"Total papers: {len(paper_docs)}")

# Let's inspect a few to understand structure
for i, doc in enumerate(paper_docs[:3]):
    print(f"\n--- Paper {i+1} ---")
    print(f"Filename: {doc.get('filename')}")
    print(f"Text snippet: {doc.get('text')[:500]}")

# Now let's extract information from all papers
extracted_papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for patterns like '2017', 'CHI \'17', 'UbiComp \'17'
    # Common patterns: venue 'YY, or venue YYYY, or year: YYYY
    year = None
    
    # Try multiple patterns
    patterns = [
        r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s+'?(\d{2})[,'\s]",  # venue 'YY
        r"(?:20\d{2})\s*(?:,\s*)?(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)",  # 2015, venue
        r"(20\d{2})\s*(?:,\s*)?(?:Proceedings|Conference|Journal|International)",  # 2017, Proceedings
        r"Copyright\s*(?:\d{4}\s*)?(20\d{2})",  # Copyright 2015
        r"(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}[,-]\s*(20\d{2})",  # September 7-11, 2015
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                # Convert YY to YYYY (assuming 2000-2099)
                year = int('20' + year_str)
            else:
                year = int(year_str)
            if 2010 <= year <= 2025:  # Reasonable range
                break
    
    # Extract contribution type - look for keywords
    contribution = []
    text_lower = text.lower()
    
    if 'empirical' in text_lower or 'study' in text_lower:
        contribution.append('empirical')
    if 'artifact' in text_lower or 'system' in text_lower or 'prototype' in text_lower:
        contribution.append('artifact')
    if 'theoretical' in text_lower or 'model' in text_lower or 'framework' in text_lower:
        contribution.append('theoretical')
    if 'survey' in text_lower or 'review' in text_lower:
        contribution.append('survey')
    if 'methodological' in text_lower:
        contribution.append('methodological')
    
    # Clean up contribution list
    contribution = list(set(contribution))  # Remove duplicates
    
    if title and year:
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })

# Filter papers with empirical contribution and year > 2016
empirical_papers = [p for p in extracted_papers if p['year'] > 2016 and 'empirical' in p['contribution']]

print(f"\nTotal extracted papers: {len(extracted_papers)}")
print(f"Papers with empirical contribution after 2016: {len(empirical_papers)}")

# Show first 5
print("\nFirst 5 empirical papers after 2016:")
for paper in empirical_papers[:5]:
    print(f"  - {paper['title']} ({paper['year']})")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
