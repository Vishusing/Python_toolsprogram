import os

def restart_computer():
  """
  Restarts the computer immediately.
  """
  os.system("shutdown /r /t 0")

if __name__ == "__main__":
  # Ask user for confirmation before restarting
  confirmation = input("Are you sure you want to restart the computer? (y/n): ")

  if confirmation.lower() == "y":
    restart_computer()
  else:
    print("Computer restart canceled.")
