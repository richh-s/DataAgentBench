code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # More robust year extraction - looking for common patterns where year appears near the beginning
    year_match = re.search(r'(?:\b(19|20)\d{2}\b|\b(20)\d{2}(?=[^\d]))', text)
    if year_match:
        year = int(year_match.group(0)) # Directly use group(0) for the whole match
    else:
        year = None

    # Check for 'physical activity' domain in the entire text, case-insensitive
    if "physical activity" in text.lower():
        extracted_papers.append({'title': title, 'year': year})

# Filter for year 2016 after extraction
filtered_papers = [p for p in extracted_papers if p['year'] == 2016]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': []}

exec(code, env_args)
