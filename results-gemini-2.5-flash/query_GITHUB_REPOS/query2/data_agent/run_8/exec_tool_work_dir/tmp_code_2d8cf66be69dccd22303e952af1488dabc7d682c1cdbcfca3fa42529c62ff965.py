code = """import json

swift_repos = [repo['repo_name'] for repo in json.load(open(locals()['var_function-call-1512978699432665502']))]

# Construct the SQL query to get the file IDs and their counts from artifacts_database
# We filter for non-binary files and for repositories identified as Swift.
# The subquery is to count distinct file IDs per repo, and then the outer query will find the max copied non-binary swift file within these repos.
# This approach ensures uniqueness of files by ID and counts copies within the specified Swift repos.
swift_repos_str = ", ".join([f"'{repo}'" for repo in swift_repos])
query = f"""
    SELECT 
        id, 
        sample_repo_name,
        COUNT(id) as copy_count
    FROM contents
    WHERE 
        sample_repo_name IN ({swift_repos_str}) AND 
        repo_data_description NOT LIKE '%binary%'
    GROUP BY id, sample_repo_name
    ORDER BY copy_count DESC
    LIMIT 1;
"""
print("__RESULT__:")
print(json.dumps(query))"""

env_args = {'var_function-call-1512978699432665502': 'file_storage/function-call-1512978699432665502.json'}

exec(code, env_args)
