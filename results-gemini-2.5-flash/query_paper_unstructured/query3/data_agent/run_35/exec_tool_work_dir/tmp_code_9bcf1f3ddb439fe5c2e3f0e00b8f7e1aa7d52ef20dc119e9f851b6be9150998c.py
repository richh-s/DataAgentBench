code = """import json
import re

with open(locals()['var_function-call-5400047117669112550'], 'r') as f:
    paper_docs = json.load(f)

parsed_papers = []
for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')

    year_match = re.search(r'([12][0-9]{3})', text)
    year = int(year_match.group(1)) if year_match else None

    contribution = None
    # Attempt to extract contribution more robustly
    # Looking for 'Contribution(s):' followed by content, up to the next major section header or end of text
    contribution_match = re.search(r'Contribution(?:s)?:\s*(.*?)(?=(?:\n(?:Venue|Domain|Source|Keywords|ABSTRACT|INTRODUCTION|BACKGROUND):)|\n\n|$) ', text, re.IGNORECASE | re.DOTALL)
    if contribution_match:
        contribution = contribution_match.group(1).strip()

    parsed_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

filtered_papers = [
    p for p in parsed_papers
    if p['year'] and p['year'] > 2016 and p['contribution'] and 'empirical' in p['contribution'].lower()
]

# Extract titles of the filtered papers
filtered_titles = [p['title'] for p in filtered_papers]

print("__RESULT__:")
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-16356890130241980815': ['paper_docs'], 'var_function-call-5400047117669112550': 'file_storage/function-call-5400047117669112550.json'}

exec(code, env_args)
