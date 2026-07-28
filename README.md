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

Create folders from a specific JSON file with a translations dictionary:
```shell
makedirs --filename path/to/file.json --translations {"my":"dict"}
```

**Options**
- --filename : path to json file to read structure, default = 'examples/nestedtstruc.json'
- --x : takes example file structures when present without specifiying full path to examples
- --translations : dictionary of translations for placeholders, default = {}

### Import in Python Script

Make sure your virtual environment with the package installed is activated.

Import the directory maker
```python
import dirhandler as dh
```

Create folders from the default example file stored at src/dirhandler/examples/nestedstruct.json in your current directory:
```python
dh.levels.start(x=True) 
```

Create folders from a specific JSON file in a specific directory:
```python
dh.levels.start(filename = "path/to/file.json", location = "path/to/dir_creation")
```

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
Square brackets represent where foldernames contain placeholders. In the example above, folder3[testword] and folder142[2]. Placeholders can be
integers or strings.

An integer placeholder such as folder142[2] should create two folders, folder1421 and folder1422.

A string placeholder requires a translations dictionary.

With a translation dictionary of:

```
translations = {"testword", "myword"}
```

folder3[testword] will create one folder - folder3myword.

With a translation dictionary of:

```
translations = {"testword", ["one","two,"three]}
```

folder[testword] will create three folders - folder3one, folder3two, folder3three.