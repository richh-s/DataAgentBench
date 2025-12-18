code = """import json

with open(locals()['var_function-call-17315922237145365346'], 'r') as f:
    swift_repos_str_from_file = json.load(f)

# The swift_repos_str_from_file is a string like "'repo1', 'repo2'".
# We need to parse it into a list of strings.
swift_repos = [repo.strip().strip("'") for repo in swift_repos_str_from_file.split(',')]

# Construct the IN clause for the SQL query
repo_names_sql_list = ', '.join([f"'{repo}'" for repo in swift_repos])

# Prepare the SQL query to get non-binary Swift files and count their occurrences
# We group by id and sample_repo_name to ensure unique files are counted across repositories, and then find the one with the highest copy_count.
query = f"SELECT sample_repo_name FROM contents WHERE sample_repo_name IN ({repo_names_sql_list}) AND repo_data_description NOT LIKE '%binary%' GROUP BY id, sample_repo_name ORDER BY COUNT(id) DESC LIMIT 1;"

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-32885752495782732': 'file_storage/function-call-32885752495782732.json', 'var_function-call-17315922237145365346': 'file_storage/function-call-17315922237145365346.json', 'var_function-call-15496077545562064206': 'file_storage/function-call-15496077545562064206.json', 'var_function-call-13373338823996565834': "SELECT id, sample_repo_name, COUNT(id) AS copy_count FROM contents WHERE sample_repo_name IN ('f', 'i', 'l', 'e', '_', 's', 't', 'o', 'r', 'a', 'g', 'e', '/', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', '-', 'c', 'a', 'l', 'l', '-', '1', '5', '4', '9', '6', '0', '7', '7', '5', '4', '5', '5', '6', '2', '0', '6', '4', '2', '0', '6', '.', 'j', 's', 'o', 'n') AND repo_data_description NOT LIKE '%binary%' GROUP BY id, sample_repo_name ORDER BY copy_count DESC LIMIT 1;", 'var_function-call-3005635829945296024': "SELECT id, sample_repo_name, COUNT(id) AS copy_count FROM contents WHERE sample_repo_name IN ('f', 'i', 'l', 'e', '_', 's', 't', 'o', 'r', 'a', 'g', 'e', '/', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', '-', 'c', 'a', 'l', 'l', '-', '1', '5', '4', '9', '6', '0', '7', '7', '5', '4', '5', '5', '6', '2', '0', '6', '4', '2', '0', '6', '.', 'j', 's', 'o', 'n') AND repo_data_description NOT LIKE '%binary%' GROUP BY id, sample_repo_name ORDER BY copy_count DESC LIMIT 1;", 'var_function-call-5099789131182729233': "SELECT sample_repo_name FROM contents WHERE sample_repo_name IN ('f', 'i', 'l', 'e', '_', 's', 't', 'o', 'r', 'a', 'g', 'e', '/', 'f', 'u', 'n', 'c', 't', 'i', 'o', 'n', '-', 'c', 'a', 'l', 'l', '-', '1', '5', '4', '9', '6', '0', '7', '7', '5', '4', '5', '5', '6', '2', '0', '6', '4', '2', '0', '6', '.', 'j', 's', 'o', 'n') AND repo_data_description NOT LIKE '%binary%' GROUP BY id, sample_repo_name ORDER BY COUNT(id) DESC LIMIT 1;"}

exec(code, env_args)
