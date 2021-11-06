import os
print ( os.path.dirname(__file__).replace("/psqlHelper", "/").replace("\psqlHelper", "\\") + "settings.conf")