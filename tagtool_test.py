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

  def testTag100LtTag200(self):
    self.assertLess(Tag([1, 0, 0]),Tag([2, 0, 0]))

  def testTag120LtTag130(self):
    self.assertLess(Tag([1, 2, 0]),Tag([1, 3, 0]))

  def testTag123LtTag124(self):
    self.assertLess(Tag([1, 2, 3]),Tag([1, 2, 4]))

  def testTag12LtTag120(self):
    self.assertLess(Tag([1, 2]),Tag([1, 2, 0]))
