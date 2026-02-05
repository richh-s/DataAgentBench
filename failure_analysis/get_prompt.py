import os

def get_prompt(trace, gt_answer, query) -> str:
    base_path = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(base_path, "failure_modes.txt"), "r") as file:
        fm_defns = file.read().strip()
    with open(os.path.join(base_path, "instruction.txt"), "r") as file:
        instruction = file.read().strip()

    return instruction.replace('<fm_defn>', fm_defns).replace('<query>', query).replace('<failed_trace>', trace).replace('<gt_answer>', gt_answer)



if __name__ == "__main__":

    trace = "<some trace>"

    gt_answer = "<some gt answer>"

    prompt = get_prompt(trace, gt_answer, "some query")

    print(prompt)