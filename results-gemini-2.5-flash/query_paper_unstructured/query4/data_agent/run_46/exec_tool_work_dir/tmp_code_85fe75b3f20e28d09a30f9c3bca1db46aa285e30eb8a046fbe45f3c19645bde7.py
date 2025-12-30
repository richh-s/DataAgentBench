code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_titles_and_years = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check if 'physical activity' is in the entire text, case-insensitive
    if "physical activity" in text.lower():
        year = None
        # More flexible year extraction: look for 4-digit numbers, prioritize those in the first 1000 chars
        year_matches = re.findall(r'\b(19|20)\d{2}\b', text)
        if year_matches:
            # Try to find a year within the first 1000 characters for higher relevance
            initial_text = text[:min(len(text), 1000)]
            initial_year_matches = re.findall(r'\b(19|20)\d{2}\b', initial_text)
            if initial_year_matches:
                year = int(initial_year_matches[0])
            else:
                year = int(year_matches[0]) # Fallback to first year found in the entire document

        if year == 2016: # Filter for papers published in 2016
            papers_titles_and_years.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(papers_titles_and_years))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': [], 'var_function-call-5306735185744050093': []}

exec(code, env_args)
