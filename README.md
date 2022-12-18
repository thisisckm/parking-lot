# Parking Lot
> version 1.0

[![codecov](https://codecov.io/gh/thisisckm/parking-lot/branch/develop/graph/badge.svg?token=WTBSORM45B)](https://codecov.io/gh/thisisckm/parking-lot)

Parking Lot is used to calculate the parking fee after unparking.

This version of Project Lot should be called as backend module of Parking Lot, because of no UI is used either GUI or TUI.

## Testing Process
### Setup
Assuming that the testing process is run on Linux based system. 
### Prerequisite
1. git - Install the latest version of git
2. python 3.11+
3. Python virtualenv if it's not installed already
### Prepare test enviorment
1. Clone the code from GitHub
```
$ git clone git@github.com:thisisckm/parking-lot.git
```
2. Switch to the parking-lot folder
```
$ cd parking-lot
```
3. Create the python virtualenv and activate it
```
$ python3 -m venv .venv
$ . .venv/bin/activate
```
4. Install required python libraries
```
$ pip install -r requirements.txt
```
### Steps to run the tests
The test cases are written using pytest testing module. The following command will run the test cases.
```
$ pytest 
```
### Steps to check the code quality
```
$ mypy src/process.py
```
### Configuration file
Some example configuration file available in config and test_config folder.

 