code = """import json, re

# Load data
cit_file = locals()['var_functions.query_db:34']
with open(cit_file) as f:
    citations = json.load(f)

paper_file = locals()['var_functions.query_db:2']
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup map
citation_map = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    citation_map[title] = count

# Process all papers
results_2016_pa = []
pa_papers_by_year = {}

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    text_lower = text.lower()
    
    # Check for physical activity in domain
    is_pa = 'physical activity' in text_lower
    
    if not is_pa:
        continue
    
    # Extract publication year
    year = None
    
    # Method 1: Copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Method 2: Conference header
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Method 3: First year in range
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    # Track by year and filter for 2016
    if year:
        if year not in pa_papers_by_year:
            pa_papers_by_year[year] = []
        pa_papers_by_year[year].append(title)
        
        if year == 2016:
            total_citations = citation_map.get(title, 0)
            results_2016_pa.append({
                'title': title,
                'total_citation_count': total_citations
            })

# Sort results by citation count
def get_citations(item):
    return item['total_citation_count']

results_2016_pa.sort(key=get_citations, reverse=True)

# Generate output
print('__RESULT__:')
print(json.dumps(results_2016_pa))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': []}

exec(code, env_args)
