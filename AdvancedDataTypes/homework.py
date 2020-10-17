from typing import List, Dict, Union, Callable

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    
    new_list = []
    for name in range(len(data)):
        new_data = {}
        new_list.append(new_data)
        for key, val in data[name].items():
            new_data[key] = str(val). title()
    return new_list
    pass


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    for item in data:
        for key in redundant_keys:
            item.pop(key)
    return data
    
    pass


def task_3_find_item_via_value(data: DT, value) -> DT:
    find = [find for find in data for n in find.values() if n==value]
    return find
    pass


def task_4_return_lambda_sum_2_ints() -> DT:
    return lambda x, y: x + y
    pass


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    my_list = input_data.copy()
    my_list.append(elem)
    return my_list
    pass


def task_6_insert_function_result_into_string(func: Callable):
    string_out = f"start {func()} finish"
    return string_out


def task_7_insert_2_vars_into_string(age: float, habit: str):
    return f"I have {int(age * 10) / 10} years and I love {habit.ljust(10)[:10]}"
