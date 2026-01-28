code = """import json
import re

# Read the file containing the MongoDB query result
with open('var_functions.query_db:2', 'r') as f:
    papers_data = json.load(f)

print("Total papers found:", len(papers_data))
print("Sample paper structure:")
if papers_data:
    print(json.dumps(papers_data[0], indent=2)[:1000])

# Extract paper titles and publication years
papers_info = []
for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '')
    
    # Try to extract year from text (look for patterns like "2015", "2016", etc.)
    year_match = re.search(r'(19|20)\d{2}', text)
    year = int(year_match.group()) if year_match else None
    
    papers_info.append({
        'title': title,
        'year': year,
        'filename': filename
    })

print("\nFirst 5 papers info:")
for p in papers_info[:5]:
    print(p)

print("\nPapers after 2016:")
after_2016 = [p for p in papers_info if p['year'] and p['year'] > 2016]
print(f"Count: {len(after_2016)}")
for p in after_2016[:10]:
    print(f"  {p['title']} ({p['year']})")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
