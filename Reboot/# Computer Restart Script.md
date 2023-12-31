 # Computer Restart Script

This script provides two methods to restart a computer: one using the `os` module and another using the `subprocess` module. Both methods are explained in detail below, along with instructions on how to use the script.

## Prerequisites

Before using this script, ensure that you have the following:

- Python 3 or later installed on your computer. 
- Administrator privileges to restart the computer.

## Method 1: Using the `os` Module

This method uses the `os.system()` function to execute the `shutdown` command on Windows or the `reboot` command on Linux. Here's a step-by-step explanation of the code:

```python
import os

def restart_computer():
  """
  Restarts the computer immediately.
  """
  os.system("shutdown /r /t 0")
```

- We import the `os` module, which provides functions for interacting with the operating system.
- We define a function called `restart_computer()` that takes no arguments.
- Inside the function, we use the `os.system()` function to execute the `shutdown` command on Windows or the `reboot` command on Linux. The `/r` flag specifies that we want to restart the computer, and the `/t 0` flag specifies that we want to restart immediately without any delay.

## Method 2: Using the `subprocess` Module

This method uses the `subprocess` module to execute the `shutdown` or `reboot` command. Here's a step-by-step explanation of the code:

```python
import subprocess

def restart_computer():
  """
  Restarts the computer using the subprocess module.
  """
  # Platform-specific commands
  if platform.system() == "Windows":
    command = ["shutdown", "-r", "-t", "0"]
  elif platform.system() == "Linux":
    command = ["reboot"]
  else:
    raise NotImplementedError("Restarting computer is not implemented for this platform.")

  # Execute the command
  subprocess.call(command)
```

- We import the `subprocess` module, which provides functions for creating and managing subprocesses.
- We define a function called `restart_computer()` that takes no arguments.
- Inside the function, we first check the platform using the `platform.system()` function. If the platform
