# -*- coding: utf-8 -*-
"""PER 5. Program single inheritance. 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qCEfbWnIx7YSmtOF7HtAnittDtST06Sk
"""

#SINGLE INHERITANCE

#PARENT CLASS
class Hewan:
  def bersuara(self):
    print('Kucing Bersuara')

# CHILD CLASS MEWARISI CLASS HEWAN
class Kucing(Hewan):
  def suara(self):
    print('meong..meog..meog..')

#obejk
k=Kucing()
k.suara()
k.bersuara()