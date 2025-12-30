code = """import json
import re

file_path = locals()['var_function-call-2573740285369106607']

with open(file_path, 'r') as f:
    docs = json.load(f)

results = []
for doc in docs:
    text = doc['text']
    filename = doc['filename']
    
    # Year extraction
    # Look for "Copyright 20xx" or "20xx" in first 500 chars
    header = text[:1000]
    years = re.findall(r'20\d\d', header)
    # Also look for "'yy" like "'18"
    short_years = re.findall(r"'\d{2}", header)
    
    # Convert short years to full years (assuming 20xx)
    full_years = [int(y) for y in years]
    for sy in short_years:
        y = int(sy[1:])
        full_years.append(2000 + y)
    
    # Filter valid years (e.g. 2010-2025)
    valid_years = [y for y in full_years if 2010 <= y <= 2025]
    if valid_years:
        # Taking the most frequent or max? Usually the max in header is the pub year or copyright year.
        year = max(valid_years)
    else:
        year = None

    # Contribution extraction
    # Search for "Contribution" keyword and grab context
    contrib_idx = text.lower().find("contribution")
    contrib_context = ""
    if contrib_idx != -1:
        contrib_context = text[contrib_idx:contrib_idx+50].replace('\n', ' ')
    
    # Check if "empirical" is in text
    has_empirical = "empirical" in text.lower()
    
    results.append({
        "filename": filename,
        "year": year,
        "contrib_context": contrib_context,
        "has_empirical": has_empirical
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7387203186474718594': 'file_storage/function-call-7387203186474718594.json', 'var_function-call-9551476032774433042': ['paper_docs'], 'var_function-call-7392786003504292061': {'explicit_contribution': '', 'empirical_context': '', 'years': ['2015', '2015', '2015', '2015', '2015', '2015', '2015', '2015', '2014', '2013']}, 'var_function-call-16070472679849682591': 'file_storage/function-call-16070472679849682591.json', 'var_function-call-14838569663088297683': 'file_storage/function-call-14838569663088297683.json', 'var_function-call-2573740285369106607': 'file_storage/function-call-2573740285369106607.json'}

exec(code, env_args)
