code = """import json
import pandas as pd
import re

# Load the languages data from file
with open('/tmp/result_6m5d07.json', 'r') as f:
    language_data = json.load(f)

# Convert to DataFrame
df_languages = pd.DataFrame(language_data)

# Parse language description to find primary language
# The descriptions look like: "This repository is mainly written in Ruby (1,897 bytes), with additional code in Shell (115 bytes)."
# Or: "The codebase includes: Ruby (22,438 bytes), Shell (465 bytes)."
# We need to extract languages and their byte counts, then determine which is primary

def extract_primary_language(lang_desc):
    if not lang_desc or pd.isna(lang_desc):
        return None
    
    # Find all language-byte pairs using regex
    pattern = r'(\w(?:[\w+#-]*\w)?)\s*\(([\d,]+)\s*bytes?\)'
    matches = re.findall(pattern, lang_desc)
    
    if not matches:
        return None
    
    # Find the language with max bytes
    max_lang = None
    max_bytes = -1
    
    for lang, byte_str in matches:
        try:
            byte_count = int(byte_str.replace(',', ''))
            if byte_count > max_bytes:
                max_bytes = byte_count
                max_lang = lang.lower()  # Normalize to lowercase for comparison
        except:
            continue
    
    return max_lang

# Apply function to get primary language
df_languages['primary_language'] = df_languages['language_description'].apply(extract_primary_language)

# Filter for repositories where primary language is not Python
df_filtered = df_languages[df_languages['primary_language'] != 'python']

result = {
    'total_repos': len(df_languages),
    'filtered_repos': len(df_filtered),
    'primary_languages': df_languages['primary_language'].value_counts().head(10).to_dict(),
    'first_filtered': df_filtered[['repo_name', 'primary_language']].head().to_dict(orient='records')
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['languages', 'repos', 'licenses'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
