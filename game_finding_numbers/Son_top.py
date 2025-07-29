#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 14:54:40 2025

@author: islomisomiddinov
"""

# 25-dars:    SON TOPISH O'YINI 
    
import random

def sontop(x=10):
    tasodifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:")
        elif taxmin>tasodifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harkat qiling:")
        else:
            break
    print(f"Tabriklaymiz. Siz {taxminlar} ta taxmin bilan topdingiz!")
    return taxminlar

def sontop_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz to'g'rimi? "
                      f"to'g'ri - t. "
                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq (-):".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar

def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        if taxminlar_user>taxminlar_pc:
            print(f"Ura! Men {taxminlar_pc} ta taxmin bilan yutdim!")
        elif taxminlar_user<taxminlar_pc:
            print("Qoyil! Siz {taxminlar_user} ta taxmin bilan yutdingiz.")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaysizmi? yes(1)/no(0): "))