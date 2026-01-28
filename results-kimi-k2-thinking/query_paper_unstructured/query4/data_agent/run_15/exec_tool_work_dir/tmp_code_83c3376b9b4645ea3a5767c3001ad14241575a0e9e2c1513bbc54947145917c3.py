code = """import json, re

# Load all data
paper_file = locals()['var_functions.query_db:2']
with open(paper_file, 'r') as f:
    all_papers = json.load(f)

citations = locals()['var_functions.query_db:16']

print("=== ALL PAPERS ANALYSIS ===")
print(f"Total documents in database: {len(all_papers)}")

# Analyze each document in detail
for i, doc in enumerate(all_papers):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else 'NO TITLE'
    text = doc.get('text', '')
    
    # Find all year mentions
    all_years = re.findall(r'\b20\d{2}\b', text[:2000])
    
    # Determine publication year (most specific pattern, usually near beginning)
    pub_year = None
    for pattern in [r'20\d{2}\s+[-–]\s+20\d{2}', r'20\d{2}\b.*?(?=Copyright|Permission|UBICOMP|CHI|CSCW)', r'20\d{2}(?=\s+[-–]\s+20\d{2})']:
        match = re.search(pattern, text[:2000])
        if match:
            year_match = re.search(r'\b20\d{2}\b', match.group())
            if year_match:
                pub_year = int(year_match.group())
                break
    
    if not pub_year and all_years:
        pub_year = int(all_years[0])
    
    # Check for physical activity
    is_physical_activity = 'physical activity' in text.lower()
    
    print(f"\nPaper {i+1}:")
    print(f"  Title: {title}")
    print(f"  Years mentioned: {all_years}")
    print(f"  Publication year: {pub_year}")
    print(f"  Contains 'physical activity': {is_physical_activity}")

# Build citation lookup
citation_dict = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('citation_count', 0))
    citation_dict[title] = citation_dict.get(title, 0) + count

print(f"\n=== CITATION DATA ===")
print(f"Citation records: {len(citations)}")
print(f"Unique papers with citations: {len(citation_dict)}")

# Sample citation entries
print(f"\nSample citation entries:")
sample_titles = list(citation_dict.keys())[:5]
for title in sample_titles:
    print(f"  - {title}: {citation_dict[title]} citations")

# Now find all 2016 physical activity papers
papers_2016_pa = []
for doc in all_papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract publication year
    pub_year = None
    # Try to find year in copyright line first
    copyright_match = re.search(r'Copyright\s+\d{4}\s+[-–]?\s*20\d{2}', text[:2000])
    if copyright_match:
        year_match = re.search(r'20\d{2}', copyright_match.group())
        if year_match:
            pub_year = int(year_match.group())
    
    # Try conference header pattern
    if not pub_year:
        conf_match = re.search(r"(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?\d{2}", text[:1000])
        if conf_match:
            year_part = re.search(r"\d{2}", conf_match.group())
            if year_part:
                pub_year = 2000 + int(year_part.group())
    
    # Fallback to first 4-digit year
    if not pub_year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        if year_matches:
            pub_year = int(year_matches[0])
    
    # Check domain
    is_physical_activity = 'physical activity' in text.lower()
    
    if pub_year == 2016 and is_physical_activity:
        papers_2016_pa.append({
            'title': title,
            'year': pub_year
        })

print(f"\n=== FINAL RESULTS ===")
print(f"Papers from 2016 in 'physical activity' domain: {len(papers_2016_pa)}")

if papers_2016_pa:
    for paper in papers_2016_pa:
        title = paper['title']
        total_citations = citation_dict.get(title, 0)
        print(f"  - {title}")
        print(f"    Total citations: {total_citations}")
else:
    print("No papers found matching the criteria")

print('__RESULT__:')
print(json.dumps(papers_2016_pa))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}}

exec(code, env_args)
