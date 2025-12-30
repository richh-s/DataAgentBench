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
    # Try to find year in the first 500 characters, or anywhere if not found there
    match_year = re.search(r'\b(19|20)\d{2}\b', text[:500]) # search for year in first 500 characters
    if match_year:
        year = int(match_year.group(0))
    else:
        match_year = re.search(r'\b(19|20)\d{2}\b', text) # search for year anywhere in the text
        if match_year:
            year = int(match_year.group(0))

    is_empirical = False
    if re.search(r'empirical', text, re.IGNORECASE):
        is_empirical = True

    extracted_papers.append({
        "title": title,
        "year": year,
        "is_empirical": is_empirical
    })

filtered_papers = [
    p for p in extracted_papers
    if p["year"] is not None and p["year"] > 2016 and p["is_empirical"]
]

print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-4212386729374979044': ['paper_docs'], 'var_function-call-801663901547964105': 'file_storage/function-call-801663901547964105.json', 'var_function-call-8923072733247941315': []}

exec(code, env_args)
