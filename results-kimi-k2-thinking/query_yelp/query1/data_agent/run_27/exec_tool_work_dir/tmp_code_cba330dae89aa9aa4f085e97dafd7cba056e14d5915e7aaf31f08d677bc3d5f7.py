code = """import re

# Filter for Indianapolis, Indiana - trying different variations
filter_conditions = [
    {"description": {"$regex": "Indianapolis.*Indiana|Indiana.*Indianapolis", "$options": "i"}},
    {"description": {"$regex": "Indianapolis", "$options": "i"}},
    {"description": {"$regex": "^Indianapolis$", "$options": "i"}}
]

print("__RESULT__:")
print(str(filter_conditions))"""

env_args = {'var_functions.query_db:0': []}

exec(code, env_args)
