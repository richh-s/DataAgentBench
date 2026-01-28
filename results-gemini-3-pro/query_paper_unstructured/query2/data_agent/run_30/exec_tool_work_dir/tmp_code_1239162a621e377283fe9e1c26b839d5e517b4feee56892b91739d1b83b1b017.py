code = """import json

file_path_citations = locals()['var_function-call-3647625760159840601']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

file_path_papers = locals()['var_function-call-13203611845597094222']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

print(f"DEBUG: Unique files in map: {len(paper_map)}")

matches = 0
acm_matches = 0
citation_sum = 0

for item in citations_data:
    fname = item['title'] + ".txt"
    if fname in paper_map:
        matches += 1
        text = paper_map[fname]
        if "ACM" in text:
            acm_matches += 1
            citation_sum += int(item['citation_count'])

print(f"DEBUG: Matches: {matches}")
print(f"DEBUG: ACM Matches: {acm_matches}")
print(f"DEBUG: Sum: {citation_sum}")

avg = citation_sum / acm_matches if acm_matches else 0
print("__RESULT__:")
print(json.dumps(avg))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json', 'var_function-call-4446662547743021233': 68.5, 'var_function-call-5958297816336582346': 'Done', 'var_function-call-18435160050971913301': {'simple': 2, 'strict': 1}, 'var_function-call-9006900951989843847': 'Done', 'var_function-call-13203611845597094222': 'file_storage/function-call-13203611845597094222.json', 'var_function-call-18347844359487883025': 'Done', 'var_function-call-3246827811593006849': 59.36363636363637, 'var_function-call-3429177790326672840': 'Done', 'var_function-call-14324070422364768195': {'count': 55, 'sum': 3265, 'average': 59.36363636363637}}

exec(code, env_args)
