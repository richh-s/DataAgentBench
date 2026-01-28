code = """import json
import re
from datetime import datetime

# Load the MongoDB results
mongo_results = locals()['var_functions.query_db:2']

# If mongo_results is a string (file path), load it
if isinstance(mongo_results, str):
    with open(mongo_results, 'r') as f:
        mongo_results = json.load(f)

# Load the citation data
citation_results = locals()['var_functions.query_db:6']
if isinstance(citation_results, str):
    with open(citation_results, 'r') as f:
        citation_results = json.load(f)

# Convert citation results to a dictionary for easy lookup
citation_dict = {item['title']: int(item['total_citations']) for item in citation_results}

# Process MongoDB documents to extract papers in 'physical activity' domain from 2016
physical_activity_papers_2016 = []

for doc in mongo_results:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is in physical activity domain (case-insensitive)
    if 'physical activity' in text.lower():
        # Extract year - look for patterns like YYYY, especially 2016
        # Common patterns: year: 2016, 2016), 2016., etc.
        year_patterns = [
            r'\b(2016)\b',  # Explicit 2016
            r'\b(2015)\b',  # Also check 2015 to be thorough
            r'\b(2017)\b',  # Also check 2017
        ]
        
        year = None
        for pattern in year_patterns:
            matches = re.findall(pattern, text)
            if matches:
                # Take the most common year mentioned
                from collections import Counter
                year_counts = Counter(matches)
                most_common = year_counts.most_common(1)[0][0]
                if most_common == '2016':
                    year = 2016
                    break
                elif year is None:
                    year = int(most_common)
        
        # Additional check: look for venue year patterns like 'CHI 2016' or 'UbiComp 2016'
        if not year:
            venue_pattern = r'\b(CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|Ubicomp)\s*[\'']?\s*(2016)\b'
            venue_matches = re.findall(venue_pattern, text, re.IGNORECASE)
            if venue_matches:
                year = 2016
        
        # Check if it's specifically 2016
        if year == 2016:
            # Get citation count if available
            total_citations = citation_dict.get(title, 0)
            
            physical_activity_papers_2016.append({
                'title': title,
                'year': year,
                'total_citations': total_citations
            })

# Sort by citations descending and prepare result
physical_activity_papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

# Format output
output = []
for paper in physical_activity_papers_2016:
    output.append(f"Title: {paper['title']}")
    output.append(f"Total Citations: {paper['total_citations']}")
    output.append("")

result = "\n".join(output)

print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
