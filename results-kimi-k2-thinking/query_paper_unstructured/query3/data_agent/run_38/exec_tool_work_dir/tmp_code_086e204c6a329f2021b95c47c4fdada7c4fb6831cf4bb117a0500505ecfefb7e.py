code = """import json
import re

# Access stored query results
papers_data = locals()['var_functions.query_db:30']
citations_data = locals()['var_functions.query_db:28']

# Debug: check data types
print('Type papers_data:', type(papers_data))
print('Type citations_data:', type(citations_data))
print('Papers count:', len(papers_data))
print('Citations count:', len(citations_data))

# Create citation lookup map
citation_map = {item['title']: int(item['total_citations']) for item in citations_data}

# Process papers
results = []
for doc in papers_data:
    # Extract title
    title = doc['filename'].replace('.txt', '')
    
    # Extract year from text
    text = doc['text']
    year_match = re.search(r'(20\d{2}|19\d{2})', text)
    year = int(year_match.group(1)) if year_match else None
    
    # Check for empirical contribution
    has_empirical = 'empirical' in text.lower()
    
    # Apply filters and match with citations
    if has_empirical and year and year > 2016 and title in citation_map:
        results.append({
            'title': title,
            'total_citations': citation_map[title]
        })

# Sort by citations descending
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

# Format final output
output_list = [f"{r['title']}: {r['total_citations']} citations" for r in results_sorted]

# Return result in required format
result_json = json.dumps(output_list)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.execute_python:40': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App: 266 citations', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection: 265 citations']}

exec(code, env_args)
