"""
def read_txt(path):
    file=open(path,'r')
    print(file.read())
    file.close()

read_txt('D:\python_file\li_sanya_thrips\enzyme\Frankliniella_intonsa')
"""
import pandas as pd
import re
import numpy as np
def read_file(path):
    data=pd.read_csv(path,header=0,encoding='utf-8')
    # data=pd.read_csv('D:\python_file\li_sanya_thrips\enzyme\Frankliniella_intonsa',header=0,encoding='utf-8')
    # print(data)
    enzyme_list=[]
    for i in data:
        enzyme_list.append(i)
    del enzyme_list[0::2]
    # print(enzyme_list)
    repeat_enzyme=[]
    for i in enzyme_list:
        x=re.findall(r'\w*.[123]$',i)
        # print(x)
        repeat_enzyme.append(x)
        # enzyme_list.remove(x)
    # print(repeat_enzyme)
    delete_non_empty_list=[i for i in repeat_enzyme if len(i)>0]
    # print(delete_non_empty_list)
    # print(set(enzyme_list))
    # 嵌套列表去嵌套，可以用numpy的ravel方法
    new=list(np.ravel(delete_non_empty_list))
    # print(new)
    # print(set(new))
    enzyme_no_repeat=list(set(enzyme_list)-set(new))
    print(path)
    print(enzyme_no_repeat)
    with open('18_species_enzyme.txt','a') as f:
        f.write(str(path))
        f.write("\n")
        f.write(str(enzyme_no_repeat))
        f.write("\n")

read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Frankliniella intonsa')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Frankliniella occidentalis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Haplothrips chinensis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Heliothrips haemorrhoidalis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Megalurothrips usitatus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Rhipiphorothrips cruentatus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Rhipiphorothrips pulchellus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Scirtothrips dorsalis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Selenothrips rubrocinctus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Stenchaetothrips victoriensis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips andrewsi')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips coloratus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips flavus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips hawaiiensis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips orientalis')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips palmi')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips physapus')
read_file('D:/python_file/li_sanya_thrips/enzyme/18 enzymes/Thrips tabaci')


