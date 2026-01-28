code = """import json

# Get the file paths
citation_file_path = locals()['var_functions.query_db:0']
paper_file_path = locals()['var_functions.query_db:2']

# Load citation data more carefully
citation_data = []
try:
    with open(citation_file_path, 'r') as f:
        content = f.read().strip()
        # Try to parse as JSON array
        if content.startswith('['):
            citation_data = json.loads(content)
        else:
            # Try line by line
            for line in content.split('\n'):
                line = line.strip()
                if line:
                    try:
                        citation_data.append(json.loads(line))
                    except:
                        pass
except Exception as e:
    print(f"Error loading citations: {e}")

# Load paper data
paper_data = []
try:
    with open(paper_file_path, 'r') as f:
        content = f.read().strip()
        if content.startswith('['):
            paper_data = json.loads(content)
        else:
            for line in content.split('\n'):
                line = line.strip()
                if line:
                    try:
                        paper_data.append(json.loads(line))
                    except:
                        pass
except Exception as e:
    print(f"Error loading papers: {e}")

# Debug info
print(f"Loaded {len(citation_data)} citation records")
print(f"Loaded {len(paper_data)} paper documents")

# Extract ACM papers
acm_titles = set()
for paper in paper_data:
    text = paper.get('text', '').lower()
    if 'acm' in text:
        filename = paper.get('filename', '')
        if filename:
            title = filename.replace('.txt', '')
            acm_titles.add(title)

print(f"Found {len(acm_titles)} ACM papers")

# Create citation dictionary
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['citation_count'])

# Find matches
matched_citations = []
for title in acm_titles:
    if title in citation_dict:
        matched_citations.append(citation_dict[title])

avg_citations = sum(matched_citations) / len(matched_citations) if matched_citations else 0

result = {
    'avg_citations': avg_citations,
    'matched_papers': len(matched_citations),
    'acm_papers': len(acm_titles)
}

print('__RESULT__')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'status': 'files_checked'}}

exec(code, env_args)
