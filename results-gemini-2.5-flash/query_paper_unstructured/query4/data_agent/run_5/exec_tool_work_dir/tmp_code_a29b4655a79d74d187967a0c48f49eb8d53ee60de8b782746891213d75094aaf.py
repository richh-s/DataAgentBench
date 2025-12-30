code = """import json
import re

file_path = locals()['var_function-call-4281778254792506949']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Try to extract year more robustly, looking for common patterns like (YEAR) or YEAR in conference info
    year = None
    year_matches = re.findall(r'\b(19|20)\d{2}\b', text)
    if year_matches:
        # Prioritize years that appear earlier in the document, as they are more likely to be publication years
        # Also, check if a common conference abbreviation is near the year
        for y in year_matches:
            if str(y) in text[:500]: # Check within the first 500 characters
                year = int(y)
                break
        if not year and year_matches: # If no year found in the first 500, take the first one found
            year = int(year_matches[0])

    # Check for 'physical activity' (case-insensitive) anywhere in the text
    is_physical_activity_domain = 'physical activity' in text.lower()

    if year is not None and is_physical_activity_domain:
        extracted_papers.append({
            'title': title,
            'year': year,
            'domain': 'physical activity' # Assigning directly since we've confirmed its presence
        })

filtered_papers = [
    p for p in extracted_papers
    if p['year'] == 2016
]

result = json.dumps(filtered_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9075844566900917724': ['paper_docs'], 'var_function-call-4281778254792506949': 'file_storage/function-call-4281778254792506949.json', 'var_function-call-6950853866291229053': [], 'var_function-call-17897123819145337208': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
