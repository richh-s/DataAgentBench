code = """import json
import re

# Load data
citations = json.load(open(locals()['var_functions.query_db:0'], 'r'))
papers = json.load(open(locals()['var_functions.query_db:2'], 'r'))

# Build citation title map (normalized)
citation_titles = {}
for c in citations:
    norm = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    citation_titles[norm] = int(c['total_citations'])

# Find empirical papers after 2016
results = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    if title and 'empirical' in text.lower():
        # Extract year
        year = 0
        # Look for year pattern
        match = re.search(r'\b(20[1-2][0-9])\b', text[:2000])
        if match:
            year = int(match.group(1))
        
        if year > 2016:
            norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            if norm_title in citation_titles:
                results.append({
                    'title': title,
                    'year': year,
                    'total_citations': citation_titles[norm_title]
                })

# Sort by citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:66': [], 'var_functions.execute_python:70': [], 'var_functions.query_db:72': 'file_storage/functions.query_db:72.json'}

exec(code, env_args)
