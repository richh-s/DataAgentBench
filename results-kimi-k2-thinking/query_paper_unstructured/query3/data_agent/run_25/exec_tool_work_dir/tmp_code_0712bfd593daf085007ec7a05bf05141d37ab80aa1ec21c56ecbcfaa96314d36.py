code = """import json
import re

# Load data
citation_path = str(locals()['var_functions.query_db:0'])
mongodb_path = str(locals()['var_functions.query_db:2'])

with open(citation_path, 'r') as f:
    citations = json.load(f)

with open(mongodb_path, 'r') as f:
    papers = json.load(f)

print('Loaded', len(citations), 'citations and', len(papers), 'papers')

# Build citation lookup (normalized title -> total citations)
citation_lookup = {}
for citation in citations:
    norm_key = re.sub(r'[^a-zA-Z0-9]', '', citation['title'].lower())
    citation_lookup[norm_key] = int(citation['total_citations'])

# Find empirical papers published after 2016
empirical_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if title:
        text = paper.get('text', '')
        
        # Extract year - multiple patterns
        year = 0
        
        # Pattern 1: Standard year format (20XX)
        match1 = re.search(r'\b(20[1-2][0-9])\b', text[:800])
        if match1:
            year = int(match1.group(1))
        else:
            # Pattern 2: Conference format like '17, '18
            match2 = re.search(r"\B'([0-9]{2})\b", text[:500])
            if match2:
                yr = int(match2.group(1))
                if yr >= 17:
                    year = 2000 + yr
        
        # Check for empirical contribution
        is_empirical = 'empirical' in text.lower()
        
        if year > 2016 and is_empirical:
            empirical_papers.append({
                'title': title,
                'year': year
            })

print('Empirical papers after 2016:', len(empirical_papers))

# Match with citation data
def normalize(text):
    return re.sub(r'[^a-zA-Z0-9]', '', text.lower())

results = []
for paper in empirical_papers:
    norm_title = normalize(paper['title'])
    if norm_title in citation_lookup:
        paper_info = {
            'title': paper['title'],
            'year': paper['year'],
            'total_citations': citation_lookup[norm_title]
        }
        results.append(paper_info)

# Sort by citation count
def compare_citations(item):
    return item['total_citations']

results.sort(key=compare_citations, reverse=True)

print('Final results count:', len(results))

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': []}

exec(code, env_args)
