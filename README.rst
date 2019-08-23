# name-mc

This python project will help you get informations from the minecraft website "namemc.com"
To add this set of utils to your python project, simply add the "name-mc" folder into your project folder, rename it whatever you want, then, using sys in your project, do
This module has been tested for the python version 3.7.3 "sys.path.insert(1, 'path/to/folder')"
This module has been tested for the namemc.com version of the 07/31/2019
Here's a list of all the functions:
  
  Check if a name is avialable:
  ---------------------------------------
  from name-mc import name
  
  
  if name.is_avialable("Name"):
   # Do Stuff (Name is avialable)
  elif not name.is_avialable("Name"):
    # Do Stuff (Name is unavialable)
  elif name.is_avialable("Name") == "Too Long":
    # Do Stuff (Name is too long)
  elif name.is_avialable("Name") == "Invalid Characters":
    # Do Stuff (Name contains invalid characters)



  Check montly searches of a name:
  ---------------------------------------
  from name-mc import name
  
  
  montly_searches = name.montly_searches("Name")
  print(montly_searches)  # Example: 6 / Month
  
  
  
  Find matching uuid for a name:
  ---------------------------------------
  from name-mc import name
  
  
  uuid = name.matching_uuid("Name")
  if uuid:
    print(uuid)  # Example: ccf4ef75-7614-4208-b2bd-162d572db18d
  else:
    # Do stuff (Name doesn't have a matching UUID)
  
  
  
  Get an account previous names:
  ---------------------------------------
  from name-mc import account
  
  
  names = account.get_previous_names("Account-Name")
  if names:
    print(names)  # Example: [Pippo123, Gianni47, Marco22]
  else:
    # Do stuff (Name doesn't exist or page wasn't found)



  Get the command to give yourself a player head:
  ---------------------------------------
  from name-mc import account
  
  
  commands = account.get_head_command("Account-Name")
  if commands:
    print(commands)  # Example: [Command-1.13+, Command-1.12-]
  else:
    # Do stuff (Name doesn't exist or page wasn't found)



  Find matching name for an uuid:
  ---------------------------------------
  from name-mc import uuid
  
  
  name = uuid.matching_name("UUID")
  if name:
    print(name)
  else:
    # Do stuff (Name doesn't exist or page wasn't found)
