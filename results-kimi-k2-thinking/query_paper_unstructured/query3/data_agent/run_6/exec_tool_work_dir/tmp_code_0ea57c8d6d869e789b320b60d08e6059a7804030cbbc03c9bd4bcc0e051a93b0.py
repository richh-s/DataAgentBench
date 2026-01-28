code = """import json
import re

# Read the full MongoDB query results
with open('/tmp/tmp4j2a9r4m.json', 'r') as f:
    papers_data = json.load(f)

# Extract paper information from the documents
papers = []

for doc in papers_data:
    filename = doc['filename']
    text = doc['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from text - look for publication year patterns
    year_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+(\d{4})', text)
    if year_match:
        year = int(year_match.group(2))
    else:
        # Try other patterns
        year_match = re.search(r'(\d{4})\s+(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)', text)
        if year_match:
            year = int(year_match.group(1))
        else:
            # Look for copyright year
            year_match = re.search(r'Copyright\s+.*\s+(\d{4})', text)
            if year_match:
                year = int(year_match.group(1))
            else:
                year = None
    
    # Check if paper has empirical contribution
    has_empirical = False
    if re.search(r'empirical', text, re.IGNORECASE):
        # Look for specific empirical indicators
        empirical_indicators = [
            r'field study', r'user study', r'interview', r'survey', r'experiment', 
            r'empirical investigation', r'empirical study', r'empirical research',
            r'participants', r'qualitative', r'quantitative', r'data collection'
        ]
        for indicator in empirical_indicators:
            if re.search(indicator, text, re.IGNORECASE):
                has_empirical = True
                break
    
    # Extract venue
    venue_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UbiComp)\s+\d{4}', text)
    venue = venue_match.group(1) if venue_match else None
    
    papers.append({
        'title': title,
        'year': year,
        'has_empirical': has_empirical,
        'venue': venue
    })

# Filter papers with empirical contribution and published after 2016
empirical_papers_after_2016 = [p for p in papers if p['has_empirical'] and p['year'] and p['year'] > 2016]

# Debug: print count
print(f"Found {len(empirical_papers_after_2016)} empirical papers after 2016")

# Create a mapping of title to paper info for later joining
title_to_paper = {p['title']: p for p in empirical_papers_after_2016}

# Print the papers we found
for p in empirical_papers_after_2016[:5]:  # Show first 5
    print(f"Title: {p['title']}, Year: {p['year']}, Venue: {p['venue']}")

# Save the result in a JSON-serializable format
result = {
    'paper_titles': list(title_to_paper.keys()),
    'paper_details': title_to_paper
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
