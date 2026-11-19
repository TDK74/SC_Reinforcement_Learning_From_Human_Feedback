import math
import subprocess
import google.cloud.aiplatform as aiplatform

from google_cloud_pipeline_components.preview.llm import rlhf_pipeline
from kfp import compiler
from utils import authenticate


## ------------------------------------------------------ ##
RLHF_PIPELINE_PKG_PATH = "rlhf_pipeline.yaml"

## ------------------------------------------------------ ##
compiler.Compiler().compile(pipeline_func= rlhf_pipeline, package_path= RLHF_PIPELINE_PKG_PATH)

## ------------------------------------------------------ ##
subprocess.run(["head", "rlhf_pipeline.yaml"])

## ------------------------------------------------------ ##
PREF_DATASET_SIZE = 3000

## ------------------------------------------------------ ##
BATCH_SIZE = 64

## ------------------------------------------------------ ##
REWARD_STEPS_PER_EPOCH = math.ceil(PREF_DATASET_SIZE / BATCH_SIZE)
print(REWARD_STEPS_PER_EPOCH)

## ------------------------------------------------------ ##
REWARD_NUM_EPOCHS = 30

## ------------------------------------------------------ ##
reward_model_train_steps = REWARD_STEPS_PER_EPOCH * REWARD_NUM_EPOCHS

## ------------------------------------------------------ ##
print(reward_model_train_steps)

## ------------------------------------------------------ ##
PROMPT_DATASET_SIZE = 2000

## ------------------------------------------------------ ##
BATCH_SIZE = 64

## ------------------------------------------------------ ##
RL_STEPS_PER_EPOCH = math.ceil(PROMPT_DATASET_SIZE / BATCH_SIZE)
print(RL_STEPS_PER_EPOCH)

## ------------------------------------------------------ ##
RL_NUM_EPOCHS = 10

## ------------------------------------------------------ ##
reinforcement_learning_train_steps = RL_STEPS_PER_EPOCH * RL_NUM_EPOCHS

## ------------------------------------------------------ ##
print(reinforcement_learning_train_steps)

## ------------------------------------------------------ ##
parameter_values = {"preference_dataset" : ("gs://vertex-ai/generative-ai/rlhf/text_small/"
                                        "summarize_from_feedback_tfds/comparisons/train/*.jsonl"),
                    "prompt_dataset" : ("gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/"
                                        "train/*.jsonl"),
                    "eval_dataset" : ("gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/"
                                        "val/*.jsonl"),
                    "large_model_reference" : "llama-2-7b",
                    "reward_model_train_steps" : 1410,
                    "reinforcement_learning_train_steps" : 320,
                    "reward_model_learning_rate_multiplier" : 1.0,
                    "reinforcement_learning_rate_multiplier" : 1.0,
                    "kl_coeff" : 0.1,
                    "instruction" : "Summarize in less than 50 words"}

## ------------------------------------------------------ ##
credentials, PROJECT_ID, STAGING_BUCKET = authenticate()

REGION = "europe-west4"

## ------------------------------------------------------ ##
aiplatform.init(project= PROJECT_ID, location= REGION, credentials= credentials)

## ------------------------------------------------------ ##
print(RLHF_PIPELINE_PKG_PATH)
