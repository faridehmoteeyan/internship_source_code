## double iterations
from collections import defaultdict
flat = dict()
first_occurance_dict = defaultdict(list)
for outer_key, outer_val in student_data.items():
    if isinstance(outer_val, dict):
        for inner_key, inner_val in outer_val.items():
            first_occurance_dict[inner_key].append(inner_val)
    else:
        first_occurance_dict[outer_key].append(outer_val)

for key, val_list in first_occurance_dict.items():
    if len(val_list) == 1:
        flat[key] = val_list[0]
    else:
        for i, val in enumerate(val_list):
            key_name = key + "_" + str(i)
            flat[key_name] = val
print(flat)

# hard way: single iteration
from collections import defaultdict
def process(key, val):
    first_occurance_dict_val_len = len(first_occurance_dict[key])
    if first_occurance_dict_val_len == 1:
        flat[key] = val
    elif first_occurance_dict_val_len == 2:
        zero_val = flat.pop(key)
        flat[f"{key}_0"] = zero_val
        flat[f"{key}_1"] = val
    else:
        flat[f"{key}_{first_occurance_dict_val_len}"] = val

flat = dict()
first_occurance_dict = defaultdict(list)
for outer_key, outer_val in student_data.items():
    if isinstance(outer_val, dict):
        for inner_key, inner_val in outer_val.items():
            first_occurance_dict[inner_key].append(inner_val)
            process(inner_key, inner_val)
    else:
        first_occurance_dict[outer_key].append(outer_val)
        process(outer_key, outer_val)
print(flat)