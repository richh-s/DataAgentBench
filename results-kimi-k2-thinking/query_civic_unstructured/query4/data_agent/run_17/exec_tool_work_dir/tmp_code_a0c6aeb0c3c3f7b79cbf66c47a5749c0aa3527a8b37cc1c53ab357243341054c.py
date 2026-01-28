code = """import json
import re
from datetime import datetime

# Load the civic documents
filepath = var_functions.query_db:5
documents = []
with open(filepath, 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            try:
                doc = json.loads(line)
                documents.append(doc)
            except:
                # If not JSON per line, try parsing as a whole
                pass

# If we couldn't parse line by line, try as complete JSON
if not documents:
    with open(filepath, 'r') as f:
        content = f.read()
        try:
            documents = json.loads(content)
        except:
            pass

print("__RESULT__:")
print(json.dumps({"num_docs": len(documents)}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
