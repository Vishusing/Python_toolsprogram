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



# import subprocess

# def restart_computer():
#   """
#   Restarts the computer using the subprocess module.
#   """
#   # Platform-specific commands
#   if platform.system() == "Windows":
#     command = ["shutdown", "-r", "-t", "0"]
#   elif platform.system() == "Linux":
#     command = ["reboot"]
#   else:
#     raise NotImplementedError("Restarting computer is not implemented for this platform.")

#   # Execute the command
#   subprocess.call(command)

# # Run the function to restart the computer
# restart_computer()
# print("Computer is restarting...")

