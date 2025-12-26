code = """import json

# Load civic docs
civic_path = var_call_IK3fn2ugEoLmAv5K3pegEKfT
with open(civic_path, "r", encoding="utf-8") as f:
    civic_docs = json.load(f)

# Load funding rows
funding_path = var_call_t4pMP4lJNGkh6vsjm9xCDWEx
with open(funding_path, "r", encoding="utf-8") as f:
    funding_rows = json.load(f)

# Helpers without regex

def has_disaster_keyword(s):
    s = (s or "").lower()
    return ("fema" in s) or ("caloes" in s) or ("caljpia" in s) or ("woolsey" in s) or ("fire" in s)


def strip_disaster_suffix(name):
    n = (name or "").strip()
    if n.endswith(")"):
        idx = n.rfind("(")
        if idx != -1:
            inside = n[idx+1:-1].lower()
            if ("fema" in inside) or ("caloes" in inside) or ("caljpia" in inside):
                n = n[:idx].strip()
    return " ".join(n.split())

eligible_base_names = set()

for doc in civic_docs:
    text = (doc.get("text") or "").replace("\r\n", "\n")
    lines = [ln.strip() for ln in text.split("\n")]
    n = len(lines)

    # Build section type map
    section_by_idx = {}
    current = None
    for i, ln in enumerate(lines):
        low = ln.lower()
        if "disaster recovery projects" in low:
            current = "disaster"
        elif "capital improvement projects" in low:
            current = "capital"
        section_by_idx[i] = current

    for i, ln in enumerate(lines):
        low = ln.lower()
        if ("begin construction" in low) and ("2022" in ln):
            # determine if disaster
            sec = section_by_idx.get(i)
            is_disaster = (sec == "disaster")
            if not is_disaster:
                start = max(0, i-10)
                end = min(n, i+10)
                ctx = "\n".join(lines[start:end]).lower()
                if has_disaster_keyword(ctx):
                    is_disaster = True
            if not is_disaster:
                continue
            # find title above
            title = None
            skip_set = {"updates", "project updates", "project schedule", "estimated schedule", "agenda", "subject", "discussion", "report", "page"}
            j = i - 1
            while j >= 0 and j >= i - 20:
                t = lines[j].strip()
                if t == "":
                    j -= 1
                    continue
                if ":" in t:
                    j -= 1
                    continue
                tl = t.lower()
                if tl in skip_set:
                    j -= 1
                    continue
                title = t
                break
            if title:
                eligible_base_names.add(strip_disaster_suffix(title))

# Sum matching funding rows
total = 0
included_records = []

for row in funding_rows:
    pname = row.get("Project_Name", "")
    if not has_disaster_keyword(pname):
        continue
    if strip_disaster_suffix(pname) in eligible_base_names:
        amt_str = row.get("Amount")
        try:
            amt = int(amt_str)
        except Exception:
            try:
                digits = "".join(ch for ch in str(amt_str) if ch.isdigit())
                amt = int(digits) if digits else 0
            except Exception:
                amt = 0
        total += amt
        included_records.append({"Project_Name": pname, "Amount": amt})

result = {
    "eligible_project_basenames": sorted(list(eligible_base_names)),
    "funding_records_included": included_records,
    "total_funding": total
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_2KKXqa5RVrT2vjHf1gQGBy65': ['civic_docs'], 'var_call_IK3fn2ugEoLmAv5K3pegEKfT': 'file_storage/call_IK3fn2ugEoLmAv5K3pegEKfT.json', 'var_call_4bAYPsTZoMODzL7tQBATHndp': ['Funding'], 'var_call_t4pMP4lJNGkh6vsjm9xCDWEx': 'file_storage/call_t4pMP4lJNGkh6vsjm9xCDWEx.json', 'var_call_kaXnF2m8GPl1J9oXIje1pDwq': 'ok'}

exec(code, env_args)
