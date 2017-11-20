#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/20 16:52
# @Author : YANGz1J
# @Site : 
# @File : MCTS_main.py
# @Software: PyCharm



class MCTS(object):
    def __init__(self,node_list,traffic):
        self.node_list = node_list
        self.state = {}
        self.action = {}
        self.traffic = traffic
    def get_available_node(self):




