code = """import re, json
from pathlib import Path

# Load full Mongo results
with open(var_call_MVg3RILQovtTlWaEl0dNkyNT, 'r') as f:
    mongo_docs = json.load(f)

# Identify CHI papers by searching for a CHI pattern in the text (conference header)
chi_titles = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    # Look for typical CHI pattern like CHI ' or CHI 20 in the conference header lines
    header = '\n'.join(text.splitlines()[:40])
    if re.search(r"CHI\s+'?\d{2}", header, re.IGNORECASE):
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load full citations results for 2020
with open(var_call_DXXmeYGQQnN75IY4o8sHRaFP, 'r') as f:
    citations = json.load(f)

# Sum citation counts for records whose title matches a CHI paper
chi_citation_total = 0
for row in citations:
    title = row.get('title', '')
    if title in chi_titles:
        try:
            chi_citation_total += int(row.get('citation_count', 0))
        except ValueError:
            pass

result = json.dumps(chi_citation_total)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_MVg3RILQovtTlWaEl0dNkyNT': 'file_storage/call_MVg3RILQovtTlWaEl0dNkyNT.json', 'var_call_DXXmeYGQQnN75IY4o8sHRaFP': 'file_storage/call_DXXmeYGQQnN75IY4o8sHRaFP.json'}

exec(code, env_args)
