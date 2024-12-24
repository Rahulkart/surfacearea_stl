#Author name : Rahul Karthik.S
#Designation : Software Development Engineer
#Program     : To calculate surface area by reading a STL file

import math
def distance(distance1,distance2):
    return math.sqrt((float(distance2[0])-float(distance1[0]))**2+(float(distance2[1])-float(distance1[1]))**2+(float(distance2[2])-float(distance1[2]))**2)

def triangle_area(side1,side2,side3):
    s1=distance(side1,side2)
    s2=distance(side2,side3)
    s3=distance(side3,side1)

    side=(s1+s2+s3)/2.0
    area=side*(side-s1)*(side-s2)*(side-s3)
    return math.sqrt(area)
    
def surface_area(file_path):
    vertexX=[]
    vertexY=[]
    vertexZ=[]
    
    area=0.0
    count=0
    file=open(file_path,'r')

    for line in file:
        if line.strip().startswith("vertex"):
            count+=1
            parts = line.strip().split()
            if(count==1):
                vertexX.append(parts[1])
                vertexX.append(parts[2])
                vertexX.append(parts[3])
            elif(count==2):
                vertexY.append(parts[1])
                vertexY.append(parts[2])
                vertexY.append(parts[3])
            elif(count==3):
                vertexZ.append(parts[1])
                vertexZ.append(parts[2])
                vertexZ.append(parts[3])
                area=area+triangle_area(vertexX,vertexY,vertexZ)
                count=0
            
    print(area)
file_path = "D:/ActuatorBody.py"
surface_area(file_path)
