#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of FTE.
#
# FTE is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# FTE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FTE.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import random

import fte.encrypter


class TestEncoders(unittest.TestCase):

    def setUp(self):
        self.encrypter = fte.encrypter.Encrypter()

    def testEncryptNoOp(self):
        for i in range(1024):
            C = self.encrypter.encrypt('')
            for j in range(10):
                self.assertEquals(self.encrypter.decrypt(C), '')

    def testEncryptDecrypt_1(self):
        for i in range(1024):
            P = 'X' * i
            C = self.encrypter.encrypt(P)
            self.assertNotEqual(C, P)
            for j in range(1):
                self.assertEquals(P, self.encrypter.decrypt(C))

    def testEncryptDecrypt_2(self):
        for i in range(1024):
            P = '\x01' * 2 ** 15
            C = self.encrypter.encrypt(P)
            self.assertNotEqual(C, P)
            for j in range(1):
                self.assertEquals(P, self.encrypter.decrypt(C))

    def testEncryptDecryptOneBlock(self):
        for i in range(128):
            for j in range(128):
                M1 = random.randint(0, (1 << 64) - 1)
                M1 = fte.bit_ops.long_to_bytes(M1, 8)
                retval = self.encrypter.encryptOneBlock(M1)
                H_out = self.encrypter.decryptOneBlock(retval)
                self.assertEquals(M1, H_out)


if __name__ == '__main__':
    unittest.main()
