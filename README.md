# react-i18next-lint

[![Python CI](https://github.com/jimexist/react-i18next-lint/actions/workflows/ci.yaml/badge.svg)](https://github.com/jimexist/react-i18next-lint/actions/workflows/ci.yaml)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/react-i18next-lint)](https://pypi.org/project/react-i18next-lint/)

A small lint tool for [react-i18next][18n].

## Install

```bash
poetry install
```

## Execution

**Usage**:

```console
$ react_i18next_lint [OPTIONS] COMMAND [ARGS]...
```

**Options**:

- `--install-completion`: Install completion for the current shell.
- `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
- `--help`: Show this message and exit.

**Commands**:

- `extract-keys`: Extract all the keys from i18n phrases...
- `group-key-locales`: Group the phrases tsv file extracted from...
- `validate-keys`: Validate the keys in the source code given...

### `react_i18next_lint extract-keys`

Extract all the keys from i18n phrases files under RESOURCE_PATH, structure them into
tsv files and write to OUTPUT if supplied, or stdout if absent

**Usage**:

```console
$ react_i18next_lint extract-keys [OPTIONS] RESOURCE_PATH
```

**Arguments**:

- `RESOURCE_PATH`: [required]

**Options**:

- `--output FILENAME`
- `--help`: Show this message and exit.

### `react_i18next_lint group-key-locales`

Group the phrases tsv file extracted from the extract_key script as given by PHRASES_FILE,
group by scope and key, and aggregate the locales, write out to OUTPUT_PATH as tsv file

**Usage**:

```console
$ react_i18next_lint group-key-locales [OPTIONS] PHRASES_FILE OUTPUT_PATH
```

**Arguments**:

- `PHRASES_FILE`: [required]
- `OUTPUT_PATH`: [required]

**Options**:

- `--help`: Show this message and exit.

### `react_i18next_lint validate-keys`

Validate the keys in the source code given by SOURCE_CODE_DIR against the keys in the resource file
provided in SCOPE_KEY_FILE tsv (transformed by `group_key_locales` script).

**Usage**:

```console
$ react_i18next_lint validate-keys [OPTIONS] SCOPE_KEY_FILE SOURCE_CODE_DIR
```

**Arguments**:

- `SCOPE_KEY_FILE`: [required]
- `SOURCE_CODE_DIR`: [required]

**Options**:

- `--ignore-dynamic-key / --no-ignore-dynamic-key`: [default: ignore-dynamic-key]
- `--print-unused-phrases / --no-print-unused-phrases`: [default: no-print-unused-phrases]
- `--help`: Show this message and exit.

## Development

### Running pytest

```bash
poetry run pytest
```

### Build and publish

```bash
poetry publish --build
```

[18n]: https://react.i18next.com/
