code = """import json

file_path_citations = locals()['var_function-call-3647625760159840601']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

file_path_papers = locals()['var_function-call-13203611845597094222']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

acm_counts = []
total_matches = 0

for item in citations_data:
    fname = item['title'] + ".txt"
    if fname in paper_map:
        total_matches += 1
        text = paper_map[fname]
        # Check for ACM
        if "ACM" in text:
            acm_counts.append(int(item['citation_count']))

if acm_counts:
    avg = sum(acm_counts) / len(acm_counts)
else:
    avg = 0

print(f"DEBUG: Total matches: {total_matches}")
print(f"DEBUG: ACM papers found: {len(acm_counts)}")
print(f"DEBUG: Average: {avg}")

print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json', 'var_function-call-4446662547743021233': 68.5, 'var_function-call-5958297816336582346': 'Done', 'var_function-call-18435160050971913301': {'simple': 2, 'strict': 1}, 'var_function-call-9006900951989843847': 'Done', 'var_function-call-13203611845597094222': 'file_storage/function-call-13203611845597094222.json', 'var_function-call-18347844359487883025': 'Done'}

exec(code, env_args)
