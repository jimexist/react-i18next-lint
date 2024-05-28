from react_i18next_lint.commands.extract_keys import flatten_keys_on_dict


def test_flatten_keys_on_dict():
    data = {
        "a": {
            "b": {
                "c": 1,
                "d": 2,
            },
            "e": 3,
        },
        "f": 4,
    }
    assert list(flatten_keys_on_dict(data)) == [
        ("a.b.c", 1),
        ("a.b.d", 2),
        ("a.e", 3),
        ("f", 4),
    ]
