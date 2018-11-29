#coding=utf-8
#/usr/bin/python

import xml.etree.ElementTree as ET
from xml.dom import minidom

def parse1(filename):
    xml_file = open(filename, 'r')
    xml_str = xml_file.read()
    # XML将字符串解析成xml特殊对象，返回xml.etree.ElementTree.Element对象，这个是根节点
    root = ET.XML(xml_str)
    print (type(root))
    print root.tag

    #遍历根得到指定节点uid的内容
    for value in root.iter("uid"):
        print(value.tag, value.text)

    #修改指定节点内容
    node1 = root.find("dataconnection")
    print node1
    node1.set("name", "here testing")
    #借助ET.ElementTree保存
    tree = ET.ElementTree(root)
    tree.write(filename, encoding = "utf-8")

    #删除指定节点
    node = root.find("uid")
    print "now here in remove:" + str(node)
    print type(node)
    #node = root.find("net")
    #root.remove(node)
    #node1.remove("uid")
    #node.remove(node)
    # 借助ET.ElementTree保存
    tree = ET.ElementTree(root)
    tree.write(filename, encoding = "utf-8")

def parse2(filename):
    #打开xml文件并且解析，返回一个xml.etree.ElementTree.ElementTree对象
    xml_tree = ET.parse(filename)
    #获取xml的根节点
    root = xml_tree.getroot()
    print (type(root))
    print root.tag



def create_xml(filename):
    print "in create_xml func"
    ##创建根节点
    root = ET.Element("home", {"name":"root"})
    # 创建节点并添加到第一个参数的节点下面
    sub = ET.SubElement(root, "son", {"subName": "sub testing"})
    subsub = ET.SubElement(sub, "son", {"subName":"subsub testing"})

    tree = ET.ElementTree(root)
    tree.write(filename)

#给生成的xml添加缩进
def prettify(elem):
    #将节点转换成字符串，并添加缩进
    #返回该对象字符串表示
    elem_str = ET.tostring(elem, "utf-8")
    print(type(elem_str))
    #对象字符串到dom对象
    elem_parse = minidom.parseString(elem_str)
    print(type(elem_parse))
    return elem_parse.toprettyxml(indent="\t")


if __name__ == "__main__":
    print "in the main func"
    parse1("data.xml")
    #parse2("data.xml")

    new_xml = "new_xml.xml"
    create_xml(new_xml)

    xml_tree = ET.parse(new_xml)
    # 获取xml的根节点
    root = xml_tree.getroot()
    newstr = prettify(root)
    file = open("pretty_xml.xml", "w")
    file.write(newstr)
    file.close()
