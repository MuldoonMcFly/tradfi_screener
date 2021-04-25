

#  Stores all the constants for this module

from apis.tokens import sandbox_token, production_token

#  Change this to switch between IEX Cloud's Sandbox or Production API.
sandbox = False


#  IEX Cloud Sandbox token and version, needed for API call arguments
sb_token = sandbox_token
sb_version = 'sandbox'


#  IEX Cloud Production token and version, needed for API call arguments
prod_token = production_token
prod_version = 'stable'
