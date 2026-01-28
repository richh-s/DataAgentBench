code = """import json
import re

# Load the data files
mongo_path = locals()['var_functions.query_db:2']
citation_path = locals()['var_functions.query_db:6']

with open(mongo_path, 'r') as f:
    mongo_results = json.load(f)

with open(citation_path, 'r') as f:
    citation_results = json.load(f)

# Create citation dictionary
citation_dict = {}
for item in citation_results:
    title = item.get('title', '')
    citations = int(item.get('total_citations', 0))
    citation_dict[title] = citations

# Find 2016 physical activity papers
papers_2016 = []

for doc in mongo_results:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    if 'physical activity' in text.lower():
        # Check if 2016
        has_2016 = bool(re.search(r'2016', text))
        has_2015 = bool(re.search(r'2015', text))
        has_2017 = bool(re.search(r'2017', text))
        
        count_2016 = len(re.findall(r'\b2016\b', text))
        count_2015 = len(re.findall(r'\b2015\b', text))
        count_2017 = len(re.findall(r'\b2017\b', text))
        
        if has_2016 and count_2016 >= count_2015 and count_2016 >= count_2017:
            citations = citation_dict.get(title, 0)
            papers_2016.append({'title': title, 'total_citations': citations})

# Sort and format
papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Build output as a simple string
output = ''
for paper in papers_2016:
    output += 'Title: ' + paper['title'] + '\n'
    output += 'Total Citations: ' + str(paper['total_citations']) + '\n\n'

print('__RESULT__:')
print(output.strip())"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
