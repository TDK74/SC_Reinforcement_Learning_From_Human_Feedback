import json


## ------------------------------------------------------ ##
preference_dataset_path = 'sample_preference.jsonl'

## ------------------------------------------------------ ##
preference_data = []

## ------------------------------------------------------ ##
with open(preference_dataset_path) as f:
    for line in f:
        preference_data.append(json.loads(line))

## ------------------------------------------------------ ##
sample_1 = preference_data[0]

## ------------------------------------------------------ ##
print(type(sample_1))

## ------------------------------------------------------ ##
print(sample_1.keys())

## ------------------------------------------------------ ##
sample_1['input_text']

## ------------------------------------------------------ ##
# preference_data[1]['input_text'][-50 : ]
preference_data[2]['input_text'][-50 : ]

## ------------------------------------------------------ ##
print(f"candidate_0:\n{sample_1.get('candidate_0')}\n")
print(f"candidate_1:\n{sample_1.get('candidate_1')}\n")

## ------------------------------------------------------ ##
print(f"choice: {sample_1.get('choice')}")

## ------------------------------------------------------ ##
prompt_dataset_path = 'sample_prompt.jsonl'

## ------------------------------------------------------ ##
prompt_data = []

## ------------------------------------------------------ ##
with open(prompt_dataset_path) as f:
    for line in f:
        prompt_data.append(json.loads(line))

## ------------------------------------------------------ ##
len(prompt_data)

## ------------------------------------------------------ ##
def print_d(d):
    for key, val in d.items():
        print(f"key: {key}\nval:  {val}\n")

## ------------------------------------------------------ ##
print_d(prompt_data[0])

## ------------------------------------------------------ ##
print_d(prompt_data[1])
