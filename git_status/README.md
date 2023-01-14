# Welcome to the Git Status ReadMe

## Was it Rufus?

This mini program checks the git status of any local git repository and if the last commit was authored by Rufus. 🤔

If you would like to try it yourself, follow the steps below:
  1. Clone the repo to your local computer
  2. Make sure you have python installed. In case you don't, here is the link https://www.python.org/. You can also check by typing the following in the command line:
  ```
  python --version
  ```
  If a version number comes up, you have python, if not, you will need to download it.

  3. Navigate inside the project folder using the command line
  4. Run the following line of code:
  ```
  pip install gitpython pytz
  ```
  5. Now you are ready to roll! Open up the git_status.py in your favorite code editor and try it out by following further instructions in the file.

You will see the Active Branch, if there are local branch changes, if there has been a commit in last week and if Rufus was the author of the last commit all printed to the terminal! Note: If this program is fun on a file path that is not a git repository, you will receive an error message.
