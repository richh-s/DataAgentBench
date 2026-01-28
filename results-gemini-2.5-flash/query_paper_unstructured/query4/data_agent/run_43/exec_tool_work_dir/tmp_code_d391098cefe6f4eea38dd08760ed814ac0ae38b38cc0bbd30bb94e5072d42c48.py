code = """import json
import re
import pandas as pd

def extract_info(text, filename):
    title = filename.replace(".txt", "")
    year = None
    domain = []

    # Simpler year extraction: just look for any 4-digit number that could be a year
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))

    # Extract domain by checking for keywords in the lowercased text
    common_domains = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    text_lower = text.lower()
    for d in common_domains:
        if re.search(r'\b' + re.escape(d) + r'\b', text_lower):
            domain.append(d)

    return {"title": title, "year": year, "domain": list(set(domain))}

# Load MongoDB data
mongo_file_path = locals()['var_function-call-12752153450719007890']
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

papers_info = []
for doc in mongo_data:
    papers_info.append(extract_info(doc['text'], doc['filename']))

# Print all extracted papers_info to inspect
print("__RESULT__:")
print(json.dumps(papers_info))"""

env_args = {'var_function-call-16161537513363771660': 'file_storage/function-call-16161537513363771660.json', 'var_function-call-12752153450719007890': 'file_storage/function-call-12752153450719007890.json', 'var_function-call-866722953621056295': [], 'var_function-call-8171478659109438870': [], 'var_function-call-16770226383205343611': [], 'var_function-call-8439373108773590095': [], 'var_function-call-2542673735042371936': [], 'var_function-call-15077404571815829099': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'domain': []}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2010, 'domain': []}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'domain': []}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'domain': []}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2016, 'domain': []}], 'var_function-call-17221929207605378594': [], 'var_function-call-15462957610608874917': []}

exec(code, env_args)
