import os
import json
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

MODEL = "gpt5.1"
# MODEL = "gemini-3-pro"
QUERY_ROOT = Path("/home/ruiying/DataAgentBench")
RESULT_ROOT = Path(f"/home/ruiying/DataAgentBench/results-{MODEL}")

def load_tool_call_trace(result_dir: Path):
    tool_call_path = result_dir / "tool_calls.jsonl"
    if not tool_call_path.exists():
        return []
    trace = []
    with open(tool_call_path, "r") as f:
        for line in f:
            tool_call = json.loads(line)
            assert tool_call["tool_name"] in ["query_db", "list_db", "execute_python", "return_answer"]
            if tool_call["tool_name"] in ["query_db", "list_db"]:
                op = "extraction"
            elif tool_call["tool_name"] in ["execute_python"]:
                op = "transformation"
            else:
                assert tool_call["tool_name"] == "return_answer"
                op = "return_answer"
            trace.append(op)
    
    if len(trace) == 0 or trace[-1] != "return_answer":
        return []
    assert trace[-1] == "return_answer"
    if len(trace) <= 1:
        return []

    assert len(trace[:-1]) >= 1

    return trace[:-1]  # remove the final "return_answer"


def plot_operation_bar(traces, n_bins, fig_name):
    sum_extracts = np.zeros(n_bins)
    for trace in traces:
        n_ops = len(trace)
        assert n_ops >= 1
        bins_per_op = [0 for _ in range(n_ops)]
        for i in range(n_bins):
            op_idx = i % n_ops
            bins_per_op[op_idx] += 1
        assert sum(bins_per_op) == n_bins
        start_idx_per_op = [sum(bins_per_op[:i]) for i in range(n_ops)]
        assert len(start_idx_per_op) == n_ops
        assert len(bins_per_op) == n_ops
        for bin_idx, bin_num, op in zip(start_idx_per_op, bins_per_op, trace):
            if op == "extraction":
                sum_extracts[bin_idx:bin_idx + bin_num] += 1

    avg_prop = sum_extracts / len(traces)

    fig, ax = plt.subplots(figsize=(12, 0.5))  # long width, thin height
    im = ax.imshow(
        avg_prop[np.newaxis, :],
        aspect="auto",
        interpolation="nearest",
        cmap="coolwarm",
    )
    # # Add horizontal colorbar
    # cbar = fig.colorbar(im, ax=ax, orientation="horizontal", pad=0.05)

    # # Set tick labels at ends of colorbar
    # cbar.set_ticks([0, 1])  # 0 = left (blue), 1 = right (red)
    # cbar.set_ticklabels(["Transformation", "Extraction"])
    # cbar.ax.tick_params(labelsize=10)

    ax.set_yticks([])
    xtick_positions = np.linspace(0, n_bins - 1, 11)
    xtick_labels = [f"{x:.1f}" for x in np.linspace(0, 1, 11)]
    ax.set_xticks(xtick_positions)
    ax.set_xticklabels(xtick_labels)
    ax.set_xlabel("Normalized Time")
    ax.set_title("Average Extraction Proportion Over Time")
    
    plt.savefig(f"figures/{fig_name}_bar.png", bbox_inches='tight')





if __name__ == "__main__":
    FIG_NAME = f"tool_call_bar_{MODEL}_all"
    N_BINS = 200

    traces = []
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
        print(task)
        result_dir = RESULT_ROOT / f"query_{task}"
        for folder_name in sorted(os.listdir(result_dir)):
            if folder_name.startswith("query"):
                try:
                    query_id = int(folder_name.replace("query", ""))
                    # print(query_id)
                except Exception as e:
                    continue
                runs = list(range(50))
                for rid in runs:
                    if MODEL == "gpt5.1":
                        run_dir = result_dir / f"query{query_id}" / f"run_{rid}"
                    elif MODEL == "gemini-3-pro":
                        run_dir = result_dir / f"query{query_id}" / "data_agent" / f"run_{rid}"
                    trace = load_tool_call_trace(run_dir)
                    if len(trace) > 0:
                        traces.append(trace)
    print(f"Loaded {len(traces)} traces.")
    # plot_operation_density(traces, n_bins=N_BINS, fig_name=FIG_NAME)
    plot_operation_bar(traces, n_bins=N_BINS, fig_name=FIG_NAME)
