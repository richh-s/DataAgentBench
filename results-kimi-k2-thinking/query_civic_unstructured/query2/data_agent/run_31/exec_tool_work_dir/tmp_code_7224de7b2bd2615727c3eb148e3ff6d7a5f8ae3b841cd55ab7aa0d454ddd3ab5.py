code = """import json

# Query civic_docs collection for park-related projects completed in 2022
query = {
    "collection": "civic_docs",
    "filter": {
        "text": {
            "$regex": "park",
            "$options": "i"
        }
    },
    "projection": {
        "filename": 1,
        "text": 1
    }
}

print("__RESULT__:")
print(json.dumps(query))"""

env_args = {}

exec(code, env_args)
