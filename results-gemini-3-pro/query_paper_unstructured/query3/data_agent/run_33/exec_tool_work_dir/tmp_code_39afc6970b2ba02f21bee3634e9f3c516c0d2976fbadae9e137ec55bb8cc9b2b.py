code = """import json

file_path = locals()['var_function-call-454889790813745050']
with open(file_path, 'r') as f:
    docs = json.load(f)

print("Total docs:", len(docs))
for i, doc in enumerate(docs[:5]):
    print("Doc:", doc.get('filename'))
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        if 'Contribution:' in line:
            print("  MATCH:", line.strip())
        if 'Year:' in line:
            print("  MATCH:", line.strip())
    print("  First 200 chars:", text[:200].replace('\n', ' '))
    print("  Last 200 chars:", text[-200:].replace('\n', ' '))"""

env_args = {'var_function-call-454889790813745050': 'file_storage/function-call-454889790813745050.json'}

exec(code, env_args)
