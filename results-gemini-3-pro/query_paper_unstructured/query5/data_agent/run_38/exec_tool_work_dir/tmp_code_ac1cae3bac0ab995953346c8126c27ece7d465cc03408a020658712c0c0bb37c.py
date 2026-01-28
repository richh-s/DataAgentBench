code = """import json
import re

# Load citations
citations_file = locals()['var_function-call-937877723818181910']
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Map title -> count
citations_map = {}
for entry in citations_data:
    citations_map[entry['title']] = int(entry['citation_count'])

# Load papers
papers_file = locals()['var_function-call-969729150992964353']
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

# Map title -> text header
papers_map = {}
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    papers_map[title] = paper.get('text', '')[:3000] # Get first 3000 chars

print(f"Loaded {len(citations_map)} citations.")
print(f"Loaded {len(papers_map)} papers.")

# Regex for CHI
chi_patterns = [
    r"CHI\s+'\d{2}",
    r"CHI\s+20\d{2}",
    r"CHI\s+Conference",
    r"Conference on Human Factors in Computing Systems",
    r"Proceedings of the \d{4} CHI Conference"
]
compiled_patterns = [re.compile(p, re.IGNORECASE) for p in chi_patterns]

total_citations = 0
matched_papers_count = 0
chi_papers_found = 0

debug_missing = []

for title, count in citations_map.items():
    if title in papers_map:
        header = papers_map[title]
        is_chi = False
        for p in compiled_patterns:
            if p.search(header):
                is_chi = True
                break
        
        if is_chi:
            total_citations += count
            chi_papers_found += 1
        else:
            # Check if maybe the venue is CHI but regex missed it?
            # Or it's another venue.
            pass
        matched_papers_count += 1
    else:
        debug_missing.append(title)

print(f"Matched {matched_papers_count} papers from citations list in papers database.")
print(f"Found {chi_papers_found} CHI papers among them.")
print(f"Total citation count for CHI papers: {total_citations}")
print(f"Missing {len(debug_missing)} papers.")
if len(debug_missing) > 0:
    print(f"Example missing: {debug_missing[:3]}")

print("__RESULT__:")
print(json.dumps(total_citations))"""

env_args = {'var_function-call-937877723818181910': 'file_storage/function-call-937877723818181910.json', 'var_function-call-937877723818184371': 'file_storage/function-call-937877723818184371.json', 'var_function-call-5956507868376137751': 'file_storage/function-call-5956507868376137751.json', 'var_function-call-4834077622578291638': 'file_storage/function-call-4834077622578291638.json', 'var_function-call-13589113433172976096': 16, 'var_function-call-17003770300273918978': 'debug', 'var_function-call-14870899513098521614': {'citations_count': 188, 'papers_count': 5, 'intersection_all': 4, 'chi_count': 1, 'intersection_chi': 1, 'sample_citations': ['Personal Tracking of Screen Time on Digital Devices', 'EdiPulse: Investigating a Playful Approach to Self-monitoring Through 3D Printed Chocolate Treats', 'Armbeta: Towards Accessible Wearable Technology to Quantify Upper Limb Movement and Activities'], 'sample_papers': ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems'], 'sample_chi': ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}, 'var_function-call-969729150992964353': 'file_storage/function-call-969729150992964353.json'}

exec(code, env_args)
