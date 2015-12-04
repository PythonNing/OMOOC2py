#qpy:console
#qpy:2
'''for QPy can usage normal system python , gen. all need Adnorid /etc/profile
usage:
    - upload this script into mobile
    - normal in /storage/sdcard0/com.hipipal.qpyplus/projects/YouProject
    - call in QPython "My QPython->projects->YouProject->gen_qpy_env.py"
config as default env:
# mount -o remount,rw /dev/block/mtdblock3 /system
# ln -s /storage/sdcard0/com.hipipal.qpyplus/projects/qpy_profil /etc/profile
# mount -o remount,ro /dev/block/mtdblock3 /system
so every time restart SSH in Android, will load the /etc/profile
can test every thing is good now:
# python
Python 2.7.2 (default, Dec 27 2013, 23:19:48)
[GCC 4.6 20120106 (prerelease)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
'''

import os
fd = open("/sdcard/qpyenv.sh", "w")
fd.write("TERM=%s\n" % os.environ.get("TERM"))
fd.write("PATH=%s\n" % os.environ.get("PATH"))
fd.write("LD_LIBRARY_PATH=%s\n" % os.environ.get("LD_LIBRARY_PATH"))
fd.write("PYTHONHOME=%s\n" % os.environ.get("PYTHONHOME"))
fd.write("ANDROID_PRIVATE=%s\n" % os.environ.get("ANDROID_PRIVATE"))
fd.write("PYTHONPATH=%s\n" % os.environ.get("PYTHONPATH"))
fd.write("PYTHONSTARTUP=%s\n" % os.environ.get("PYTHONSTARTUP"))
fd.write("PYTHONOPTIMIZE=%s\n" % os.environ.get("PYTHONOPTIMIZE"))
fd.write("TMPDIR=%s\n" % os.environ.get("TMPDIR"))
fd.write("AP_HOST=%s\n" % os.environ.get("AP_HOST"))
fd.write("AP_PORT=%s\n" % os.environ.get("AP_PORT"))
fd.write("AP_HANDSHAKE=%s\n" % os.environ.get("AP_HANDSHAKE"))
fd.write("ANDROID_PUBLIC=%s\n" % os.environ.get("ANDROID_PUBLIC"))
fd.write("ANDROID_PRIVATE=%s\n" % os.environ.get("ANDROID_PRIVATE"))
fd.write("ANDROID_ARGUMENT=%s\n" % os.environ.get("ANDROID_ARGUMENT"))