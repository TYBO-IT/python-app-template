# Python Template

Helps you getting started creating python applications. The architecture is heavily inspired by Java and Spring Boot, and it is our intention to gradually improve this over time, so that we can achieve a level of dependency injection and inversion to make further development a breeze.

## Prerequisites
```bash
# On Ubuntu:
sudo apt install python3.10-venv
```

## Setup project and install dependencies

```bash
# Creates virtual environment
python -m venv venv

# Jump into the virtual environment
## IF Windows:
# .\venv\Scripts\Activate.ps1

## IF on Ubuntu/Linux:
source venv/bin/activate


# Install dependencies
pip install -r requirements.txt
```

## Run Project

- Edit `src/main/resources/application.yml` and populate with desired values.  
- Run `src/main/python/main.py` from commandline or the IDE. If you are using an IDE other than VS Code, please generate a gitignore (see `.gitignore` for edit URL)

# Contributions

Contributions are always welcome from anyone. 

## How to Contribute in 1-2-3-4-5

1. Fork this project
2. Create a branch of your own
3. Make changes
4. Create PR asking to merge to our branch
5. Await feedback

- Don't forget to run the activation script in /venv/Scripts/ before installing: `pip install -r requirements.txt`  
- If you add a dependency, remember to update requirements.txt by running: `pip freeze > requirements.txt`  

----

# MIT License

Copyright (c) 2022 Ivan Skodje

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.