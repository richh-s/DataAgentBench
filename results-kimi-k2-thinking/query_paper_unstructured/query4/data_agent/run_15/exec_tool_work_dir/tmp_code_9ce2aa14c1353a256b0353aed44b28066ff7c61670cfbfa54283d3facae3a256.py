code = """import json, os, re

# Read the paper documents from the file
result_path = var_functions.query_db:2

with open(result_path, 'r') as f:
    paper_docs = json.load(f)

# Sample some documents to better understand structure
print(f"Total documents: {len(paper_docs)}")
print("\nFirst 3 documents:")
for i, doc in enumerate(paper_docs[:3]):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text_preview = doc.get('text', '')[:500]
    print(f"\n{i+1}. {title}")
    print(f"   Text preview: {text_preview[:100]}...")
    
    # Check for 'physical activity' in the text
    contains_pa = 'physical activity' in doc.get('text', '').lower()
    print(f"   Contains 'physical activity': {contains_pa}")
    
    # Search for year in text
    year_patterns = [r"(\b20\d{2}\b)"]
    year = None
    for pattern in year_patterns:
        matches = re.findall(pattern, text_preview)
        if matches:
            for match in matches:
                year_val = int(match)
                if 2010 <= year_val <= 2020:
                    year = year_val
                    break
            if year:
                break
    print(f"   Year found: {year}")

# Now process all documents more carefully
papers_info = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    if not title:
        continue
    
    year = None
    # Look for year in first 1000 characters where headers are
    header_text = text[:1000]
    year_matches = re.findall(r"\b20\d{2}\b", header_text)
    if year_matches:
        for match in year_matches:
            year_val = int(match)
            if 2010 <= year_val <= 2020:
                year = year_val
                break
    
    # Check for physical activity - case insensitive
    is_physical_activity = 'physical activity' in text.lower()
    
    # Only add if we have both title and valid year
    if title and year:
        papers_info.append({
            'title': title,
            'year': year,
            'is_physical_activity': is_physical_activity
        })

# Count by year and domain
from collections import Counter
year_counts = Counter([p['year'] for p in papers_info])
pa_counts = Counter([p['year'] for p in papers_info if p['is_physical_activity']])

print(f"\nTotal papers with valid years: {len(papers_info)}")
print("\nPapers by year:")
for year in sorted(year_counts.keys()):
    print(f"  {year}: {year_counts[year]} total, {pa_counts[year]} physical activity")

# Filter for 2016 physical activity papers
papers_2016_pa = [p for p in papers_info if p['year'] == 2016 and p['is_physical_activity']]

print(f"\nFound {len(papers_2016_pa)} papers from 2016 in physical activity domain")
if papers_2016_pa:
    print("Paper titles:")
    for p in papers_2016_pa:
        print(f"  - {p['title']}")
else:
    # Let's check all 2016 papers to see if we're missing domain classification
    papers_2016 = [p for p in papers_info if p['year'] == 2016]
    print(f"\nAll 2016 papers ({len(papers_2016)} total):")
    for p in papers_2016:
        print(f"  - {p['title']} (PA: {p['is_physical_activity']})")

filtered_titles = [p['title'] for p in papers_2016_pa]

print('__RESULT__:')
print(json.dumps(filtered_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}]}

exec(code, env_args)
