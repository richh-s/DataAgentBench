code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    citations = json.load(f)

with open(locals()['var_functions.query_db:2'], 'r') as f:
    papers = json.load(f)

print('Data loaded: ' + str(len(citations)) + ' citations, ' + str(len(papers)) + ' papers')

# Build citation map (normalized title -> citation count)
citation_map = {}
for c in citations:
    norm = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    citation_map[norm] = int(c['total_citations'])

# First, let's just find ANY empirical papers to verify the keyword search
empirical_papers_all = []
empirical_papers_after_2016 = []

for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if not title or not text:
        continue
    
    # Check for empirical
    has_empirical = 'empirical' in text.lower()
    
    # Extract year with multiple patterns
    year = 0
    
    # Pattern 1: Look for year in first 500 chars (header)
    header_match = re.search(r'\b(20[1-2][0-9])\b', text[:500])
    if header_match:
        year = int(header_match.group(1))
    else:
        # Pattern 2: Look for conference year format like '17, '18
        conf_match = re.search(r"[A-Z]+\s+'([0-9]{2})\b", text[:500])
        if conf_match:
            yr = int(conf_match.group(1))
            if yr >= 17:
                year = 2000 + yr
        else:
            # Pattern 3: Look anywhere in text
            any_match = re.search(r'\b(201[7-9]|202[0-9])\b', text)
            if any_match:
                year = int(any_match.group(1))
    
    if has_empirical:
        empirical_papers_all.append({'title': title, 'year': year})
        if year > 2016:
            empirical_papers_after_2016.append({'title': title, 'year': year})

print('\nTotal empirical papers found: ' + str(len(empirical_papers_all)))
print('Empirical papers after 2016: ' + str(len(empirical_papers_after_2016)))

if len(empirical_papers_all) > 0:
    print('\nSample empirical papers:')
    for i, p in enumerate(empirical_papers_all[:5]):
        print(str(i+1) + '. ' + p['title'][:80] + ' (' + str(p['year']) + ')')

# Now find matches with citations
matched_results = []

for paper_info in empirical_papers_after_2016:
    title = paper_info['title']
    year = paper_info['year']
    
    # Try to match with citations using normalized title
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
    
    if norm_title in citation_map:
        matched_results.append({
            'title': title,
            'year': year,
            'total_citations': citation_map[norm_title]
        })

if len(matched_results) == 0:
    # Try a different matching strategy - substring matching
    print('\nTrying substring matching...')
    
    for paper_info in empirical_papers_after_2016:
        title = paper_info['title']
        year = paper_info['year']
        
        # For each citation, check if paper title is contained within it
        for cit_title, cit_count in citation_map.items():
            # Check if paper title appears in citation title (or vice versa)
            paper_clean = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            cit_clean = cit_title
            
            if paper_clean in cit_clean or cit_clean in paper_clean:
                matched_results.append({
                    'title': title,
                    'year': year,
                    'total_citations': cit_count
                })
                break

print('\nMatched papers with citations: ' + str(len(matched_results)))

if len(matched_results) > 0:
    matched_results.sort(key=lambda x: x['total_citations'], reverse=True)
    print('\nTop papers:')
    for i, p in enumerate(matched_results[:10]):
        print(str(i+1) + '. ' + p['title'][:70] + ' - ' + str(p['year']) + ' - ' + str(p['total_citations']) + ' citations')

print('\n__RESULT__:')
print(json.dumps(matched_results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': []}

exec(code, env_args)
