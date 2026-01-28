code = """import json, re

# Load all data
cit_file = locals()['var_functions.query_db:34']
paper_file = locals()['var_functions.query_db:2']

with open(cit_file) as f:
    citations = json.load(f)
with open(paper_file) as f:
    papers = json.load(f)

# Build citation lookup
citation_lookup = {rec['title']: int(rec['total_citations']) for rec in citations}

# Find all papers with valid years
papers_with_years = []
for doc in papers:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if not title:
        continue
    
    text = doc.get('text', '')
    
    # Extract year
    year = None
    
    # Try multiple methods
    methods = []
    
    # Copyright
    m = re.search(r'Copyright\s+(?:\d{4}\s+[-–]?\s*)?(20\d{2})', text[:3000])
    if m:
        year = int(m.group(1))
        methods.append('copyright')
    
    # Conference
    if not year:
        m = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+'?(\d{2})\b", text[:2000])
        if m:
            yr = int(m.group(1))
            if yr < 50:
                year = 2000 + yr
                methods.append('conference')
    
    # Published
    if not year:
        m = re.search(r'(?:published|presentation|proceeding).*?\b(20\d{2})\b', text[:3000], re.I)
        if m:
            year = int(m.group(1))
            methods.append('published')
    
    # Fallback
    if not year:
        years = re.findall(r'\b20\d{2}\b', text[:3000])
        for y in years:
            y_int = int(y)
            if 2010 <= y_int <= 2025:
                year = y_int
                methods.append('fallback')
                break
    
    if year:
        papers_with_years.append({
            'title': title,
            'year': year,
            'text': text
        })

print(f'Total papers with valid years: {len(papers_with_years)}')

# Check 2016 papers specifically
papers_2016 = [p for p in papers_with_years if p['year'] == 2016]
print(f'\nTotal 2016 papers: {len(papers_2016)}')

# Analyze domains in 2016 papers
print('\n=== DOMAIN ANALYSIS FOR 2016 PAPERS ===')

# Define domain keywords
domain_keywords = {
    'physical activity': ['physical activity', 'fitness', 'exercise', 'workout', 'sedentary', 'step count', 'active living'],
    'food': ['food', 'diet', 'nutrition', 'eating', 'meal', 'calorie'],
    'sleep': ['sleep', 'insomnia', 'circadian', 'bedtime'],
    'mental': ['mental', 'anxiety', 'depression', 'stress', 'mood', 'emotion'],
    'health': ['health', 'wellness', 'medical', 'clinical', 'disease', 'chronic'],
    'productivity': ['productivity', 'work', 'task', 'goal', 'performance']
}

papers_2016_with_domains = []
for paper in papers_2016:
    text_lower = paper['text'].lower()
    title_lower = paper['title'].lower()
    
    domains = []
    for domain, keywords in domain_keywords.items():
        if any(keyword in text_lower or keyword in title_lower for keyword in keywords):
            domains.append(domain)
    
    papers_2016_with_domains.append({
        'title': paper['title'],
        'domains': domains
    })
    
    if domains:
        print(f"Title: {paper['title']}")
        print(f"Domains: {', '.join(domains)}")
        print()

# Check if any are physical activity
pa_papers_2016 = [p for p in papers_2016_with_domains if 'physical activity' in p['domains']]
print(f'\n=== 2016 PHYSICAL ACTIVITY PAPERS ===')
print(f'Count: {len(pa_papers_2016)}')

for paper in pa_papers_2016:
    title = paper['title']
    citations = citation_lookup.get(title, 0)
    print(f'Title: {title}')
    print(f'Total citations: {citations}')
    print()

# If none found with physical activity domain, show papers with fitness/exercise keywords
if len(pa_papers_2016) == 0:
    print('No papers with "physical activity" domain found. Checking related terms...')
    
    related_keywords = ['fitness', 'exercise', 'workout', 'active', 'steps', 'running', 'walking']
    related_papers = []
    
    for paper in papers_2016:
        text_lower = paper['text'].lower()
        title_lower = paper['title'].lower()
        
        if any(keyword in text_lower or keyword in title_lower for keyword in related_keywords):
            related_papers.append(paper['title'])
    
    print(f'Papers with fitness/exercise keywords: {len(related_papers)}')
    for title in related_papers:
        citations = citation_lookup.get(title, 0)
        print(f'  - {title} (citations: {citations})')

# Prepare final results
final_results = []
for paper in pa_papers_2016:
    title = paper['title']
    final_results.append({
        'title': title,
        'total_citation_count': citation_lookup.get(title, 0)
    })

# Sort by citation count
final_results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print()
print('__RESULT__:')
print(json.dumps(final_results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:28': {'total_papers': 5, 'papers_2016': 0}, 'var_functions.execute_python:32': {'papers_count': 0, 'papers': []}, 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:38': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:50': []}

exec(code, env_args)
