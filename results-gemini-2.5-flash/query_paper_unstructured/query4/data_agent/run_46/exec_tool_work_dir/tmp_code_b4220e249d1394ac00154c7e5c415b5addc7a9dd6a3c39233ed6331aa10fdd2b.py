code = """import json
import re

file_path = locals()['var_function-call-3558235726139819418']

with open(file_path, 'r') as f:
    paper_docs = json.load(f)

papers_titles_and_years = []
for doc in paper_docs:
    title = doc['filename'].replace('.txt', '')
    text = doc['text']

    # Check if 'physical activity' is in the entire text, case-insensitive
    if "physical activity" in text.lower():
        year = None
        # Look for common patterns of year in academic papers, prioritizing closer to the beginning
        # Pattern 1: Year in a conference/journal header, e.g., 'CHI '16', 'UbiComp 2016'
        year_match_header = re.search(r'\b(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH) \'?(\d{2})\b', text, re.IGNORECASE)
        if year_match_header:
            two_digit_year = int(year_match_header.group(1))
            year = 2000 + two_digit_year # Assuming 21st century
        else:
            # Pattern 2: Four digit year (e.g., 2016) often appearing in copyright or date lines
            four_digit_year_matches = re.findall(r'\b(19|20)\d{2}\b', text[:min(len(text), 1500)]) # Limit search to first 1500 chars
            if four_digit_year_matches:
                # Get the first full 4-digit year found
                year = int(four_digit_year_matches[0]) # re.findall returns list of tuples, so take first element of the first tuple
                # If the regex was r'\\b((?:19|20)\\d{2})\\b', then it would be int(four_digit_year_matches[0])
                # With r'\\b(19|20)(\\d{2})\\b', it would be int(four_digit_year_matches[0][0] + four_digit_year_matches[0][1])
                # Correcting to match the full year: using r'\\b((?:19|20)\\d{2})\\b'
                year_match_full = re.search(r'\b((?:19|20)\d{2})\b', text[:min(len(text), 1500)])
                if year_match_full:
                    year = int(year_match_full.group(1))

        if year == 2016: # Filter for papers published in 2016
            papers_titles_and_years.append({'title': title, 'year': year})

print("__RESULT__:")
print(json.dumps(papers_titles_and_years))"""

env_args = {'var_function-call-8630541941916938296': ['paper_docs'], 'var_function-call-3558235726139819418': 'file_storage/function-call-3558235726139819418.json', 'var_function-call-3135368326337721740': [], 'var_function-call-16744607929935420672': [], 'var_function-call-2945847925733583850': [], 'var_function-call-1383064261380446342': [], 'var_function-call-5306735185744050093': [], 'var_function-call-15853859611646052612': []}

exec(code, env_args)
