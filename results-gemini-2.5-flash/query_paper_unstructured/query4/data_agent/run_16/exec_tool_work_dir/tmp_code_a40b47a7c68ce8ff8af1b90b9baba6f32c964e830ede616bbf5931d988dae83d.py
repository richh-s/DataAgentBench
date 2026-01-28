code = """import json
import re

file_path = locals()['var_function-call-1692856430574437230']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_2016 = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # Try to extract the year from the text. This is a heuristic and might need refinement.
    # Look for a 4-digit number that could represent a year, often near copyright info or conference details.
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = None
    if year_match:
        # Let's try to get the year from the first few lines of the paper, often found there.
        # Refined regex to search within the first 500 characters, usually enough for metadata.
        first_part_text = text[:500] if len(text) > 500 else text
        year_match_refined = re.search(r'\b(19|20)\d{2}\b', first_part_text)
        if year_match_refined:
            year = int(year_match_refined.group(0))

    if year == 2016:
        papers_2016.append({'title': title, 'year': year})

print('__RESULT__:')
print(json.dumps(papers_2016))"""

env_args = {'var_function-call-1692856430574437230': 'file_storage/function-call-1692856430574437230.json'}

exec(code, env_args)
