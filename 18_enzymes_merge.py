Frankliniella_intonsa=['SnaBI', 'BstEII', 'SpeI', 'BclI', 'DraI', 'ScaI', 'AhaIII', 'EcoNI']
Frankliniella_occidentalis=['BsmI', 'NsiI', 'BclI', 'DraI', 'BspMI', 'VspI', 'SspI', 'AhaIII']
Haplothrips_chinensis=['BspMII', 'AccIII', 'SwaI', 'SpeI', 'DraI', 'VspI', 'SspI', 'AhaIII', 'Eco57I', 'EcoNI']
Heliothrips_haemorrhoidalis=['HpaI', 'SnaBI', 'BstEII', 'MfeI', 'Alw44I', 'SpeI', 'BclI', 'ApaLI', 'BspMI', 'VspI', 'DraI', 'SspI', 'AhaIII']
Megalurothrips_usitatus=['BglII', 'Eco31I', 'BclI', 'EcoRI', 'DraI', 'VspI', 'BspMI', 'SspI', 'AhaIII', 'Eco57I']
Rhipiphorothrips_cruentatus=['SciI', 'HindIII', 'Eco57I', 'VspI', 'SspI', 'XhoI', 'XmnI']
Rhipiphorothrips_pulchellus=['NsiI', 'SspI', 'AccIII', 'VspI', 'BspMII', 'Eco57I']
Scirtothrips_dorsalis=['SacI', 'EcoICRI', 'SstI', 'Asp718I', 'KpnI', 'ApaLI', 'SspI', 'Acc65I', 'XmnI', 'Alw44I', 'Ecl136II', 'BclI', 'BspMI', 'VspI', 'Eco57I']
Selenothrips_rubrocinctus=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
Stenchaetothrips_victoriensis=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
Thrips_andrewsi=['NsiI', 'ScaI', 'BspMI', 'SspI', 'MfeI']
Thrips_coloratus=['SnaBI', 'MfeI', 'BsmI', 'SwaI', 'XmnI', 'BclI', 'DraI', 'ScaI', 'VspI', 'SspI', 'AhaIII']
Thrips_flavus=['MfeI', 'ApaI', 'ScaI', 'BclI', 'DraI', 'VspI', 'SspI', 'AhaIII', 'AflII']
Thrips_hawaiiensis=['BsmI', 'SwaI', 'BclI', 'DraI', 'BspMI', 'VspI', 'AhaIII', 'EcoNI']
Thrips_orientalis=['SacI', 'EcoICRI', 'MfeI', 'SstI', 'Eco31I', 'BclI', 'DraI', 'VspI', 'AhaIII']
Thrips_palmi=['BstXI', 'SacI', 'EcoICRI', 'MfeI', 'SstI', 'SwaI', 'Ecl136II', 'BclI', 'DraI', 'ScaI', 'VspI', 'SspI', 'AhaIII']
Thrips_physapus=['BspMII', 'MfeI', 'AccIII', 'BclI', 'DraI', 'VspI', 'AhaIII', 'Eco57I', 'EcoNI']
Thrips_tabaci=['BglII', 'BsiI', 'EcoICRI', 'SacI', 'SstI', 'MfeI', 'PflMI', 'AclI', 'Eam1105I', 'BstD102I', 'VspI', 'BstEII', 'Ecl136II', 'BclI', 'Eco57I', 'EcoNI']
all=Frankliniella_intonsa+Frankliniella_occidentalis+Haplothrips_chinensis+Heliothrips_haemorrhoidalis+\
    Megalurothrips_usitatus+Rhipiphorothrips_cruentatus+Rhipiphorothrips_pulchellus+Scirtothrips_dorsalis+\
    Selenothrips_rubrocinctus+Stenchaetothrips_victoriensis+Thrips_andrewsi+Thrips_coloratus+Thrips_flavus+\
    Thrips_hawaiiensis+Thrips_orientalis+Thrips_palmi+Thrips_physapus+Thrips_tabaci
all.sort()
def all_list(list1):
    all_dict={}
    for i in set(list1):
        all_dict[i]=list1.count(i)
    print(all_dict)
all_list(all)
