import os


def toggle(name):
    if not os.path.exists(name):
        print name + " does not exist"
        return

    new_name = _get_name(name)
    if os.path.exists(new_name):
        print new_name + " already exists. Will not switch"
    else:
        os.rename(name, new_name)


def _get_name(name):
    if name.startswith("."):
        return name[1:]
    else:
        return "." + name
