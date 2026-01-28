code = """import json
import pandas as pd
import re

# Load Citations
with open(locals()['var_function-call-10263286268720561281'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
# Convert citation_count to int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
# Sum citations by title
citation_sums = df_citations.groupby('title')['citation_count'].sum().to_dict()

# Load Paper Docs Candidates
with open(locals()['var_function-call-4190209602007516202'], 'r') as f:
    papers = json.load(f)

results = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Check for "physical activity" (already filtered by Mongo, but good to be sure if case sensitivity matters)
    # Mongo regex was case insensitive, so it's fine.
    
    # Extract Year
    # Heuristic: Look for years in the first 500 characters
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    # Also check for 'YY format if 4-digit not found or to supplement?
    # e.g. "UbiComp '16"
    short_years = re.findall(r"'\d{2}", header) # matches '16
    
    pub_year = None
    
    # Logic: 
    # If 2016 is in years, checks if it's the primary one.
    # Often the first year is the conference year.
    # However, sometimes there are years in email addresses or other things? Unlikely.
    # If 2016 is the first year found, assume 2016.
    
    if years:
        first_year = int(years[0])
        if first_year == 2016:
            pub_year = 2016
        else:
            # If first year is not 2016, maybe it's 2015 (published 2015).
            # If 2016 appears later in header?
            # E.g. "Copyright 2016".
            # If 2016 is in the list of years found in header, and no later year (2017+) is found before it?
            if 2016 in [int(y) for y in years]:
                # If 2016 is present, it might be the year. 
                # But if 2015 is first, it might be a 2015 paper.
                # Let's look at the context of 2016.
                # Simplification: If "2016" is in the first 300 characters, it's very likely the year.
                if "2016" in header[:300]:
                    pub_year = 2016
                else:
                    # check if '16 is there
                    pass
    
    # Check for short year '16 if 2016 not found
    if not pub_year:
        # Check for specific conference patterns: "CHI '16", "UbiComp '16"
        if re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|MobileHCI|PervasiveHealth|WWW)\s*'?16", header, re.IGNORECASE):
            pub_year = 2016
            
    # Final check
    if pub_year == 2016:
        # Check if title is in citations
        # Title matching: exact match expected as per hints
        total_cites = citation_sums.get(title, 0)
        
        # Add to results
        results.append({
            "title": title,
            "total_citation_count": total_cites
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-4042789943322229169': ['paper_docs'], 'var_function-call-4042789943322227422': ['Citations', 'sqlite_sequence'], 'var_function-call-12606358993077835147': 'file_storage/function-call-12606358993077835147.json', 'var_function-call-9821348660880975822': 'file_storage/function-call-9821348660880975822.json', 'var_function-call-10263286268720561281': 'file_storage/function-call-10263286268720561281.json', 'var_function-call-4190209602007516202': 'file_storage/function-call-4190209602007516202.json'}

exec(code, env_args)
