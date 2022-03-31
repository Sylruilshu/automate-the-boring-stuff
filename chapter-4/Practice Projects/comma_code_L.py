def list_to_string(list_to_convert: list[str]) -> str:
    if list_to_convert == []:
        return ''
    
    last_item = list_to_convert[-1]
    list_without_last_item = list_to_convert[0:len(list_to_convert) - 1]
    string_without_last_item = ', '.join(list_without_last_item)
    string_with_last_item = string_without_last_item + f' and {last_item}'

    return string_with_last_item

initial_list = ['apples', 'bananas', 'tofu', 'cats']

result = list_to_string(initial_list)
print(result)