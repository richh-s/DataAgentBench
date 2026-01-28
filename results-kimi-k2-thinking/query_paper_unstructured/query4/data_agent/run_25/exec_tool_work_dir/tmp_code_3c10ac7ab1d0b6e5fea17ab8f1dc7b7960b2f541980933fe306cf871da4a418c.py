code = """import json

# Read the MongoDB query result
with open('/tmp/tmpj8l7g3q4.json', 'r') as f:
    papers_data = json.load(f)

print(f"Total papers retrieved: {len(papers_data)}")

# Process the papers to extract relevant information
filtered_papers = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title (remove .txt extension)
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if published in 2016 (search for 2016 in text, typically in header/footer)
    # Also check for 'physical activity' domain
    text_lower = text.lower()
    
    # Look for year indicators (2016 and common venue years)
    year_indicators = ['2016', 'chi 2016', 'ubicomp 2016', 'cscw 2016', 'dis 2016', 
                       'pervasivehealth 2016', 'www 2016', 'iui 2016', 'ozchi 2016', 
                       'tei 2016', 'ah 2016']
    
    has_2016 = any(indicator in text_lower for indicator in [y.lower() for y in year_indicators])
    
    # Check for physical activity domain
    has_physical_activity = 'physical activity' in text_lower or 'physical activities' in text_lower
    
    if has_2016 and has_physical_activity:
        filtered_papers.append({
            'title': title,
            'filename': filename
        })

print(f"Filtered papers (2016 + physical activity): {len(filtered_papers)}")
print("Sample filtered papers:")
for i, paper in enumerate(filtered_papers[:5]):
    print(f"  {i+1}. {paper['title']}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
