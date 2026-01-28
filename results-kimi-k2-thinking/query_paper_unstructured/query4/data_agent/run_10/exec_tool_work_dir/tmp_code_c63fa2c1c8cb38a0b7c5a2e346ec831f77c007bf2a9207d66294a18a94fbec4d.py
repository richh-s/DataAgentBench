code = """import json
import re

# Get the file path from storage
mongo_file_path = locals()['var_functions.query_db:2']

# Read the MongoDB data
with open(mongo_file_path, 'r') as f:
    papers = json.load(f)

# Extract relevant information from each paper
papers_2016_physical_activity = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Get title from filename
    title = filename.replace('.txt', '')
    
    # Find year in text
    year_match = re.search(r'20(16)', text)
    if not year_match:
        continue
    year = int(year_match.group(0))
    
    # Check if it's from 2016
    if year != 2016:
        continue
    
    # Check for physical activity domain
    text_lower = text.lower()
    physical_activity_keywords = ['physical activity', 'fitness', 'exercise', 'workout', 'step count']
    has_physical_activity = any(keyword in text_lower for keyword in physical_activity_keywords)
    
    if has_physical_activity:
        papers_2016_physical_activity.append({
            'title': title,
            'year': year
        })

print('__RESULT__:')
print(json.dumps(papers_2016_physical_activity, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
