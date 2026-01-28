code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-8931525846963248243']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Load paper docs
papers_file = locals()['var_function-call-4192422070354728246']
with open(papers_file, 'r') as f:
    papers = json.load(f)

# Map title -> citation_count
# Note: There might be multiple citation records for same title if I didn't filter year properly, 
# but I filtered year=2020 in SQL. So one record per title (or none).
citation_map = {c['title']: c['citation_count'] for c in citations}

total_citations = 0
chi_papers = []

for p in papers:
    # Filename is "Title.txt"
    if not p['filename'].endswith('.txt'):
        continue
    title = p['filename'][:-4]
    
    if title in citation_map:
        text = p['text']
        # Check for CHI venue in the first 1000 characters
        header = text[:1000]
        
        # Patterns for CHI
        # 1. "CHI 'XX" or "CHI 20XX"
        # 2. "Conference on Human Factors in Computing Systems"
        # 3. "CHI Conference"
        # 4. "Proceedings of the ... CHI"
        
        is_chi = False
        if "Conference on Human Factors in Computing Systems" in header:
            is_chi = True
        elif re.search(r"CHI\s*['\u2019]?\d{2}", header, re.IGNORECASE):
            is_chi = True
        elif "CHI Conference" in header:
            is_chi = True
        
        # Check if it matches other venues to avoid false positives?
        # e.g. "Ubicomp", "CSCW", "DIS"
        if is_chi:
            total_citations += citation_map[title]
            chi_papers.append(title)

print("__RESULT__:")
print(json.dumps({"total_citations": total_citations, "chi_paper_count": len(chi_papers), "sample_chi_papers": chi_papers[:5]}))"""

env_args = {'var_function-call-8931525846963248243': 'file_storage/function-call-8931525846963248243.json', 'var_function-call-17301308444494823963': {'count': 188, 'filenames': ['Exploring the Value of Parent Tracked Baby Data in Interactions with Healthcare Professionals: A Data-Enabled Design Exploration.txt', 'SweatAtoms: Materializing Physical Activity.txt', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness.txt', 'Personal Informatics for Sport: Meaning, Body, and Social Relations in Amateur and Elite Athletes.txt', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media.txt', 'Crafting a View of Self-Tracking Data in the Clinical Visit.txt', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms.txt', 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps.txt', 'Sensor Requirements for Activity Recognition on Smart Watches.txt', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations.txt']}, 'var_function-call-6838254019764142939': 'file_storage/function-call-6838254019764142939.json', 'var_function-call-4192422070354728246': 'file_storage/function-call-4192422070354728246.json'}

exec(code, env_args)
