code = """import json
import re

# Read the MongoDB query results from the file
with open('var_functions.query_db:0', 'r') as f:
    papers_data = json.load(f)

# Function to extract year from paper text
def extract_year(text):
    # Look for patterns like '2016', 'CHI 2016', 'Ubicomp 2016', etc.
    year_patterns = [
        r"\b(20\d{2})\b",  # Four digit year starting with 20
        r"\b(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?\s*(\d{2})\b",  # Venue with year
        r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s*(20\d{2})\b",  # Date format
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text)
        if matches:
            for match in matches:
                if len(match) == 4:  # Full year
                    year = int(match)
                    if 2010 <= year <= 2020:  # Reasonable range
                        return year
                elif len(match) == 2:  # Two digit year
                    year = 2000 + int(match)
                    if 2010 <= year <= 2020:
                        return year
    return None

# Process papers to extract relevant information
papers_2016 = []
for paper in papers_data:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = extract_year(paper['text'])
    
    # Check if it's from 2016
    if year == 2016:
        papers_2016.append({
            'title': title,
            'year': year,
            'text_preview': paper['text'][:500]  # Store preview for debugging
        })

print(f"Found {len(papers_2016)} papers from 2016 in physical activity domain")

# Show first few papers if any found
if papers_2016:
    print("Sample papers:")
    for p in papers_2016[:3]:
        print(f"  - {p['title']}")
        
# Save results
result = {
    'papers_2016': papers_2016,
    'count': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
