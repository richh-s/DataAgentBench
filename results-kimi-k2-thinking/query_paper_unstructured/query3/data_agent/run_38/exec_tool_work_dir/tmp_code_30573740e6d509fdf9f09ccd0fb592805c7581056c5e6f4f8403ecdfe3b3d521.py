code = """import json
import re

# Load the data files
with open('var_functions.query_db:30.json', 'r') as f:
    paper_docs = json.load(f)

with open('var_functions.query_db:28.json', 'r') as f:
    citations = json.load(f)

# Create citation lookup dictionary
citation_dict = {cit['title']: int(cit['total_citations']) for cit in citations}

# Process all papers
results = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    year_match = re.search(r'(20\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    has_empirical = 'empirical' in text.lower()
    
    if has_empirical and year and year > 2016 and title in citation_dict:
        results.append({
            'title': title,
            'total_citations': citation_dict[title]
        })

# Sort by citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Format output
output = []
for item in results_sorted:
    output.append(item['title'] + ': ' + str(item['total_citations']) + ' citations')

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations']}

exec(code, env_args)
