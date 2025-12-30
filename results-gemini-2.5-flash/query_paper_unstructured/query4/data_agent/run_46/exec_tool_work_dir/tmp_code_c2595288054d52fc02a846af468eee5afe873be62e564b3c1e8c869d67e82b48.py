code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_2016_physical_activity_titles = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check for year 2016 within the first 500 characters of the text
    # Publication year is often at the beginning of the paper
    year_in_intro = False
    if len(text) > 0:
        intro_text = text[:min(len(text), 500)] # Take first 500 chars or less if paper is shorter
        if re.search(r'\b2016\b', intro_text):
            year_in_intro = True
    
    # Check if 'physical activity' is in the entire text, case-insensitive
    if year_in_intro and "physical activity" in text.lower():
        papers_2016_physical_activity_titles.append(title)

print("__RESULT__:")
print(json.dumps(papers_2016_physical_activity_titles))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': []}

exec(code, env_args)
