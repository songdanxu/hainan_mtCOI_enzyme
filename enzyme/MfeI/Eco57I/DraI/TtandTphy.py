Thrips_physapus=['BspMII', 'MfeI', 'AccIII', 'BclI', 'DraI', 'VspI', 'AhaIII', 'Eco57I', 'EcoNI']
Thrips_tabaci=['BglII', 'BsiI', 'EcoICRI', 'SacI', 'SstI', 'MfeI', 'PflMI', 'AclI', 'Eam1105I', 'BstD102I', 'VspI', 'BstEII', 'Ecl136II', 'BclI', 'Eco57I', 'EcoNI']
all=list(set(Thrips_tabaci)|set(Thrips_physapus))
Tphy=list(set(all).difference(set(Thrips_tabaci)))
Tt=list(set(all).difference(set(Thrips_physapus)))
print(all)
print(Tphy)
print(Tt)