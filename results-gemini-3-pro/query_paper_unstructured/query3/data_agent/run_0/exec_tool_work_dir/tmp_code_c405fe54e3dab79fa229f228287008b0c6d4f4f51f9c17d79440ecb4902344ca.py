code = """import json
import re

# Load the documents
with open('var_function-call-4290533744407008086.json', 'r') as f:
    docs = json.load(f)

print(f"Total docs: {len(docs)}")

matches = []

for doc in docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for year in the first 500 characters
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    # Simple heuristic: year is likely the first year mentioned in header or copyright
    # Papers usually start with Venue Year, or Copyright Year.
    # Exclude citation years if possible, but in header they are usually the pub year.
    pub_year = None
    if years:
        # Cast to int
        years = [int(y) for y in years]
        # Filter reasonable years (e.g. 2000-2025)
        years = [y for y in years if 2000 <= y <= 2025]
        if years:
            # Take the first one found in the header
            pub_year = years[0]
    
    # Extract Contribution
    # Check if "empirical" is in text (case insensitive)
    # The prompt hints "use substring/contains matching"
    is_empirical = 'empirical' in text.lower()
    
    if pub_year and pub_year > 2016 and is_empirical:
        matches.append(title)

print(f"Found {len(matches)} matching papers.")
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_function-call-1070528273488687685': ['paper_docs'], 'var_function-call-1070528273488689510': ['Citations', 'sqlite_sequence'], 'var_function-call-3440707792195880886': 'file_storage/function-call-3440707792195880886.json', 'var_function-call-4290533744407008086': 'file_storage/function-call-4290533744407008086.json'}

exec(code, env_args)
