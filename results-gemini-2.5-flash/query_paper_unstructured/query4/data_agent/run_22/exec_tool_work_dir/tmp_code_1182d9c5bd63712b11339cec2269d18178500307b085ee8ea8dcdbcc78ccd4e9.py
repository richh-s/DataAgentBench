code = """import json
import re

paper_docs_file_path = locals()['var_function-call-6544619829393036365']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_titles_for_2016_physical_activity = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # --- Year Extraction ---
    # Prioritize years that appear early in the document (first 1000 chars)
    # and are within a reasonable publication range (e.g., 1990-2023)
    year = None
    potential_years = re.findall(r'\b(19|20)\d{2}\b', text[:1000])
    for py_str in potential_years:
        py = int(py_str)
        if 1990 <= py <= 2023:
            year = py
            break # Take the first plausible year found early

    # If no year found in the first 1000 chars, try the whole text but still prioritize plausible years
    if year is None:
        potential_years_full = re.findall(r'\b(19|20)\d{2}\b', text)
        for py_str in potential_years_full:
            py = int(py_str)
            if 1990 <= py <= 2023:
                year = py
                break

    # Also look for common conference/journal year patterns if a year is still not found
    if year is None:
        # Escaping the single quote for the code argument. This regex searches for patterns like "CHI '16"
        conf_year_match = re.search(r'\b(ACM|CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*\'\'\'(\d{2})\b', text, re.IGNORECASE)
        if conf_year_match:
            short_year = int(conf_year_match.group(2))
            # Heuristic for century: if 'YY' < 50, assume 20YY, otherwise 19YY
            century = 2000 if short_year < 50 else 1900
            year = century + short_year

    # --- Domain Extraction ---
    # Check for 'physical activity' explicitly in the text
    is_physical_activity_domain = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity_domain:
        extracted_titles_for_2016_physical_activity.append(title)

print("__RESULT__:")
print(json.dumps(extracted_titles_for_2016_physical_activity))"""

env_args = {'var_function-call-17463833612075543362': ['paper_docs'], 'var_function-call-6544619829393036365': 'file_storage/function-call-6544619829393036365.json', 'var_function-call-15282443211329679729': [], 'var_function-call-3755615379006169032': ['Citations', 'sqlite_sequence'], 'var_function-call-8085450063270148717': []}

exec(code, env_args)
