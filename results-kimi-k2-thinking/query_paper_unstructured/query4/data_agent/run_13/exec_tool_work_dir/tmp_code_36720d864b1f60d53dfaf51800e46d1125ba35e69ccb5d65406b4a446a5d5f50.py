code = """import json
import re

# Load the query result from the file
result_file = locals()['var_functions.query_db:0']
with open(result_file, 'r') as f:
    papers = json.load(f)

# Function to extract paper information from text
extracted_papers = []

for paper in papers:
    filename = paper['filename']
    text = paper['text']
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    # Try to extract year from text
    # Look for patterns like "2016" that might indicate publication year
    # Common patterns: conference years, copyright years, etc.
    year_match = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH).*?20(1[0-9])', text, re.IGNORECASE)
    if not year_match:
        year_match = re.search(r'20(1[0-9])', text)
    
    year = None
    if year_match:
        try:
            year_str = year_match.group(1)
            year = int(year_str)
            if year < 10 or year > 20:
                year = None
            else:
                year = 2000 + year
        except:
            year = None
    
    # Check if paper is from 2016
    if year != 2016:
        continue
    
    # Check if domain is 'physical activity'
    # Look for the domain in the text
    domain_match = re.search(r'physical activity', text, re.IGNORECASE)
    
    if domain_match:
        extracted_papers.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

# Print the extracted papers
result = json.dumps(extracted_papers, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
