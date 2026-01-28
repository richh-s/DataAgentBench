code = """import json
import re

# Load data files
citation_file_path = locals()['var_functions.query_db:0']
papers_file_path = locals()['var_functions.query_db:2']

with open(citation_file_path, 'r') as f:
    citations_data = json.load(f)

with open(papers_file_path, 'r') as f:
    papers_data = json.load(f)

# Build a citation dictionary with normalized titles for matching
citation_dict = {}
for citation_record in citations_data:
    normalized_title = re.sub(r'[^a-zA-Z0-9]', '', citation_record['title'].lower())
    citation_dict[normalized_title] = int(citation_record['total_citations'])

# Find empirical papers published after 2016 and join with citation data
final_results = []

for paper_document in papers_data:
    # Extract title from filename
    file_name = paper_document.get('filename', '')
    paper_title = file_name.replace('.txt', '') if file_name else ''
    
    if not paper_title:
        continue
    
    paper_text = paper_document.get('text', '')
    
    # Extract publication year from the paper text
    publication_year = 0
    
    # Try to find a four-digit year in the format 20XX (e.g., 2017, 2018, etc.)
    year_match = re.search(r'\b(20[1-2][0-9])\b', paper_text[:2000])
    if year_match:
        publication_year = int(year_match.group(1))
    else:
        # Try alternative format: conference year like '17, '18, etc.
        year_match_alt = re.search(r"\B'([0-9]{2})\b", paper_text[:2000])
        if year_match_alt:
            two_digit_year = int(year_match_alt.group(1))
            if two_digit_year >= 17:
                publication_year = 2000 + two_digit_year
    
    # Check if the paper has an empirical contribution
    is_empirical = 'empirical' in paper_text.lower()
    
    # Only process papers published after 2016 with empirical contribution
    if publication_year > 2016 and is_empirical:
        normalized_paper_title = re.sub(r'[^a-zA-Z0-9]', '', paper_title.lower())
        
        if normalized_paper_title in citation_dict:
            citation_count = citation_dict[normalized_paper_title]
            final_results.append({
                'title': paper_title,
                'year': publication_year,
                'total_citations': citation_count
            })

# Sort results by total citations in descending order
final_results.sort(key=lambda x: x['total_citations'], reverse=True)

# Output the results as JSON
output_json = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': [], 'var_functions.execute_python:14': [], 'var_functions.execute_python:20': [], 'var_functions.execute_python:22': [], 'var_functions.execute_python:26': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:38': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:48': [], 'var_functions.query_db:50': [{'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'citation_count': '53'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '58'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '3'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '12'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '38'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '29'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '52'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '89'}, {'title': 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'citation_count': '32'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': '77'}], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.execute_python:62': [], 'var_functions.execute_python:66': []}

exec(code, env_args)
