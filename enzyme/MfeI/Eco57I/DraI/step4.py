Selenothrips_rubrocinctus=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
Rhipiphorothrips_cruentatus=['SciI', 'HindIII', 'Eco57I', 'VspI', 'SspI', 'XhoI', 'XmnI']
Rhipiphorothrips_pulchellus=['NsiI', 'SspI', 'AccIII', 'VspI', 'BspMII', 'Eco57I']
Scirtothrips_dorsalis=['SacI', 'EcoICRI', 'SstI', 'Asp718I', 'KpnI', 'ApaLI', 'SspI', 'Acc65I', 'XmnI', 'Alw44I', 'Ecl136II', 'BclI', 'BspMI', 'VspI', 'Eco57I']
all=Selenothrips_rubrocinctus+Rhipiphorothrips_cruentatus+Rhipiphorothrips_pulchellus+Scirtothrips_dorsalis
all_dict={}
for i in all:
    all_dict[i]=all.count(i)
print(all_dict)
SrandRc=list(set(Selenothrips_rubrocinctus)|set(Rhipiphorothrips_cruentatus))
Sr=list(set(SrandRc).difference(Rhipiphorothrips_cruentatus))
Rc=list(set(SrandRc).difference(Selenothrips_rubrocinctus))
print(SrandRc)
print(Sr)
print(Rc)