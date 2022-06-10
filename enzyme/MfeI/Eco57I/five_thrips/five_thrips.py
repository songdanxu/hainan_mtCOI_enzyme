Thrips_orientalis=['SacI', 'EcoICRI', 'MfeI', 'SstI', 'Eco31I', 'BclI', 'DraI', 'VspI', 'AhaIII']
Thrips_palmi=['BstXI', 'SacI', 'EcoICRI', 'MfeI', 'SstI', 'SwaI', 'Ecl136II', 'BclI', 'DraI', 'ScaI', 'VspI', 'SspI', 'AhaIII']
Thrips_andrewsi=['NsiI', 'ScaI', 'BspMI', 'SspI', 'MfeI']
Thrips_coloratus=['SnaBI', 'MfeI', 'BsmI', 'SwaI', 'XmnI', 'BclI', 'DraI', 'ScaI', 'VspI', 'SspI', 'AhaIII']
Thrips_flavus=['MfeI', 'ApaI', 'ScaI', 'BclI', 'DraI', 'VspI', 'SspI', 'AhaIII', 'AflII']
all=Thrips_flavus+Thrips_coloratus+Thrips_andrewsi+Thrips_palmi+Thrips_orientalis
all_dict={}
for i in all:
    all_dict[i]=all.count(i)
print(all_dict)
ToandTp=list(set(Thrips_orientalis)|set(Thrips_palmi))
To=list(set(ToandTp).difference(Thrips_palmi))
Tp=list(set(ToandTp).difference(Thrips_orientalis))
print(To)
print(Tp)