code = """import json
import re

# Load data
citation_path = locals()['var_functions.query_db:0']
mongodb_path = locals()['var_functions.query_db:2']

with open(citation_path, 'r') as f:
    citations_data = json.load(f)

with open(mongodb_path, 'r') as f:
    papers_data = json.load(f)

# Build citation dictionary with normalized titles
citation_dict = {}
for citation in citations_data:
    normalized = re.sub(r'[^a-zA-Z0-9]', '', citation['title'].lower())
    citation_dict[normalized] = {
        'original_title': citation['title'],
        'citation_count': int(citation['total_citations'])
    }

# Find empirical papers published after 2016 and match with citations
final_results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename:
        continue
    
    title = filename.replace('.txt', '')
    text = paper.get('text', '')
    
    # Extract year from the paper text
    year = 0
    
    # Try multiple year extraction patterns
    # Pattern 1: Four digit year in header or throughout text
    year_match = re.search(r'\b(20[1-2][0-9])\b', text)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Pattern 2: Try conference format like '17, '18, etc.
        year_match = re.search(r"\B'([0-9]{2})\b", text)
        if year_match:
            two_digit = int(year_match.group(1))
            if two_digit >= 17:
                year = 2000 + two_digit
    
    # Check if paper is empirical (contains "empirical")
    is_empirical = 'empirical' in text.lower()
    
    # Only process papers after 2016 with empirical contribution
    if year > 2016 and is_empirical:
        # Normalize title for matching
        normalized_title = re.sub(r'[^a-zA-Z0-9]', '', title.lower())
        
        # Check if this paper has citation data
        if normalized_title in citation_dict:
            citation_info = citation_dict[normalized_title]
            final_results.append({
                'title': title,
                'year': year,
                'total_citations': citation_info['citation_count']
            })

# Sort results by total citations (descending)
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

# Return JSON string
output = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': []}

exec(code, env_args)
