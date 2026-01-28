code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

print('=== COMPREHENSIVE DATA AUDIT ===')
print(f'Citations: {len(citations)} records')
print(f'Papers: {len(papers)} records')

# Step 1: Analyze year distribution
year_counts = {}
for paper in papers:
    text = paper.get('text', '')
    years = re.findall(r'\b(20[0-9]{2})\b', text)
    if years:
        year = int(years[0])
        year_counts[year] = year_counts.get(year, 0) + 1

print(f'\nYear distribution:')
for year in sorted(year_counts.keys()):
    print(f'  {year}: {year_counts[year]} papers')

# Step 2: Check if any papers have "empirical" text
empirical_papers_all_years = []
for paper in papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if 'empirical' in text and title:
        # Extract year for this paper
        years = re.findall(r'\b(20[0-9]{2})\b', paper.get('text', ''))
        year = int(years[0]) if years else 0
        empirical_papers_all_years.append({'title': title, 'year': year})

print(f'\nEmpirical papers (all years): {len(empirical_papers_all_years)}')
if len(empirical_papers_all_years) > 0:
    print('Sample empirical papers:')
    for i, p in enumerate(empirical_papers_all_years[:10]):
        print(f'  {i+1}. {p["title"][:80]} (Year: {p["year"]})')

# Step 3: Check which empirical papers are after 2016
empirical_after_2016 = [p for p in empirical_papers_all_years if p['year'] > 2016]
print(f'\nEmpirical papers after 2016: {len(empirical_after_2016)}')

# Step 4: Check titles that exist in both datasets
paper_titles = [p['title'] for p in empirical_after_2016]
citation_titles = set(c['title'] for c in citations)

print(f'\nMatching titles (exact match):')
exact_matches = []
for title in paper_titles:
    if title in citation_titles:
        exact_matches.append(title)

print(f'  Found {len(exact_matches)} exact matches')

# Step 5: Try flexible matching with normalized titles
print(f'\nFlexible title matching:')
flexible_matches = []
norm_citation_map = {}

for c in citations:
    norm = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    norm_citation_map[norm] = {
        'original_title': c['title'],
        'total_citations': int(c['total_citations'])
    }

for paper in empirical_after_2016:
    paper_norm = re.sub(r'[^a-zA-Z0-9]', '', paper['title'].lower())
    if paper_norm in norm_citation_map:
        cit_data = norm_citation_map[paper_norm]
        flexible_matches.append({
            'paper_title': paper['title'],
            'citation_title': cit_data['original_title'],
            'year': paper['year'],
            'total_citations': cit_data['total_citations']
        })

print(f'  Found {len(flexible_matches)} flexible matches')

# Step 6: Generate final results
final_results = [
    {
        'title': match['paper_title'],
        'year': match['year'],
        'total_citations': match['total_citations']
    }
    for match in flexible_matches
]

final_results.sort(key=lambda x: x['total_citations'], reverse=True)

print(f'\n=== FINAL RESULTS ===')
print(f'Number of papers: {len(final_results)}')

if final_results:
    print(f'Top 10 by citations:')
    for i, paper in enumerate(final_results[:10]):
        print(f"{i+1}. {paper['title'][:80]}...")
        print(f"   Year: {paper['year']}, Total Citations: {paper['total_citations']}")

print('\n__RESULT__:')
print(json.dumps(final_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
