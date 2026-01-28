code = """import json
import re

# Load data
with open(locals()['var_functions.query_db:0'], 'r') as f:
    citations = json.load(f)

with open(locals()['var_functions.query_db:2'], 'r') as f:
    papers = json.load(f)

# Build citation map with normalized keys
norm_citation_map = {}
for c in citations:
    norm_key = re.sub(r'[^a-zA-Z0-9]', '', c['title'].lower())
    norm_citation_map[norm_key] = int(c['total_citations'])

# Extract empirical papers after 2016
empirical_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if title:
        text = paper.get('text', '')
        
        # Extract year - more flexible patterns
        year = 0
        
        # Pattern 1: Standard four-digit year
        match = re.search(r'\b(20[1-2][0-9])\b', text)
        if match:
            year = int(match.group(1))
        else:
            # Pattern 2: Conference format like '17, '18, '19, '20, '21, '22
            match = re.search(r"\B'([0-9]{2})\b", text)
            if match:
                year_num = int(match.group(1))
                if year_num >= 17:  # 2017 and later
                    year = 2000 + year_num
        
        # Check for empirical contribution
        has_empirical = 'empirical' in text.lower()
        
        if year > 2016 and has_empirical:
            # Prepare normalized title
            norm_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
            
            # Get citation count if available
            citation_count = norm_citation_map.get(norm_title, 0)
            
            if citation_count > 0:
                empirical_papers.append({
                    'title': title,
                    'year': year,
                    'total_citations': citation_count
                })

# Sort by citation count descending
empirical_papers.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(empirical_papers, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}]}

exec(code, env_args)
