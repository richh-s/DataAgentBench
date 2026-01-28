code = """import json, re
from pathlib import Path

# Load full results for CHI-related papers (var_call_55LL6M7PnkHzb4wIyJ1rVStc)
chi_path = Path(var_call_55LL6M7PnkHzb4wIyJ1rVStc)
with chi_path.open() as f:
    chi_docs = json.load(f)

# Extract titles (filename without .txt) for papers whose venue is CHI.
# We approximate venue=CHI by detecting 'CHI' near ACM conference headers in text.
chi_titles = set()
for doc in chi_docs:
    text = doc.get('text','')
    # Heuristic: look for CHI in typical ACM conference header lines
    if re.search(r"CHI '\d{2}|ACM CHI|Conference on Human Factors in Computing Systems", text, re.IGNORECASE):
        filename = doc.get('filename','')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load all 2020 citations
cits_path = Path(var_call_6ua7TwgZH94THBZV10X5ODia)
with cits_path.open() as f:
    cits = json.load(f)

# Sum citation counts for 2020 for titles that are CHI papers
# Titles in Citations table exactly match filenames without .txt
chi_citation_total = 0
for row in cits:
    title = row['title']
    if title in chi_titles:
        chi_citation_total += int(row['total_citations'])

result = {'total_citations_2020_for_CHI_papers': chi_citation_total}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_55LL6M7PnkHzb4wIyJ1rVStc': 'file_storage/call_55LL6M7PnkHzb4wIyJ1rVStc.json', 'var_call_6ua7TwgZH94THBZV10X5ODia': 'file_storage/call_6ua7TwgZH94THBZV10X5ODia.json'}

exec(code, env_args)
