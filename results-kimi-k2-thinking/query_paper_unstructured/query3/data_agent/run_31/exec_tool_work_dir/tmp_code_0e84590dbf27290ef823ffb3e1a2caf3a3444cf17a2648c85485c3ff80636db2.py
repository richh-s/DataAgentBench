code = """import json
import re

# Get the MongoDB paper documents
papers_data = var_functions.query_db:4

# Extract paper information from the documents
papers_info = []

for doc in papers_data:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Extract year from the text
    # Look for patterns like: YEAR 'YY, YYYY, etc.
    year_match = re.search(r"\b(20\d{2})\b", text[:1000])  # Search in first 1000 chars
    if year_match:
        year = int(year_match.group(1))
    else:
        # Try alternative patterns
        year_match = re.search(r"(CHI|CSCW|Ubicomp|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['\s]\s*(20\d{2})", text[:1000], re.IGNORECASE)
        if year_match:
            year = int(year_match.group(2))
        else:
            # Default to 2015 if not found
            year = 2015
    
    # Extract contribution type
    # Look for keywords related to contribution in the text
    contribution = []
    text_lower = text.lower()
    
    # Check for empirical contribution
    if 'empirical' in text_lower or 'study' in text_lower or 'survey' in text_lower or 'interview' in text_lower or 'experiment' in text_lower:
        contribution.append('empirical')
    
    # Check for theoretical contribution
    if 'theoretical' in text_lower or 'theory' in text_lower:
        contribution.append('theoretical')
    
    # Check for artifact contribution
    if 'artifact' in text_lower or 'system' in text_lower or 'prototype' in text_lower:
        contribution.append('artifact')
    
    # Check for methodological contribution
    if 'methodological' in text_lower or 'method' in text_lower or 'framework' in text_lower:
        contribution.append('methodological')
    
    papers_info.append({
        'title': title,
        'year': year,
        'contribution': ','.join(contribution) if contribution else 'unknown',
        'text_preview': text[:200]  # Store preview for debugging
    })

# Print the extracted papers info
print('__RESULT__:')
print(json.dumps(papers_info[:10]))  # Print first 10 for preview"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
