# dir-handler

Create directory structures from JSON files 

### Warning
This tool is under development and may give errors. Please check any output before using. 

## Installation:

### Virtual Environment

You may wish to use a virtual environment e.g. with `venv`:

```
python -m venv dirhandler-env
source dirhandler-env/bin/activate
```

### Standard Installation

Clone to your local system and `cd` to the root directory of `dirhandler`. Ensure you virtual environment is activated and run from the `dirhandler` root directory:

```
pip install .
```

### Developer Installation

To create an editable installation, follow the instructions for a standard installation but run:

```
pip install -e .
```

## Usage and Options

### Terminal

**Example Usage**
Make sure your virtual environment with the package installed is activated.

Create folders from the default example file stored at src/dirhandler/examples/json_template.json in your current directory:
```shell
makedirs -x
```

Create folders from a specific example file stored at src/dirhandler/examples/ in your current directory:
```shell
makedirs --filename examples/name_of_example.json -x
```

Create folders from a specific JSON file in your current directory:
```shell
makedirs --filename path/to/file.json
```

Create folders from a named template (no `.json` needed, resolved via `filename_opts.set_json`):
```shell
makedirs --filename example -x
makedirs --filename processed -x
```
`example` resolves to `json_template.json`, `processed` resolves to `processeddata.json`. Any other name without `.json` falls back to `json_template.json`.

Create folders from a specific JSON file with a translations dictionary:
```shell
makedirs --filename path/to/file.json --translations {"my":"dict"}
```

Create folders with custom separators and test output path:
```shell
makedirs --filename path/to/file.json -x --separator ["-","_","~"] --testing
```

**Options**
- --filename : path to json file to read structure, default = 'json_template.json'. If the value does not end in `.json` it is treated as a template name (`example`, `processed`) and resolved with `set_json`.
- --example / -x : takes example file structures when present without specifiying full path to examples (looks in `src/dirhandler/examples/`)
- --testing / -t : write output to `./testpath/my_generated_project` instead of `./my_generated_project`
- --translations : dictionary of translations for placeholders, default = {}
- --separator : list of values to separate placeholders and
base folder names, default = ["", "", ""]. Order is `[int, str, list]`. A single string is reused for all three. A 2-element list uses the second value for both `str` and `list`.

### Import in Python Script

Make sure your virtual environment with the package installed is activated.

Import the directory maker
```python
import dirhandler as dh
```

Set translation dictionary if required:

```python
translations = {"testword_list": ["one", "two", "three"], "testword":"mytestword"}
```

Create folders from the default example file stored at src/dirhandler/examples/json_template.json in your current directory:
```python
dh.json_maker.start(example=True)
# equivalent to:
# import dirhandler as dh
# dh.start(example=True)
```

Create folders from a specific JSON file, a named template, or an example file:
```python
dh.json_maker.start(filename = "path/to/file.json")
dh.json_maker.start(filename = "example", example=True)
dh.json_maker.start(filename = "processed", example=True)
dh.json_maker.start(filename = "path/to/file.json", example=True)
```

Full example with translations, separators, and testing path:
```python
dh.json_maker.start(filename = "json_template.json",
                    example = True,
                    testing = True,
                    translations = translations,
                    separator = ["-", " ", "~"])
```
- `example=True` loads from `src/dirhandler/examples/`
- `testing=True` writes to `./testpath/my_generated_project` instead of `./my_generated_project`
- `separator=[int_sep, str_sep, list_sep]` controls joining of base names and placeholders
- `filename` without `.json` is resolved as a named template (`example` -> `json_template.json`, `processed` -> `processeddata.json`)

Only `dirhandler.json_maker` is public (`dh.start`, `dh.create_structure`, `dh.parse_placeholder`). Legacy modules `levels`, `foldermaker`, `make_struct`, and `replacer` were removed.

## Creating JSON structures

The following shows how a directory structure file could look, where subfolders could be represented by another dictionary, or a list.

```json
{
    "folder1": {
        "folder11": {
            "folder111": {},
            "folder112": {}
        },
        "folder12": {
            "folder121": {},
            "folder122": {}
        },
        "folder13[testword]": {
            "folder131": {},
            "folder132": {},
            "folder133[2]": {}
        },
        "folder14": ["folder141", "folder142[2]", "folder143"]
    }
}
```
Square brackets represent where foldernames contain placeholders. In the example above, `folder13[testword]` and `folder142[2]`. Placeholders can be
integers or strings.

An integer placeholder such as `folder142[2]` should create two folders, `folder1421` and `folder1422`.
With `separator=["-", "", ""]` it would create `folder142-1` and `folder142-2` (first separator entry is for integers).

A string placeholder requires a translations dictionary.

With a translation dictionary of:

```
translations = {"testword": "myword"}
```

`folder13[testword]` will create one folder - `folder13myword` (second separator entry is for single strings, e.g. `folder13-myword` with `separator=["", "-", ""]`).

With a translation dictionary of:

```
translations = {"testword": ["one", "two", "three"]}
```

`folder13[testword]` will create three folders - `folder13one`, `folder13two`, `folder13three` (third separator entry is for lists, e.g. `folder13~one` with `separator=["", "", "~"]`).