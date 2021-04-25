

#  Calls all the functions and constants needed for this module. This file should be called by main.py.

import pyEX as pyex
from apis.helpers import iex_token, iex_version


#  Delivers connection to the IEX Cloud APIs and warns if the Sandbox is turned on.
iex_api = pyex.Client(api_token=iex_token, version=iex_version)


# print(iex_token, iex_version)
