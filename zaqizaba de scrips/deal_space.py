import re
def deal_space(path):
    with open(path,'r') as f:
        lines=f.readlines()
        print(lines)
    space2_=re.compile(r'\w{6,} \w{5,}')
    result=space2_.sub(r' ','_',lines)





deal_space("D:/python_file/li_sanya_thrips/18_species_enzyme.txt")