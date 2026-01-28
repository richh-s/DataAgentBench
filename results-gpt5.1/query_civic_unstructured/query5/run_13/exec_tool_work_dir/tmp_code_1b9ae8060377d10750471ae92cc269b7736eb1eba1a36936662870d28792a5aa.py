code = """import re, json
from pathlib import Path

path_civic = Path(var_call_yNtVSmduS3ElgyoR68hOJd3Y)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)
texts = [d['text'] for d in civic_docs]

path_funding = Path(var_call_RmmqeZSUIviHqbSnwcZ6H1mz)
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Identify disaster-related projects in funding by name patterns
keywords = ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']
disaster_funding = [row for row in funding if any(k in row['Project_Name'] for k in keywords)]

# Heuristic: consider a disaster project to have started in 2022 if its name or related text co-occurs with '2022'

def started_in_2022(name, texts):
    main_token = name.split()[0]
    for text in texts:
        if main_token in text and '2022' in text:
            return True
    return False

eligible = [row for row in disaster_funding if started_in_2022(row['Project_Name'], texts)]

total = 0
for row in eligible:
    try:
        total += int(row['Amount'])
    except Exception:
        pass

print("__RESULT__:")
print(json.dumps(total))"""

env_args = {'var_call_yNtVSmduS3ElgyoR68hOJd3Y': 'file_storage/call_yNtVSmduS3ElgyoR68hOJd3Y.json', 'var_call_RmmqeZSUIviHqbSnwcZ6H1mz': 'file_storage/call_RmmqeZSUIviHqbSnwcZ6H1mz.json'}

exec(code, env_args)
