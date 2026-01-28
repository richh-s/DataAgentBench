code = """import json
# Load the previous query result file containing Swift repos
path = var_call_eqmaxZmpNBz9YcLhcZjH9GHM
with open(path, 'r') as f:
    data = json.load(f)
repo_names = [rec['repo_name'] for rec in data]
# Build SQL IN clause safely by escaping single quotes
def esc(s):
    return s.replace("'", "''")
in_list = ','.join("'{}'".format(esc(r)) for r in repo_names)
sql = "SELECT id, sample_repo_name, sample_path, repo_data_description, COUNT(*) AS copies FROM contents WHERE lower(sample_path) LIKE '%.swift' AND lower(repo_data_description) NOT LIKE '%binary%' AND sample_repo_name IN ({}) GROUP BY id, sample_repo_name, sample_path, repo_data_description ORDER BY copies DESC LIMIT 1;".format(in_list)
import json
print("__RESULT__:")
print(json.dumps(sql))"""

env_args = {'var_call_2gtzgNNl3PMagWzeyUFOG8tg': ['commits', 'contents', 'files'], 'var_call_2thghvSm3un1065ccJcpEVQM': ['languages', 'repos', 'licenses'], 'var_call_eqmaxZmpNBz9YcLhcZjH9GHM': 'file_storage/call_eqmaxZmpNBz9YcLhcZjH9GHM.json', 'var_call_OHPBAiNSWIOZuym0KCceIXBX': [], 'var_call_Rq4MWAoTRLMNwK8iINY1wrAn': []}

exec(code, env_args)
