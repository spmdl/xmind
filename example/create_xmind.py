# -*- coding: utf-8 -*-

import xmind
from xmind.core.const import TOPIC_DETACHED
from xmind.core.markerref import MarkerId
from xmind.core.topic import TopicElement

import os

import time


def gen_my_xmind_file():

    workbook = xmind.load("my.xmind")
    sheet1 = workbook.getPrimarySheet()
    time_name = basic_sheet(sheet1, workbook)
    # gen_sheet2(sheet1, workbook)

    xmind.save(workbook, path='minmap/{}.xmind'.format(time_name))


def tomato():
    os.system("../tomato-clock/tomato.py")

def create_node(get_node, get_web):

    b_web = True
    while b_web:
        task_node = input("create node | end  \n at {}->{}\n input node：".format(get_web, get_node))

        if task_node == "end":
            b_web = False
            # dict['node'].append(get_node.copy())
        else:
            get_node.append(task_node)

    return get_node

def creat_child_node(child_node):
    test = {'child_node': "如何傳值到後端", 'web': [
        {"name": "b", "src": "https://github.com/zhuifengshen/xmind"},
        {"name": "c", "src": "https://github.com/zhuifengshen/xmind"}
    ], 'node': [
        ["fals 阻止頁面更新", "jQuery 動態生成物件"],
        ["頁面沒有刷新因為 hs6"]
    ]
     }

    # return (test)
    dict = {"child_node": child_node, "web":[], "node":[]}

    b = True
    get_web = {"name":"", "src":""}
    get_now_web = ""
    get_now_node = []
    while b:


        task_web = input("w:web | k:keep | ed:edic web | e:end  \n 當前 web {}->{} \n 請輸入選擇：".format(get_now_web, get_now_node))

        if task_web =="w" or task_web =="web":
            get_web["name"] = input("web_name：")
            get_web["src"] = input("web_src：")
            dict['web'].append(get_web.copy())

            get_now_web = get_web["name"]

            # dict['node'].extend(create_node([], get_now_web).copy())
            node = create_node([], get_now_web).copy()
            dict['node'].append(node)
            get_now_node = node
            get_web = {"name": "", "src": ""}

        if task_web == 'k' or task_web == 'keep':
            tomato()

        if task_web == "ed" or task_web == "edic":
            web_name = input("web_name：")

            b_edic = True
            while b_edic:

                try:
                    num = [i for i, _ in enumerate(dict['web']) if _['name'] == web_name][0]

                    get_now_web = web_name
                    # dict['node'] = (create_node(dict['node'], get_now_web).copy())
                    node  = create_node(dict['node'][num], get_now_web).copy()
                    dict['node'][num] = node
                    get_now_node = node

                    b_edic = False
                except IndexError:
                    if web_name == "end" or web_name == "e":
                        b_edic = False
                    else:
                        web_name = input("請輸入正確 web_name | end：")

        if task_web =="e" or task_web =="end" or task_web =="q":
            b = False

    return dict

def get_tree(a):

    c = a['child_node']
    c2 = a['web']
    c3 = a['node']
    # for i, val in enumerate(c):

    print(".{}".format(c))

    for i2, val2 in enumerate(c2):
        print("├── {}".format(val2['name']))

        for i4, val4 in enumerate(c3):
            if i4 == i2:
                for i5, val5 in enumerate(val4):
                    print("│   ├──  {}".format(val5))

    print("└───")

def painting_time(s1, time, child_node):

    t1 = s1.getRootTopic()
    t1.setTitle("Time")

    t = t1.addSubTopic()
    t.setTitle("{}-{}".format(time['st'], time['et']))

    tt = t.addSubTopic()
    tt.setTitle(child_node)

def painting_child_node(s1, root, dict):

    r1 = s1.getRootTopic()  # get the root topic of this sheet
    r1.setTitle(root)  # set its title

    c = dict['child_node']
    c2 = dict['web']
    c3 = dict['node']

    a = r1.addSubTopic()
    a.setTitle(c)  # set its title

    print(".{}".format(c))
    for i2, val2 in enumerate(c2):

        a2 = a.addSubTopic()
        #        if isinstance(val, list):

        print("├── {}".format(val2['name']))

        a3 = 'b3' + str(val2['name'])
        a3 = a2.addSubTopic()
        a3.setTitle(val2['name'])
        a3.setURLHyperlink("{}".format(val2['src']))

        for i4, val4 in enumerate(c3):
            if i4 == i2:
                for i5, val5 in enumerate(val4):
                    print("│   ├──  {}".format(val5))
                    a4 = a3.addSubTopic()
                    a4.setTitle(val5)

    print("└───")

