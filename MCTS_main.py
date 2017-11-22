#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/20 16:52
# @Author : YANGz1J
# @Site : 
# @File : MCTS_main.py
# @Software: PyCharm


class node(object):
    def __init__(self,state,server_state,parent = None):
        self.state = state
        self.child = []
        self.parent = parent
        self.value = None
        self.visit_count = 0
        self.server_state = server_state

class MCTS(object):
    def __init__(self,server_list,traffic):
        self.server_root_state = server_list
        self.state = {}
        self.action = {}
        self.traffic = traffic
    def init_original_state(self):
        self.last_node_embedded = self.traffic.srcnode
        self.available_node_set = self.server_root_state
        self.vnf_node_no_map_set = self.traffic.vnfsec[1:]
        self.last_vnf_node_embedded = self.traffic.vnfsec[0]
        self.state = {self.available_node_set:self.last_node_embedded,self.vnf_node_no_map_set:self.last_vnf_node_embedded}
    def server_detection(self,server):
        can_map = False
        for vnf in server.vnf_used_set:
            if vnf.name == self.vnf_node_no_map_set[0]:
                if vnf.used_bandwidth+self.traffic.bandwidth <= vnf.bandwidth:
                    can_map = True
                    return can_map
        for vnf in server.vnf_not_used_set:
            if vnf.name == self.vnf_node_no_map_set[0]:
                if server.used_cpu_num + vnf.cpu_num <= server.cpu_num:
                    if vnf.used_bandwidth + self.traffic.bandwidth <= vnf.bandwidth:
                        can_map = True
                        return can_map
    def get_available_node_set(self):
        available_node_set = []
        for server in self.server_root_state:
            if self.server_detection(server):
                available_node_set.append(server)
        self.available_node_set = available_node_set





    def start(self):
        self.root = node(self.state,self.server_root_state)
        self.get_available_node_set()





