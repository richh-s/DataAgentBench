code = """import json
import re

file_path = locals()["var_function-call-801663901547964105"]
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers = []
for paper in paper_docs:
    filename = paper["filename"]
    title = filename.replace(".txt", "")
    text = paper["text"]

    year = None
    # Try to find year in the first 500 characters
    match_year = re.search(r'(?:19|20)\d{2}', text[:500])
    if match_year:
        year = int(match_year.group(0))

    contribution_type = "unknown"
    if re.search(r'contribution(?:s)?:.*empirical', text, re.IGNORECASE) or re.search(r'empirical.*contribution', text, re.IGNORECASE):
        contribution_type = "empirical"
    elif re.search(r'empirical', text, re.IGNORECASE): # Broader search if not found with 'contribution' keyword
        contribution_type = "empirical"


    extracted_papers.append({
        "title": title,
        "year": year,
        "contribution": contribution_type
    })

filtered_papers = [
    p for p in extracted_papers
    if p["year"] is not None and p["year"] > 2016 and "empirical" in p["contribution"]
]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-4212386729374979044': ['paper_docs'], 'var_function-call-801663901547964105': 'file_storage/function-call-801663901547964105.json'}

exec(code, env_args)
