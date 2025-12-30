code = """import json

# Load citation data
path_citations = locals()['var_function-call-14272256085625645601']
with open(path_citations, 'r') as f:
    citations_data = json.load(f)

# Load ALL papers filenames (since all seem to be ACM)
path_all_files = locals()['var_function-call-1392913307814716380']
with open(path_all_files, 'r') as f:
    all_files_data = json.load(f)

# Titles in MongoDB
mongo_titles = set()
for item in all_files_data:
    fname = item['filename']
    if fname.endswith('.txt'):
        mongo_titles.add(fname[:-4])
    else:
        mongo_titles.add(fname)

# Titles cited in 2018
# And filter by those present in MongoDB
cited_in_2018_and_in_mongo = []
for item in citations_data:
    if item['title'] in mongo_titles:
        cited_in_2018_and_in_mongo.append(int(item['citation_count']))

average = sum(cited_in_2018_and_in_mongo) / len(cited_in_2018_and_in_mongo) if cited_in_2018_and_in_mongo else 0

print(f"Intersection size: {len(cited_in_2018_and_in_mongo)}")
print(f"Average: {average}")

print("__RESULT__:")
print(average)"""

env_args = {'var_function-call-14272256085625645601': 'file_storage/function-call-14272256085625645601.json', 'var_function-call-14136390404799655173': 'file_storage/function-call-14136390404799655173.json', 'var_function-call-4110130816572520237': 'file_storage/function-call-4110130816572520237.json', 'var_function-call-11739023071620531107': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-1392913307814716380': 'file_storage/function-call-1392913307814716380.json', 'var_function-call-12385441691313061416': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-9226180729544213779': 'file_storage/function-call-9226180729544213779.json', 'var_function-call-14229864823544554196': 59.36363636363637, 'var_function-call-9049171449856789962': {'acm_count': 99, 'cited_count': 158}, 'var_function-call-15039418553757060138': 99}

exec(code, env_args)
