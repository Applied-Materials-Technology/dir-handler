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

Create folders from the default example file stored at src/dirhandler/examples/nestedstruct.json in your current directory:
```shell
makedirs -x
```

Create folders from a specific example file stored at src/dirhandler/examples/ in your current directory:
```shell
makedirs -x --filename examples/name_of_example.json
```

Create folders from a specific JSON file in your current directory:
```shell
makedirs --filename path/to/file.json
```

Create folders from a specific JSON file in a specific directory:
```shell
makedirs --filename path/to/file.json --location path/to/dir_creation
```

**Options**
- --x : takes example file structures when present without specifiying full path to examples
- --filename : path to json file to read structure, default = 'examples/nestedtstruc.json'
- --location : path to create folders in, default = '.'

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

JSON directory files should follow the following structure

```json
{
  "folder1": {
    "folder11": {
      "folder111":{},
      "folder112":{},
      "folder113":{}
    },
    "folder12": {
      "folder121": {},
      "folder122": {}
    },
    "folder13": {
      "folder131": {},
      "folder132": {}
    },
    "folder14": {}
  },
  "folder2": {}
}
```

which will result in the following folders:

<img width="185" height="293" alt="image" src="https://github.com/user-attachments/assets/a1fb2790-1bad-490f-aaac-1059165344fa" />
