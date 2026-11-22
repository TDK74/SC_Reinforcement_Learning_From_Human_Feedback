import os
import subprocess


## ------------------------------------------------------ ##
port = os.environ["PORT1"]

## ------------------------------------------------------ ##
process = subprocess.Popen(["tensorboard",
                            "--logdir",
                            "reward-logs",
                            "--port",
                            port,
                            "--bind_all"], )
