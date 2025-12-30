code = """import json
import re

# Load the paper_docs result
# Since the previous result was stored in a file, I need to read it.
# The variable name is var_function-call-1634184987777097794 (from the second query which returned a large result)
# Wait, the second query was {"count": true} but returned a list of docs.
# The variable name for that is var_function-call-1634184987777097794.

try:
    with open(locals()['var_function-call-1634184987777097794'], 'r') as f:
        papers = json.load(f)
except Exception as e:
    # Fallback to the first query variable if the second one was invalid, but the second one produced a file so it should be fine.
    # The first query was limit 1.
    papers = []
    print(f"Error reading file: {e}")

extracted_data = []

for paper in papers:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
    # Pattern: \b20[12]\d\b
    # We want publication year. Usually in the first few lines.
    # Let's take the first 500 characters.
    header = text[:1000]
    years = re.findall(r'\b(20\d{2})\b', header)
    
    # Heuristic: The publication year is likely the first year found, or the one appearing in a venue line.
    # Often venue lines are like "CHI '17" or "CHI 2017".
    # If we find " '17 ", it corresponds to 2017.
    # Let's look for "2017", "2018", etc.
    # Filter years to be reasonable (e.g., 2000-2024).
    valid_years = [int(y) for y in years if 2000 <= int(y) <= 2024]
    
    # Also look for 'YY pattern (e.g. '17, '18, '19, '20)
    # Be careful with '15 meaning 2015.
    short_years = re.findall(r"\b'([12]\d)\b", header)
    for sy in short_years:
        valid_years.append(2000 + int(sy))
        
    if valid_years:
        # Most frequent or first?
        # Usually the first one is the conference year.
        year = valid_years[0]
    else:
        year = None

    # Check contribution
    # We need "empirical".
    # Let's search for "empirical" in the text (case insensitive).
    # Since the hint says "use substring/contains matching since values may be part of a list", 
    # it implies if "empirical" is mentioned, it might be the contribution.
    # But we want to be sure it's the contribution type. 
    # However, without better structure, "contains 'empirical'" is the best bet.
    is_empirical = 'empirical' in text.lower()
    
    if year and year > 2016 and is_empirical:
        extracted_data.append(title)

print("__RESULT__:")
print(json.dumps(extracted_data))"""

env_args = {'var_function-call-4642845267965044101': ['paper_docs'], 'var_function-call-4642845267965042778': ['Citations', 'sqlite_sequence'], 'var_function-call-10467492128798022417': 'file_storage/function-call-10467492128798022417.json', 'var_function-call-1634184987777097794': 'file_storage/function-call-1634184987777097794.json'}

exec(code, env_args)
