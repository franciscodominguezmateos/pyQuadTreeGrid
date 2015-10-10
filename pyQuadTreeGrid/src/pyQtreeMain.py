'''
Created on 12/07/2015

@author: Francisco Dominguez
'''
from pyQTree import *

def getColor(i):
    if i==0:
        return (0,0,0)
    if i==1:
        return (128,0,0)
    if i==2:
        return (128,0,128)
    if i==3:
        return (128,128,0)
    if i==4:
        return (0,128,128)
    if i==2:
        return (128,128,128)
    if i==5:
        return (255,0,128)
    if i==6:
        return (128,0,255)
    if i==7:
        return (128,255,128)
    
if __name__ == '__main__':
    qt=pyQTree()
    np=1<<pyQTree.MAX_LEVEL
    imm=Image.open("Circular_path_planning.png")
    imm.thumbnail((np,np), Image.ANTIALIAS)
    imm.show()
    (sx,sy)=imm.size
    for i in range(sx):
        #print "x=%d" % i
        for j in range(sy):
            if imm.getpixel((i,j))[1]<129:
                qt.insert(Point(i,j))
    im = Image.new("RGB", (np, np), "white")
    draw=ImageDraw.Draw(im)
    rs0=qt.getRectangles(Rectangle(0,0,np<<0,np<<0),0)
    rs1=qt.getRectangles(Rectangle(0,0,np<<0,np<<0),1)
    rs2=qt.getRectangles(Rectangle(0,0,np<<0,np<<0),2)
    rs3=qt.getRectangles(Rectangle(0,0,np<<0,np<<0),3)
    rs=rs0
    print len(rs)
    for r in rs:
        draw.rectangle(r.asTuple(),fill=getColor(r.node.level))
    del(draw)
    im.show()
    im.save("quadtree.png")
    #print qt