code = """import re, json
from pathlib import Path

# Load full Mongo results
mongo_path = Path(var_call_Gymm3J85qt3RfYGSHPygH4lN)
import pandas as pd
mongo_records = json.loads(mongo_path.read_text())

# Extract CHI titles from filenames by simple heuristic: look for 'CHI' in text near the copyright/venue line
chi_titles = set()
for rec in mongo_records:
    text = rec.get('text', '')
    # crude CHI detection
    if re.search(r"CHI '\d{2}", text, re.IGNORECASE):
        fname = rec.get('filename', '')
        if fname.lower().endswith('.txt'):
            title = fname[:-4]
        else:
            title = fname
        chi_titles.add(title)

# Load citation records
sql_path = Path(var_call_3mkLHw44ZDxrSGp30Vi57BIq)
sql_records = json.loads(sql_path.read_text())

# Sum citation counts for titles that are CHI papers
total_citations = 0
for row in sql_records:
    title = row.get('title')
    if title in chi_titles:
        try:
            total_citations += int(row.get('citation_count', 0))
        except ValueError:
            pass

result = total_citations

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_Gymm3J85qt3RfYGSHPygH4lN': 'file_storage/call_Gymm3J85qt3RfYGSHPygH4lN.json', 'var_call_3mkLHw44ZDxrSGp30Vi57BIq': 'file_storage/call_3mkLHw44ZDxrSGp30Vi57BIq.json'}

exec(code, env_args)
