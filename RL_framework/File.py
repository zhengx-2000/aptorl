def alter(file_old, file_new, line_num, old_str, new_str):
    """
    A method to replace specified string in a file

    Parameters:
        file_old: input file name
        file_new: output file name
        line_num: the row of code needed to be modified (start from 0)
        old_str: the string needed to be replaced
        new_str: the string being to replace the old string

    Return:
        1 for nothing replaced, 0 for operation successful
    """
    file_data = ''
    state = 1
    with open(file_old, 'r') as g:
        test_line = g.readlines()[line_num]
    g.close()
    with open(file_old, "r") as f:
        for line in f:
            if old_str in line and line == test_line:
                line = line.replace(old_str, new_str)
                state = 0
            file_data += line
    f.close()
    with open(file_new, "w") as f:
        f.write(file_data)
    f.close()
    return state


def line_count(file):
    """
    A simple method to tell the total line number in the file
    """
    with open(file, 'r') as f:
        return len(f.readlines())
