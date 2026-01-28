code = """import json, re

# Load the query_db result stored in the file path variable
path = var_call_LXL8ZA4trbYjT9RIvZMnHL63
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

selected_titles = []

for rec in records:
    filename = rec.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = rec.get('text','')
    # Look for publication year: search first 1000 chars, then whole text
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    pub_year = None
    if years:
        pub_year = int(years[0])
    else:
        years_all = re.findall(r'\b(20\d{2})\b', text)
        if years_all:
            pub_year = int(years_all[0])
    # Domain check: 'physical activity' anywhere in text
    domain_match = bool(re.search(r'physical activity', text, re.I))
    if domain_match and pub_year == 2016:
        selected_titles.append(title)

# Deduplicate
selected_titles = list(dict.fromkeys(selected_titles))

# Output as JSON string
output = json.dumps(selected_titles)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_dZzFsi4SOtro7Uw908RvLc2W': ['paper_docs'], 'var_call_LXL8ZA4trbYjT9RIvZMnHL63': 'file_storage/call_LXL8ZA4trbYjT9RIvZMnHL63.json'}

exec(code, env_args)
