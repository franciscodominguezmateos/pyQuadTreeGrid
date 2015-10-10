'''
Created on 27/02/2015

@author: Francisco Dominguez
'''
from PIL import Image,ImageDraw
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
class Rectangle:
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.node=None
    def asTuple(self):
        return (self.x,self.y,self.x+self.w-1,self.y+self.h-1)
    def getCenter(self):
        return Point(self.x+self.w/2,self.y+self.h/2)
class pyQTree:
    '''
    Easy Quadtree implementation
    '''
    MAX_LEVEL=10
    def __init__(self,level=MAX_LEVEL):
        self.full=False
        self.level=level
        self.nodes=[None,None,None,None]
        self.father=None
    def allNodesFull(self):
        for n in self.nodes:
            if n==None:
                return False
            elif not n.full:
                return False
        return True
    def cleanNodes(self):
        self.nodes=[None,None,None,None]
    def splitRectangle(self,r,i):
        wMid=r.w>>1
        hMid=r.h>>1
        xMid=r.x+wMid
        yMid=r.y+hMid
        if i==0:
            return Rectangle(r.x ,r.y ,wMid,hMid)
        if i==1:
            return Rectangle(xMid,r.y ,wMid,hMid)
        if i==2:
            return Rectangle(r.x ,yMid,wMid,hMid)
        if i==3:
            return Rectangle(xMid,yMid,wMid,hMid)
            
    def getRectangles(self,r,maxLevel=0):
        if self.full or self.level==maxLevel:
            r.node=self
            return [r]
        else:
            recs=[]
            for i,n in enumerate(self.nodes):
                if n!=None:
                    ri=self.splitRectangle(r, i)
                    recs.extend(n.getRectangles(ri,maxLevel))
            return recs
    def containRectangle(self,r):
        pass
    def containPoint(self,p):
        if self.full:
            return True
        if self.level==0:
            return True
        nPos=self.getPosNodeAtThisLevel(p)
        if self.nodes[nPos]==None:
            return False
        return self.nodes[nPos].containPoint(p)
    def getPosNodeAtThisLevel(self,p):
        lsb=p.x>>self.level-1 & 1
        msb=p.y>>self.level-1 & 1
        return (msb<<1)+lsb
    def insert(self,p):
        if self.full:
            return
        if self.level==0:
            #TODO: Reached a leaf we should insert data p in this node
            self.full=True
        else:
            nPos=self.getPosNodeAtThisLevel(p)
            if self.nodes[nPos]==None:
                self.nodes[nPos]=pyQTree(self.level-1)
            self.nodes[nPos].insert(p)
            if self.allNodesFull():
                self.full=True
                #TODO: Before cleaning we should summary the data
                self.cleanNodes()
    def __str__(self):
        sv="level= %d full=%d"%(self.level,self.full)
        if not self.full:
            for i,n in enumerate(self.nodes):
                sv+=" %d-%d"%(i,self.level)
                if n!=None:
                    sv+="["+n.__str__()+"]"
                else:
                    sv+="[]"
        return sv
        

