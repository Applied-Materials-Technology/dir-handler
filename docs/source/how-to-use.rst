=================================
How to Use
=================================

Dir-handler uses JSON templates to create directory structures.
An example can be seen below:

.. code-block:: json

    {
        "folder1": {
            "folder11": {
                "folder111": {},
                "folder112": {}
            },
            "folder12[testword]": {
                "folder121": {},
                "folder122": {}
            },
            "folder13[testword_list]": {
                "folder131": {},
                "folder132": {},
                "folder133[2]": {}
            },
            "folder14": ["folder141", "folder142[2]", "folder143"]
        }
    }

Square brackets `[]` indicate placeholder, which can come in three forms:

- Integers: Will make the folder x amount of times, including subfolders
- Strings: Will replace the contents of the `[]` with a Strings
- Lists: Will create a folder for each list item, where the contents of `[]` are the list items

Placeholder values for strings and lists can be set with a translations dictionary. For example:

.. code-block:: json
    translations = {"testword_list": ["one", "two", "three"], "testword":"mytestword"}

Separator values can be set to specify what will separate the base folder name and the placeholder
value:

.. code-block:: python

    separators = ["-",":",":"]

The first value in the list is the integer separator, the second the string separator, and the third
the list separator. 

The above separator example would create `folder-1` from `folder[1]`, and `folder:value` from `folder[value]`.

=================================
Usage Options
=================================
=================================
Terminal
=================================

Use the `makedirs` command in your terminal.

Options:

--filename : path to json file to read structure, default = 'examples/json_template.json'

--x : takes example file structures when present without specifiying full path to examples

--translations : dictionary of translations for placeholders, default = {}

--separator : list of values to separate placeholders and base folder names, default = ["", "", ""]

Example Usage:

Create folders from the default example file stored at src/dirhandler/examples/json_template.json in your current directory:

.. code-block:: bash

    makedirs -x

Create folders from a specific example file stored at src/dirhandler/examples/ in your current directory:

.. code-block:: bash

    makedirs --filename examples/name_of_example.json -x

Create folders from a specific JSON file in your current directory:

.. code-block:: bash

    makedirs --filename path/to/file.json

Create folders from a specific JSON file with a translations dictionary:

.. code-block:: bash

    makedirs --filename path/to/file.json --translations {"my":"dict"}

=================================
Import in Python Script
=================================

Import the directory maker:

.. code-block:: python

    import dirhandler as dh

Set translation dictionary if required:

.. code-block:: python

    translations = {"testword_list": ["one", "two", "three"], "testword":"mytestword"}

Create folders from the default example file stored at src/dirhandler/examples/json_template.json in your current directory:

.. code-block:: python

    dh.json_maker.start(example=True)

Create folders from a specific JSON:

.. code-block:: python
    
    dh.json_maker.start(filename = "path/to/file.json", example=True)

