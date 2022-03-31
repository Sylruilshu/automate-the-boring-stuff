def list_to_string(list_to_convert: list) -> list | None:
    if list == []:
        return None

    return (
        ", ".join(list_to_convert[: len(list_to_convert) - 1])
        + f" and {list_to_convert[-1]}"
    )


initial_list = ["apples", "bananas", "tofu", "cats"]

result = list_to_string(initial_list)

print(result)
