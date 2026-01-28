code = """import json, statistics
import pandas as pd
from pathlib import Path

path = var_call_9Aon4l7H2C0mtCnK8b6th7lc
with open(path, 'r') as f:
    data = json.load(f)

# Assume all these papers are ACM unless we filter via paper_docs, but question only wants ACM; need filter using Mongo.
# Collect titles to query paper_docs.
titles = [d['title'] for d in data]

result = json.dumps(titles)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_9Aon4l7H2C0mtCnK8b6th7lc': 'file_storage/call_9Aon4l7H2C0mtCnK8b6th7lc.json'}

exec(code, env_args)
