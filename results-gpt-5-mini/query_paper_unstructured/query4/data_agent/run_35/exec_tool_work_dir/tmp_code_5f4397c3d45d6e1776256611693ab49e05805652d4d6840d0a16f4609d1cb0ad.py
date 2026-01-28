code = """import json, re

# The variable var_call_nbkjSzhK5ThCLjNr4s2knSBh is available from storage and
# contains the path to the JSON file with the Mongo query results.
path = var_call_nbkjSzhK5ThCLjNr4s2knSBh

with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

titles_2016_physical = []

for d in docs:
    filename = d.get('filename', '')
    if not filename.lower().endswith('.txt'):
        continue
    title = filename[:-4]
    text = d.get('text', '')
    if not text:
        continue
    text_l = text.lower()
    # Check for presence of the year 2016 in the document text
    year = None
    if '2016' in text_l:
        year = 2016
    else:
        # also check for patterns like "'16" e.g., CHI '16
        if "'16" in text_l:
            year = 2016
    # Check for domain: physical activity substring
    domain_match = 'physical activity' in text_l
    if year == 2016 and domain_match:
        titles_2016_physical.append(title)

# Deduplicate and sort
titles_2016_physical = sorted(list(dict.fromkeys(titles_2016_physical)))

print("__RESULT__:")
print(json.dumps(titles_2016_physical))"""

env_args = {'var_call_t0eGZ0V7Vx2mFRtY6V1NTGeA': ['paper_docs'], 'var_call_nbkjSzhK5ThCLjNr4s2knSBh': 'file_storage/call_nbkjSzhK5ThCLjNr4s2knSBh.json'}

exec(code, env_args)
