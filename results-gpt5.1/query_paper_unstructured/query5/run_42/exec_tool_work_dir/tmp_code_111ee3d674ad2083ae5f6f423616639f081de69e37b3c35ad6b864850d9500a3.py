code = """import re, json
from pathlib import Path

# Load full Mongo result
mongo_path = Path(var_call_UbI1HkqiBv58X3RrtwahaDnr)
import pandas as pd
mongo_records = pd.read_json(mongo_path).to_dict(orient='records')

# Identify CHI papers by searching for 'CHI' near 'Conference' or ACM CHI formatting in text
chi_titles = set()
for doc in mongo_records:
    text = doc.get('text','')
    # Heuristic: look for 'CHI ' followed by year, or 'In Proceedings of the SIGCHI' etc.
    if re.search(r"CHI '\d{2}|CHI [12][09]\d{2}|SIGCHI|Conference on Human Factors in Computing Systems", text, re.IGNORECASE):
        filename = doc.get('filename','')
        if filename.lower().endswith('.txt'):
            title = filename[:-4]
        else:
            title = filename
        chi_titles.add(title)

# Load citation records for 2020
sql_path = Path(var_call_DdvCWGcXConUMQgzBQMl5M2Y)
sql_df = pd.read_json(sql_path)

# Normalize titles
sql_df['norm_title'] = sql_df['title'].str.strip()
chi_norm = {t.strip() for t in chi_titles}

# Filter to CHI papers
chi_citations_2020 = sql_df[sql_df['norm_title'].isin(chi_norm)]

# Sum citation counts (ensure int)
chi_citations_2020['citation_count'] = chi_citations_2020['citation_count'].astype(int)
Total = int(chi_citations_2020['citation_count'].sum())

result = {"total_citations_2020_for_CHI_papers": Total, "matched_paper_count": int(len(chi_citations_2020)), "chi_title_count_detected": int(len(chi_titles))}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_UbI1HkqiBv58X3RrtwahaDnr': 'file_storage/call_UbI1HkqiBv58X3RrtwahaDnr.json', 'var_call_DdvCWGcXConUMQgzBQMl5M2Y': 'file_storage/call_DdvCWGcXConUMQgzBQMl5M2Y.json'}

exec(code, env_args)
