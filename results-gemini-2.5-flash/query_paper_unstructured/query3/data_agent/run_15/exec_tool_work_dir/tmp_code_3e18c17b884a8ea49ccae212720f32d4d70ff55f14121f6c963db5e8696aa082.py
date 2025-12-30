code = """import json
import re

file_path = locals()['var_function-call-15714299474452988754']

with open(file_path, 'r') as f:
    papers_data = json.load(f)

extracted_papers = []

for paper in papers_data:
    filename = paper['filename']
    text = paper['text']

    title = filename.replace('.txt', '')
    year = None
    contribution = None

    # Extract year
    year_match_1 = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*['’]\s*(\d{2})", text, re.IGNORECASE)
    year_match_2 = re.search(r"(\d{4})", text) # General four digit year search
    if year_match_1:
        year_str = year_match_1.group(1)
        year = int("20" + year_str) if int(year_str) <= 99 else int("19" + year_str) # Assuming 2-digit years are for 20xx or 19xx
    elif year_match_2:
        # Heuristic: Find the earliest year in the first 5000 characters and consider it the publication year.
        all_years = re.findall(r"(\d{4})", text[:5000])
        if all_years:
            potential_years = [int(y) for y in all_years if 1900 < int(y) < 2030] # Filter for reasonable year ranges
            if potential_years:
                year = min(potential_years)

    # Extract contribution - looking for 'contribution:' or 'contribution type:'
    contribution_match = re.search(r"contribution(?:s)?[:\s].*?(empirical|artifact|theoretical|survey|methodological)", text, re.IGNORECASE)
    if contribution_match:
        contribution = contribution_match.group(1).lower()
    else: # Fallback to search within abstract/introduction
        abstract_intro_match = re.search(r"(abstract|introduction).*?(empirical|artifact|theoretical|survey|methodological)", text, re.IGNORECASE | re.DOTALL)
        if abstract_intro_match:
            contribution = abstract_intro_match.group(2).lower()


    if year and contribution: # Only include if both are found
        extracted_papers.append({
            'title': title,
            'year': year,
            'contribution': contribution
        })

# Filter for 'empirical' contribution and year > 2016
filtered_papers = [
    p for p in extracted_papers
    if p['contribution'] == 'empirical' and p['year'] > 2016
]

# Get titles of filtered papers
filtered_titles = [p['title'] for p in filtered_papers]

print('__RESULT__:')
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-7820274075231447229': ['paper_docs'], 'var_function-call-15714299474452988754': 'file_storage/function-call-15714299474452988754.json'}

exec(code, env_args)
