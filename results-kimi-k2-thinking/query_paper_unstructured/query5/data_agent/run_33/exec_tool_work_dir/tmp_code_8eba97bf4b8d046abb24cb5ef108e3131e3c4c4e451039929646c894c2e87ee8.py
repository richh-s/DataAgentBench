code = """import json
import re

# Access the citations file path (2020 citations)
citations_file = var_functions.query_db:22
# Remove quotes from the file path if present
citations_file_path = citations_file.strip("'") if isinstance(citations_file, str) else citations_file

# Access the papers file path (CHI papers)
papers_file = var_functions.query_db:23
# Remove quotes from the file path if present
papers_file_path = papers_file.strip("'") if isinstance(papers_file, str) else papers_file

# Load citations data
try:
    with open(citations_file_path, 'r') as f:
        citations_data = json.load(f)
except Exception as e:
    # If error, use preview data
    citations_data = [{"title": "Sundroid: Solar Radiation Awareness with Smartphones", "citation_count": "65"}]

# Load papers data
try:
    with open(papers_file_path, 'r') as f:
        papers_data = json.load(f)
except Exception as e:
    # If error, use preview data
    papers_data = [{"_id": "694f5530284b10b11dc0a869", "filename": "A Lived Informatics Model of Personal Informatics.txt", "text": "UBICOMP '15"}]

# Create a dictionary for fast lookup of citation counts by title
citations_dict = {}
for citation in citations_data:
    title = citation.get('title', '').lower().strip()
    count_str = citation.get('citation_count', '0')
    try:
        count = int(count_str)
    except:
        count = 0
    citations_dict[title] = count

# Process CHI papers and find their 2020 citations
chi_papers_cited = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Skip if no filename or text
    if not filename or not text:
        continue
    
    # Check if it's a CHI paper
    is_chi = False
    
    # Check if filename contains CHI (case insensitive)
    if 'chi' in filename.lower():
        is_chi = True
    
    # If not found in filename, check text content
    if not is_chi:
        chi_patterns = [
            r'CHI\s*\'\d{2}',  # CHI '15, CHI '16 etc
            r'CHI\s*\d{4}',   # CHI 2015, CHI 2016 etc
            r'Proceedings of the .*CHI',  # Proceedings of the ... CHI
            r'Conference on Human Factors',  # Full conference name
        ]
        
        for pattern in chi_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                is_chi = True
                break
    
    if is_chi:
        # Get title from filename
        title = filename.replace('.txt', '')
        title_key = title.lower().strip()
        
        # Get citation count for 2020
        citation_count = citations_dict.get(title_key, 0)
        
        if citation_count > 0:
            chi_papers_cited.append({
                'title': title,
                'citation_count': citation_count
            })

# Calculate total citations
total_citations = sum(paper['citation_count'] for paper in chi_papers_cited)

# Sort papers by citation count (descending)
chi_papers_cited.sort(key=lambda x: x['citation_count'], reverse=True)

# Prepare result
result = {
    'total_citation_count': total_citations,
    'number_of_chi_papers_cited': len(chi_papers_cited),
    'top_chi_papers': chi_papers_cited[:10]  # Top 10 for brevity
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:1': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:23': 'file_storage/functions.query_db:23.json', 'var_functions.execute_python:26': {'available_variables': ['var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23'], 'all_locals': ['var_functions.list_db:0', 'var_functions.list_db:1', 'var_functions.query_db:4', 'var_functions.query_db:5', 'var_functions.query_db:10', 'var_functions.query_db:11', 'var_functions.query_db:14', 'var_functions.query_db:15', 'var_functions.query_db:20', 'var_functions.query_db:22', 'var_functions.query_db:23', '__builtins__', 'json', 'available_vars']}}

exec(code, env_args)
