code = """import json

file_path_citations = locals()['var_function-call-3647625760159840601']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

file_path_papers = locals()['var_function-call-7977022267260973965']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

count_simple = 0
count_strict = 0
strict_indices = []

for i, item in enumerate(citations_data):
    filename = item['title'] + ".txt"
    if filename in paper_map:
        text = paper_map[filename]
        if "ACM" in text:
            count_simple += 1
            
            # Strict logic:
            # 1. Look for "ACM" in the first 2000 characters.
            # 2. Most ACM papers have "ACM Classification Keywords" or "Copyright ... ACM".
            head = text[:2000]
            is_strict = False
            if "ACM Classification Keywords" in head:
                is_strict = True
            elif "Copyright" in head and "ACM" in head:
                is_strict = True
            elif "\u00a9 ACM" in head:
                is_strict = True
            
            if is_strict:
                count_strict += 1
                strict_indices.append(i)

result_obj = {
    "simple": count_simple,
    "strict": count_strict
}
print("__RESULT__:")
print(json.dumps(result_obj))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json', 'var_function-call-4446662547743021233': 68.5, 'var_function-call-5958297816336582346': 'Done'}

exec(code, env_args)
