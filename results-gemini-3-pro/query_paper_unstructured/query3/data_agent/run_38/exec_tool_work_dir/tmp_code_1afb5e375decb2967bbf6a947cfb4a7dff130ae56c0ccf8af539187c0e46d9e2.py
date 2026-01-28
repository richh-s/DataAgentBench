code = """import json
import re

# Load the sample paper
with open(locals()['var_function-call-5688695509175080773'], 'r') as f:
    papers = json.load(f)

paper = papers[0]
text = paper['text']
print(f"Title: {paper['filename']}")
print("First 500 chars:")
print(text[:500])

# Search for "Contribution"
matches = [m.start() for m in re.finditer(r'contribution', text, re.IGNORECASE)]
print(f"\n'Contribution' found at indices: {matches[:5]}")
for m in matches[:3]:
    print(f"Context around {m}: {text[m-50:m+50].replace(chr(10), ' ')}")

# Search for "Empirical"
matches_emp = [m.start() for m in re.finditer(r'empirical', text, re.IGNORECASE)]
print(f"\n'Empirical' found at indices: {matches_emp[:5]}")
for m in matches_emp[:3]:
    print(f"Context around {m}: {text[m-50:m+50].replace(chr(10), ' ')}")

# Search for Year
year_match = re.search(r'\b(20\d\d)\b', text[:1000])
print(f"\nYear match in first 1000 chars: {year_match.group(0) if year_match else 'None'}")"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json'}

exec(code, env_args)
