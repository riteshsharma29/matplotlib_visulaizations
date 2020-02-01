import matplotlib.pyplot as plt

# creating donut with subgroups

group_names = ["Blue","Red","Green"]
group_size = [17,12,28]
subgroup_names = ["B1","B2","B3","R1","R2","C1","C2","C3","C4","C5"]
subgroup_size = [6,4,7,5,7,7,4,8,5,4]

# create colors
a,b,c = [plt.cm.Blues,plt.cm.Reds,plt.cm.Greens]

#first Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie,_ = ax.pie(group_size,radius=1.8,labels=group_names,colors=[a(0.6),b(0.6),c(0.6)])
plt.setp(mypie,width=0.5,edgecolor='black')


mypie2,_ = ax.pie(subgroup_size,radius=1.8-0.3,labels=subgroup_names,labeldistance=0.7,colors=[a(0.5),a(0.4),a(0.3),b(0.5),b(0.4),c(0.6),c(0.5),c(0.4),c(0.3),c(0.2)])
plt.setp(mypie2,width=0.6,edgecolor='black')

plt.margins(0,0)

plt.show()


