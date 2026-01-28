code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    year = None
    # Try to find year in the first 500 characters of the text
    initial_text = text[:500]
    year_match = re.search(r'\b(2016)\b', initial_text)
    if year_match:
        year = int(year_match.group(0))
    
    # Check for 'physical activity' domain in the entire text, case-insensitive
    if year == 2016 and "physical activity" in text.lower():
        extracted_papers.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': []}

exec(code, env_args)
