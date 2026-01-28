code = """import re

# First, let's get all Swift repositories from the metadata database
from metadata_database import query_db

# Query languages table to get all Swift repositories
swift_repos_query = """
SELECT DISTINCT repo_name, language_description 
FROM languages 
WHERE language_description LIKE '%Swift%'
"""

# Let's also query artifacts to understand the structure better
artifacts_query = """
SELECT DISTINCT sample_repo_name, sample_path, repo_data_description, id
FROM contents 
WHERE sample_path LIKE '%.swift%' OR sample_path LIKE '%Swift%'
LIMIT 20
"""

print("__RESULT__:")
print(json.dumps({"swift_repos_query": swift_repos_query, "artifacts_query": artifacts_query}))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'language_description': 'This repository is mainly written in Swift (16,364 bytes), with additional code in Ruby (7,243 bytes), Shell (94 bytes).'}, {'language_description': 'The codebase includes: Swift (109,540 bytes), Ruby (3,068 bytes), Shell (762 bytes).'}, {'language_description': 'The codebase includes: Swift (18,238 bytes), Ruby (716 bytes), Shell (211 bytes).'}, {'language_description': 'The majority of the code is in Swift (1,723,695 bytes), followed by Shell (17,716 bytes), Ruby (297 bytes).'}, {'language_description': 'While most of the project is built in Swift (585,714 bytes), it also incorporates Ruby (3,447 bytes), Shell (190 bytes).'}, {'language_description': 'The codebase includes: Swift (33,632 bytes), Shell (711 bytes), Ruby (434 bytes).'}, {'language_description': 'The majority of the code is in Swift (747,765 bytes), followed by Ruby (3,949 bytes), Shell (393 bytes).'}, {'language_description': 'While most of the project is built in Swift (419,579 bytes), it also incorporates Ruby (767 bytes), Shell (169 bytes).'}, {'language_description': 'While most of the project is built in Swift (87,439 bytes), it also incorporates Ruby (2,165 bytes), Shell (65 bytes).'}, {'language_description': 'While most of the project is built in Swift (71,711 bytes), it also incorporates Shell (3,156 bytes), Ruby (3,009 bytes).'}]}

exec(code, env_args)
