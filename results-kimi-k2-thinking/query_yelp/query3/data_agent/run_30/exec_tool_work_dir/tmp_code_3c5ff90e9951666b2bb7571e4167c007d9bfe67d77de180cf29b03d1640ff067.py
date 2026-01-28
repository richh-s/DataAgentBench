code = """import json

# Query review table for 2018 reviews
# We'll use DuckDB syntax since user_database is DuckDB
query_2018_reviews = """
SELECT DISTINCT business_ref 
FROM review 
WHERE date >= '2018-01-01' AND date < '2019-01-01'
"""

print("__RESULT__:")
print(json.dumps(query_2018_reviews))"""

env_args = {}

exec(code, env_args)
