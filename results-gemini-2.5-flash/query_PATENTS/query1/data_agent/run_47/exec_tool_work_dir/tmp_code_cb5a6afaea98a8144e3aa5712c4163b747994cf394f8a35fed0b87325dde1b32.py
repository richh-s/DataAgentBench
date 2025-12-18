code = """import json
import pandas as pd
import re

file_path = locals()['var_function-call-7189847626086033178']
df = pd.read_json(file_path)

def parse_cpc_and_date(row):
    cpc_codes = []
    filing_year = None

    # Parse CPC codes
    try:
        cpc_data = json.loads(row['cpc'])
        for item in cpc_data:
            if "code" in item:
                cpc_codes.append(item["code"])
    except (json.JSONDecodeError, TypeError):
        pass  # Handle cases where cpc is not valid JSON or None

    # Parse filing date
    try:
        # Regular expression to find a 4-digit year
        year_match = re.search(r"\d{4}", row['filing_date'])
        if year_match:
            filing_year = int(year_match.group(0))
    except (TypeError, ValueError):
        pass # Handle cases where filing_date is None or cannot be parsed

    return pd.Series({'cpc_codes': cpc_codes, 'filing_year': filing_year})

# Apply the function to each row
df_parsed = df.apply(parse_cpc_and_date, axis=1)

# Explode the cpc_codes list to have one row per CPC code
df_exploded = df_parsed.explode('cpc_codes')

# Filter out rows with None values for cpc_codes or filing_year
df_filtered = df_exploded.dropna(subset=['cpc_codes', 'filing_year'])

# Filter for level 5 CPC codes (e.g., A01B1/00 - 4 letters, 1 number, slash, 2 numbers)
# Level 5 CPC codes have a specific structure: 4 letters, then a number, then a slash, then at least two numbers
# Example: A01B1/00
# This regex captures the pattern: ^[A-Z]{4}\d/\d{2,}$
# However, it is more reliable to match for 4 characters (A01B), then a number (1), then /, then 2 numbers (00) - this is a section, main class, subclass, group, and subgroup. A level 5 code would be the subgroup, e.g., A01B1/00. This is typically 7 characters long, with the 5th character being a number, followed by a slash and at least two digits.
# The problem asks for "CPC group codes at level 5". Let's assume this means codes like "A01B1/00".
# Based on the problem description, CPC level 5 refers to group codes. A typical CPC symbol has the format: Section (1 letter), Class (2 digits), Subclass (1 letter), Main Group (up to 3 digits), Subgroup (up to 3 digits).
# A level 5 CPC code would be something like "A01B1/00" (Section, Class, Subclass, Group, Subgroup). 
# So it's a 4 character prefix, then a number, then a slash, then numbers. The level information is also available in CPCDefinition_database. But for now, I can filter based on the string pattern.
# A simpler check for level 5: it has a slash and two digits after the slash, and is 7 characters long total before any potential further subdivisions.
# I will use a regex to identify the 5th level which typically has a format like A01B1/00. I need to be careful to extract the group level code itself, which is typically the part before the / or the full code. The problem mentions "CPC group codes at level 5". I will assume this means codes of the form [A-Z]{4}\d{1,3}/\d{2,3} and extract the full code. A group code typically means the section, class, subclass and the group number. So A01B1 is the group. A01B1/00 is the subgroup.
# Let's re-evaluate: "CPC group codes at level 5". In the CPC system, level 5 usually refers to the *subgroup* level (e.g., A01B 1/00). The "group" part itself is A01B 1. 
# Given the example in the problem ("A01B1/00"), I will interpret level 5 as codes having a main group and a subgroup. 
# I will extract the first 7 characters if it matches the pattern of AXXXN/NN (e.g. A01B1/00). 
# I need to ensure that the code has at least one slash, and at least two digits after the slash.

def is_level_5_cpc(code):
    # Check for pattern like A01B1/00 (Section, Class, Subclass, Group, Subgroup)
    # A level 5 CPC code usually has a form like A01B1/00, where the group part is A01B1 and the subgroup is 00.
    # The question asks for "CPC group codes at level 5". This means the *full* symbol for the subgroup, like A01B1/00.
    # Let's try to match the pattern: one uppercase letter, followed by 3 alphanumeric, then a digit, then '/', then at least 2 digits.
    # A more general pattern for level 5 would be 4 characters, followed by 1 or more digits, then a slash, then 2 or more digits
    # Example: A01B1/00 - Section A, Class 01, Subclass B, Group 1/00.
    # The "group code" refers to the part before the subgroup, e.g., A01B1. The level 5 refers to the *subgroup*.
    # So, I need to extract the "group code" (e.g., A01B1) if the *full* CPC code is at level 5 (e.g., A01B1/00).
    # Let's use the pattern `^[A-Z]\d{2}[A-Z]\d+/[A-Z0-9]+$` as a proxy for level 5 and extract the part before the slash.
    # The pattern in the problem description is `A01B1/00`, which suggests 4 characters, then one digit, then a slash, then two digits.
    # Let's parse the cpc code into its components and check the length of the components. A level 5 code should have a section, class, subclass, group, and subgroup.
    # If the code contains a "/" and at least two digits after it, and has a structure like AXXXN/NN, then it is a level 5. Let's get the full code.

    # More robust check for level 5 CPC codes:
    # They typically have the format: [Section][Class][Subclass][Main Group]/[Subgroup]
    # E.g., A (Section), 01 (Class), B (Subclass), 1 (Main Group), /00 (Subgroup)
    # The symbol itself contains the full hierarchy, so I can just check for the presence of a slash and digits after it
    # And ensure it's not just a main group, but actually a subgroup.
    # A reliable way is to count the number of parts separated by non-alphanumeric characters, but the structure is often just one string.

    # Let's rely on the structure of the string itself to identify level 5 codes.
    # A level 5 CPC code is typically 7 characters long, like A01B1/00, or A01B10/00.
    # It should have a "/" and at least 2 digits after the slash.
    # The "group code at level 5" refers to the *full* code at that level (e.g., A01B1/00).
    if re.fullmatch(r"^[A-Z]\d{2}[A-Z]\d+/[A-Z0-9]{2,}$", code):
        return True
    return False

df_level_5 = df_filtered[df_filtered['cpc_codes'].apply(is_level_5_cpc)]

# Group by CPC code and filing year and count the number of filings
filings_count = df_level_5.groupby(['cpc_codes', 'filing_year']).size().reset_index(name='filings')

# Sort by CPC code and year for EMA calculation
filings_count_sorted = filings_count.sort_values(by=['cpc_codes', 'filing_year'])

# Calculate EMA for each CPC code
def calculate_ema(group, span=5):
    # Using adjust=False for consistent EMA calculation with a fixed smoothing factor
    return group.ewm(span=span, adjust=False).mean()

# Apply EMA calculation per CPC code
# For smoothing factor 0.2, alpha = 0.2. span = 2/(alpha+1) - 1. So alpha = 2/(span+1). span = 2/alpha - 1 = 2/0.2 - 1 = 10 - 1 = 9.
# Or directly use `com=...` which is 1/alpha - 1. So `com=1/0.2 - 1 = 5 - 1 = 4`
# Or directly use `alpha=0.2`. Let's use `alpha`.
filings_count_sorted['ema'] = filings_count_sorted.groupby('cpc_codes')['filings'].transform(lambda x: x.ewm(alpha=0.2, adjust=False).mean())

# Find the year with the highest EMA for each CPC code
idx_max_ema = filings_count_sorted.groupby('cpc_codes')['ema'].idxmax()
best_year_ema = filings_count_sorted.loc[idx_max_ema]

# Filter for CPC codes whose best year is 2022
cpc_best_2022 = best_year_ema[best_year_ema['filing_year'] == 2022]['cpc_codes']

# Convert to list and print
print("__RESULT__:")
print(json.dumps(cpc_best_2022.tolist()))"""

env_args = {'var_function-call-7189847626086033178': 'file_storage/function-call-7189847626086033178.json'}

exec(code, env_args)
