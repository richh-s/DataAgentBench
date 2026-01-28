code = """import json
import re

paper_docs_data = json.loads(open(locals()['var_function-call-5976115717685306466'], 'r').read())

extracted_papers = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Try to extract year with venue
    year_venue_match = re.search(r'(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s+\'?(?P<year_val>\d{4})', text)
    if year_venue_match:
        year = int(year_venue_match.group('year_val'))
    else:
        # If not found with venue, try to find a 4-digit year generally
        year_match = re.search(r'([1-2][0-9]{3})', text)
        if year_match:
            year = int(year_match.group(1))

    contribution = []
    contribution_types = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    for c_type in contribution_types:
        if re.search(r'\\b' + c_type + r'\\b', text, re.IGNORECASE):
            contribution.append(c_type)
    
    extracted_papers.append({
        "title": title,
        "year": year,
        "contribution": contribution
    })

filtered_papers = [
    p for p in extracted_papers
    if p["year"] is not None and p["year"] > 2016 and "empirical" in p["contribution"]
]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-1149772925907859432': ['paper_docs'], 'var_function-call-5976115717685306466': 'file_storage/function-call-5976115717685306466.json'}

exec(code, env_args)
