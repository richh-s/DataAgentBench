code = """import json
import re

# Load papers
with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    all_papers = json.load(f)

print("Total papers: " + str(len(all_papers)))

for i, paper in enumerate(all_papers[:10]):
    text = paper['text']
    filename = paper['filename']
    print("Paper: " + filename)
    
    lines = text.split('\n')
    # Print header
    for line in lines[:3]:
        if line.strip():
            print("  Header: " + line.strip())

    # Look for Contribution/Domain lines
    for line in lines:
        l_lower = line.lower()
        if "contribution" in l_lower and ":" in line:
            if len(line) < 200: # heuristic to avoid long sentences
                print("  Found Field: " + line.strip())
        if "domain" in l_lower and ":" in line:
            if len(line) < 200:
                print("  Found Field: " + line.strip())"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json'}

exec(code, env_args)
