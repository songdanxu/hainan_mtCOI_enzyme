Frankliniella_intonsa=['SnaBI', 'BstEII', 'SpeI', 'BclI', 'DraI', 'ScaI', 'AhaIII', 'EcoNI']
Frankliniella_occidentalis=['BsmI', 'NsiI', 'BclI', 'DraI', 'BspMI', 'VspI', 'SspI', 'AhaIII']
Haplothrips_chinensis=['BspMII', 'AccIII', 'SwaI', 'SpeI', 'DraI', 'VspI', 'SspI', 'AhaIII', 'Eco57I', 'EcoNI']
Megalurothrips_usitatus=['BglII', 'Eco31I', 'BclI', 'EcoRI', 'DraI', 'VspI', 'BspMI', 'SspI', 'AhaIII', 'Eco57I']
Thrips_hawaiiensis=['BsmI', 'SwaI', 'BclI', 'DraI', 'BspMI', 'VspI', 'AhaIII', 'EcoNI']
Rhipiphorothrips_cruentatus=['SciI', 'HindIII', 'Eco57I', 'VspI', 'SspI', 'XhoI', 'XmnI']
Rhipiphorothrips_pulchellus=['NsiI', 'SspI', 'AccIII', 'VspI', 'BspMII', 'Eco57I']
Scirtothrips_dorsalis=['SacI', 'EcoICRI', 'SstI', 'Asp718I', 'KpnI', 'ApaLI', 'SspI', 'Acc65I', 'XmnI', 'Alw44I', 'Ecl136II', 'BclI', 'BspMI', 'VspI', 'Eco57I']
Selenothrips_rubrocinctus=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
Stenchaetothrips_victoriensis=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
all=Frankliniella_intonsa+Frankliniella_occidentalis+Haplothrips_chinensis+Megalurothrips_usitatus+Thrips_hawaiiensis+\
Rhipiphorothrips_cruentatus+Rhipiphorothrips_pulchellus+Scirtothrips_dorsalis+Selenothrips_rubrocinctus+\
    Stenchaetothrips_victoriensis
all_dict={}
for i in all:
    all_dict[i]=all.count(i)
print(all_dict)

