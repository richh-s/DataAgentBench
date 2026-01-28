code = """import json
import re

paper_docs_file_path = locals()['var_function-call-6544619829393036365']

with open(paper_docs_file_path, 'r') as f:
    paper_docs = json.load(f)

extracted_papers_titles = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    # More robust year extraction:
    year = None
    # Search for year patterns (e.g., '2016', 'CHI '16') within the first 1000 characters
    year_matches = re.findall(r'\b(19|20)\d{2}\b', text[:1000])
    if year_matches:
        # Prioritize years that are typically publication years and appear early
        for potential_year_str in year_matches:
            potential_year = int(potential_year_str)
            if 2000 <= potential_year <= 2023:  # Assume reasonable publication year range
                year = potential_year
                break # Take the first reasonable year found early
    
    # Fallback for years in 'ACM X 'YY' or similar patterns
    if not year:
        conference_year_match = re.search(r'\b(ACM|CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*\'(\d{2})\b', text, re.IGNORECASE)
        if conference_year_match:
            century = 2000 if int(conference_year_match.group(2)) < 50 else 1900 # Heuristic for century
            year = century + int(conference_year_match.group(2))

    # Check for 'physical activity' domain within the entire text
    is_physical_activity = 'physical activity' in text.lower()

    if year == 2016 and is_physical_activity:
        extracted_papers_titles.append(title)

print("__RESULT__:")
print(json.dumps(extracted_papers_titles))"""

env_args = {'var_function-call-17463833612075543362': ['paper_docs'], 'var_function-call-6544619829393036365': 'file_storage/function-call-6544619829393036365.json', 'var_function-call-15282443211329679729': [], 'var_function-call-3755615379006169032': ['Citations', 'sqlite_sequence'], 'var_function-call-8085450063270148717': []}

exec(code, env_args)
