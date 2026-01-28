code = """import json, re

# Load all data
cit_file = locals()['var_functions.query_db:34']
with open(cit_file, 'r') as f:
    citations = json.load(f)

paper_file = locals()['var_functions.query_db:2']
with open(paper_file, 'r') as f:
    papers = json.load(f)

print("=== DATA SUMMARY ===")
print(f"Total paper documents: {len(papers)}")
print(f"Total citation summaries: {len(citations)}")

# Build quick citation lookup
cit_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# Find ALL physical activity papers first (any year)
pa_papers = []
for doc in papers:
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check for physical activity domain
    text_lower = text.lower()
    has_pa = 'physical activity' in text_lower
    
    if has_pa:
        # Extract year carefully
        year = None
        
        # Method 1: Copyright line
        m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
        if m:
            year = int(m.group(1))
        
        # Method 2: Conference header
        if not year:
            m = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1000])
            if m:
                yr = int(m.group(1))
                if yr < 50:
                    year = 2000 + yr
        
        # Method 3: Look for specific patterns like "2016 ACM" or "Copyright 2016"
        if not year:
            m = re.search(r'\b(20\d{2})\s+(?:ACM|IEEE|PubMed|DOI|ISBN)', text[:2000])
            if m:
                year = int(m.group(1))
        
        # Method 4: First reasonable year in text
        if not year:
            years = re.findall(r'\b20\d{2}\b', text[:2000])
            for y in years:
                y_int = int(y)
                if 2010 <= y_int <= 2025:
                    year = y_int
                    break
        
        if year:
            pa_papers.append({'title': title, 'year': year, 'doc': doc})

print(f"\nPhysical activity papers found: {len(pa_papers)}")

# Show distribution by year
from collections import Counter
year_dist = Counter([p['year'] for p in pa_papers])
print("\nDistribution by year:")
for yr in sorted(year_dist.keys()):
    print(f"  {yr}: {year_dist[yr]} papers")

# Show 2016 papers specifically
papers_2016 = [p for p in pa_papers if p['year'] == 2016]
print(f"\n2016 physical activity papers: {len(papers_2016)}")

if papers_2016:
    print("\n2016 Papers:")
    for p in papers_2016:
        title = p['title']
        citations = cit_lookup.get(title, 0)
        print(f"  - {title}")
        print(f"    Citations: {citations}")
else:
    # Let's check what domains 2016 papers actually have
    print("\n=== Checking all 2016 papers for domains ===")
    all_2016 = []
    for doc in papers:
        title = doc.get('filename', '').replace('.txt', '')
        if not title:
            continue
        
        text = doc.get('text', '')
        
        year = None
        m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
        if m:
            year = int(m.group(1))
        
        if not year:
            years = re.findall(r'\b20\d{2}\b', text[:2000])
            for y in years:
                y_int = int(y)
                if 2010 <= y_int <= 2025:
                    year = y_int
                    break
        
        if year == 2016:
            # Check for various domains
            text_lower = text.lower()
            domains = []
            if 'physical activity' in text_lower:
                domains.append('physical activity')
            if 'food' in text_lower or 'diet' in text_lower:
                domains.append('food')
            if 'sleep' in text_lower:
                domains.append('sleep')
            if 'mental' in text_lower or 'anxiety' in text_lower or 'depression' in text_lower:
                domains.append('mental')
            if 'fitness' in text_lower or 'exercise' in text_lower:
                domains.append('fitness')
            
            all_2016.append({'title': title, 'domains': domains})
    
    print(f"Total 2016 papers: {len(all_2016)}")
    for p in all_2016:
        if p['domains']:
            print(f"  - {p['title'][:80]}")
            print(f"    Domains: {', '.join(p['domains'])}")

print()
print('__RESULT__:')
print(json.dumps([{'title': p['title'], 'total_citation_count': cit_lookup.get(p['title'], 0)} for p in papers_2016]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': []}

exec(code, env_args)
