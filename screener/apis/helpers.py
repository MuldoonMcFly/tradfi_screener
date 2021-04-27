

#  Contains all the functions needed for this module

from apis.constants import sandbox, sb_token, prod_token


#  For the IEX Cloud API calls, delivers the right token and version for when either Sandbox or Production is turned on, and sends along a warning if Sandbox is on.
if sandbox:
    iex_token = sb_token
    iex_version = 'sandbox'
    print("""

!!

Sandbox is turned on!

!!

""")
else:
    iex_token = prod_token
    iex_version = 'stable'
