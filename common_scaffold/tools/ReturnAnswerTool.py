from common_scaffold.tools.BaseTool import BaseTool

class ReturnAnswerTool(BaseTool):
    def __init__(self, log_path, name):
        super().__init__(log_path, name)

    def get_spec(self):
        spec = {
            "type": "function",
            "function": {
                "name": self.name,
                "description": "Return the final answer string and stop the task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "answer": {
                            "type": "string",
                            "description": "The final answer to the task."
                        }
                    },
                    "required": ["answer"]
                }
            }
        }
        return spec

    def clean_up(self):
        return super().clean_up()
    
    def _check_args(self, args: dict):
        args = super()._check_args(args)
        if "answer" not in args:
            raise ValueError("Missing required argument: `answer`")
        if not isinstance(args["answer"], str):
            raise ValueError(f"`answer` must be a string, got {type(args['answer']).__name__}")
        return {
            "answer": args["answer"]
        }
    
    def _exec(self, args):
        super()._exec(args)
        return args["answer"]