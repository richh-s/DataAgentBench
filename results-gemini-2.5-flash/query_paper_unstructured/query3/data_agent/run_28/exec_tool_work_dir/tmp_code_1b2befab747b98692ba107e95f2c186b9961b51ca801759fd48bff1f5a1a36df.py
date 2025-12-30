code = """import json
import re

paper_docs_data = json.loads(open(locals()['var_function-call-5976115717685306466'], 'r').read())

extracted_papers = []
for doc in paper_docs_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Try to extract year after a venue name like "UbiComp '15" or "CHI 2018"
    venue_year_match = re.search('(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\\s+\'?(?P<year_val>\\d{2}|\\d{4})', text, re.IGNORECASE)
    if venue_year_match:
        year_str = venue_year_match.group('year_val')
        if len(year_str) == 2:
            year = 2000 + int(year_str) if int(year_str) < 50 else 1900 + int(year_str)
        else:
            year = int(year_str)
    else:
        # If not found with venue, try to find "Copyright YYYY"
        copyright_year_match = re.search('Copyright\\s+(\\d{4})', text, re.IGNORECASE)
        if copyright_year_match:
            year = int(copyright_year_match.group(1))
        else:
            # Fallback: look for a four-digit year (this is less precise)
            general_year_match = re.search('([1-2][0-9]{3})', text)
            if general_year_match:
                year = int(general_year_match.group(1))

    contribution = []
    contribution_types = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    for c_type in contribution_types:
        # Use \\b for word boundary
        if re.search('\\b' + c_type + '\\b', text, re.IGNORECASE):
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
