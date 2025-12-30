code = """import json
import re

def extract_info(text, filename):
    title = filename.replace(".txt", "")
    year = None
    domain = []

    # Try to extract year from common patterns: copyright, conference year, or general 4-digit year
    copyright_year_match = re.search(r"Copyright\s+(?:\(c\)|\u00a9)?\s*(\d{4})", text, re.IGNORECASE)
    if copyright_year_match:
        year = int(copyright_year_match.group(1))
    else:
        conference_year_match = re.search(r"(?:UbiComp|CHI|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*(?:'\d{2}|\d{4})", text, re.IGNORECASE)
        if conference_year_match:
            year_str = conference_year_match.group(0)
            year_digits = re.search(r"\d{4}", year_str) 
            if year_digits:
                year = int(year_digits.group(0))
            else:
                year_digits_short = re.search(r"'(\d{2})", year_str) 
                if year_digits_short:
                    year = 2000 + int(year_digits_short.group(1))
        else:
            general_year_match = re.search(r"\b(19|20)\d{2}\b", text)
            if general_year_match:
                year = int(general_year_match.group(0))
    
    common_domains = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    for d in common_domains:
        pattern = r"\b" + re.escape(d) + r"\b"
        if re.search(pattern, text, re.IGNORECASE):
            domain.append(d)

    return {"title": title, "year": year, "domain": list(set(domain))}

mongo_file_path = locals()['var_function-call-12752153450719007890']
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

papers_info = []
for doc in mongo_data:
    papers_info.append(extract_info(doc['text'], doc['filename']))

print("__RESULT__:")
print(json.dumps(papers_info))"""

env_args = {'var_function-call-16161537513363771660': 'file_storage/function-call-16161537513363771660.json', 'var_function-call-12752153450719007890': 'file_storage/function-call-12752153450719007890.json', 'var_function-call-866722953621056295': [], 'var_function-call-8171478659109438870': [], 'var_function-call-16770226383205343611': [], 'var_function-call-8439373108773590095': [], 'var_function-call-2542673735042371936': []}

exec(code, env_args)
