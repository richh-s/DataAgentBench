code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers_with_domain = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check for 'physical activity' domain in the entire text, case-insensitive
    if "physical activity" in text.lower():
        year = None
        # Try to find a 4-digit number that likely represents a year (2000-2029 range as common publication years)
        # Prioritize matches found earlier in the text to be more likely the publication year
        year_matches = re.findall(r'\b(20(?:0[0-9]|1[0-9]|2[0-9]))\b', text)
        if year_matches:
            # Take the first year found, as it's often the publication year
            year = int(year_matches[0])

        extracted_papers_with_domain.append({'title': title, 'year': year})

# Now filter for papers published in 2016
papers_2016_physical_activity = [p for p in extracted_papers_with_domain if p['year'] == 2016]

print("__RESULT__:")
print(json.dumps(papers_2016_physical_activity))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': []}

exec(code, env_args)
