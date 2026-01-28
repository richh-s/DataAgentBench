code = """import json
import re

# Load all paper documents
paper_file_path = locals()['var_functions.query_db:2']
with open(paper_file_path, 'r') as f:
    all_papers = json.load(f)

# Load citations data
citations_data = locals()['var_functions.query_db:16']

# Build citation lookup: title -> total citations
citation_lookup = {}
for record in citations_data:
    title = record.get('title', '')
    count = int(record.get('citation_count', 0))
    if title in citation_lookup:
        citation_lookup[title] += count
    else:
        citation_lookup[title] = count

print("Total papers loaded:", len(all_papers))
print("Total citation records:", len(citations_data))
print("Unique papers with citations:", len(citation_lookup))

# Find all 2016 papers in physical activity domain
papers_2016_pa = []

for doc in all_papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract publication year
    year = None
    
    # Method 1: Look for copyright year (most reliable)
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Method 2: Look for conference header with year
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1000])
        if conf_match:
            year_num = int(conf_match.group(1))
            if year_num < 50:  # Assume 2000s
                year = 2000 + year_num
    
    # Method 3: Use first 4-digit year in reasonable range
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            year_val = int(match)
            if 2010 <= year_val <= 2025:
                year = year_val
                break
    
    # Check if paper mentions physical activity (domain)
    is_physical_activity = 'physical activity' in text.lower()
    
    if year == 2016 and is_physical_activity:
        papers_2016_pa.append({
            'title': title,
            'year': year
        })

# Get citation counts for these papers
final_results = []
for paper in papers_2016_pa:
    paper_title = paper['title']
    total_citations = citation_lookup.get(paper_title, 0)
    final_results.append({
        'title': paper_title,
        'total_citation_count': total_citations
    })

# Sort by citation count (descending)
final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("Found results:", len(final_results))
for result in final_results:
    print("Title:", result['title'])
    print("Citations:", result['total_citation_count'])
    print()

# Return structured results
output = {
    'papers_count': len(final_results),
    'papers': final_results
}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}}

exec(code, env_args)
