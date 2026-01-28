code = """import json, re

# Load data files
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup
citation_lookup = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    citation_lookup[title] = count

# Process all papers
all_results = []
pa_term_counts = {}

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check for physical activity
    text_lower = text.lower()
    has_physical_activity = 'physical activity' in text_lower
    
    if not has_physical_activity:
        continue
    
    # Extract year
    year = None
    
    # Try copyright
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    if not year:
        # Try conference
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    if not year:
        # Try any year
        years = re.findall(r'\b20\d{2}\b', text[:2000])
        for y in years:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                break
    
    # Track by year
    if year:
        if year not in pa_term_counts:
            pa_term_counts[year] = 0
        pa_term_counts[year] += 1
        
        if year == 2016:
            total_citations = citation_lookup.get(title, 0)
            all_results.append({
                'title': title,
                'total_citation_count': total_citations
            })

# Sort results
all_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print('Total papers in dataset: ' + str(len(papers)))
print('Papers with physical activity terms by year:')
for year in sorted(pa_term_counts.keys()):
    print(f"  {year}: {pa_term_counts[year]}")

print('Total 2016 physical activity papers: ' + str(len(all_results)))

# Print results
for result in all_results:
    print(f"Title: {result['title']}")
    print(f"Total citations: {result['total_citation_count']}")
    print()

print('__RESULT__:')
print(json.dumps(all_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
