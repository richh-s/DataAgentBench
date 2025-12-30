code = """import json
import re

paper_docs_data = json.load(open(locals()['var_function-call-2625422400010944557'], 'r'))

parsed_papers = []

for doc in paper_docs_data:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')
    
    # Extract year
    year = None
    # Try to find year from conference pattern like 'UBICOMP 'YY'
    venue_year_match = re.search('(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\\s*\'(\\d{2})', text, re.IGNORECASE)
    if venue_year_match:
        year = int('20' + venue_year_match.group(1))
    else:
        # Try to find year from 'Copyright YYYY' or '© YYYY'
        copyright_year_match = re.search('Copyright\\s*\\d{4}\\s*\\u00a9\\s*|Copyright\\s*\\u00a9\\s*(\\d{4})', text, re.IGNORECASE)
        if copyright_year_match:
            year = int(copyright_year_match.group(1))
        else:
            # Try to find year directly in the first 500 characters
            direct_year_match = re.search('\\b(20\\d{2})\\b', text[:500])
            if direct_year_match:
                year = int(direct_year_match.group(1))

    # Extract contribution type
    contribution = None
    contribution_keywords = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    
    # Look for "contribution" section or keywords in the abstract/introduction
    # Search for "contribution" near the beginning of the paper
    contribution_section_match = re.search('\\b(CONTRIBUTIONS|CONTRIBUTION)\\b.*?((?:empirical|artifact|theoretical|survey|methodological).*?)(?:\\n\\n|\\Z)', text, re.DOTALL | re.IGNORECASE)

    if contribution_section_match:
        contribution_text = contribution_section_match.group(2)
        for keyword in contribution_keywords:
            if re.search('\\b' + re.escape(keyword) + '\\b', contribution_text, re.IGNORECASE):
                contribution = keyword
                break
    
    if contribution is None:
        # If no explicit contribution section, search throughout the text, prioritizing "empirical"
        if re.search('\\bempirical\\b', text, re.IGNORECASE):
            contribution = "empirical"
        else:
            for keyword in contribution_keywords:
                if re.search('\\b' + re.escape(keyword) + '\\b', text, re.IGNORECASE):
                    contribution = keyword
                    break

    parsed_papers.append({
        'title': title,
        'year': year,
        'contribution': contribution
    })

# Filter papers based on the criteria
filtered_papers = [
    p for p in parsed_papers
    if p['contribution'] == 'empirical' and p['year'] and p['year'] > 2016
]

# Convert to JSON string
result = json.dumps(filtered_papers)

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-13732734259648990433': ['paper_docs'], 'var_function-call-2625422400010944557': 'file_storage/function-call-2625422400010944557.json'}

exec(code, env_args)
