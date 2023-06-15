# simple_python_webapp using Flask framework

# About search4letters module

**search4letters** is a custom python module installed as a third party module into site packages directory. The module contains two functions. The module's code is provided by Head First Python book.

Here's the complete content of the module.

```python
def search4vowels(phrase: str) -> set:
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))

```

## The algorith of turning a local module into a distribution and installing the module
### 1. Create a distribution description
**This identifies the module we want "setuptools" to install.**  
    - create 'setup.py' - a distribution description file for setuptools mechanism  
    - create readme file (can be empty) - the setuptools requires the distribution to have a readme file  

### 2. Generate a distribution file
**Using Python at the command line/terminal, we'll create a shareable distribution file to contain our module's code.**  
    - create a distribution file on UNIX-like OSes  
    ```
    $: python3 setup.py sdist
    ```

### 3. Install the distribution file
**Again, using Python at the command line/terminal, install the distribution file (which includes out module) into site-packages.**  
    - On Linux, Unix, or Mac OS. open a terminal within the newly created *dist* folder, and the issue thid command at the promt"  
    ```
    .../dist$: sudo python3 -m pip install vsearch-1.0.tar.gz
    ```





# Source of static files
- https://github.com/EiChinn/HeadFirstPython2/blob/master/chapter5/webapp/static/hf.css


## Some commands
- pycodestyle vsearch4web.py - check for PEP8 compliance