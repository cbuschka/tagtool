#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import re
import sys

class Tag:
  def __init__(self, parts):
    self.parts = parts

  def __eq__(self, other):
    return self.__cmp__(other) == 0

  def __cmp__(self, other):
    for i in range(max(len(self.parts), len(other.parts))):
      if i > len(self.parts)-1:
        return -1
      if i > len(other.parts)-1:
        return 1
      if self.parts[i] < other.parts[i]:
        return -1 if self.parts[i]-other.parts[i] < 0 else 1
 
    return 0

  def __lt__(self, other):
    return self.__cmp__(other) == -1

  def __str__(self):
    return str(self.parts)

class TagFormat:
  def __init__(self, pattern):
    self.pattern = pattern

  def match(self, tagName):
    return self.pattern.match(tagName)

  def format(self, tag):
    return "v{}.{}.{}".format(tag.parts[0], tag.parts[1], tag.parts[2])

  def nextTag(self, sortedTags):
    lastTag = self.lastTag(sortedTags)
    if lastTag is None:
      nextTag = Tag([1, 0, 0])
    else:
      nextTag = Tag([lastTag.parts[0], lastTag.parts[1], lastTag.parts[2]+1 ])
    return nextTag

  def lastTag(self, sortedTags):
    if len(sortedTags) == 0:
      return None
    else:
      return sortedTags[-1]

class Git:
  def __init__(self):
   pass

  def getTags(self, tagFormat):
    tags = [] 
    proc = subprocess.Popen(['git', 'tag', '-l'], shell=False, stdout=subprocess.PIPE)
    for line in proc.stdout:
      match = tagFormat.match(line.rstrip())
      if match:
        tagParts = [int(match.group(1)), int(match.group(2)), int(match.group(3)) ]
        tag = Tag(tagParts)
        tags.append(tag)
    tags.sort()

    return tags

class Command:
  def __init__(self):
    self.git = Git()
    pattern = re.compile('^v([0-9]+)\.([0-9]+)\.([0-9]+)$')
    self.tagFormat = TagFormat(pattern)

  def _printLast(self):
    tags = self.git.getTags(self.tagFormat)
    lastTag = self.tagFormat.lastTag(tags)
    if lastTag is not None:
      print(self.tagFormat.format(lastTag))
      return 0
    return 1

  def _printNext(self):
    tags = self.git.getTags(self.tagFormat)
    nextTag = self.tagFormat.nextTag(tags)
    print(self.tagFormat.format(nextTag))
    return 0

  def _printList(self):
    tags = self.git.getTags(self.tagFormat)
    for tag in tags:
      print(self.tagFormat.format(tag))
    return 0

  def run(self, args):
    if len(args) > 1 and args[1] == 'last':
      return self._printLast()
    elif len(args) > 1 and args[1] == 'next':
      return self._printNext()
    elif len(args) > 1 and args[1] == 'list':
      return self._printList()
    else:
      print("tagtool last|next|list")
      return 1
 
if __name__ == '__main__':
  command = Command()
  exitCode = command.run(sys.argv)
  sys.exit(exitCode)

