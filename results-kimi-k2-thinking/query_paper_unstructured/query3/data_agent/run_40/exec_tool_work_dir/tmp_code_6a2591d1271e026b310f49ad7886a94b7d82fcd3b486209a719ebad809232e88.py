code = """import json
import re

# Read the MongoDB query results from the file
mongo_file_path = locals()['var_functions.query_db:6']
with open(mongo_file_path, 'r') as f:
    mongo_papers = json.load(f)

print(f"Total papers with 'empirical' and year found (regex): {len(mongo_papers)}")

# Extract paper information: title and year
paper_info = []
year_pattern = re.compile(r'(20(17|18|19|20|21|22|23|24|25))')

for paper in mongo_papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year_match = year_pattern.search(text)
    if year_match:
        year = int(year_match.group(1))
        if year >= 2017:
            paper_info.append({
                'title': title,
                'year': year
            })

print(f"Filtered papers after year check (>= 2017): {len(paper_info)}")

# Output result in required format
result = json.dumps(paper_info[:10])  # Just show first 10 for preview
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
