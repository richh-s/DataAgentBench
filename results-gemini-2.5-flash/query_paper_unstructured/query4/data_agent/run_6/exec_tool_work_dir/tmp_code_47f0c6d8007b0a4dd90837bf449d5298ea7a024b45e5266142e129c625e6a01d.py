code = """import json
import re

file_path = locals()['var_function-call-4321601777141184157']
with open(file_path, 'r') as f:
    physical_activity_papers = json.load(f)

filtered_papers_info = []
for paper in physical_activity_papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    # Extract year: look for 'year: YYYY' or 'YYYY' in the context of a conference/journal line
    year_match_strict = re.search(r'year: (\\d{4})', text, re.IGNORECASE)
    year_match_venue = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH) (\\d{4})', text, re.IGNORECASE)

    year = None
    if year_match_strict:
        year = int(year_match_strict.group(1))
    elif year_match_venue:
        year = int(year_match_venue.group(2))

    # Extract domain: look for 'domain: ...' or 'Author Keywords' followed by a list of keywords
    domain_match = re.search(r'domain: ([^\\n]*)', text, re.IGNORECASE)
    author_keywords_match = re.search(r'Author Keywords\\n([^\\n]*)', text, re.IGNORECASE)

    domain = None
    if domain_match:
        domain = domain_match.group(1).strip()
    elif author_keywords_match:
        domain = author_keywords_match.group(1).strip()

    if year == 2016 and domain and 'physical activity' in domain.lower():
        filtered_papers_info.append({'title': title, 'year': year, 'domain': domain})

print('__RESULT__:')
print(json.dumps(filtered_papers_info))"""

env_args = {'var_function-call-3967600453842721378': [], 'var_function-call-8271451008217141183': [], 'var_function-call-5153703013806353214': [], 'var_function-call-12010824351002747580': [], 'var_function-call-4575013761380349714': 'file_storage/function-call-4575013761380349714.json', 'var_function-call-4978139874907222296': [], 'var_function-call-1601887262241212093': [], 'var_function-call-4321601777141184157': 'file_storage/function-call-4321601777141184157.json'}

exec(code, env_args)
