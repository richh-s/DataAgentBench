code = """import json, re
# var_call_VNEvq032PXm1hSsPWSIEbAc4 is the storage key containing the file path to the Mongo query result
path = var_call_VNEvq032PXm1hSsPWSIEbAc4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

results = []
for doc in docs:
    filename = doc.get('filename','')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    text = doc.get('text','')
    # Check domain mention
    if re.search(r'physical activity', text, re.I):
        # search for publication year near top of document (first 800 chars)
        head = text[:800]
        year_match = re.search(r'\b(19|20)\d{2}\b', head)
        pub_year = None
        if year_match:
            pub_year = int(year_match.group(0))
        # fallback: search whole text for an explicit 'Published' line
        if pub_year != 2016:
            # also check for patterns like 'CHI 2016' anywhere
            if re.search(r'\b2016\b', text):
                # but ensure it refers to publication rather than citation: check near top again
                if re.search(r'\b2016\b', head):
                    pub_year = 2016
        if pub_year == 2016:
            results.append({'title': title, 'filename': filename})

# Prepare JSON-serializable output: list of titles
titles = [r['title'] for r in results]
import json
out = json.dumps(titles)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VNEvq032PXm1hSsPWSIEbAc4': 'file_storage/call_VNEvq032PXm1hSsPWSIEbAc4.json'}

exec(code, env_args)
