code = """import json

file_path_papers = locals()['var_function-call-13203611845597094222']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

count_simple = 0
count_strict = 0

for doc in paper_docs:
    text = doc['text']
    if "ACM" in text:
        count_simple += 1
        
        # Strict
        head = text[:5000].lower() # Check first 5000 chars
        if "copyright" in head and "acm" in head:
            count_strict += 1
        elif "© acm" in head or "\u00a9 acm" in head:
            count_strict += 1
        elif "permission" in head and "acm" in head:
            count_strict += 1
        elif "association for computing machinery" in head:
            count_strict += 1

print(f"DEBUG: Simple count: {count_simple}")
print(f"DEBUG: Strict count: {count_strict}")
print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json', 'var_function-call-4446662547743021233': 68.5, 'var_function-call-5958297816336582346': 'Done', 'var_function-call-18435160050971913301': {'simple': 2, 'strict': 1}, 'var_function-call-9006900951989843847': 'Done', 'var_function-call-13203611845597094222': 'file_storage/function-call-13203611845597094222.json', 'var_function-call-18347844359487883025': 'Done', 'var_function-call-3246827811593006849': 59.36363636363637}

exec(code, env_args)
