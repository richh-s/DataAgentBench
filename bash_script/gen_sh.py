from pathlib import Path
import os

QUERY_ROOT = Path("/home/ruiying/DataAgentBench")

MODEL = "gemini-3-pro-preview"
# MODEL = "gemini-2.5-flash"

if __name__ == "__main__":
    tot_cmd = ""
    for task in [
        "bookreview",
        "crmarenapro",
        "DEPS_DEV_V1",
        "GITHUB_REPOS",
        "googlelocal",
        "PANCANCER_ATLAS",
        "PATENTS",
        "stockindex",
        "stockmarket",
        "yelp"
    ]:
        query_dir = QUERY_ROOT / f"query_{task}"
        for folder_name in sorted(os.listdir(query_dir)):
            if folder_name.startswith("query"):
                try:
                    query_id = int(folder_name.replace("query", ""))
                except Exception as e:
                    continue
                for rid in range(50):
                    cmd = f"python /home/ruiying/DataAgentBench/run_agent.py --task {task} --query_id {query_id} --llm {MODEL} --iterations 100 --use_hints --root_name run_{rid}"
                    tot_cmd += cmd + "\n"

            tot_cmd += "\n"
        tot_cmd += "\n"
    
    with open(f"run_all_{MODEL}.sh", "w") as f:
        f.write(tot_cmd)