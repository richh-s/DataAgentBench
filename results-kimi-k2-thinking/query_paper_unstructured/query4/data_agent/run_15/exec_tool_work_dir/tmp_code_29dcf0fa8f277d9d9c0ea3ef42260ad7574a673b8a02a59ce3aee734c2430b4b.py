code = """import json, re

# Load data
cit_file = locals()['var_functions.query_db:34']
with open(cit_file) as f:
    citations = json.load(f)

paper_file = locals()['var_functions.query_db:2']
with open(paper_file) as f:
    papers = json.load(f)

print("=== LOADING COMPLETE ===")
print(f"Papers: {len(papers)}")
print(f"Citations: {len(citations)}")

# Build citation lookup
cit_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# Debug first few papers
print("\n=== FIRST 5 PAPERS ===")
for i in range(min(5, len(papers))):
    doc = papers[i]
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    
    # Search for year
    year = None
    
    # Try different approaches
    approaches = []
    
    # 1. Copyright
    m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
    if m:
        year = int(m.group(1))
        approaches.append(f"Copyright: {year}")
    
    # 2. Conference format
    if not year:
        m = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1000])
        if m:
            yr = int(m.group(1))
            if yr < 50:
                year = 2000 + yr
                approaches.append(f"Conference: {year}")
    
    # 3. Look for patterns
    if not year:
        patterns = [
            r'(?:published|presentation|conference|proceeding).*?\b(20\d{2})\b',
            r'\b(20\d{2})\s+(?:ACM|IEEE)',
            r'\b(20\d{2})\b(?=.*?(?:ACM|IEEE|DOI|ISBN|http))'
        ]
        for pat in patterns:
            m = re.search(pat, text[:2000], re.IGNORECASE)
            if m:
                year = int(m.group(1))
                approaches.append(f"Pattern: {year}")
                break
    
    # 4. First year
    if not year:
        years = re.findall(r'\b20\d{2}\b', text[:2000])
        for y in years:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                approaches.append(f"First year: {year}")
                break
    
    # Check for physical activity
    has_pa = 'physical activity' in text.lower()
    
    print(f"{i+1}. {title}")
    print(f"   Year: {year} ({', '.join(approaches) if approaches else 'none'})")
    print(f"   Physical activity: {has_pa}")
    
    if i == 0:
        print(f"   Text preview: {text[:300].replace(chr(10), ' ')}")

# Now scan ALL papers for physical activity and 2016
print("\n=== SCANNING ALL PAPERS ===")
pa_papers = []
for doc in papers:
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check for physical activity
    if 'physical activity' not in text_lower:
        continue
    
    # Extract year
    year = None
    m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:2000])
    if m:
        year = int(m.group(1))
    
    if not year:
        m = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1000])
        if m:
            yr = int(m.group(1))
            if yr < 50:
                year = 2000 + yr
    
    if not year:
        years = re.findall(r'\b20\d{2}\b', text[:2000])
        for y in years:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                break
    
    if year:
        pa_papers.append({'title': title, 'year': year})

print(f"Physical activity papers found: {len(pa_papers)}")

# Show by year
from collections import Counter
year_counts = Counter([p['year'] for p in pa_papers])
print("\nDistribution by year:")
for yr in sorted(year_counts.keys()):
    print(f"  {yr}: {year_counts[yr]}")

# Show 2016 specifically
papers_2016 = [p for p in pa_papers if p['year'] == 2016]
print(f"\n2016 physical activity papers: {len(papers_2016)}")
for p in papers_2016:
    title = p['title']
    citations = cit_lookup.get(title, 0)
    print(f"  - {title}")
    print(f"    Citations: {citations}")

print()
print('__RESULT__:')
print(json.dumps([{'title': p['title'], 'total_citation_count': cit_lookup.get(p['title'], 0)} for p in papers_2016]))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': []}

exec(code, env_args)
