code = """import json
import re
import pandas as pd
from collections import Counter

# Load citations
with open(locals()['var_function-call-15161005825129355678'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])
citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()

# Load papers
with open(locals()['var_function-call-11547214803313997726'], 'r') as f:
    papers_data = json.load(f)

extracted_papers = []

for doc in papers_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Extract Year
    year = None
    
    # Regex for Copyright
    # Looking for patterns like "Copyright 2017" or "© 2017" or "Copyright © 2017"
    copy_matches = re.findall(r'Copyright.*?20(\d{2})', text, re.IGNORECASE)
    if not copy_matches:
        copy_matches = re.findall(r'©.*?20(\d{2})', text)
    
    if copy_matches:
        # Take the most frequent or max? 
        # Usually the copyright year is the publication year.
        # But sometimes references have copyright statements? Unlikely in plain text.
        # Let's take the first one found (top of text usually) or max?
        # Actually, "Copyright 20xx" usually appears in the footer of the first page.
        # The matches in the references list usually look different.
        # Let's try to find "Copyright 20xx" in the first 5000 chars.
        early_matches = re.findall(r'Copyright.*?20(\d{2})', text[:5000], re.IGNORECASE)
        if not early_matches:
             early_matches = re.findall(r'©\s*20(\d{2})', text[:5000])
        
        if early_matches:
            year = 2000 + int(early_matches[0])
    
    # If still no year, check headers
    if not year:
        # CHI '17, UbiComp '18
        header_matches = re.findall(r"[A-Z]{3,}\s+'(\d{2})", text[:1000])
        if header_matches:
            year = 2000 + int(header_matches[0])

    # If still no year, look for "20xx" in the first 500 chars (likely date)
    if not year:
         date_matches = re.findall(r'\b20(\d{2})\b', text[:500])
         if date_matches:
             year = 2000 + int(date_matches[0])
             
    # Contribution Heuristic
    # Prompt says "empirical" is a type.
    text_lower = text.lower()
    is_empirical = False
    
    if "empirical" in text_lower:
        is_empirical = True
    else:
        # Infer from keywords
        # If "participants" and "results" are present, it's likely empirical
        if ("participants" in text_lower or "interview" in text_lower or "survey" in text_lower or "user study" in text_lower) and ("results" in text_lower or "findings" in text_lower):
            is_empirical = True
            
    if year and year > 2016 and is_empirical:
        extracted_papers.append({
            "title": title,
            "year": year
        })

# Join
df_papers = pd.DataFrame(extracted_papers)
if not df_papers.empty:
    result_df = pd.merge(df_papers, citation_sums, on='title', how='inner')
    final_output = result_df[['title', 'citation_count']].to_dict(orient='records')
else:
    final_output = []

final_output = sorted(final_output, key=lambda x: x['citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(final_output))"""

env_args = {'var_function-call-15870197178321181346': 'file_storage/function-call-15870197178321181346.json', 'var_function-call-15870197178321180761': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-5877010014911458978': 'file_storage/function-call-5877010014911458978.json', 'var_function-call-15161005825129355678': 'file_storage/function-call-15161005825129355678.json', 'var_function-call-14023155913287027792': 'file_storage/function-call-14023155913287027792.json', 'var_function-call-14333893458989342011': [], 'var_function-call-16530110269305427312': [{'title': "Everybody Knows What You'Re Doing: A Critical Design Approach to Personal Informatics", 'total_citations': '694'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'total_citations': '595'}, {'title': 'See Friendship, Sort of: How Conversation and Digital Traces Might Support Reflection on Friendships', 'total_citations': '593'}, {'title': 'Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'total_citations': '587'}], 'var_function-call-11547214803313997726': 'file_storage/function-call-11547214803313997726.json', 'var_function-call-4200250418715985286': [], 'var_function-call-1245089211776131836': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'extracted_year': None, 'has_empirical': False, 'text_preview': 'Beyond Abandonment to Next Steps: Understanding and \nDesigning for Life after Personal Informatics Tool Use \n\nDaniel A. Epstein1, Monica Caraway2, Chuck Johnston2, \nAn Ping2, James Fogarty1, Sean A. M'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'extracted_year': None, 'has_empirical': False, 'text_preview': 'Contextual Influences on the Use and Non-Use of Digital \nTechnology While Exercising at the Gym \n\nMisha Patel \nFoolproof and University College London \nLondon, United Kingdom \nmisha.patel@foolproof.co'}]}

exec(code, env_args)
