code = """import json
import re

# Load the full citations data
citations_file = locals()['var_functions.query_db:34']
with open(citations_file, 'r') as f:
    all_citations = json.load(f)

# Load paper documents
paper_file = locals()['var_functions.query_db:2']
with open(paper_file, 'r') as f:
    all_papers = json.load(f)

print("=== DATA LOADED ===")
print(f"Total citation entries: {len(all_citations)}")
print(f"Total paper documents: {len(all_papers)}")

# Find papers with physical activity in title or domain
print("\n=== FINDING PHYSICAL ACTIVITY PAPERS ===")

pa_papers = []
for doc in all_papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check if physical activity domain (in text) or in title
    is_pa_domain = 'physical activity' in text.lower()
    is_pa_title = 'physical activity' in title.lower()
    
    if is_pa_domain or is_pa_title:
        # Extract publication year
        year = None
        
        # Try copyright line first
        copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
        if copyright_match:
            year = int(copyright_match.group(1))
        
        # Try conference header
        if not year:
            conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1000])
            if conf_match:
                year_num = int(conf_match.group(1))
                if year_num < 50:
                    year = 2000 + year_num
        
        # Fallback to first year in text
        if not year:
            year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
            for match in year_matches:
                year_val = int(match)
                if 2010 <= year_val <= 2025:
                    year = year_val
                    break
        
        if year:
            pa_papers.append({
                'title': title,
                'year': year,
                'is_pa_domain': is_pa_domain,
                'is_pa_title': is_pa_title
            })

print(f"Found {len(pa_papers)} physical activity papers total")

# Filter for 2016
papers_2016_pa = [p for p in pa_papers if p['year'] == 2016]
print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")

# Build citation lookup
citation_lookup = {}
for rec in all_citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    citation_lookup[title] = count

# Add citation counts
results = []
for paper in papers_2016_pa:
    title = paper['title']
    total_citations = citation_lookup.get(title, 0)
    results.append({
        'title': title,
        'total_citation_count': total_citations
    })

# Sort by citation count
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print(f"\n=== FINAL RESULTS ===")
for r in results:
    print(f"Title: {r['title']}")
    print(f"Citations: {r['total_citation_count']}")
    print()

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json'}

exec(code, env_args)
