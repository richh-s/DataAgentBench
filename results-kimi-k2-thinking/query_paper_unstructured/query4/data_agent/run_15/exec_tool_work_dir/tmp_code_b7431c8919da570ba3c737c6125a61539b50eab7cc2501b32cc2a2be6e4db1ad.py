code = """import json, os, re

# Load paper documents
file_path = locals()['var_functions.query_db:2']
with open(file_path) as f:
    paper_docs = json.load(f)

print(f"Total documents: {len(paper_docs)}")

# Let's analyze a few documents more carefully to understand structure
sample_docs = paper_docs[:10]
for i, doc in enumerate(sample_docs):
    print(f"\n--- Document {i+1} ---")
    title = doc.get('filename', '').replace('.txt', '')
    print(f"Title: {title}")
    
    # Show first 200 chars of text to see structure
    text_preview = doc.get('text', '')[:200]
    print(f"Text start: {text_preview}")
    
    # Check for year patterns more carefully
    text = doc.get('text', '')
    year_matches = re.findall(r'\b20\d{2}\b', text[:1000])
    print(f"Year matches: {year_matches}")
    
    # Check for physical activity
    has_pa = 'physical activity' in text.lower()
    print(f"Has 'physical activity': {has_pa}")

# Now process all documents to see overall distribution
all_years = []
pa_by_year = {}

for doc in paper_docs:
    text = doc.get('text', '')
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    # Get year
    year = None
    matches = re.findall(r'\b20\d{2}\b', text[:1000])
    for m in matches:
        y = int(m)
        if 2010 <= y <= 2020:
            year = y
            break
    
    if year:
        all_years.append(year)
        
        # Check for physical activity
        if 'physical activity' in text.lower():
            pa_by_year[year] = pa_by_year.get(year, 0) + 1

print(f"\n\nOverall statistics:")
print(f"Total papers with valid years: {len(all_years)}")
print(f"Year range: {min(all_years) if all_years else 'N/A'} - {max(all_years) if all_years else 'N/A'}")

print(f"\nPhysical activity papers by year:")
for year in sorted(pa_by_year.keys()):
    print(f"  {year}: {pa_by_year[year]} papers")

# Check 2016 specifically
papers_2016 = [i for i, y in enumerate(all_years) if y == 2016]
print(f"\nTotal 2016 papers: {len(papers_2016)}")

# Look at all 2016 papers to see their domains
print(f"\nAll 2016 papers:")
titles_2016 = []
for doc in paper_docs:
    text = doc.get('text', '')
    title = doc.get('filename', '').replace('.txt', '')
    if not title:
        continue
    
    matches = re.findall(r'\b20\d{2}\b', text[:1000])
    year = None
    for m in matches:
        y = int(m)
        if 2010 <= y <= 2020:
            year = y
            break
    
    if year == 2016:
        has_pa = 'physical activity' in text.lower()
        titles_2016.append(title)
        print(f"  - {title[:60]}... (PA: {has_pa})")

print('__RESULT__:')
print(json.dumps({'total_2016': len(titles_2016), 'pa_by_year': pa_by_year}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': [], 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.execute_python:22': []}

exec(code, env_args)
