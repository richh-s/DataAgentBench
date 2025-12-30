code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    year = int(year_match.group(0)) if year_match else None

    # Check for 'physical activity' domain
    domain_match = re.search(r'domain: (.*)', text, re.IGNORECASE)
    domain_text = domain_match.group(1) if domain_match else ""
    
    # Also check the abstract or main body for domain mentions
    if "physical activity" in text.lower():
        if year == 2016 and ("physical activity" in domain_text.lower() or "physical activity" in text.lower()):
            extracted_papers.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(extracted_papers))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json'}

exec(code, env_args)
