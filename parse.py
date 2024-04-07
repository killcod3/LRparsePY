import re

def lr(input_str, left, right, recursive=False, use_regex=False):
    # No L and R = return full input
    if left == '' and right == '':
        return [input_str]

    # L or R not present and not empty = return nothing
    elif (left != '' and left not in input_str) or (right != '' and right not in input_str):
        return []

    list = []
    partial = input_str

    if recursive:
        if use_regex:
            try:
                pattern = build_lr_pattern(left, right)
                mc = re.finditer(pattern, partial)
                for m in mc:
                    list.append(m.group())
            except Exception as e:
                pass  # Handle exceptions or log as needed
        else:
            try:
                while (left == '' or left in partial) and (right == '' or right in partial):
                    p_from = 0 if left == '' else partial.find(left) + len(left)
                    partial = partial[p_from:]
                    p_to = len(partial) - 1 if right == '' else partial.find(right)
                    parsed = partial[:p_to]
                    list.append(parsed)
                    partial = partial[len(parsed) + len(right):]
            except Exception as e:
                pass  # Handle exceptions or log as needed
    else:
        if use_regex:
            try:
                pattern = build_lr_pattern(left, right)
                mc = list(re.finditer(pattern, partial))
                if mc:
                    list.append(mc[0].group())
            except Exception as e:
                pass  # Handle exceptions or log as needed
        else:
            try:
                p_from = 0 if left == '' else partial.find(left) + len(left)
                partial = partial[p_from:]
                p_to = len(partial) if right == '' else partial.find(right)
                list.append(partial[:p_to])
            except Exception as e:
                pass  # Handle exceptions or log as needed

    return list
