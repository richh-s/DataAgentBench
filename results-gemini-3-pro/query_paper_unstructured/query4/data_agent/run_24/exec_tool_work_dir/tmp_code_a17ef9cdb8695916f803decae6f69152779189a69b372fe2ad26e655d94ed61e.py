code = """import json
import re

try:
    with open(locals()['var_function-call-5276622005229675102'], 'r') as f:
        papers = json.load(f)
except:
    papers = []

print(f"Total papers from Mongo: {len(papers)}")

# Debug: check first few papers
for i, p in enumerate(papers[:5]):
    text = p.get('text', '')
    header = text[:1000]
    print(f"--- Paper {i} ---")
    print(f"Title: {p.get('filename')}")
    print(f"Header snippet: {header.replace(chr(10), ' ')}") # remove newlines for compact print
    
    # Check "physical activity"
    if 'physical activity' in text.lower():
        print("Domain check: PASS")
    else:
        print("Domain check: FAIL")

    # Check year 2016
    if re.search(r'(?:Copyright|©).{0,20}2016', header, re.IGNORECASE):
        print("Year check: PASS (Copyright)")
    elif re.search(r'\b2016\b', header):
        print("Year check: PASS (Presence)")
    else:
        print("Year check: FAIL (Not found in header)")

print("__RESULT__:")
print(json.dumps("Debug info printed"))"""

env_args = {'var_function-call-13566097313952112574': 'file_storage/function-call-13566097313952112574.json', 'var_function-call-5276622005229675102': 'file_storage/function-call-5276622005229675102.json', 'var_function-call-15838140455159973064': []}

exec(code, env_args)
