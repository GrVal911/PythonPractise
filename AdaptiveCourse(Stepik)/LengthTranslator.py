lengths={'mile':1609, 'yard':0.9144, 'foot':0.3048, 'inch':0.0254, 'km':1000, 'm':1, 'cm':0.01, 'mm':0.001}
a=[]
a=input().split()
print("%.2e" %(float(a[0])*(float(lengths.get(a[1]))/float(lengths.get(a[3])))))