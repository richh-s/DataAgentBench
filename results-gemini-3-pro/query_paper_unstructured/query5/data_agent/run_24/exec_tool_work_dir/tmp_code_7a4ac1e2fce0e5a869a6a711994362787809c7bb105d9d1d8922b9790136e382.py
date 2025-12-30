code = """import json
import re

with open(locals()['var_function-call-3271567953918083251'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-17597164597794673073'], 'r') as f:
    paper_docs = json.load(f)

print("DEBUG: Sample Citations Titles:")
for c in citations_data[:5]:
    print(" - " + c['title'])

print("\nDEBUG: Sample Paper Filenames:")
for d in paper_docs[:5]:
    print(" - " + d['filename'])

print("\nDEBUG: Sample Paper Headers:")
for d in paper_docs[:5]:
    print("--- Header for " + d['filename'] + " ---")
    print(repr(d['text'][:300]))

venue_regex = re.compile(r"CHI\s?'\d{2}|CHI\s?20\d{2}|Conference on Human Factors in Computing Systems", re.IGNORECASE)

print("\nDEBUG: Regex Match Check:")
for d in paper_docs[:5]:
    match = venue_regex.search(d['text'][:1000])
    print(" - " + d['filename'] + ": " + ("MATCH" if match else "NO MATCH"))

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json', 'var_function-call-6676021066055813703': 0}

exec(code, env_args)
