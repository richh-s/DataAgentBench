code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_titles_2016_physical_activity = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    is_2016 = False
    # Check for '2016' within the first 2000 characters (publication year is typically early in the document)
    if len(text) > 0:
        search_area = text[:min(len(text), 2000)]
        if re.search(r'\b2016\b', search_area):
            is_2016 = True

    # Check if 'physical activity' is in the entire text, case-insensitive
    if is_2016 and "physical activity" in text.lower():
        papers_titles_2016_physical_activity.append(title)

print("__RESULT__:")
print(json.dumps(papers_titles_2016_physical_activity))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': [], 'var_function-call-5306735185744050093': [], 'var_function-call-15853859611646052612': [], 'var_function-call-14370408823091377003': [], 'var_function-call-11267708266785219733': []}

exec(code, env_args)
