code = """import json
import re

paper_docs_file_path = locals()['var_function-call-6544619829393036365']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # More robust year extraction: search in the first 500 characters and for common patterns
    year = None
    year_match_early = re.search(r'\b(19|20)\d{2}\b', text[:500])
    if year_match_early:
        year = int(year_match_early.group(0))
    else:
        # Fallback to search in the whole text if not found early, but prioritize early matches
        year_match_late = re.search(r'\b(19|20)\d{2}\b', text)
        if year_match_late:
            year = int(year_match_late.group(0))

    # Check for 'physical activity' domain within the entire text
    is_physical_activity = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity:
        extracted_papers.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-17463833612075543362': ['paper_docs'], 'var_function-call-6544619829393036365': 'file_storage/function-call-6544619829393036365.json', 'var_function-call-15282443211329679729': [], 'var_function-call-3755615379006169032': ['Citations', 'sqlite_sequence']}

exec(code, env_args)
