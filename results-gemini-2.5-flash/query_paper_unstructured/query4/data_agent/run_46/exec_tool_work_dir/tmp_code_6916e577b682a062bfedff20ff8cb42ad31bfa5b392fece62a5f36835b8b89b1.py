code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_titles_2016_physical_activity = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check for 'physical activity' domain in the entire text, case-insensitive
    if "physical activity" in text.lower():
        # Extract all 4-digit years (19xx or 20xx) from the entire text
        potential_years = re.findall(r'\b(19|20)\d{2}\b', text)
        
        # Convert extracted year strings to integers
        potential_years = [int(y) for y in potential_years]

        # Check if 2016 is among the potential years found
        if 2016 in potential_years:
            papers_titles_2016_physical_activity.append(title)

print("__RESULT__:")
print(json.dumps(papers_titles_2016_physical_activity))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': [], 'var_function-call-5306735185744050093': [], 'var_function-call-15853859611646052612': [], 'var_function-call-14370408823091377003': [], 'var_function-call-11267708266785219733': [], 'var_function-call-8110784088001934800': []}

exec(code, env_args)
