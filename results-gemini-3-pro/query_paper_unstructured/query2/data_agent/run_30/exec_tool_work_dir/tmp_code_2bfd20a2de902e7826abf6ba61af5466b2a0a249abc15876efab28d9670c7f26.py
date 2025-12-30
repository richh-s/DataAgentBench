code = """import json

file_path_citations = locals()['var_function-call-3647625760159840601']
with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

file_path_papers = locals()['var_function-call-7977022267260973965']
with open(file_path_papers, 'r') as f:
    paper_docs = json.load(f)

paper_map = {doc['filename']: doc['text'] for doc in paper_docs}

matches = 0
for item in citations_data:
    if (item['title'] + ".txt") in paper_map:
        matches += 1

print(f"DEBUG: Total citations: {len(citations_data)}")
print(f"DEBUG: Total papers in Mongo dump: {len(paper_docs)}")
print(f"DEBUG: Matches found: {matches}")

# Check the text of one matching paper
if matches > 0:
    first_match_title = citations_data[0]['title'] + ".txt"
    if first_match_title in paper_map:
        print(f"DEBUG: Sample text start: {paper_map[first_match_title][:500]}")
    else:
        # Find one that matches
        for item in citations_data:
            fname = item['title'] + ".txt"
            if fname in paper_map:
                print(f"DEBUG: Sample text start for {fname}: {paper_map[fname][:500]}")
                break

print("__RESULT__:")
print(json.dumps("Done"))"""

env_args = {'var_function-call-5264272901715907644': ['Citations', 'sqlite_sequence'], 'var_function-call-5264272901715907989': ['paper_docs'], 'var_function-call-3647625760159840601': 'file_storage/function-call-3647625760159840601.json', 'var_function-call-16517880119813488158': 158, 'var_function-call-6596666326870079897': 'file_storage/function-call-6596666326870079897.json', 'var_function-call-7977022267260973965': 'file_storage/function-call-7977022267260973965.json', 'var_function-call-4446662547743021233': 68.5, 'var_function-call-5958297816336582346': 'Done', 'var_function-call-18435160050971913301': {'simple': 2, 'strict': 1}}

exec(code, env_args)
