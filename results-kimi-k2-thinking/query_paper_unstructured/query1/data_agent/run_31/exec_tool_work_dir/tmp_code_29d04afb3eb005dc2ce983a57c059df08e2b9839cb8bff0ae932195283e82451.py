code = """import os
import json

# Let me explore the directory structure to find the data files
def find_data_files():
    data_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if 'query_' in file and file.endswith('.json'):
                filepath = os.path.join(root, file)
                data_files.append(filepath)
    return data_files

data_files = find_data_files()

print('Found the following data files:')
for i, f in enumerate(data_files):
    print(f"{i}: {f}")

# Try to load the most likely candidates
if len(data_files) >= 2:
    # Load citations
    citations_path = data_files[0]
    papers_path = data_files[1]
    
    with open(citations_path) as cf:
        citations = json.load(cf)
    with open(papers_path) as pf:
        papers = json.load(pf)
    
    print(f"\nLoaded {len(citations)} citations from {citations_path}")
    print(f"Loaded {len(papers)} papers from {papers_path}")
    
    # Identify food-related papers
    food_keywords = ['food', 'diet', 'nutrition', 'eating', 'meal', 'dietary', 'calorie']
    food_titles = []
    
    for paper in papers:
        text = paper.get('text', '').lower()
        filename = paper.get('filename', '')
        if any(kw in text for kw in food_keywords):
            title = filename.replace('.txt', '')
            food_titles.append(title)
    
    print(f"Found {len(food_titles)} food-related papers")
    
    # Calculate citations for food papers
    citation_dict = {c.get('title'): int(c.get('total_citations', 0)) for c in citations}
    total_citations = sum(citation_dict[t] for t in food_titles if t in citation_dict)
    
    print(f"Total citations for food papers: {total_citations}")

result = {"total_citations": total_citations if 'total_citations' in locals() else 0}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
