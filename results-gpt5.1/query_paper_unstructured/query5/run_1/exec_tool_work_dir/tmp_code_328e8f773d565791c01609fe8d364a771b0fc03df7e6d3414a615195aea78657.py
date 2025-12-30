code = """import re, json, pandas as pd
from pathlib import Path

# Load full Mongo results
mongo_file = Path(var_call_DZv9eU4TmwPmILS2JDPsoZtk)
with mongo_file.open() as f:
    mongo_docs = json.load(f)

# Filter CHI venue papers by searching for typical CHI strings in text (ACM CHI conference)
chi_titles = set()
for doc in mongo_docs:
    text = doc.get('text', '')
    # Look for patterns that strongly indicate CHI venue
    if re.search(r"CHI '\d{2}", text) or 'ACM CHI' in text or 'Conference on Human Factors in Computing Systems' in text:
        filename = doc.get('filename', '')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load citation results
sql_file = Path(var_call_KzOVzWbtjAEZ5sH4CxBwpyLc)
with sql_file.open() as f:
    citations = json.load(f)

# Sum citation counts for records whose titles are in chi_titles, for citation_year=2020 (already filtered in SQL)
# Normalize titles by stripping whitespace
chi_titles_norm = {t.strip(): t for t in chi_titles}

total_citations = 0
for row in citations:
    title = row.get('title', '').strip()
    if title in chi_titles_norm:
        try:
            c = int(row.get('citation_count', 0))
        except ValueError:
            c = 0
        total_citations += c

result = json.dumps(total_citations)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_DZv9eU4TmwPmILS2JDPsoZtk': 'file_storage/call_DZv9eU4TmwPmILS2JDPsoZtk.json', 'var_call_KzOVzWbtjAEZ5sH4CxBwpyLc': 'file_storage/call_KzOVzWbtjAEZ5sH4CxBwpyLc.json'}

exec(code, env_args)
