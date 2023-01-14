import git
import datetime
import pytz

utc=pytz.UTC

def git_status(git_dir):
  try:
    repo = git.Repo(git_dir)
    head = repo.head
    active_branch = repo.active_branch
    local_changes = repo.is_dirty()
    last_week = datetime.datetime.now().replace(tzinfo=utc) - datetime.timedelta(weeks=1)
    authored_recently = head.commit.authored_datetime > last_week
    authored_by_rufus = head.commit.author.name == "Rufus"
    print(f"Active Branch: {active_branch}")
    print(f"Local Changes: {local_changes}")
    print(f"Recent Commit: {authored_recently}")
    print(f"Blame Rufus: {authored_by_rufus}")
  except:
    print("An error occurred. Path may not be a git repository.")

# Sample local path test below, simply uncomment the line below and fill in a local path to test the program
# git_status("sample/local/path/to/git/repo")