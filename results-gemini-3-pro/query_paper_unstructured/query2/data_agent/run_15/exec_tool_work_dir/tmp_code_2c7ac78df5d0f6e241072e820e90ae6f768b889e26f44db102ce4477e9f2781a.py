code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-974393757557094033']

# Load the SQLite result
with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Extract titles and create a map of title -> citation_count
title_citation_map = {item['title']: int(item['citation_count']) for item in citations_data}
titles = list(title_citation_map.keys())
filenames = [t + ".txt" for t in titles]

print(f"Number of papers cited in 2018: {len(filenames)}")

# I will return the list of filenames to be used in the next step, 
# but also the map so I can use it later. 
# Since I can't pass complex objects easily between steps without printing,
# I'll just print the list of filenames for the query construction 
# and keep the logic of joining in the next python step by reloading the citations file.

print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-974393757557094033': 'file_storage/function-call-974393757557094033.json'}

exec(code, env_args)
