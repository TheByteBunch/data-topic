
def get_change(array):
    result = []
    for index, item in enumerate(array):
        if(index + 1 == len(array)):
            continue
        result.append(array[index+1] - array[index])

    return result