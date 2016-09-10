#!/usr/bin/env python
# -*- coding: utf-8 -*-


list_ = [3,1,5,7,9]

def main():
    pass

def while_method():
    i = 0
    sum = 0
    while i != len(list_):
        sum = sum + list_[i]
        i = i + 1
    return sum

def for_method():
    sum = 0
    for i in list_:
        sum = sum + i
    return sum

def third_method(list_, i, result):
    if i == len(list_):
         return result
    return third_method(list_, i + 1, result + list_[i])


if __name__ == "__main__":
    first = while_method()
    second = for_method()
    third = third_method(list_, 0, 0)
    print first 
    print second
    print third

