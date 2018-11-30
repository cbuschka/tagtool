# -*- coding: UTF-8 -*-

from __future__ import unicode_literals
import unittest
from tagtool import Tag

class TagTest(unittest.TestCase):
  def testTagStr(self):
    self.assertEqual("[1, 2, 3]", str(Tag([1,2,3])) )

  def testEmptyTagsAreEqual(self):
    self.assertEqual(Tag([]),Tag([]))

  def testTagsAreEqual(self):
    self.assertEqual(Tag([1, 2, 3]),Tag([1, 2, 3]))
