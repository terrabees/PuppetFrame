def remove_children(input_dict: dict):
    for item in dict(input_dict):
        if not isinstance(input_dict[item], (str, int, float)):
            del input_dict[item]
