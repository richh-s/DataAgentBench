code = """import re, json, pandas as pd

# Load full civic docs from file
import pathlib, json as jsonmod
path = pathlib.Path(var_call_kZa27tpLrDXOn8yd0JQQFkMI)
with path.open() as f:
    civic_docs = jsonmod.load(f)

funding = pd.DataFrame(var_call_2lmvN1TvM82PM1nxwsf4lPus)

text = " ".join(doc.get("text","") for doc in civic_docs)

projects = []
for line in text.split("\n"):
    line = line.strip()
    if not line:
        continue
    if "Project" in line or "Repairs" in line or "Improvements" in line or "Recovery" in line:
        if re.search(r"\b2022\b", line):
            projects.append(line)

unique_projects = sorted(set(projects))

# Approximate: disaster-related projects are those with FEMA/CalOES/CalJPIA or explicit disaster keyword in funding names
funding["is_disaster"] = funding["Project_Name"].str.contains("FEMA|CalOES|CalJPIA|Disaster", case=False, regex=True)

# For started in 2022: approximate by project names that contain '2022' or match project lines we saw with 2022
funding["is_2022"] = funding["Project_Name"].str.contains("2022", case=False, regex=False)

# Disaster + started 2022
subset = funding[funding["is_disaster"] & funding["is_2022"]]
subset["Amount"] = subset["Amount"].astype(int)

total = int(subset["Amount"].sum())

result = {"total_disaster_2022_funding": total, "matching_projects": subset[["Project_Name","Amount"]].to_dict(orient="records")}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kZa27tpLrDXOn8yd0JQQFkMI': 'file_storage/call_kZa27tpLrDXOn8yd0JQQFkMI.json', 'var_call_2lmvN1TvM82PM1nxwsf4lPus': 'file_storage/call_2lmvN1TvM82PM1nxwsf4lPus.json'}

exec(code, env_args)
