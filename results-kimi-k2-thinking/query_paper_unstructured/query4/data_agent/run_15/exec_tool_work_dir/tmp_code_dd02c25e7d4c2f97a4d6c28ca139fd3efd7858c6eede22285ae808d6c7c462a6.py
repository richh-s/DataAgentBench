code = """import json, os, re

# Get the file path from storage
result_key = 'var_functions.query_db:2'
if result_key in locals():
    result_path = locals()[result_key]
    print("Found file path:", result_path)
else:
    print("Key not found in locals")
    result_path = None

# List available files to debug
print("\nFiles in current directory:")
for f in os.listdir('.'):
    if '.json' in f:
        print(" ", f)

# Try to load and process documents
papers_2016_pa_titles = []

if result_path and os.path.exists(result_path):
    with open(result_path, 'r') as f:
        paper_docs = json.load(f)
    
    print(f"\nLoaded {len(paper_docs)} documents")
    
    papers_info = []
    for doc in paper_docs:
        filename = doc.get('filename', '')
        text = doc.get('text', '')
        title = filename.replace('.txt', '') if filename else ''
        
        if not title:
            continue
        
        # Extract year
        year = None
        header_text = text[:1000]
        year_matches = re.findall(r'\b20\d{2}\b', header_text)
        if year_matches:
            for match in year_matches:
                year_val = int(match)
                if 2010 <= year_val <= 2020:
                    year = year_val
                    break
        
        # Check for physical activity
        is_physical_activity = 'physical activity' in text.lower()
        
        if title and year:
            papers_info.append({
                'title': title,
                'year': year,
                'is_physical_activity': is_physical_activity
            })
    
    # Filter for 2016 physical activity
    papers_2016_pa = [p for p in papers_info if p['year'] == 2016 and p['is_physical_activity']]
    papers_2016_pa_titles = [p['title'] for p in papers_2016_pa]
    
    print(f"Found {len(papers_2016_pa_titles)} papers from 2016 in physical activity domain")
    
    # Show some stats
    all_years = [p['year'] for p in papers_info]
    pa_by_year = {}
    for p in papers_info:
        if p['is_physical_activity']:
            year = p['year']
            pa_by_year[year] = pa_by_year.get(year, 0) + 1
    
    print("\nPhysical activity papers by year:")
    for year in sorted(pa_by_year.keys()):
        print(f"  {year}: {pa_by_year[year]}")

print('__RESULT__:')
print(json.dumps(papers_2016_pa_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
