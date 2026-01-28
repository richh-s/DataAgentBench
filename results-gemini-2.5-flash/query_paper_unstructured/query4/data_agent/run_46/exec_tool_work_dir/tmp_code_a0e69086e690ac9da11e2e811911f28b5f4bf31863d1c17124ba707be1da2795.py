code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_with_physical_activity = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check if 'physical activity' is in the entire text, case-insensitive
    if "physical activity" in text.lower():
        year = None
        # Attempt to find a year (4-digit number) anywhere in the text
        year_matches = re.findall(r'\b(19|20)\d{2}\b', text)
        if year_matches:
            # Take the first matched year, assuming it's the publication year
            # Correcting to capture the full 4-digit year directly
            full_year_matches = re.findall(r'\b((?:19|20)\d{2})\b', text)
            if full_year_matches:
                year = int(full_year_matches[0])
        
        papers_with_physical_activity.append({'title': title, 'year': year})

# Filter for papers published in 2016
papers_2016_physical_activity = [p for p in papers_with_physical_activity if p['year'] == 2016]

print("__RESULT__:")
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': [], 'var_function-call-5306735185744050093': [], 'var_function-call-15853859611646052612': [], 'var_function-call-14370408823091377003': []}

exec(code, env_args)
