code = """import json

# Load the citations from the previous tool's output file
file_path = locals()['var_function-call-3451325983418300049']
with open(file_path, 'r') as f:
    citations = json.load(f)

# Extract filenames (title + .txt) and keep a map of title -> citation_count
title_to_citations = {}
filenames = []
for c in citations:
    title = c['title']
    citation_count = c['citation_count']
    title_to_citations[title] = citation_count
    filenames.append(title + ".txt")

print(f"Total papers cited in 2020: {len(filenames)}")
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-17105601548522055632': ['Citations', 'sqlite_sequence'], 'var_function-call-17105601548522056131': ['paper_docs'], 'var_function-call-3451325983418300049': 'file_storage/function-call-3451325983418300049.json'}

exec(code, env_args)
