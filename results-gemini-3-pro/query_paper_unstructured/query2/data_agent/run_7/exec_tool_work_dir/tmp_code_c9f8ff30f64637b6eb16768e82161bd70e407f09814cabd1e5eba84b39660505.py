code = """import json

# Load citation data (title and citation_count)
# This file contains the list of dicts: [{"title": "...", "citation_count": ...}, ...]
path_citations = locals()['var_function-call-14272256085625645601']
with open(path_citations, 'r') as f:
    citations_data = json.load(f)

# Load ACM papers filenames
# This file contains a list of dicts: [{"_id": "...", "filename": "..."}, ...]
path_acm_files = locals()['var_function-call-9226180729544213779']
with open(path_acm_files, 'r') as f:
    acm_files_data = json.load(f)

# Create a set of titles for ACM papers
# filename = title + ".txt" -> title = filename[:-4]
acm_titles = set()
for item in acm_files_data:
    fname = item['filename']
    if fname.endswith('.txt'):
        acm_titles.add(fname[:-4])
    else:
        acm_titles.add(fname)

# Filter citation data to include only ACM papers
acm_citations = []
for item in citations_data:
    if item['title'] in acm_titles:
        acm_citations.append(int(item['citation_count']))

# Calculate average
if len(acm_citations) > 0:
    average_citation = sum(acm_citations) / len(acm_citations)
else:
    average_citation = 0

print(f"Number of papers cited in 2018: {len(citations_data)}")
print(f"Number of ACM papers found: {len(acm_titles)}")
print(f"Number of ACM papers cited in 2018: {len(acm_citations)}")
print(f"Average citation count: {average_citation}")

print("__RESULT__:")
print(average_citation)"""

env_args = {'var_function-call-14272256085625645601': 'file_storage/function-call-14272256085625645601.json', 'var_function-call-14136390404799655173': 'file_storage/function-call-14136390404799655173.json', 'var_function-call-4110130816572520237': 'file_storage/function-call-4110130816572520237.json', 'var_function-call-11739023071620531107': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-1392913307814716380': 'file_storage/function-call-1392913307814716380.json', 'var_function-call-12385441691313061416': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-9226180729544213779': 'file_storage/function-call-9226180729544213779.json'}

exec(code, env_args)
