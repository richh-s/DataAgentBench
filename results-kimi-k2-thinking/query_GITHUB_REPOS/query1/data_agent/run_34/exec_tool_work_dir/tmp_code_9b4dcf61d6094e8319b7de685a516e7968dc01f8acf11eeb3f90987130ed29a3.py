code = """import json
import pandas as pd

# Read the full result from the query
with open(var_functions.query_db_0, 'r') as f:
    languages_data = json.load(f)

# Convert to DataFrame
df_languages = pd.DataFrame(languages_data)

# Check for Python in language descriptions
df_languages['has_python'] = df_languages['language_description'].str.contains('Python', case=False, na=False)

# Show some examples
print("Total repositories:", len(df_languages))
print("Repos with Python:", df_languages['has_python'].sum())
print("Repos without Python:", (~df_languages['has_python']).sum())

# Show some examples of both
print("\nExample repos WITHOUT Python:")
print(df_languages[~df_languages['has_python']].head(3)['language_description'].tolist())

print("\nExample repos WITH Python:")
print(df_languages[df_languages['has_python']].head(3)['language_description'].tolist())

# Get list of repos without Python
repos_without_python = df_languages[~df_languages['has_python']]['repo_name'].tolist()

# Save this for later use
result = {
    'total_repos': len(df_languages),
    'repos_with_python': int(df_languages['has_python'].sum()),
    'repos_without_python': int((~df_languages['has_python']).sum()),
    'repos_without_python_list': repos_without_python[:10]  # Sample for debugging
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
