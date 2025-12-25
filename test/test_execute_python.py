import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from common_scaffold.tools.ExecTool import ExecTool
import logging_config



def test():
    tool = ExecTool(
        log_path="test_execute_python.jsonl",
        name="test_execute_python",
        work_dir="/home/ruiying/DataAgentBench/test/exec_python_work_dir",
        timeout=600
    )

    args = {
        "code": "print('__RESULT__:')\nprint(locals()['var-func_call'])",
        "env": {"var-func_call": "Hello, World!"}
    }

    result = tool.exec(args)

    print(result)

    tool.clean_up()

if __name__ == "__main__":
    test()  