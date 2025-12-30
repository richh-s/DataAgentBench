code = """import json
import re

file_path = locals()['var_function-call-3921672676854055861']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'([A-Z]{3,}\s+\'\d{2}|\d{4})', text)
    year = None
    if year_match:
        year_str = year_match.group(1)
        if year_str.isdigit() and len(year_str) == 4:
            year = int(year_str)
        elif "'" in year_str:
            year_suffix = year_str.split("'")[1]
            if year_suffix.isdigit():
                full_year = int("20" + year_suffix) if int(year_suffix) < 50 else int("19" + year_suffix)
                year = full_year

    domain = []
    # Attempt to find common domains if a 'domain' or similar keyword is present
    domain_keywords = ["domain", "domains", "topic", "topics"]
    found_domain_text = None
    for keyword in domain_keywords:
        domain_match = re.search(fr'{keyword}[s]?:\s*(.*?)(?:\n|ACM|Author Keywords|ABSTRACT)', text, re.IGNORECASE | re.DOTALL)
        if domain_match:
            found_domain_text = domain_match.group(1).strip()
            break

    common_domains = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    if found_domain_text:
        for d in common_domains:
            if d in found_domain_text.lower():
                domain.append(d)
    
    # If 'physical activity' is not found in the identified domain section, check the entire text.
    if 'physical activity' in text.lower() and 'physical activity' not in domain:
        domain.append('physical activity')

    if year == 2016 and 'physical activity' in domain:
        extracted_papers.append({
            'title': title
        })

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-4911569923958279959': ['paper_docs'], 'var_function-call-3921672676854055861': 'file_storage/function-call-3921672676854055861.json', 'var_function-call-12899150304275043457': []}

exec(code, env_args)
