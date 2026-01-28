code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

print('=== DATA SUMMARY ===')
print('Total citations:', len(citations))
print('Total papers:', len(papers))

# Check year distribution
year_dist = {}
for paper in papers:
    text = paper.get('text', '')
    years = re.findall(r'\b(20[0-9]{2})\b', text)
    if years:
        yr = int(years[0])
        year_dist[yr] = year_dist.get(yr, 0) + 1

print('\nYear distribution:')
for yr in sorted(year_dist.keys()):
    print('Year', yr, ':', year_dist[yr], 'papers')

# Find empirical papers
emp_papers = []
for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    years = re.findall(r'\b(20[0-9]{2})\b', text)
    year = int(years[0]) if years else 0
    
    if year > 2016 and 'empirical' in text.lower():
        emp_papers.append({'title': title, 'year': year})

print('\nEmpirical papers after 2016:', len(emp_papers))

# Build citation map
norm_citations = {}
for c in citations:
    norm = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    norm_citations[norm] = int(c['total_citations'])

# Match papers with citations
results = []
for paper in emp_papers:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', paper['title'].lower())
    if norm_title in norm_citations:
        results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': norm_citations[norm_title]
        })

results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\nMatched with citations:', len(results))
print('\n__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
