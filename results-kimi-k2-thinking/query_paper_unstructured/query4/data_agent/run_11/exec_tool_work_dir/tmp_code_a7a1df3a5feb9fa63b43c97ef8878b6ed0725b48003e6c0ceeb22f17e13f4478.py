code = """import json
import re

# Access the large result from the stored variable
papers_file_path = locals()['var_functions.query_db:2']

# Load the papers data from file
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

# Initialize a list to store papers from 2016 in physical activity domain
papers_2016_physical_activity = []

for paper in papers:
    paper_text = paper.get('text', '')
    filename = paper.get('filename', '')
    
    # Extract title as the filename without .txt extension
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if the paper is from 2016
    # Look for 2016 in various patterns (year mention, copyright, etc.)
    year_patterns = [
        r'2016[,\s]+[^\d]{0,30}(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)',
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[^\d]{0,30}2016',
        r'Copyright[^\d]{0,50}2016',
        r'2016[^\d]{0,100}Copyright',
        r'DOI[^\d]{0,100}2016',
        r'ISBN[^\d]{0,100}2016'
    ]
    
    is_2016 = any(re.search(pattern, paper_text, re.IGNORECASE) for pattern in year_patterns)
    
    # Check if paper is in 'physical activity' domain
    # Look for keywords related to physical activity
    activity_patterns = [
        r'physical activity', r'exercise', r'fitness', r'step count', r'steps',
        r'activity tracking', r'fitness tracker', r'workout', r'sedentary',
        r'walking', r'running', r'sports', r'calorie', r'energy expenditure'
    ]
    
    is_physical_activity = any(re.search(pattern, paper_text, re.IGNORECASE) for pattern in activity_patterns)
    
    if is_2016 and is_physical_activity:
        papers_2016_physical_activity.append({
            'title': title,
            '_id': paper.get('_id'),
            'filename': filename
        })

# Print the result
result = json.dumps(papers_2016_physical_activity, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
