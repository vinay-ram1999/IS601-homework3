# Homework 3

Removed remote origin from my Homework 2 local repository and added a new remote origin to this GitHub repo (Now this repo contains all the contents of Homework2 master branch)

## Install

* To install this application in your local machine:
```
git clone git@github.com:vinay-ram1999/IS601-homework3.git
pip3 install -r requirements.txt
```

## Run Tests

* After installing the dependencies, to run the test cases:
```
pytest --pylint --cov <-Runs tests, pylint, and coverage to check if you have all your code tested.
```

## Modifications

I have implemented sevaral modifications to the calculator functionality, which are:

1. Implemented Single-input and Dual-input calculations
2. Added sigma (sum of n numbers) operation to the operations (which is a single-input operation)
3. For saving history, only the input values and the operation name are being stored, in my code I have history which stores all the previous funstionalities and also stores the calculated/measured output in a dictonary
4. Implemented sufficients test cases for all existing and new functionalities in pytest

Note: The `my_test.py` file is used to directly run and check the calculator outputs. In-order to implement that make sure to export the `PYTHONPATH' variable to the virtual environment (follow the steps below to do it)

```
# Edit venv/bin/activate
nano venv/bin/activate

# Add this line with the path to your projects root folder (the parent directory of calculator folder in your project)
export PYTHONPATH='/user/name/path/to/the/folder'

# Add this line in the deactivate function
unset PYTHONPATH # This will reset this variable once you deactivate your venv

# save the changes and close the venv/bin/activate file

source venv/bin/activate
echo $PYTHONPATH # Check if this returns the path you have entered

# Now, you can run my_test.py and play around
python3 my_test.py
```
