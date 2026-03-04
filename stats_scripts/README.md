# Scripts for Statistics of Agent Trajectories

- [accuracy.py](./accuracy.py): calculate the **pass@k** accuracy of *n* agent runs on **one query**.

- [avg_accuracy.py](./avg_accuracy.py): calcuate the **average pass@1** accuracy of *n* agent runs on **one dataset**.

- [avg_pass_k.py](./avg_pass_k.py): calcuate the **average pass@k** accuracy of *n* agent runs on **one dataset**.

- [cost.py](./cost.py): calculate the **total cost (USD)** of *n* agent runs on **one query**.

- [llm_calls.py](./llm_calls.py): calculate the **average count, latency, and input/output tokens of API calls** of *n* agent runs on **one query**.

- [tool_calls.py](./tool_calls.py): calculate the **average count, execution latency, and success rate of tool execution** of *n* agent runs on **one query**.

- [traj_stats.py](./traj_stats.py): caculcate the **average latency, #iterations, #tool calls, #db queries, #python execs** of *n* agent runs on **one query**.

- [python_exec_failure_rate.py](./python_exec_failure_rate.py): calculate the **average failure rate of execute_python** of *n* agent runs on **one query**

- [parellel_rate.py](./parallel_rate.py): calculate the **average/max parallel rate** of API call across all agent API calls on **all datatsets**.