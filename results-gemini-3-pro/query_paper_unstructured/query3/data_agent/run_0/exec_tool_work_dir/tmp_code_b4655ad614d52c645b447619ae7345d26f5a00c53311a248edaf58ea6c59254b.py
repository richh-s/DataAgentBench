code = """import json
import re

# Get the file path from the variable
file_path = locals()['var_function-call-4290533744407008086']

# Load the documents
with open(file_path, 'r') as f:
    docs = json.load(f)

print(f"Total docs: {len(docs)}")

matches = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for year in the first 1000 characters
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    pub_year = None
    if years:
        # Cast to int
        years = [int(y) for y in years]
        # Filter reasonable years (e.g. 2000-2025)
        valid_years = [y for y in years if 2000 <= y <= 2025]
        if valid_years:
            # Take the first one found in the header
            pub_year = valid_years[0]
            
            # Additional check: sometimes the first year might be a citation like "Smith 2010".
            # Usually the venue line is like "CHI 2019".
            # If the year is very recent (e.g. > 2016), it's likely the pub year.
            # If the year is old, it might be a citation.
            # But "Published after 2016" means we only care if pub_year > 2016.
            # If we pick a citation year 2010 erroneously, it will be filtered out anyway.
            # If we pick a citation year 2018 erroneously, we might include it.
            # Let's hope the header mentions the conference year first.
    
    # Extract Contribution
    # Check if "empirical" is in text (case insensitive)
    is_empirical = 'empirical' in text.lower()
    
    if pub_year and pub_year > 2016 and is_empirical:
        matches.append(title)

print(f"Found {len(matches)} matching papers.")
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-1070528273488687685': ['paper_docs'], 'var_function-call-1070528273488689510': ['Citations', 'sqlite_sequence'], 'var_function-call-3440707792195880886': 'file_storage/function-call-3440707792195880886.json', 'var_function-call-4290533744407008086': 'file_storage/function-call-4290533744407008086.json'}

exec(code, env_args)
