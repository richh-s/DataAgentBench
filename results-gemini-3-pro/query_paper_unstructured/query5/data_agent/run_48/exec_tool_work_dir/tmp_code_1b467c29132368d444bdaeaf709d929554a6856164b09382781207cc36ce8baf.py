code = """import json
import re

with open(locals()['var_function-call-8351315325764085192'], 'r') as f:
    papers_list = json.load(f)

print("Checking non-matched papers:")
count = 0
for p in papers_list:
    text = p['text'][:3000]
    
    # Check if it was matched
    matched = False
    if re.search(r"CHI\s+['’]?\s*\d{2,4}", text):
        matched = True
    elif "Conference on Human Factors in Computing Systems" in text:
        matched = True
    if re.search(r"OzCHI", text, re.IGNORECASE) or re.search(r"CHI Play", text, re.IGNORECASE):
        matched = False
        
    if not matched:
        # Check if it looks like CHI
        if "CHI" in text:
            print(f"--- {p['filename']} (Not Matched but has CHI) ---")
            # Print context of CHI
            matches = re.findall(r".{0,40}CHI.{0,40}", text)
            for m in matches:
                print(m)
            count += 1
            if count > 5:
                break
print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-264858034059979045': 'file_storage/function-call-264858034059979045.json', 'var_function-call-16262197769178367218': {'count': 188, 'sample_title': 'Sundroid: Solar Radiation Awareness with Smartphones'}, 'var_function-call-2494524119581093015': 'file_storage/function-call-2494524119581093015.json', 'var_function-call-3380312142503180972': 'file_storage/function-call-3380312142503180972.json', 'var_function-call-8351315325764085192': 'file_storage/function-call-8351315325764085192.json', 'var_function-call-1959921926523090950': {'total_citations': 0, 'num_papers': 0}, 'var_function-call-8389437484024645991': 'Done', 'var_function-call-2898140987180465692': 'Done', 'var_function-call-8612993969594668577': {'total_citations': 114, 'num_papers': 2}}

exec(code, env_args)
