import os, glob
import sys
import zipfile
from shutil import copyfile
import shutil

fileconversions = [
        ['-B.Cu.gbr',       '.GBL'],
        ['-F.Cu.gbr',       '.GTL'],
        ['-B.SilkS.gbr',    '.GBO'],
        ['-F.SilkS.gbr',    '.GTO'],
        ['-B.Mask.gbr',     '.GBS'],
        ['-F.Mask.gbr',     '.GTS'],
        ['-B.Paste.gbr',    '.GBP'],
        ['-F.Paste.gbr',    '.GTP'],
        ['-Edge.Cuts.gbr',  '.GML'],
        ['.drl',            '.DRL']
        ]


tempFolder = 'tempFolderForBoardFiles'

os.mkdir(tempFolder)

for filename in os.listdir(os.curdir):
    for oldextension, newextension  in fileconversions:
        if filename.endswith(oldextension):
            copyfile(filename, tempFolder + '/' + filename[:-len(oldextension)]+newextension)

shutil.make_archive('board', 'zip', tempFolder)

os.rmdir(tempFolder)
