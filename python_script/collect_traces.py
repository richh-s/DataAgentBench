import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pathlib import Path
import logging_config
import json
import shutil

RESULT_ROOT = Path("/home/ruiying/DataAgentBench")
# DST_ROOT = Path("/home/ruiying/DataAgentBench/results-gemini-2.5-flash")
DST_ROOT = Path("/home/ruiying/DataAgentBench/results-gemini-3-pro")
# DST_ROOT = Path("/home/ruiying/DataAgentBench/results-gpt5.1")

if __name__ == "__main__":
    for task in [
        # "bookreview",
        # "crmarenapro",
        # "DEPS_DEV_V1",
        # "GITHUB_REPOS",
        # "googlelocal",
        # "PANCANCER_ATLAS",
        # "PATENTS",
        # "stockindex",
        # "stockmarket",
        # "yelp",
        "agnews",
        "music_brainz_20k",
    ]:
        query_dir = RESULT_ROOT / f"query_{task}"
        for folder_name in sorted(os.listdir(query_dir)):
            if folder_name.startswith("query"):
                try:
                    query_id = int(folder_name.replace("query", ""))
                    # print(query_id)
                except Exception as e:
                    continue
                if "gpt5.1" in DST_ROOT.name:
                    result_dir = query_dir / folder_name / "logs" / "data_agent"
                else:
                    result_dir = query_dir / folder_name / "logs"
                if result_dir.exists():
                    print(f"Copying results for task {task}, query {query_id}...")
                    dst_dir = DST_ROOT / f"query_{task}" / folder_name
                    assert not dst_dir.exists(), f"Destination directory {dst_dir} already exists!"
                    shutil.copytree(result_dir, dst_dir)

        print("\n\n")