def time_sheet(s2, time, child_node):

    t1 = s2.getRootTopic()
    t1.setTitle("Time")

    t = t1.addSubTopic()
    t.setTitle("{}-{}".format(time['st'], time['et']))

    tt = t.addSubTopic()
    tt.setTitle(child_node)

def basic_sheet(s1, workbook):
    s1.setTitle("child_node sheet")  # set its title

    s2 = workbook.createSheet()
    s2.setTitle("time sheet")

    creat_child = []
    creat_child_time = []

    result = True
    root = input("create root node: \n")
    start_time = time.strftime("%b%d|%H:%M")


    while result:

        task = input("t:tree | c:create child_node | e:end  \ninput:")
        child_time = {"st": "", "et": ""}

        if task == "t" or task == "tree":

            for i, val in enumerate(creat_child):
                get_tree(val)

        if task == "c" or task == "create":
            child_node = input("child_node_name：")

            child_time['st'] = time.strftime("%H:%M")
            tomato()

            creat_child.append(creat_child_node(child_node).copy())
            child_time['et'] = time.strftime("%H:%M")
            creat_child_time.append(child_time)

        if task == "e" or task == "end" or task == "q":
            end_time = time.strftime("%H:%M")

            for i, val in enumerate(creat_child):
                painting_child_node(s1, root, val)
                time_sheet(s2, creat_child_time[i], val['child_node'])


            result = False

    print('\n {}-{}.xmind'.format(start_time, end_time))
    return("{}-{}".format(start_time, end_time))


def gen_sheet2(workbook, sheet1):
    # ***** second sheet *****
    # create a new sheet and add to the workbook by default
    sheet2 = workbook.createSheet()
    sheet2.setTitle("second sheet")

    # a sheet has a blank sheet by default
    root_topic2 = sheet2.getRootTopic()
    root_topic2.setTitle("root node")

    # use other methods to create some sub topic element
    topic1 = TopicElement(ownerWorkbook=workbook)
    # set a topic hyperlink from this topic to the first sheet given by s1.getID()
    topic1.setTopicHyperlink(sheet1.getID())
    topic1.setTitle("redirection to the first sheet")  # set its title

    topic2 = TopicElement(ownerWorkbook=workbook)
    topic2.setTitle("topic with an url hyperlink")
    topic2.setURLHyperlink("https://github.com/zhuifengshen/xmind")  # set an url hyperlink

    topic3 = TopicElement(ownerWorkbook=workbook)
    topic3.setTitle("third node")
    topic3.setPlainNotes("notes for this topic")  # set notes (F4 in XMind)
    topic3.setTitle("topic with \n notes")

    topic4 = TopicElement(ownerWorkbook=workbook)
    topic4.setFileHyperlink("logo.png")  # set a file hyperlink
    topic4.setTitle("topic with a file")

    topic1_1 = TopicElement(ownerWorkbook=workbook)
    topic1_1.setTitle("sub topic")
    topic1_1.addLabel("a label")  # official XMind only can a one label

    topic1_1_1 = TopicElement(ownerWorkbook=workbook)
    topic1_1_1.setTitle("topic can add multiple markers")
    topic1_1_1.addMarker(MarkerId.starBlue)
    topic1_1_1.addMarker(MarkerId.flagGreen)

    topic2_1 = TopicElement(ownerWorkbook=workbook)
    topic2_1.setTitle("topic can add multiple comments")
    topic2_1.addComment("I'm a comment!")
    topic2_1.addComment(content="Hello comment!", author='devin')

    # then the topics must be added to the root element
    root_topic2.addSubTopic(topic1)
    root_topic2.addSubTopic(topic2)
    root_topic2.addSubTopic(topic3)
    root_topic2.addSubTopic(topic4)
    topic1.addSubTopic(topic1_1)
    topic2.addSubTopic(topic2_1)
    topic1_1.addSubTopic(topic1_1_1)

    # to loop on the subTopics
    topics = root_topic2.getSubTopics()
    for index, topic in enumerate(topics):
        topic.addMarker("priority-" + str(index + 1))

    # create a relationship
    sheet2.createRelationship(topic1.getID(), topic2.getID(), "relationship test")


if __name__ == '__main__':
    gen_my_xmind_file()
