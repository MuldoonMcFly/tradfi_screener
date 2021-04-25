

#  Contains all the functions needed for this module

from apis.constants import sandbox


#  For the IEX Cloud API calls, delivers the right token and version for when either Sandbox or Production is turned on, and sends along a warning if Sandbox is on.
if sandbox:
    iex_token = 'Tsk_8ada74e0932141b982408148b13d107d'
    iex_version = 'sandbox'
    print("""

!!

Sandbox is turned on!

!!

""")
else:
    iex_token = 'sk_552fce3cd32a4293be7b56fac900b651'
    iex_version = 'stable'
