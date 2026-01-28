code = """import json

with open(locals()['var_function-call-454889790813745050'], 'r') as f:
    docs = json.load(f)

print(f"Total docs: {len(docs)}")
for i, doc in enumerate(docs[:5]):
    print(f"--- Doc {i} : {doc.get('filename')} ---")
    text = doc.get('text', '')
    # Search for metadata-like lines
    lines = text.split('\n')
    for line in lines:
        if 'contribution' in line.lower() or 'year' in line.lower() or 'venue' in line.lower():
            if len(line) < 100: # print short lines that might be metadata
                print(f"  Found potential metadata: {line.strip()}")
    # Also print the last 500 chars to check for appended metadata
    print(f"  End of text snippet: {text[-500:]}")"""

env_args = {'var_function-call-454889790813745050': 'file_storage/function-call-454889790813745050.json'}

exec(code, env_args)
