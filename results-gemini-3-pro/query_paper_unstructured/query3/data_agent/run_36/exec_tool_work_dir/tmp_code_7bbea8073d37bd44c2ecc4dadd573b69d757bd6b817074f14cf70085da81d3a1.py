code = """import json
import re

with open('var_function-call-5013530171335894864', 'r') as f:
    papers = json.load(f)

for p in papers:
    print(f"--- Processing {p['filename']} ---")
    text = p['text']
    print("Start:", text[:200])
    print("End:", text[-200:])
    
    # Check for Contribution
    matches = list(re.finditer(r"contribution", text, re.IGNORECASE))
    for m in matches[:3]:
        start = max(0, m.start() - 50)
        end = min(len(text), m.end() + 50)
        print(f"Match 'contribution': ...{text[start:end]}...")
        
    # Check for Empirical
    matches = list(re.finditer(r"empirical", text, re.IGNORECASE))
    for m in matches[:3]:
        start = max(0, m.start() - 50)
        end = min(len(text), m.end() + 50)
        print(f"Match 'empirical': ...{text[start:end]}...")

    # Check for Year
    # Look for 20xx in first 500 chars
    years = re.findall(r"20\d{2}", text[:1000])
    print("Potential years:", years)

print("__RESULT__:")
print("Done")"""

env_args = {'var_function-call-16234015966319740507': 'file_storage/function-call-16234015966319740507.json', 'var_function-call-12802565498323795136': ['Citations', 'sqlite_sequence'], 'var_function-call-5013530171335894864': 'file_storage/function-call-5013530171335894864.json'}

exec(code, env_args)
