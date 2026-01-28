code = """import json
import re

# Load data files
citation_path = locals()['var_functions.query_db:0']
papers_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(papers_path, 'r') as f:
    papers = json.load(f)

print('=== DATA OVERVIEW ===')
print('Total citations:', len(citations))
print('Total papers:', len(papers))

# Build citation title set for exact matching
citation_titles_exact = set(c['title'] for c in citations)

# Year distribution analysis
year_stats = {}
empirical_papers_all = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if not title or not text:
        continue
    
    # Find all years mentioned in the paper (first 2000 chars for header focus)
    years = re.findall(r'\b(20[0-9]{2})\b', text[:2000])
    
    # Check if paper is empirical
    is_empirical = 'empirical' in text.lower()
    
    if years:
        year = int(years[0])
        year_stats[year] = year_stats.get(year, 0) + 1
        
        if is_empirical:
            empirical_papers_all.append({
                'title': title,
                'year': year,
                'in_citations': title in citation_titles_exact
            })

# Display year distribution
print('\n=== YEAR DISTRIBUTION ===')
for year in sorted(year_stats.keys()):
    print('Year %d: %d papers' % (year, year_stats[year]))

# Check empirical papers
emp_after_2016 = [p for p in empirical_papers_all if p['year'] > 2016]
print('\n=== EMPIRICAL PAPERS ===')
print('Total empirical papers:', len(empirical_papers_all))
print('Empirical papers after 2016:', len(emp_after_2016))

if len(emp_after_2016) > 0:
    print('\nFirst 10 empirical papers after 2016:')
    for i, p in enumerate(emp_after_2016[:10]):
        citation_status = 'Yes' if p['in_citations'] else 'No'
        print('%d. %s (Year: %d, In Citations: %s)' % (i+1, p['title'][:80], p['year'], citation_status))
else:
    # Check the maximum year in empirical papers
    if empirical_papers_all:
        max_year = max(p['year'] for p in empirical_papers_all)
        print('\nMax year in empirical papers:', max_year)
        
        # Show papers from max year
        recent_emp = [p for p in empirical_papers_all if p['year'] == max_year]
        print('Empirical papers from max year (%d):' % max_year)
        for i, p in enumerate(recent_emp[:5]):
            print('  %d. %s' % (i+1, p['title'][:80]))

# Build final results with citation counts
final_results = []
norm_citation_map = {}

for c in citations:
    norm = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    norm_citation_map[norm] = int(c['total_citations'])

for paper in emp_after_2016:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', paper['title'].lower())
    if norm_title in norm_citation_map:
        final_results.append({
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': norm_citation_map[norm_title]
        })

# Sort by citations descending
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print('\n=== FINAL MATCHED RESULTS ===')
print('Papers with citation data:', len(final_results))

if final_results:
    print('\nTop results:')
    for i, paper in enumerate(final_results[:10]):
        print('%d. %s' % (i+1, paper['title']))
        print('   Year: %d, Total Citations: %d' % (paper['year'], paper['total_citations']))
else:
    print('No empirical papers after 2016 matched with citation data.')

# Always output a valid JSON array
print('\n__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:66': [], 'var_functions.execute_python:70': [], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
