code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_titles_and_years = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    year = None
    # Look for '2016' within the first 1000 characters (where publication year is often stated)
    intro_text = text[:min(len(text), 1000)]
    if re.search(r'\b2016\b', intro_text):
        year = 2016

    # Check if 'physical activity' is in the entire text, case-insensitive
    if year == 2016 and "physical activity" in text.lower():
        papers_titles_and_years.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(papers_titles_and_years))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': [], 'var_function-call-5306735185744050093': [], 'var_function-call-15853859611646052612': []}

exec(code, env_args)
