code = """import json
import re

# Get the file path from storage
papers_file_path = var_functions.query_db:20
print(f"Papers file path: {papers_file_path}")

# Load the papers data from the file
with open(papers_file_path, 'r') as f:
    papers_2016_raw = json.load(f)

print(f"Successfully loaded {len(papers_2016_raw)} papers")
print(f"First paper keys: {list(papers_2016_raw[0].keys())}")

# Initialize list to store papers from 2016 in physical activity domain
papers_2016_physical_activity = []

for paper in papers_2016_raw:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Check if published in 2016 and related to physical activity
    # Look for venue year patterns
    import re
    venue_year_matches = re.findall(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|ISS)\s+(20\d{2})', text)
    
    is_2016 = False
    venue = None
    
    for v, y in venue_year_matches:
        if int(y) == 2016:
            is_2016 = True
            venue = v
            break
    
    # Also check for physical activity domain
    physical_activity_match = re.search(r'physical activity', text, re.IGNORECASE)
    
    if is_2016 and physical_activity_match:
        papers_2016_physical_activity.append({
            'title': title,
            'venue': venue
        })

print(f"\nPapers from 2016 in physical activity domain: {len(papers_2016_physical_activity)}")
for p in papers_2016_physical_activity:
    print(f"- {p['title']} ({p['venue']})")

# Extract titles for citation lookup
titles_to_lookup = [p['title'] for p in papers_2016_physical_activity]

result_dict = {
    'papers': papers_2016_physical_activity,
    'titles': titles_to_lookup
}

print("__RESULT__:")
print(json.dumps(result_dict))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:8': ['paper_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json'}

exec(code, env_args)
