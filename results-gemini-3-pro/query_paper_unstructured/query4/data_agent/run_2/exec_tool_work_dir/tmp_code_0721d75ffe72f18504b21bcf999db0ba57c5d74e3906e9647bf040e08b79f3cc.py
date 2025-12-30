code = """import json
import re

# Load the large result from the file
file_path = locals()['var_function-call-332077821725117771']
with open(file_path, 'r') as f:
    docs = json.load(f)

titles_2016 = []

for doc in docs:
    text = doc['text']
    filename = doc['filename']
    
    # Check for Year 2016
    # Look in the first 2000 characters for header/copyright info
    header_text = text[:2000]
    
    # Patterns for 2016
    # 1. Conference headers often have "VENUE 'YY" or "VENUE 20YY"
    #    e.g., CHI '16, CHI 2016, UbiComp '16, UbiComp 2016
    # 2. Copyright statements: Copyright 2016, (c) 2016
    # 3. Dates: Month ... 2016
    
    is_2016 = False
    
    # Regex for conference headers
    if re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|WWW|OzCHI|TEI|AH|UIST|MobileHCI)\s*['\u2019]?16", header_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|WWW|OzCHI|TEI|AH|UIST|MobileHCI).*?2016", header_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"Copyright\s*(©|\(c\)|@)?\s*2016", header_text, re.IGNORECASE):
        is_2016 = True
    elif re.search(r"\b2016\b", header_text): 
        # Fallback: if 2016 appears in first 500 chars (likely header/copyright)
        if text.find("2016") < 500:
            is_2016 = True
            
    # Explicitly exclude if it looks like a different year
    # e.g., if "CHI '18" is found, it's not 2016, even if "2016" is in the text
    if re.search(r"(CHI|UbiComp|CSCW|DIS|IUI|PervasiveHealth|WWW|OzCHI|TEI|AH|UIST|MobileHCI)\s*['\u2019]?(15|17|18|19|20|14)", header_text, re.IGNORECASE):
        # Double check: if it has BOTH (e.g. workshop 2016 paper in 2017 proceedings - unlikely), but usually if '18 is there, it's 2018.
        # However, checking for "Copyright 2016" is a strong indicator.
        # Let's rely on the positive match for 2016 first.
        # If we found 2016 but also 2018, we might want to discard.
        # But let's assume the Positive match for specific 2016 patterns is good.
        pass
        
    if is_2016:
        # Check domain "physical activity"
        # The filter already ensured "physical activity" is in the text.
        # But let's verify it's not just a passing mention?
        # The prompt says "matching domains... use substring/contains".
        # This implies simple containment is enough.
        if "physical activity" in text.lower():
            title = filename.replace('.txt', '')
            titles_2016.append(title)

print("__RESULT__:")
print(json.dumps(titles_2016))"""

env_args = {'var_function-call-13901959142060692971': 'file_storage/function-call-13901959142060692971.json', 'var_function-call-1843899810838592799': 'file_storage/function-call-1843899810838592799.json', 'var_function-call-332077821725117771': 'file_storage/function-call-332077821725117771.json'}

exec(code, env_args)
