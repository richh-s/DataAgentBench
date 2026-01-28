code = """import json
import re

# Load citations
with open(locals()['var_function-call-12774124181016146207'], 'r') as f:
    citations_data = json.load(f)

# Aggregate citations by title
citation_map = {}
for entry in citations_data:
    title = entry['title'].strip()
    # Normalize title? The filename doesn't have special chars usually, but sqlite might.
    # We will match exactly or case-insensitive if needed.
    # Let's keep a map of lower-case title to citations just in case
    citation_map[title.lower()] = citation_map.get(title.lower(), 0) + int(entry['citation_count'])

# Load papers
with open(locals()['var_function-call-13170612458633614498'], 'r') as f:
    papers_data = json.load(f)

total_citations = 0
matched_papers = []

for p in papers_data:
    filename = p['filename']
    title = filename.replace('.txt', '').strip()
    title_lower = title.lower()
    text_lower = p['text'].lower()
    
    is_food = False
    
    # 1. Check Title for "food"
    if 'food' in title_lower:
        is_food = True
    
    # 2. Check Keywords for "food"
    if not is_food:
        # Find keywords block
        # We look for "author keywords" or "keywords" or "index terms"
        # Then grab a chunk of text
        match = re.search(r'(author keywords|keywords|index terms)', text_lower)
        if match:
            start_idx = match.start()
            # Look ahead until we hit a likely next section header like "introduction", "abstract" (if after), "acm classification", "general terms"
            # Or just take 500 chars
            snippet = text_lower[start_idx:start_idx+1000]
            # Verify "food" is in this snippet
            if 'food' in snippet:
                # We should be careful not to match "food" in the next section's text if the snippet is too long.
                # But typically keywords are short.
                # Let's try to refine the end of the snippet.
                # Split by double newline?
                parts = snippet.split('\n\n')
                # Usually keywords are in the first paragraph after the header.
                keywords_para = parts[0] 
                if len(keywords_para) < 50: # If the header is on one line and keywords on next
                    if len(parts) > 1:
                        keywords_para += " " + parts[1]
                
                if 'food' in keywords_para:
                    is_food = True

    if is_food:
        citations = citation_map.get(title_lower, 0)
        total_citations += citations
        matched_papers.append({"title": title, "citations": citations})

print(f"Matched {len(matched_papers)} papers.")
for mp in matched_papers:
    print(f"- {mp['title']}: {mp['citations']}")

print("__RESULT__:")
print(json.dumps(str(total_citations)))"""

env_args = {'var_function-call-2229407460365091455': 'file_storage/function-call-2229407460365091455.json', 'var_function-call-12774124181016146207': 'file_storage/function-call-12774124181016146207.json', 'var_function-call-12774124181016147194': 'file_storage/function-call-12774124181016147194.json', 'var_function-call-12375458960310420055': '0', 'var_function-call-10051261772612968329': 'done', 'var_function-call-10959694939226740713': {'count': 3, 'examples': ['--- Match in: A Lived Informatics Model of Personal Informatics.txt --- Context: ...r  tracking  location  [24,30],  finances  [20],  food  [11],  weight  [19,25],  and  physical  acti...', '--- Match in: A Stage-based Model of Personal Informatics Systems.txt --- Context: ...projects  on  her  personal  behavior,  such  as  food  consumption  and  sneezes  (http://ellieharr...', '--- Match in: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt --- Context: ...sist  of  avoiding  bladder  irritants  (certain  food  and  drinks)  and  consuming  a  proper  amo...']}, 'var_function-call-4866543357424117340': ['--- File: A Lived Informatics Model of Personal Informatics.txt --- Keywords Section: Author Keywords  Lived Informatics; Personal Informatics; Self-Tracking;  Lapsing; Physical Activity; Finances; Location.   ACM Classification Keywords  H.5.m. Information interfaces and presentation (e.g., HCI).   INTRODUCTION  Personal informatics, or collecting and reflecting on personal  informa', '--- File: A Stage-based Model of Personal Informatics Systems.txt --- Keywords Section: Author Keywords  Personal informatics, collection, reflection, model, barriers   ACM Classification Keywords  H5.m.  Information  interfaces  and  presentation  (e.g.,  HCI):  Miscellaneous.    General Terms  Design, Human Factors   INTRODUCTION AND MOTIVATION  The  importance  of  knowing  oneself ', '--- File: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt --- Keywords Section: KEYWORDS  Mobile  Health  Applications;  Assistive  Technology;  Co-Design;  Interviews; Usability; Overactive Bladder   ACM Reference format:   Ana-Maria  Salai  and  Lynne  Baillie.  2019.  A  Wee  Bit  More  Interaction:  Designing  and  Evaluating  an  Overactive  Bladder  App.  In  2019  CHI  C'], 'var_function-call-11110012245174004178': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-8695831653977518594': 'file_storage/function-call-8695831653977518594.json', 'var_function-call-13170612458633614498': 'file_storage/function-call-13170612458633614498.json'}

exec(code, env_args)
