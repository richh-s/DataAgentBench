code = """import json
import re

# Load the MongoDB paper documents from the file
with open('paper_docs_query_result.json', 'r') as f:
    paper_docs = json.load(f)

print(f"Loaded {len(paper_docs)} paper documents")

# Extract paper information: title, year, domain
papers_info = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for year patterns (e.g., 2016, '16)
    year = None
    # Look for patterns like: year numbers in headers, or specific year mentions
    year_patterns = [
        r"(\b20\d{2}\b)",  # Full year like 2016
        r"'\s?(\d{2})\b",  # '16 format - but this might match other things
    ]
    
    # Search in the first 500 characters where headers usually are
    header_text = text[:500]
    for pattern in year_patterns:
        matches = re.findall(pattern, header_text)
        if matches:
            for match in matches:
                if len(match) == 4:  # Full year
                    year = int(match)
                    break
                elif len(match) == 2:  # Short year format
                    # Try to convert to full year (assuming 2000s)
                    if match.isdigit():
                        year_num = int(match)
                        if 0 <= year_num <= 99:
                            year = 2000 + year_num
                            break
            if year:
                break
    
    # Check if paper is in physical activity domain
    # Look for 'physical activity' in text (case-insensitive)
    is_physical_activity = 'physical activity' in text.lower()
    
    papers_info.append({
        'title': title,
        'year': year,
        'is_physical_activity': is_physical_activity
    })

# Filter papers from 2016 in physical activity domain
papers_2016_physical_activity = [p for p in papers_info if p['year'] == 2016 and p['is_physical_activity']]

print(f"Found {len(papers_2016_physical_activity)} papers from 2016 in 'physical activity' domain")
for paper in papers_2016_physical_activity[:5]:  # Show first 5
    print(f"  - {paper['title']}")

# Save the filtered paper titles for joining with citations
filtered_titles = [p['title'] for p in papers_2016_physical_activity]

# Store results for next step
print('__RESULT__:')
print(json.dumps(filtered_titles))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
