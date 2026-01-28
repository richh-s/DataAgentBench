code = """import json
import re

# Read the file containing papers with 2016
papers_2016_path = var_functions.query_db:2

with open(papers_2016_path, 'r') as f:
    papers_2016 = json.load(f)

print(f"Number of papers found with '2016' mentioned: {len(papers_2016)}")

# Sample a few papers to understand the structure
print("\nSample paper structure:")
for i, paper in enumerate(papers_2016[:3]):
    print(f"\nPaper {i+1}:")
    print(f"Filename: {paper['filename']}")
    print(f"Text preview: {paper['text'][:500]}...")

# Check for 'physical activity' in the text
physical_activity_papers = []
for paper in papers_2016:
    if re.search(r'physical activity', paper['text'], re.IGNORECASE):
        physical_activity_papers.append(paper)

print(f"\nNumber of papers with 'physical activity' mentioned: {len(physical_activity_papers)}")

# Extract titles and try to find publication year
results = []
for paper in physical_activity_papers:
    title = paper['filename'].replace('.txt', '')
    
    # Try to find the actual publication year in the text
    # Look for patterns like "CHI 2016" or conference year information
    text = paper['text']
    
    # Common patterns for year and venue
    year_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+(20\d{2})', text)
    if year_match:
        venue = year_match.group(1)
        year = int(year_match.group(2))
        if year == 2016:
            results.append({
                'title': title,
                'venue': venue,
                'year': year,
                'source': 'paper_docs_database'
            })
    else:
        # Other patterns for year
        year_match2 = re.search(r'20\d{2}', text)
        if year_match2:
            year = int(year_match2.group())
            if year == 2016:
                results.append({
                    'title': title,
                    'year': year,
                    'source': 'paper_docs_database'
                })"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}]}

exec(code, env_args)
