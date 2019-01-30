#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from unittest import TestCase, main
from safeclean.safeclean import SafeClean


class Tests_Safeclean(TestCase):

    def setUp(self):
        self.sc = SafeClean()

    def test_verify_user(self):
        self.assertTrue(self.sc.verify_user(0))
    
    def test_python_version_required(self):
        self.assertTrue(self.sc.python_version_required(3))

    def test_verify_dependencies(self):
        self.assertTrue(self.sc.verify_dependencies())

    def test_clean(self):
        self.assertTrue(self.sc.clean())
        

if __name__ == '__main__':
    main()
    