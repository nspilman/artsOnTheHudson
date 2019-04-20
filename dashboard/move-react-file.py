import os
import shutil

try:
    shutil.move("dashboardreact/build/index.html", "templates/dashboard/index.html")
except:
    pass

try:
    shutil.move("dashboardreact/build/static/css", "static/css")
except:
    pass