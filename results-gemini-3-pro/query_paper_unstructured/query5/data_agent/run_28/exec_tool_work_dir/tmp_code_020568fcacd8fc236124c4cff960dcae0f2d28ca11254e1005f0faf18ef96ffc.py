code = """import json

with open(locals()['var_function-call-15345152852245153349'], 'r') as f:
    papers_data = json.load(f)

print("First 5 filenames:")
for paper in papers_data[:5]:
    print(paper['filename'])

count_chi = 0
for paper in papers_data:
    if "CHI" in paper['text'][:500]:
        count_chi += 1

print("Number of papers with CHI in first 500 chars:", count_chi)

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-9042960770956765793': ['Citations', 'sqlite_sequence'], 'var_function-call-9042960770956765216': ['paper_docs'], 'var_function-call-9700206069512387348': 'file_storage/function-call-9700206069512387348.json', 'var_function-call-9700206069512385745': 'file_storage/function-call-9700206069512385745.json', 'var_function-call-15345152852245153349': 'file_storage/function-call-15345152852245153349.json', 'var_function-call-13303026502511534090': 0}

exec(code, env_args)
