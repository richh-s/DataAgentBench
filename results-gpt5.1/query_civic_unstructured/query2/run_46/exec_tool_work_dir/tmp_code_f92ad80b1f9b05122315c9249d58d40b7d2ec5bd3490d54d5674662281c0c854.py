code = """import re, json, pandas as pd
from datetime import datetime

# Load full civic docs
path_docs = var_call_BDw70ni8117NDNAZ51i2exyr
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_4XPsRAW1Xzg8SR3hwSWqljjt)
funding['Amount'] = funding['Amount'].astype(int)

park_keywords = ['park', 'playground']

project_pattern = re.compile(r"^(?P<name>.+?)(?:\n\(cid:190\)|\n\u2022|- )", re.MULTILINE)
completed_pattern = re.compile(r"Construction was completed,? (?P<date>[A-Za-z]+ \d{4}|[A-Za-z]+ \d{1,2},? \d{4}|\w+ 2022|November 2022|December 2022|2022)", re.IGNORECASE)

completed_2022_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text or 'completed' not in text.lower():
        continue
    for match in project_pattern.finditer(text):
        name = match.group('name').strip()
        block_start = match.start()
        block_end = text.find('\n\n', block_start)
        if block_end == -1:
            block_end = len(text)
        block = text[block_start:block_end]
        if 'construction was completed' in block.lower() and '2022' in block:
            if any(kw in name.lower() for kw in park_keywords) or any(kw in block.lower() for kw in park_keywords):
                completed_2022_projects.add(name)

funding_2022_park = funding[funding['Project_Name'].isin(completed_2022_projects)]

total_funding = int(funding_2022_park['Amount'].sum())

result = {
    'completed_2022_park_projects': sorted(list(completed_2022_projects)),
    'total_funding': total_funding
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_BDw70ni8117NDNAZ51i2exyr': 'file_storage/call_BDw70ni8117NDNAZ51i2exyr.json', 'var_call_4XPsRAW1Xzg8SR3hwSWqljjt': 'file_storage/call_4XPsRAW1Xzg8SR3hwSWqljjt.json'}

exec(code, env_args)
