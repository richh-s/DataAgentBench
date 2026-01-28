code = """import json
import pandas as pd
import re

# Load the Chi papers data
chi_papers_data = locals().get('var_functions.query_db:18', [])

# Check if it's a file path or actual data
if isinstance(chi_papers_data, str) and chi_papers_data.endswith('.json'):
    with open(chi_papers_data, 'r') as f:
        chi_papers = json.load(f)
else:
    chi_papers = chi_papers_data

print(f"Total documents with 'CHI' in text: {len(chi_papers)}")

# Let's examine the documents to find CHI papers
chi_venues = []
for doc in chi_papers:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract title from filename (remove .txt)
    title = filename.replace('.txt', '') if filename else ''
    
    # Look for CHI venue information in the text
    # Common patterns: CHI 'YY, CHI 20YY, CHI Conference, etc.
    chi_patterns = [
        r"CHI\s+'\d{2}",
        r"CHI\s+20\d{2}",
        r"CHI\s+\d{4}",
        r"CHI\s+Conference",
        r"Proceedings of the SIGCHI",
        r"Proceedings of CHI"
    ]
    
    venue_found = False
    for pattern in chi_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            venue_found = True
            break
    
    if venue_found:
        # Try to extract year
        year_match = re.search(r"(CHI\s+'\d{2}|CHI\s+20\d{2}|CHI\s+\d{4}|20\d{2})", text)
        year = None
        if year_match:
            year_str = year_match.group(1)
            # Parse year
            if "'" in year_str:
                year = int("20" + year_str.split("'")[1])
            elif "CHI 20" in year_str:
                year = int(year_str.split()[1])
            elif year_str.isdigit() and len(year_str) == 4:
                year = int(year_str)
        
        chi_venues.append({
            'title': title,
            'year': year,
            'venue': 'CHI',
            'filename': filename
        })

print(f"Identified {len(chi_venues)} CHI papers")

# Save CHI papers info
result = {
    'total_chi_papers': len(chi_venues),
    'chi_papers': chi_venues[:5]  # Sample first 5
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.execute_python:10': {'status': 'success', 'total_records': 100, 'message': 'Loaded 100 citation records for 2020'}, 'var_functions.query_db:12': [], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': {'total_papers': 5}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
