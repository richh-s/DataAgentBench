import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from pathlib import Path
import time
import logging
import logging_config
from openai import AzureOpenAI
from dotenv import load_dotenv
from failure_analysis.get_prompt import get_prompt
from failure_analysis.get_trace import get_trace

CNT_PER_QUERY = 5
JUDGE_MODEL = "gpt-5"

load_dotenv()
client = AzureOpenAI(
    api_key=os.getenv("AZURE_API_KEY"),
    api_version=os.getenv("AZURE_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_API_BASE")
)


model_list = [
    "gemini-2.5-flash",
    "gemini-3-pro",
    "gpt-5-mini",
    "gpt-5.2",
    "gpt5.1",
    "kimi-k2-thinking",
]

task_list = [
    "bookreview",
    "crmarenapro",
    "DEPS_DEV_V1",
    "GITHUB_REPOS",
    "googlelocal",
    "PANCANCER_ATLAS",
    "PATENTS",
    "stockindex",
    "stockmarket",
    "yelp",
    "agnews",
    "music_brainz_20k",
]

for model in model_list:
    for task in task_list:
        query_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f"query_{task}")
        assert os.path.exists(query_dir), f"⚠️ {query_dir} not found"
        query_id_list = []
        for d in Path(query_dir).iterdir():
            try:
                query_id = int(d.name.replace("query", ""))
                query_id_list.append(query_id)
            except:
                continue
        for query_id in sorted(query_id_list):
            answer_file = os.path.join(query_dir, f"query{query_id}", "ground_truth.csv")
            with open(answer_file, "r", encoding="utf-8") as f:
                gt_answer = f.read().strip()
            query_file = os.path.join(query_dir, f"query{query_id}", "query.json")
            with open(query_file, "r", encoding="utf-8") as f:
                query_json = json.load(f)

            llm_judge_cnt = 0
            judge_result_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "failure_analysis", f"results-{model}", f"query_{task}", f"query{query_id}.jsonl")
            os.makedirs(os.path.dirname(judge_result_path), exist_ok=True)
            existing_judge_results = set()
            if os.path.exists(judge_result_path):
                with open(judge_result_path, 'r') as file:
                    for line in file:
                        try:
                            log_entry = json.loads(line)
                            existing_judge_results.add(log_entry["run_id"])
                        except:
                            continue
            for run_id in range(50):
                if llm_judge_cnt >= CNT_PER_QUERY:
                    break
                if run_id in existing_judge_results:
                    logging.getLogger(__name__).info(f"ℹ LLM judge already exists for query_{task} query{query_id} run_{run_id} using {model}, skipping...")
                    continue
                is_failed, failed_reason, failed_trace = get_trace(model, task, query_id, run_id)
                judge_result = None
                if failed_trace != None:
                    assert is_failed == True
                    assert failed_reason == "return_answer", f"Expected failed_reason to be 'return_answer', but got {failed_reason}"
                    prompt = get_prompt(failed_trace, gt_answer, str(query_json))
                    try:
                        response = client.chat.completions.create(
                            model=JUDGE_MODEL,
                            messages=[
                                {
                                    "role": "user",
                                    "content": prompt
                                }
                            ],
                            temperature=1.0,
                        )
                        if response.choices and len(response.choices) > 0:
                            llm_judge_cnt += 1
                            judge_result = {
                                "judge": response.choices[0].message.content,
                                "input_tokens": response.usage.prompt_tokens,
                                "output_tokens": response.usage.completion_tokens
                            }
                            logging.getLogger(__name__).info(f"✅ LLM judge succeeded for query_{task} query{query_id} run_{run_id} using {model}")
                            logging.getLogger(__name__).info(f"\tInput tokens: {response.usage.prompt_tokens}, Output tokens: {response.usage.completion_tokens}")
                    except Exception as e:
                        logging.getLogger(__name__).error(f"⚠️ LLM judge failed for query_{task} query{query_id} run_{run_id} using {model}: {str(e)}")
                        time.sleep(5)
                        judge_result = "Failed to get LLM judge result."
                    
                # log judge result
                log_entry = {
                    "run_id": run_id,
                    "is_failed": is_failed,
                    "failed_reason": failed_reason,
                    "judge_result": judge_result
                }

                with open(judge_result_path, "a", encoding="utf-8") as f:
                    f.write(json.dumps(log_entry) + "\n")

                    
