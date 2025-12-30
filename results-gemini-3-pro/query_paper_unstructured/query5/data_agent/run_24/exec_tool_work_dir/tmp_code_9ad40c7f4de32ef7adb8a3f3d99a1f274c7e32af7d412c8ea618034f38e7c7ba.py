code = """import json
import re

with open(locals()['var_function-call-3271567953918083251'], 'r') as f:
    citations_data = json.load(f)
with open(locals()['var_function-call-17597164597794673073'], 'r') as f:
    paper_docs = json.load(f)

c_titles = set(c['title'] for c in citations_data)
p_titles = set(d['filename'][:-4] for d in paper_docs if d['filename'].endswith('.txt'))
common = c_titles.intersection(p_titles)
print("DEBUG: Common titles count:", len(common))

# regex for CHI
# We use simple patterns
regex_str = r"CHI\s?'\d{2}|CHI\s?20\d{2}|Conference on Human Factors in Computing Systems"
venue_regex = re.compile(regex_str, re.IGNORECASE)

chi_papers = []
for d in paper_docs:
    if venue_regex.search(d['text'][:1000]):
        chi_papers.append(d['filename'])

print("DEBUG: CHI papers found:", len(chi_papers))
if len(chi_papers) > 0:
    print("DEBUG: Sample CHI papers:", chi_papers[:3])
    # Check if these are in common
    chi_titles = set(n[:-4] for n in chi_papers)
    common_chi = chi_titles.intersection(c_titles)
    print("DEBUG: CHI papers with citations in 2020:", len(common_chi))
else:
    print("DEBUG: No CHI papers found. Checking sample headers again.")
    for d in paper_docs[:3]:
        print("HEADER:", repr(d['text'][:100]))

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json', 'var_function-call-6676021066055813703': 0}

exec(code, env_args)
