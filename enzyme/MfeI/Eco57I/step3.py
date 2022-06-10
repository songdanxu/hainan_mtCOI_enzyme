Frankliniella_intonsa=['SnaBI', 'BstEII', 'SpeI', 'BclI', 'DraI', 'ScaI', 'AhaIII', 'EcoNI']
Frankliniella_occidentalis=['BsmI', 'NsiI', 'BclI', 'DraI', 'BspMI', 'VspI', 'SspI', 'AhaIII']
Selenothrips_rubrocinctus=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
Stenchaetothrips_victoriensis=['VspI', 'BsmI', 'BamHI', 'BclI', 'SspI', 'AvrII', 'EcoNI']
Thrips_hawaiiensis=['BsmI', 'SwaI', 'BclI', 'DraI', 'BspMI', 'VspI', 'AhaIII', 'EcoNI']
all=Frankliniella_intonsa+Frankliniella_occidentalis+Selenothrips_rubrocinctus+Stenchaetothrips_victoriensis+\
Thrips_hawaiiensis
all_dict={}
for i in all:
    all_dict[i]=all.count(i)
print(all_dict)
