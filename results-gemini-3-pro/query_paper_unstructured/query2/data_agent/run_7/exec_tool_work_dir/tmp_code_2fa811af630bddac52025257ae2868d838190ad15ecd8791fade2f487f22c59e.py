code = """import json

# Get the file path from the variable
file_path = locals()['var_function-call-14272256085625645601']

# Read the result
with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Extract titles and map to citation count
# We need to keep citation counts to calculate the average later
paper_citations = {item['title']: item['citation_count'] for item in citations_data}
filenames = [t + ".txt" for t in paper_citations.keys()]

print(f"Total papers cited in 2018: {len(filenames)}")

# Print the filenames to use in the next step, but limited if too many
# Actually, I need to pass this list to the next query_db call. 
# I will print the list of filenames.
print("__RESULT__:")
print(json.dumps(filenames))"""

env_args = {'var_function-call-14272256085625645601': 'file_storage/function-call-14272256085625645601.json'}

exec(code, env_args)
