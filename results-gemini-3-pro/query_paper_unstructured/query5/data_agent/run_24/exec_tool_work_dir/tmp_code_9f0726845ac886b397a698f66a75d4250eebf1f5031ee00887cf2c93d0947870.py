code = """import json
import re

with open(locals()['var_function-call-5688223812059050868'], 'r') as f:
    paper_docs = json.load(f)

regex_str = r"CHI\s?'\d{2}|CHI\s?20\d{2}|Conference on Human Factors in Computing Systems"
venue_regex = re.compile(regex_str, re.IGNORECASE)

missed_candidates = []

for d in paper_docs:
    header = d['text'][:2000]
    if "CHI" in header:
        if not venue_regex.search(header):
            # Check if it's OzCHI or CHI Play which we want to exclude?
            # Or if it is a CHI paper missed by regex.
            missed_candidates.append(header[:200])

print("__RESULT__:")
print(json.dumps(missed_candidates))"""

env_args = {'var_function-call-3271567953918083251': 'file_storage/function-call-3271567953918083251.json', 'var_function-call-3271567953918083494': ['paper_docs'], 'var_function-call-17597164597794673073': 'file_storage/function-call-17597164597794673073.json', 'var_function-call-6676021066055813703': 0, 'var_function-call-7180838607779027661': 'Done', 'var_function-call-14386505862075830980': {'total_citations_records': 188, 'total_paper_docs': 5, 'common_titles': 4, 'chi_papers_found': 0, 'chi_papers_with_citations': 0, 'sample_chi_headers': [], 'final_sum': 0}, 'var_function-call-5688223812059050868': 'file_storage/function-call-5688223812059050868.json', 'var_function-call-3535785703897433951': 61, 'var_function-call-5714243465560524221': {'total_docs': 99, 'chi_papers_found': 3, 'chi_papers_with_citations': 3, 'total_citations': 61, 'matched_samples': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'citations': 16}, {'title': 'Patient Perspectives on Self-Management Technologies for Chronic Fatigue Syndrome', 'citations': 43}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'citations': 2}]}}

exec(code, env_args)
