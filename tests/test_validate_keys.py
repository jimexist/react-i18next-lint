from dataclasses import astuple
from pathlib import Path

from react_i18next_lint.commands.validate_keys import LineInfo, init_count_dict


def test_init_count_dict():
    scope_key_dict = {
        "common": {"key1": ["en"], "key2": ["en"]},
        "home": {"key3": ["en"]},
    }
    assert init_count_dict(scope_key_dict) == {
        "common": {"key1": 0, "key2": 0},
        "home": {"key3": 0},
    }


def test_line_info_parsing():
    line = "/packages/app/src/pages/Membership/PaymentLanding.tsx:193:t"
    source_file_path, line_no, scope, key = astuple(LineInfo.from_grep_line(line))
    assert source_file_path == Path(
        "/packages/app/src/pages/Membership/PaymentLanding.tsx"
    )
    assert line_no == 193
    assert scope == "common"
    assert key == "t"
