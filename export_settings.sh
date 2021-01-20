
#!/bin/bash

# this will read all html files and replace dj-* attributes with django code
# YOU MAY NEED TO copy the python export.py script to the same folder as where BSS app image is located

logfile="/tmp/bss_export.log"

# if you have a venv setup, replace the following
source ~/.pyenv/versions/3.7.7/envs/python_tools/bin/activate

echo "run at `date`" >> $logfile
echo "`which python3`" >> $logfile
echo /Users/isman/Documents/devproj/tools/bss_export >> $logfile
echo $1 >> $logfile
pushd $1
for f in *.html
do
    echo python3 /Users/isman/Documents/devproj/tools/bss_export/bss_export.py $f >> $logfile 
    python3 /Users/isman/Documents/devproj/tools/bss_export/bss_export.py $f 
done
popd