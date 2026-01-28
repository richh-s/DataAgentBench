code = """import json
import re

# Read the papers that contain both 'physical activity' and '2016'
papers_file = var_functions.query_db:10

with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f"Total papers found with 'physical activity' and '2016' mentions: {len(papers)}")

# Extract paper information
paper_info = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Try to find the actual publication year from conference/journal headers
    # Look for patterns like "CHI 2016" or conference information with year
    year_match = None
    
    # Common venue patterns
    patterns = [
        r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|ISS)\s+(20\d{2})',
        r'(Proceedings of .*?20\d{2})',
        r'(April\s+\d{1,2}\s*[-,]\s*)?(\d{4})',
    ]
    
    year = None
    venue = None
    
    # First try to find venue + year pattern
    venue_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST|ISS)\s+(20\d{2})', text)
    if venue_match:
        venue = venue_match.group(1)
        year = int(venue_match.group(2))
    else:
        # Look for copyright year which is often near the beginning
        copyright_match = re.search(r'\u00a9\s+(20\d{2})', text)
        if copyright_match:
            year = int(copyright_match.group(1))
        else:
            # Look for any 2016 in the text as fallback
            year_match = re.search(r'\b2016\b', text)
            if year_match:
                year = 2016
    
    if year == 2016:
        # Check if it mentions physical activity domain
        if re.search(r'physical activity', text, re.IGNORECASE):
            paper_info.append({
                'title': title,
                'year': year,
                'venue': venue,
                'source': 'paper_docs_database'
            })

print(f"\nPapers from 2016 in physical activity domain: {len(paper_info)}")
for p in paper_info:
    print(f"- {p['title']}")

# Store the titles for the next query
titles = [p['title'] for p in paper_info]
print("\nTitles to query for citations:")
for t in titles[:10]:  # Print first 10
    print(f"- {t}")

print(f"__RESULT__:")
print(json.dumps(titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.list_db:8': ['paper_docs'], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json'}

exec(code, env_args)
