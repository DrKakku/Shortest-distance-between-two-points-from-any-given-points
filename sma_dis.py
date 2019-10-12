from math import*
def dis(x1,x2,y1,y2):
     print(x1,y1,x2,y2)
     dist = sqrt((x2-x1)^2+(y2-y1)^2)
     return dist
def inte (lis):
     listt = []
     for i in lis:
          x = int(i)
          listt.append(x)
     return listt    
def short_dist (points):
     for i in points:
        for j in points:
          if i == j:
               pass
          else:
               print("value of points before spliting",i,j)
               p1 = i.split(',')
               p2 = j.split(',')
               print("value of points after splitting",p1,p2)
               p1 = inte(p1)
               p2 = inte(p2)
               print("value of points after convertina as a intiger",p1,p2)
               dist = dis(p1[0],p2[0],p1[1],p2[1])
               min_val = None
               if min_val is None:
                    short_p1 = p1
                    short_p2 = p2
                    min_val = dist
               elif min_val > dist:
                    min_val = dist
                    short_p1 = p1
                    short_p2 = p2
               elif min_val == dist:
                    pass
     return (min_val,short_p1,short_p2)

