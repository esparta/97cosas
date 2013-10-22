from __future__ import print_function
import sys
import os

def main(argv):
   if len(argv) < 2:
     sys.stderr.write("Usage: {0}  <filename>\n".format(argv[0]))
     return 2
   filename = argv[1]
   if not os.path.exists(filename):
     sys.stderr.write("ERROR: file {filename} not found!\n"\
                      .format(filename=filename))
     return 1
   justfilename, _ = os.path.splitext(\
                           os.path.basename(filename))

   with open(filename,"r") as f, open(filename+".jk","w") as newfile:
      ## Get the title and remove the newline
      title = f.readline().rstrip(os.linesep)
      if title in ("---", ""):
        sys.stderr.write("Warning! This file appears to be already formatted\n")
        return 1
      ## skip the next line, should be ===
      _ = f.readline()
      ## Get the authoer (should be the third line)
      author = f.readline().rstrip(os.linesep)[4:]
      ## skip the next line, should be ===
      _ = f.readline()
      ## create the head
      head = \
"""---
layout: page
title: {title}
overview: true
permalink: /libro/{filename}/
author: {author}
---
""".format(title=title,filename=justfilename,author=author)
      #print(head)
      content = f.read()

      newfile.write(head+content)
      print("Finished transforming {0}".format(filename))

if __name__ == "__main__":
  sys.exit(main(sys.argv))

