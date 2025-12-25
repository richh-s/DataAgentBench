from abc import ABC, abstractmethod
import time
from pathlib import Path
from datetime import datetime
import json
import logging

class FatalError(Exception):
    """An engineering error occurred; the tool cannot continue; for debugging."""
    pass

class BaseTool(ABC):
    def __init__(self, log_path: Path, name: str):
        self.logger = logging.getLogger(__name__)
        self.logger.info(f"🔧 Initializing {name}...")
        self.log_path = log_path
        self.name = name
        self.logger.info(f"\tlog: {self.log_path}")

    def to_dict(self):
        return {
            "name": self.name,
            "log_path": str(self.log_path),
        }


    @abstractmethod
    def get_spec(self):
        '''
        Return the tool specification as a dict.
        '''
        pass

    @abstractmethod
    def _check_args(self, args: dict):
        '''
        Return the validated and possibly transformed arguments, or raise an Exception on failure.
        '''
        self.logger.info(f"\tChecking args: {args}")
        return args
    
    @abstractmethod
    def _exec(self, args: dict):
        '''
        Return the actual execution result if successful, or raise an Exception on failure.
        '''
        self.logger.info(f"\tExecuting with args: {args}")
        pass

    def exec(self, args: dict):
        self.logger.info(f"🔧 {self.name}({args})")
        start_ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        start = time.time()
        val_args = None
        try:
            val_args = self._check_args(args)
            result = self._exec(val_args)
            exec_result = {"success": True, "result": result}
        except FatalError as fe:
            raise fe
        except Exception as e:
            exec_result = {"success": False, "result": f"{str(e)}"}
        end = time.time()
        end_ts = datetime.now().strftime("%Y%m%d_%H%M%S")

        serialized_result = json.dumps(exec_result["result"])
        if len(serialized_result) > 10000:
            serialized_result = serialized_result[:10000]
        self.logger.info(f"\tResult: {exec_result}")
        log_entry = {
            "start": start_ts,
            "end": end_ts,
            "time": end - start,
            "tool_name": self.name,
            "result": {"success": exec_result["success"], "preview": serialized_result},
            "args": args,
            "val_args": val_args,
        }

        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")


        return exec_result
    
    @abstractmethod
    def clean_up(self):
        '''
        Clean up any resources used by the tool.
        '''
        self.logger.info(f"🧹 Cleaning up tool: {self.name}")
        pass
        
    