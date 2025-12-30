code = """import json

# Load the citations result
# The key for the previous result is var_function-call-1018587870991830331
with open(locals()['var_function-call-1018587870991830331'], 'r') as f:
    citations_data = json.load(f)

# Create a dictionary of title -> citation_count
title_citations = {item['title']: item['citation_count'] for item in citations_data}
titles = list(title_citations.keys())

# Create the list of filenames
filenames = [t + ".txt" for t in titles]

print("__RESULT__:")
print(json.dumps({"filenames": filenames, "title_citations": title_citations}))"""

env_args = {'var_function-call-2890407691846929350': ['Citations', 'sqlite_sequence'], 'var_function-call-2890407691846929759': 'file_storage/function-call-2890407691846929759.json', 'var_function-call-1018587870991830331': 'file_storage/function-call-1018587870991830331.json'}

exec(code, env_args)
