code = """import json
import re
from collections import defaultdict

# Load the MongoDB results from the file
mongo_result_path = var_functions.query_db:2
with open(mongo_result_path, 'r') as f:
    mongo_papers = json.load(f)

# Extract relevant papers from 2016 in physical activity domain
papers_2016 = []

for paper in mongo_papers:
    text = paper.get('text', '').lower()
    filename = paper.get('filename', '')
    
    # Check if text contains 'physical activity' and '2016'
    if 'physical activity' in text and '2016' in text:
        # Extract title from filename
        title = filename.replace('.txt', '')
        
        # Try to find the publication year more precisely
        # Look for patterns like "CHI 2016" or similar in the text
        year_match = re.search(r'(chi|ubicomp|cscw|dis|pervasivehealth|www|iui|ozchi|tei|ah)\s+2016', text, re.IGNORECASE)
        if year_match:
            # Verify this is actually a 2016 paper by checking the full text context
            papers_2016.append({
                'title': title,
                'filename': filename,
                '_id': str(paper.get('_id'))
            })

print('__RESULT__:')
print(json.dumps({
    'papers_found': len(papers_2016),
    'papers': papers_2016
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:4': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
