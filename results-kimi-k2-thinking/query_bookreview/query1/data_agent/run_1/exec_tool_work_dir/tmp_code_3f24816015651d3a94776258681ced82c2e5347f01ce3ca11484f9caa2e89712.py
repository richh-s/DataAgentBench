code = """import json
import re

# Load the query result
result_key = 'var_functions.query_db:5'
query_result = locals().get(result_key, [])

# If it's a file path, read from file
if isinstance(query_result, str) and '.json' in query_result:
    with open(query_result, 'r') as f:
        query_result = json.load(f)

# Function to extract publication year from details
def extract_year_from_details(details_str):
    if not details_str or details_str == '':
        return None
    
    # Look for patterns like "January 1, 2004" or "May 20, 1996"
    patterns = [
        r'on\s+\w+\s+\d{1,2},\s+(\d{4})',  # "on May 20, 1996" or "on January 1, 2004"
        r'published\s+\w+\s+\d{1,2},\s+(\d{4})',  # "published May 8, 2012"
        r'Published\s*:\s*\w+\s+\d{1,2},\s+(\d{4})',  # "Published: May 8, 2012"
        r'\d{1,2},\s+(\d{4})',  # "May 8, 2012"
    ]
    
    for pattern in patterns:
        match = re.search(pattern, details_str, re.IGNORECASE)
        if match:
            try:
                year = int(match.group(1))
                return year
            except:
                continue
    
    # Check for "published in 2014" format
    match = re.search(r'published\s+in\s+(\d{4})', details_str, re.IGNORECASE)
    if match:
        try:
            return int(match.group(1))
        except:
            pass
    
    return None

# Extract years from the sample data
sample_books = query_result[:10]  # First 10 books
books_with_years = []

for book in sample_books:
    title = book.get('title', 'Unknown')
    details = book.get('details', '')
    year = extract_year_from_details(details)
    
    books_with_years.append({
        'title': title,
        'year': year,
        'details': details[:100] + '...' if details else ''
    })

# Print results
print('__RESULT__:')
print(json.dumps(books_with_years, indent=2))"""

env_args = {'var_functions.list_db:0': ['review'], 'var_functions.list_db:2': ['books_info'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
