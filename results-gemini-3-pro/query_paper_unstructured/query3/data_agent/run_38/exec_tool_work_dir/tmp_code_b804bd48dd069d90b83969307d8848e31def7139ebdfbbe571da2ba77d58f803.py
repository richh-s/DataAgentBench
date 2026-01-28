code = """import json
import re

# Load papers (limit to 20 for inspection)
with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    all_papers = json.load(f)

print(f"Total papers: {len(all_papers)}")

print("--- Inspecting Metadata Formats ---")
for paper in all_papers[:20]:
    text = paper['text']
    filename = paper['filename']
    print(f"\nPaper: {filename}")
    
    # Check first few lines for Year/Venue
    print("Header lines:")
    lines = text.split('\n')
    for line in lines[:5]:
        if line.strip():
            print(f"  {line.strip()}")
            
    # Check for "Contribution" or "Domain" keywords in the whole text
    # We look for lines that look like fields
    for line in lines:
        if "contribution" in line.lower() and ":" in line:
            print(f"  Possible Contribution Line: {line.strip()}")
        if "domain" in line.lower() and ":" in line:
            print(f"  Possible Domain Line: {line.strip()}")
            
    # Check for Year
    # specific regex for typical venues
    venue_match = re.search(r'\b(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)[\s\S]{0,20}\b(20\d\d)\b', text, re.IGNORECASE)
    if venue_match:
        print(f"  Found Venue/Year: {venue_match.group(0)}")
    else:
        # Just find first 20xx
        y_match = re.search(r'\b20\d\d\b', text[:1000])
        if y_match:
             print(f"  Found Year (fallback): {y_match.group(0)}")"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json'}

exec(code, env_args)
