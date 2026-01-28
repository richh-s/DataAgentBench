code = """import json

# Read the MongoDB results file
result_path = var_functions.query_db:14
with open(result_path, 'r') as f:
    papers = json.load(f)

print('Total papers loaded:', len(papers))

# Find papers from 2016 mentioning physical activity in their content
physical_activity_papers_2016 = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Look for publication year in text (various patterns)
    year = None
    text_preview = text[:2000]
    
    # Check for year patterns
    import re
    year_match = re.search(r"(20\d{2})[^a-zA-Z0-9]", text_preview)
    if year_match:
        found_year = int(year_match.group(1))
        if 2010 <= found_year <= 2020:
            year = found_year
    
    # Check if it's from 2016 and mentions physical activity
    if year == 2016:
        # Check for physical activity domain
        if 'physical activity' in text.lower():
            physical_activity_papers_2016.append(title)
            print('Found:', title)

print('\nTotal 2016 physical activity papers:', len(physical_activity_papers_2016))

# Return the list of titles
print('__RESULT__:')
print(json.dumps(physical_activity_papers_2016))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:10': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.list_db:12': ['paper_docs'], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
