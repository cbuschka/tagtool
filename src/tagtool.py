#!/usr/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import re
import sys

MAJOR=0
MINOR=1
PATCH=2

class Tag:
  def __init__(self, parts):
    self.parts = parts

  def next(self, pos=PATCH):
    newParts = list(self.parts)
    for i in range(len(newParts)):
      if i == pos:
        newParts[pos] = newParts[pos]+1
      elif i > pos:
        newParts[i] = 0
    return Tag(newParts)

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

  def nextTag(self, sortedTags, pos):
    lastTag = self.lastTag(sortedTags)
    if lastTag is None:
      nextTag = Tag([1, 0, 0])
    else:
      nextTag = lastTag.next(pos)
    return nextTag

  def lastTag(self, sortedTags):
    if len(sortedTags) == 0:
      return None
    else:
      return sortedTags[-1]

class Git:
  def __init__(self):
   pass

  def exists(self):
    try:
      proc = subprocess.Popen(['git', 'version'], shell=False, stdout=subprocess.PIPE)
      return proc.wait() == 0
    except OSError:
      return False

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

  def _printNext(self, pos=PATCH):
    tags = self.git.getTags(self.tagFormat)
    nextTag = self.tagFormat.nextTag(tags, pos)
    print(self.tagFormat.format(nextTag))
    return 0

  def _printList(self):
    tags = self.git.getTags(self.tagFormat)
    for tag in tags:
      print(self.tagFormat.format(tag))
    return 0

  def run(self, args):
    if not self.git.exists():
      print("No git found.")
      return 1

    if len(args) > 1 and args[1] == 'last':
      return self._printLast()
    elif len(args) > 1 and args[1] == 'next':
      return self._printNext(PATCH)
    elif len(args) > 1 and args[1] == 'nextPatch':
      return self._printNext(PATCH)
    elif len(args) > 1 and args[1] == 'nextMinor':
      return self._printNext(MINOR)
    elif len(args) > 1 and args[1] == 'nextMajor':
      return self._printNext(MAJOR)
    elif len(args) > 1 and args[1] == 'list':
      return self._printList()
    else:
      print("tagtool last|next|nextPatch|nextMinor|nextMajor|list")
      return 1
 
if __name__ == '__main__':
  command = Command()
  exitCode = command.run(sys.argv)
  sys.exit(exitCode)

