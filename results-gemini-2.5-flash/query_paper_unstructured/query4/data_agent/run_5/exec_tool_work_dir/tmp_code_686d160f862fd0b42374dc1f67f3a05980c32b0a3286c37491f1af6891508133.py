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

    year = None
    # Broader search for year, looking for 4-digit numbers that could be years
    # Prioritizing years that appear with conference names or at the beginning of the text
    year_matches = re.findall(r'\b(19|20)\d{2}\b', text)
    if year_matches:
        # Let's try to find the earliest year that appears in the first 1000 characters
        # as this is more likely to be the publication year.
        for match_year in year_matches:
            if text.find(match_year) < 1000:
                year = int(match_year)
                break
        if not year and year_matches: # If no year in the first 1000, take the very first match
            year = int(year_matches[0])

    is_physical_activity_domain = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity_domain:
        extracted_papers.append({
            'title': title,
            'year': year,
            'domain': 'physical activity'
        })

result = json.dumps(extracted_papers)
print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-9075844566900917724': ['paper_docs'], 'var_function-call-4281778254792506949': 'file_storage/function-call-4281778254792506949.json', 'var_function-call-6950853866291229053': [], 'var_function-call-17897123819145337208': ['Citations', 'sqlite_sequence'], 'var_function-call-6166251359363205848': []}

exec(code, env_args)
