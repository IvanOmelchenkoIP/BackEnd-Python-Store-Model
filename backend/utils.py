def contains(storage, attribute, value):
    for element in storage:
        if str(element[attribute]) == str(value):
            return True
    return False

def select(storage, attribute, value):
    selected = []
    for element in storage:
        if str(element[attribute]) == str(value):
            selected.append(element)
    return selected
