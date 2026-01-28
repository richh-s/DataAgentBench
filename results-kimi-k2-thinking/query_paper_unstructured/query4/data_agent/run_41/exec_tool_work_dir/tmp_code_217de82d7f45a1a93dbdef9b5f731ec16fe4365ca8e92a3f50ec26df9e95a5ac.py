code = """import json

# Read the MongoDB query results (stored in file)
mongo_result_path = locals()['var_functions.query_db:0']
with open(mongo_result_path, 'r') as f:
    mongo_papers = json.load(f)

# Read the citations data
citations_result_path = locals()['var_functions.query_db:2']
with open(citations_result_path, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary of citations by title for easy lookup
citations_dict = {item['title']: int(item['total_citations']) for item in citations_data}

# Process MongoDB papers to extract relevant info
physical_activity_2016 = []

for paper in mongo_papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title (filename without .txt)
    title = filename.replace('.txt', '')
    
    # Check if paper is from 2016 and related to physical activity
    # Look for 2016 in text and check for physical activity domain
    if '2016' in text and 'physical activity' in text.lower():
        # Check if we have citation data for this title
        if title in citations_dict:
            physical_activity_2016.append({
                'title': title,
                'total_citations': citations_dict[title]
            })

# Sort by citation count (descending)
physical_activity_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Print results
result_str = json.dumps(physical_activity_2016, indent=2)
print('__RESULT__:')
print(result_str)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
