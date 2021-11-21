#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def func(type):
    def inner(value):
        gen = (e for e in value.split())
        if type == 'list':
            return list(gen)
        return tuple(gen)

    return inner
