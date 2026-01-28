code = """import json

# Load the data
chi_file_path = "file_storage/functions.query_db:26.json"
with open(chi_file_path, 'r') as f:
    chi_docs = json.load(f)

citations_file_path = "file_storage/functions.query_db:24.json"
with open(citations_file_path, 'r') as f:
    citations_2020 = json.load(f)

# Show CHI papers
print("CHI Papers identified:")
chi_titles = []
for doc in chi_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    chi_titles.append(title)
    print(f"- {title}")

# Create a dict of citations for easier lookup
citations_dict = {c['title']: int(c['total_citations_2020']) for c in citations_2020}

# Show which CHI papers were cited and how many times
print("\nCHI Papers cited in 2020:")
total = 0
for title in chi_titles:
    if title in citations_dict:
        count = citations_dict[title]
        total += count
        print(f"- {title}: {count} citations")

print(f"\nTotal citations for CHI papers in 2020: {total}")"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.execute_python:18': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_citations_count': 243, 'chi_papers_identified': 5, 'chi_papers_cited_in_2020': 4}}

exec(code, env_args)
