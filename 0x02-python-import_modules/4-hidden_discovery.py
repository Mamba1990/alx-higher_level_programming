#!/usr/bin/python3

if __name__ == "__main__":
    """Display the names defined by hidden_4 module."""
    import hidden_4

    _names = dir(hidden_4)
    for _name in _names:
        if _name[:2] != "__":
            print(_name)
