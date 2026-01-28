code = """import json
import re

papers_file = var_functions.query_db:10

# Read the file from the path that was provided
with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers found: {len(papers)}")

# Process papers to extract title and year information
papers_2016_physical_activity = []

for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Check if paper is from 2016 by looking for venue+year patterns
    venue_year_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|ISS)\s+(20\d{2})', text)
    
    year = None
    venue = None
    
    if venue_year_match:
        venue = venue_year_match.group(1)
        year = int(venue_year_match.group(2))
    else:
        # Try to extract year from copyright line
        copyright_match = re.search(r'20\d{2}', text)
        if copyright_match:
            year = int(copyright_match.group())
    
    # Only include papers from 2016
    if year == 2016:
        # Check if it mentions physical activity
        if re.search(r'physical activity', text, re.IGNORECASE):
            papers_2016_physical_activity.append({
                'title': title,
                'year': year,
                'venue': venue
            })

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_physical_activity)}")

# Display the papers found
for paper in papers_2016_physical_activity:
    print(f"Title: {paper['title']}")
    print(f"Venue: {paper['venue']}")
    print()

# Get just the titles for citation lookup
titles = [p['title'] for p in papers_2016_physical_activity]

print("__RESULT__:")
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:8': ['paper_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
