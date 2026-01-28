code = """import json

with open(locals()['var_function-call-15345152852245153349'], 'r') as f:
    papers_data = json.load(f)

print("Checking for CHI in first 100 papers...")
for paper in papers_data[:100]:
    text = paper.get('text', '')
    if "CHI" in text[:500]:
        print("Filename:", paper['filename'])
        print("Header:", text[:300])
        break

print("\nFirst 5 papers headers:")
for paper in papers_data[:5]:
    print("Filename:", paper['filename'])
    print("Header:", paper['text'][:200])
    print("-" * 20)

print("__RESULT__:")
print("done")"""

env_args = {'var_function-call-9042960770956765793': ['Citations', 'sqlite_sequence'], 'var_function-call-9042960770956765216': ['paper_docs'], 'var_function-call-9700206069512387348': 'file_storage/function-call-9700206069512387348.json', 'var_function-call-9700206069512385745': 'file_storage/function-call-9700206069512385745.json', 'var_function-call-15345152852245153349': 'file_storage/function-call-15345152852245153349.json', 'var_function-call-13303026502511534090': 0}

exec(code, env_args)
