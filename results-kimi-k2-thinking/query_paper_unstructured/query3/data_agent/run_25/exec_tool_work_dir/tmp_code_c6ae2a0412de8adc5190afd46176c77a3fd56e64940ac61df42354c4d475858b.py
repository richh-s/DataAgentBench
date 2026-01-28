code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

# Build citation map
citation_map = {}
for c in citations:
    norm_title = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    citation_map[norm_title] = int(c['total_citations'])

# Find empirical papers after 2016 and match with citations
results = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if title:
        text = paper.get('text', '')
        
        # Extract year with multiple patterns
        year = 0
        
        # Pattern 1: Four digit year in header
        match = re.search(r'\b(20[1-2][0-9])\b', text[:1000])
        if match:
            year = int(match.group(1))
        else:
            # Pattern 2: Conference format '17, '18
            match = re.search(r"\B'([0-9]{2})\b", text[:500])
            if match:
                yr = int(match.group(1))
                if yr >= 17:
                    year = 2000 + yr
        
        # Check if empirical and after 2016
        is_empirical = 'empirical' in text.lower()
        
        if is_empirical and year > 2016:
            norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            citations_total = citation_map.get(norm_title, 0)
            
            if citations_total > 0:
                results.append({
                    'title': title,
                    'year': year,
                    'total_citations': citations_total
                })

# Sort by citations
def citation_key(item):
    return item['total_citations']

results.sort(key=citation_key, reverse=True)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:62': []}

exec(code, env_args)
