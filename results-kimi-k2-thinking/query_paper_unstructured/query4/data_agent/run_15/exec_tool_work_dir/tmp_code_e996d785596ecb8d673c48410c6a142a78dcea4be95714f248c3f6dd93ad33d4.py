code = """import json, re

# Load citation data
cit_file = locals()['var_functions.query_db:34']
with open(cit_file, 'r') as f:
    citations = json.load(f)

# Load paper documents  
paper_file = locals()['var_functions.query_db:2']
with open(paper_file, 'r') as f:
    papers = json.load(f)

# Build citation lookup map
citation_map = {}
for rec in citations:
    title = rec.get('title', '')
    count = int(rec.get('total_citations', 0))
    citation_map[title] = count

# Process all papers to find 2016 physical activity papers
results = []
found_pa_papers = []

for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Check for physical activity domain
    text_lower = text.lower()
    title_lower = title.lower()
    
    has_physical_activity = 'physical activity' in text_lower or 'physical activity' in title_lower
    has_fitness = 'fitness' in text_lower or 'fitness' in title_lower
    has_exercise = 'exercise' in text_lower or 'exercise' in title_lower
    has_workout = 'workout' in text_lower or 'workout' in title_lower
    has_sedentary = 'sedentary' in text_lower or 'sedentary' in title_lower
    has_step_count = 'step count' in text_lower or 'step count' in title_lower
    
    is_pa_paper = has_physical_activity or has_fitness or has_exercise or has_workout or has_sedentary or has_step_count
    
    if not is_pa_paper:
        continue
    
    # Extract publication year
    year = None
    
    # Method 1: Copyright line
    copyright_match = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if copyright_match:
        year = int(copyright_match.group(1))
    
    # Method 2: Conference header with year
    if not year:
        conf_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:1500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr < 50:
                year = 2000 + yr
    
    # Method 3: Published year
    if not year:
        pub_match = re.search(r'(?:published|presentation|proceeding).*?\b(20\d{2})\b', text[:3000], re.IGNORECASE)
        if pub_match:
            year = int(pub_match.group(1))
    
    # Method 4: Fall back to first reasonable year in text
    if not year:
        year_matches = re.findall(r'\b20\d{2}\b', text[:2000])
        for match in year_matches:
            y = int(match)
            if 2010 <= y <= 2025:
                year = y
                break
    
    # Skip if no valid year found
    if not year:
        continue
    
    # Track all PA papers for debugging
    found_pa_papers.append({'title': title, 'year': year})
    
    # Filter specifically for 2016
    if year == 2016:
        total_citations = citation_map.get(title, 0)
        results.append({
            'title': title,
            'total_citation_count': total_citations
        })

# Sort results by citation count (descending)
def get_citation_count(item):
    return item['total_citation_count']

results.sort(key=get_citation_count, reverse=True)

# Count PA papers by year for debugging
year_counts = {}
for paper in found_pa_papers:
    year = paper['year']
    year_counts[year] = year_counts.get(year, 0) + 1

print('Total papers processed: ' + str(len(papers)))
print('Total PA papers found: ' + str(len(found_pa_papers)))
print('PA papers by year: ' + str(dict(sorted(year_counts.items()))))
print('2016 PA papers matching criteria: ' + str(len(results)))

# Output final results
print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': []}

exec(code, env_args)
