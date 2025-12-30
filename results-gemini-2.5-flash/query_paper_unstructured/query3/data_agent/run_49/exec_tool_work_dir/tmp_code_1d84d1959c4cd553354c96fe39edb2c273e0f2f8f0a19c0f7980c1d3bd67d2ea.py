code = """import json
import re

def extract_paper_info(paper_docs_filepath):
    with open(paper_docs_filepath, 'r') as f:
        paper_docs = json.load(f)

    papers_info = []
    for doc in paper_docs:
        filename = doc['filename']
        title = filename.replace('.txt', '')
        text = doc['text']

        year = None
        year_match = re.search(r'\b(?:JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)?\s*\\?\s*(\d{4})\b', text)
        if year_match:
            year = int(year_match.group(1))

        contribution_types = []
        if re.search(r'empirical', text, re.IGNORECASE):
            contribution_types.append('empirical')
        if re.search(r'artifact', text, re.IGNORECASE):
            contribution_types.append('artifact')
        if re.search(r'theoretical', text, re.IGNORECASE):
            contribution_types.append('theoretical')
        if re.search(r'survey', text, re.IGNORECASE):
            contribution_types.append('survey')
        if re.search(r'methodological', text, re.IGNORECASE):
            contribution_types.append('methodological')

        papers_info.append({
            'title': title,
            'year': year,
            'contribution': contribution_types
        })
    return papers_info

papers_data = extract_paper_info(locals()['var_function-call-14853405185317032894'])

filtered_papers = []
for paper in papers_data:
    if paper['year'] is not None and paper['year'] > 2016 and 'empirical' in paper['contribution']:
        filtered_papers.append({'title': paper['title'], 'year': paper['year']})

print('__RESULT__:')
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-17299675907723448706': ['paper_docs'], 'var_function-call-14853405185317032894': 'file_storage/function-call-14853405185317032894.json'}

exec(code, env_args)
