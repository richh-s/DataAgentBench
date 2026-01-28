code = """import json
import re
import os

# Access the papers file path from the storage
papers_file_path = var_functions.query_db:10

# Read the papers data
with open(papers_file_path, 'r') as f:
    papers = json.load(f)

print(f"Found {len(papers)} papers with 'physical activity' and '2016' mentions")

# Filter for papers actually published in 2016 in physical activity domain
papers_2016 = []

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Look for venue year patterns (e.g., "CHI 2016")
    matches = re.findall(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|ISS)\s+(20\d{2})', text)
    
    if matches:
        for venue, year_str in matches:
            year = int(year_str)
            if year == 2016:
                # Double check physical activity mention
                if re.search(r'physical activity', text, re.IGNORECASE):
                    papers_2016.append({
                        'title': title,
                        'venue': venue
                    })
                break
    else:
        # Fallback to looking for 2016 in copyright
        copyright_match = re.search(r'20\d{2}', text[:1000])
        if copyright_match:
            year = int(copyright_match.group())
            if year == 2016 and re.search(r'physical activity', text, re.IGNORECASE):
                papers_2016.append({
                    'title': title,
                    'venue': None
                })

print(f"Papers from 2016 in physical activity domain: {len(papers_2016)}")
for p in papers_2016:
    print(f"  - {p['title']}")

# Extract titles for citation lookup
titles_to_lookup = [p['title'] for p in papers_2016]

result = {
    'papers': papers_2016,
    'titles': titles_to_lookup
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:8': ['paper_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
