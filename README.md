# taipy-gui-ext-konva

A [Taipy GUI](https://github.com/Avaiga/taipy-gui) extension library that contains the `stage`
visual element, allowing to display and interact with 2D shapes.

## Prerequisites

To build the extension library, you need to have installed:

- Python 3.9 or above
- Node 18.2 or above (and npm)
- Taipy GUI 4.0 or above

## Repository structure

- `README.md`: this file.
- `demo.py`: Python script demonstrating the usage of the library.
- `pyproject.toml`: Python project settings file for the extension library package.
- `MANIFEST.in`: This file lists the commands to be executed when the Python package
  is built as a source distribution.
- `taipy_konva/`: The directory where all the Python and TypeScript code for
   the extension library can be found.<br/>
   This directory contains the following:
   - `front-end/`: The directory where all the front-end code is located.<br/>
      This directory contains the following:
      - `src/`: Where the source files for components are located.
         - `index.ts`: the entry point for the front-end bundle.<br/>
           This file typically just exports all the component classes so Taipy GUI can
           use them.
         - `Stage.tsx`: TypeScript source for the React component associated with
           the custom element called "stage".
      - `scripts/install.js`: a JavaScript script used by `npm` when installing the
        dependencies for building the main JavaScript bundle of the extension library.
      - `package.json`: Holds the meta-data for the Node project.
      - `tsconfig.json`: Holds the options to compile the TypeScript project.

## Building the extension library

You must take several steps to build the Python package that holds the extension library
and the JavaScript code it uses.

### Setting up the JavaScript build

- Change your directory to where the front-end code is located:<br/>
  `cd taipy_konva/front-end`
- Install the packages that your library depends on:<br/>
  `npm install`<br/>
  This will run a NodeJS script that installs the Taipy GUI Extension API library.<br/>
  This command will fail if the environment variable "TAIPY_DIR" is not set properly.

The 'front-end' directory will have an additional subdirectory called 'node_modules' where all
dependent libraries are installed.

### Building the JavaScript bundle

To build the JavaScript bundle that holds the code for the front-end part of the extension
library, you must still be in the 'front-end' directory and run:
`npm run build`

Note that you can use `npm run build:dev` to keep debugging information to
spot and fix potential problems in your TypeScript code.

An additional directory called 'dist' is created in the 'front-end' directory, where
your JavaScript bundle was created.

### Testing the extension library

Now that the JavaScript bundle of the extension library is built, you can run the
[test application](demo.py) to verify it works properly.<br/>
Your current directory must be set to the root directory of the repository.

Assuming your Python environment is properly setup (that is, Taipy GUI is installed),
you can run the following:

```
python demo.py
```

A Taipy GUI application is launched, and your browser opens on the test page that
displays the custom visual element.

### Accessing the library's elements from the Page Builder API

At runtime, and *after* the library is registered (that is, after `Gui.add_library()` is invoked),
functions are dynamically added to the library's module to access its elements, exposing them with
the Page Builder API.

A typical code will look like:
```python
import taipy_konva

...

with tgb.Page() as page:
  ...
  taipy_konva.stage(<properties>)
  ...
```

To provide developers with autocompletion and type checking when coding, you can generate a Python
Interface Definition file next to your module's `__init__.py` file that will define function stubs
for every element of the extension library, with their properties, including their potential
documentation.

To create the Python Interface Definition file (called `__init__.pyi`, located next to the 
`__init__.py` file), go to the project directory (above the '<package_dir_name>' directory) and
run:
```sh
python -m taipy.gui.extension generate_tgb <package_dir_name>
```
This file will provide support for developers in their IDEs.

### Packaging the extension library

If you wish to use your custom Taipy GUI extension library in several projects or share
it with other users of Taipy GUI, you can turn it into a standalone Python package.

From the root directory of this repository, run:

```
pip install build
python -m build
```

This creates a directory called 'dist' where the Taipy GUI extension library
has been packaged into a file called `taipy_konva-1.0.0.tar.gz`.<br/>
You can distribute this file as a regular Python package archive.
