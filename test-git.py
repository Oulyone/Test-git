from cgi import test
from importlib.resources import path
from msilib.schema import Directory
from telnetlib import STATUS


def hello(time):
    for count in range(1,time):
        print('hello')
try:
    time = int(input('Enter how many time do you want to print hello: '))
except ValueError as err:
    print(err)

hello(time)


# git clone https://github.com/Oulyone/Test-git.git

# get in Test-git path

# git status

# git add test-git.py

# git commit -m"message"

# git push

# Create new branch

# git branch newBranch

# git checkout newbranch

