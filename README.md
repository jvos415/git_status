# Welcome to the Git Status ReadMe

## Was it Rufus?

This mini program checks the git status of any local git repository and if the last commit was authored by Rufus. 🤔

If you would like to try it yourself, follow the steps below:
  1. Clone the repo to your local computer
  2. Make sure you have python installed. In case you don't, here is the link https://www.python.org/. You can also check by typing the following in the command line:
  ```
  python --version
  ```
  If a version number comes up, you have python, if not, you will need to download it using the link provided above.

  3. Navigate inside the project folder using the command line:
  ```
  cd git_status
  ```
  4. Run the following line of code:
  ```
  pipenv install
  ```
  5. Enter your python shell with:
  ```
  pipenv shell
  ```
  6. Now you are ready to roll! Open up the git_status.py file and follow the instructions for entering a file path at the end of the file.

  7. To test your file using the program you can run:
  ```
  python git_status/git_status.py
  ```
  Or you can navigate into git_status folder Using
  ```
  Cd git_status
  ```
  And then run
  ```
  Python git_status.py
  ```

You will see the Active Branch, if there are local branch changes, if there has been a commit in last week and if Rufus was the author of the last commit all printed to the terminal! Note: If this program is run on a file path that is not a git repository, you will receive an error message.
