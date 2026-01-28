code = """import json
import re

# Read the MongoDB results file
with open('/tmp/tmpa8i6hpt8.json', 'r') as f:
    papers_data = json.load(f)

print(f"Total papers with 'physical activity' found: {len(papers_data)}")

# Function to extract year from paper text
def extract_year(text):
    # Look for year patterns in the text
    year_patterns = [
        r"\b(20\d{2})\b",  # Four digit year starting with 20
        r"\b(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*'?\s*(\d{2})\b",  # Venue with year
        r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s*(20\d{2})\b",  # Date format
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            for match in matches:
                if pattern.count('(') > 1:  # Multiple groups
                    for group in match:
                        if group and len(group) == 4:
                            year = int(group)
                            if 2010 <= year <= 2020:
                                return year
                        elif group and len(group) == 2:
                            year = 2000 + int(group)
                            if 2010 <= year <= 2020:
                                return year
                else:
                    if match and len(match) == 4:
                        year = int(match)
                        if 2010 <= year <= 2020:
                            return year
                    elif match and len(match) == 2:
                        year = 2000 + int(match)
                        if 2010 <= year <= 2020:
                            return year
    return None

# Extract paper information
papers_2016 = []
paper_titles_all = []

for paper in papers_data:
    # Extract title from filename
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Extract year from text
    year = extract_year(paper['text'])
    
    # Store for reference
    paper_titles_all.append({
        'title': title,
        'year': year,
        'filename': filename
    })
    
    # Check if it's from 2016
    if year == 2016:
        papers_2016.append({
            'title': title,
            'year': year
        })

print(f"Papers from 2016: {len(papers_2016)}")

# Show sample papers from 2016
if papers_2016:
    print("\nSample 2016 papers:")
    for p in papers_2016[:5]:
        print(f"  - {p['title']}")
else:
    print("No 2016 papers found in physical activity domain")
    # Show year distribution
    year_counts = {}
    for p in paper_titles_all:
        year = p['year']
        if year in year_counts:
            year_counts[year] += 1
        else:
            year_counts[year] = 1
    print("\nYear distribution:")
    for year in sorted(year_counts.keys()):
        if year:
            print(f"  {year}: {year_counts[year]}")

# Prepare result for next step
result = {
    'papers_2016': papers_2016,
    'count': len(papers_2016)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:9': {'status': 'debugging'}}

exec(code, env_args)
