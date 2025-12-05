import re

def levenshtein(s1: str, s2: str) -> int:
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
    return previous_row[-1]

def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]", "", text.lower())

# -----------------------------
# Ground Truth Data
# -----------------------------
ground_truth = [
    ("BAKING; EDIBLE DOUGHS", "A21", "2015"),
    ("MEDICAL OR VETERINARY SCIENCE; HYGIENE", "A61", "2016"),
    ("MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR", "B23", "2015"),
    ("WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL", "B29", "2012"),
    ("PRINTING; LINING MACHINES; TYPEWRITERS; STAMPS", "B41", "2007"),
    ("VEHICLES IN GENERAL", "B60", "2016"),
    ("LAND VEHICLES FOR TRAVELLING OTHERWISE THAN ON RAILS", "B62", "2010"),
    ("SHIPS OR OTHER WATERBORNE VESSELS; RELATED EQUIPMENT", "B63", "2014"),
    ("DYES; PAINTS; POLISHES; NATURAL RESINS; ADHESIVES; COMPOSITIONS NOT OTHERWISE PROVIDED FOR; APPLICATIONS OF MATERIALS NOT OTHERWISE PROVIDED FOR", "C09", "2015"),
    ("HYDRAULIC ENGINEERING; FOUNDATIONS; SOIL SHIFTING", "E02", "2012"),
    ("LOCKS; KEYS; WINDOW OR DOOR FITTINGS; SAFES", "E05", "2012"),
    ("COMBUSTION ENGINES; HOT-GAS OR COMBUSTION-PRODUCT ENGINE PLANTS", "F02", "2018"),
    ("ENGINEERING ELEMENTS AND UNITS; GENERAL MEASURES FOR PRODUCING AND MAINTAINING EFFECTIVE FUNCTIONING OF MACHINES OR INSTALLATIONS; THERMAL INSULATION IN GENERAL", "F16", "2014"),
    ("COMBUSTION APPARATUS; COMBUSTION PROCESSES", "F23", "2018"),
    ("HEATING; RANGES; VENTILATING", "F24", "2018"),
    ("WEAPONS", "F41", "2012"),
    ("MEASURING; TESTING", "G01", "2018"),
    ("OPTICS", "G02", "2018"),
    ("SIGNALLING", "G08", "2017"),
    ("ELECTRIC ELEMENTS", "H01", "2018"),
    ("GENERATION; CONVERSION OR DISTRIBUTION OF ELECTRIC POWER", "H02", "2009"),
    ("ELECTRONIC CIRCUITRY", "H03", "2015"),
    ("ELECTRIC COMMUNICATION TECHNIQUE", "H04", "2015"),
    # ("TECHNOLOGIES OR APPLICATIONS FOR MITIGATION OR ADAPTATION AGAINST CLIMATE CHANGE", "Y02", "2018"),  # 包含你提到的样例
]

# -----------------------------
# Main validate function
# -----------------------------
def validate(llm_output: str):
    llm_clean = normalize(llm_output)

    for raw_name, cpc_code, year in ground_truth:
        norm_name = normalize(raw_name)
        name_len = len(norm_name)

        # Fuzzy match window scan
        best_match = None
        best_dist = float('inf')
        best_idx = -1

        for i in range(len(llm_clean) - name_len + 1):
            candidate = llm_clean[i:i + name_len]
            dist = levenshtein(candidate, norm_name)
            if dist < best_dist:
                best_dist = dist
                best_match = candidate
                best_idx = i
            if best_dist == 0:
                break

        if best_dist > 5:
            reason = f"Name fuzzy match failed for '{raw_name}' (best match: '{best_match}', distance={best_dist})"
            return False, reason

        # Define window: 15 before and 15 after name end
        start = max(0, best_idx - 15)
        end = min(len(llm_clean), best_idx + name_len + 15)
        window = llm_clean[start:end]

        if normalize(cpc_code) not in window or normalize(year) not in window:
            reason = f"Code/year not found near '{raw_name}' (CPC: {cpc_code}, Year: {year}, Window: '{window}')"
            return False, reason

    return True, "All fuzzy names matched, and CPC/year found near each name."
