code = """import json
import re

citations_path = locals()['var_function-call-14128661174357449322']
papers_path = locals()['var_function-call-2576569028969272389'] # Use the larger file

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_counts = {}
for row in citations_data:
    t = row['title']
    c = int(row['citation_count'])
    citation_counts[t] = citation_counts.get(t, 0) + c

with open(papers_path, 'r') as f:
    papers_data = json.load(f)

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    text = paper.get('text', '')
    
    # Domain check
    if 'physical activity' not in text.lower():
        continue

    # Year check
    # Heuristics:
    # 1. Look for 'Copyright 2016' or '(c) 2016' or '© 2016'
    # 2. Look for conference acronym + '16 or 2016 in first 1000 chars.
    # 3. Look for 'Published in 2016' or similar.
    
    is_2016 = False
    
    # Check Copyright/Header in first 3000 chars (header/footer usually there)
    header_text = text[:3000]
    
    if re.search(r'Copyright\s*(©|\(c\))?\s*2016', header_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b(CHI|UbiComp|CSCW|DIS|TEI|PervasiveHealth|WWW|IUI|OzCHI|AH|MobileHCI|ISWC)\s*['’]16", header_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b(CHI|UbiComp|CSCW|DIS|TEI|PervasiveHealth|WWW|IUI|OzCHI|AH|MobileHCI|ISWC)\s*2016", header_text, re.IGNORECASE):
        is_2016 = True
    elif '2016' in header_text:
        # Fallback: if 2016 is in header but no "2017" or later
        if not any(y in header_text for y in ['2017', '2018', '2019', '2020']):
             # Stronger check: is it "September 2016" or similar?
             if re.search(r'(January|February|March|April|May|June|July|August|September|October|November|December)\s*\d{1,2}.*2016', header_text, re.IGNORECASE):
                 is_2016 = True
             elif re.search(r'2016\s*(January|February|March|April|May|June|July|August|September|October|November|December)', header_text, re.IGNORECASE):
                 is_2016 = True
             # If just "2016" alone, it's risky but might be the only indicator.
             # Let's check if the title is in citations. If so, and we found 2016, maybe it's correct.
             # But let's be conservative. If "2016" is the *only* year in header, it's a good guess.
             elif header_text.count('2016') > 0 and not re.search(r'20\d{2}', header_text.replace('2016', '')):
                 is_2016 = True
             # Check for "Permission to make ... 2016"
             elif "2016" in header_text and "Permission" in header_text:
                 is_2016 = True

    if is_2016:
        count = citation_counts.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-2089186070141819768': 'file_storage/function-call-2089186070141819768.json', 'var_function-call-17809202052441850212': 'file_storage/function-call-17809202052441850212.json', 'var_function-call-17961397819046338500': [{'count(*)': '1405'}], 'var_function-call-2833110841078300927': 'file_storage/function-call-2833110841078300927.json', 'var_function-call-14128661174357449322': 'file_storage/function-call-14128661174357449322.json', 'var_function-call-14339253743603628220': [], 'var_function-call-15019217085141925878': {'total_papers': 5, 'domain_match_count': 4, 'sample_headers': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali', 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E']}, 'var_function-call-2576569028969272389': 'file_storage/function-call-2576569028969272389.json'}

exec(code, env_args)
