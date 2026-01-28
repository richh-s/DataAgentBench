code = """import pandas as pd
import json
import re

file_path = locals()['var_function-call-4813969159932217082']

with open(file_path, 'r') as f:
    mongo_docs = json.load(f)

papers_data = []
for doc in mongo_docs:
    filename = doc['filename']
    text = doc['text']

    title = filename.replace('.txt', '')

    year = None
    # Try to find year from patterns like "YYYY" in "UbiComp '15, SEPTEMBER 7-11, 2015" or "Copyright 2015"
    year_match_copyright = re.search(r"Copyright\s+\d{4}", text)
    if year_match_copyright:
        year = int(year_match_copyright.group().split()[-1])
    else:
        year_match_conf = re.search(r"\d{4}[,]\s+(JANUARY|FEBRUARY|MARCH|APRIL|MAY|JUNE|JULY|AUGUST|SEPTEMBER|OCTOBER|NOVEMBER|DECEMBER)", text, re.IGNORECASE)
        if year_match_conf:
            year = int(year_match_conf.group().split(',')[0])
        else:
            year_match_conf_alt = re.search(r"(?:'|\b)\d{2}(?:\b)", text) # e.g. '15 for 2015
            if year_match_conf_alt:
                # Add 2000 to get the full year
                year = 2000 + int(year_match_conf_alt.group().replace("'", ""))


    domain = 'physical activity' if 'physical activity' in text.lower() else None

    if year is not None and domain == 'physical activity' and year == 2016:
        papers_data.append({'title': title, 'year': year, 'domain': domain})

filtered_papers_df = pd.DataFrame(papers_data)
print('__RESULT__:')
print(filtered_papers_df.to_json(orient='records'))"""

env_args = {'var_function-call-3869615726933000262': ['paper_docs'], 'var_function-call-4813969159932217082': 'file_storage/function-call-4813969159932217082.json'}

exec(code, env_args)
