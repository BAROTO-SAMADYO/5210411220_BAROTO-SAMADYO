# -*- coding: utf-8 -*-
"""PER 5. Program Multilevel inheritance. 2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qCEfbWnIx7YSmtOF7HtAnittDtST06Sk
"""

class Hewan:
  def bersuara(self):
    print('kUCING BERSUARA')

class Kucing(Hewan):
  def suara(self):
    print('meog..meog..meog..')

class AnakKucing(Kucing):
  def minum(self):
    print('minum susu')

#objek
ak=AnakKucing()
ak.bersuara()
ak.suara()
ak.minum()