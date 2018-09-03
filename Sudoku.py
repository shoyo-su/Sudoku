
def Sudoku(S,rindex,cindex):
    faltulist=[1,2,3,4,5,6,7,8,9]
    eprl=[1,2,3,4,5,6,7,8,9]
    eprc=9
    for i in S[rindex]:
        if i in faltulist:
            if i!=0:
                eprl.remove(i)
                eprc=eprc-1    
    epcc=9
    
    epcl=[1,2,3,4,5,6,7,8,9]
    r1index=0
    while r1index<9:
        x=S[r1index][cindex]
        if x in faltulist:
            if x!=0:
                epcl.remove(x)
                epcc=epcc-1
        r1index=r1index+1    
    
    rl=[value for value in eprl if value in epcl]# 
    return rl            


def lrem(S):
    for row in S:
        for ele in row:
            if ele in range(1,10):
                for ele2 in row:
                    if ele2 in range(1,10):
                        None
                    else:
                        for tval in ele2:
                            if ele==tval:
                                ele2.remove(tval)

    return S                             

def valuedel1(S,pos,tval):
  x=pos[0]
  y=pos[1]
  indexr=0
  while indexr<9:
    var=S[indexr][y]
    if var in range(1,10):
      None
    else:
      index=0
      for ele in var:
        if ele==tval:
          S[indexr][y].remove(tval)
        index=index+1
    indexr=indexr+1
  indexc=0
  while indexc<9:
    var=S[x][indexc]
    if var in range(1,10):
        None
    else:
      index=0
      for ele in var:
        if ele==tval:
          S[x][indexc].remove(tval)
        index=index+1
    indexc=indexc+1
  return S
                





def valuedel(S,pos,tval,posl):
  x=pos[0]
  y=pos[1]
  indexr=0
  while indexr<9:
    var=S[indexr][y]
    if var in range(1,10):
      None
    else:
      index=0
      for ele in var:
        if ele==tval:
          S[indexr][y].remove(tval)
        index=index+1
    indexr=indexr+1
  indexc=0
  while indexc<9:
    var=S[x][indexc]
    if var in range(1,10):
        None
    else:
      index=0
      for ele in var:
        if ele==tval:
          S[x][indexc].remove(tval)
        index=index+1
    indexc=indexc+1
  S=singleremove(S,posl)
  return S

             


def Check(l):
    count=0
    for i in l:
        count=count+1
    if count>1:
        return False
    else:
        return True
def boxcheck(S,pos,ele):
  x=pos[0]
  y=pos[1]
  if x<3:
    if y<3:
      ix=0
      while ix<3:
        ic=0
        while ic<3:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False 
        ix=ix+1
  if x<3:
    if 2<y<6:
      ix=0
      while ix<3:
        ic=3
        while ic<=5:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False

        ix=ix+1       
  if x<3:
    if y>5:
      ix=0
      while ix<3:
        ic=6
        while ic<9:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False
        ix=ix+1          
  if 2<x<6:
    if y<3:
      ix=3
      while ix<6:
        ic=0
        while ic<=3:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False
        ix=ix+1    

  if 2<x<6:
    if 2<y<6:
      ix=3
      while ix<6:
        ic=3
        while ic<=5:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False 
        ix=ix+1

  if 2<x<5:
    if y>5:
      ix=3
      while ix<6:
        ic=6
        while ic<9:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False
        ix=ix+1    

  if x>5:
    if y<3:
      ix=6
      while ix<9:
        ic=0
        while ic<=3:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False 
        ix=ix+1

  if x>5:
    if 2<y<6:
      ix=6
      while ix<9:
        ic=3
        while ic<=5:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False 
        ix=ix+1

      
      
  if x>5:
    if y>5:
      ix=6
      while ix<9:
        ic=6
        while ic<9:
          dum=S[ix][ix]
          ic=ic+1
          if dum==ele:
            return False 
        ix=ix+1    



  return True





def rowcolcheck(S,posl):
    for pos in posl:
      rowpos=pos[0]
      colpos=pos[1]
      wkl=S[rowpos][colpos]
      row=S[rowpos]
      col=[]
      index=0
      while index<9:
        col.append(S[index][colpos])
        index=index+1
      for i in wkl:
        if i not in row:
          if i not in col:
            S[rowpos][colpos]=i
    return S        


def colfill(S,pos,wklr1,wklr2,adjcol1,adjcol2,adjrow1,adjrow2,posl,wkl):
  #print(pos)
  rowpos=pos[0]
  colpos=pos[1]
  drindex=0
  while drindex<9:
   # print("ok")
    ele=S[drindex][adjcol1]
    if ele in range(1,10):
      dr1index=0
      while dr1index<9:
        #print("ok"+str(drindex))
        ele2=S[dr1index][adjcol2]
        #print(ele2)
        if ele==ele2:
          val=boxcheck(S,pos,ele)
         # print("pass")
          if val==True:
            v1=S[adjrow1][colpos]
            v2=S[adjrow2][colpos]

           # print("pass1")
            if v1 in range(1,10):
            #  print("v1p")
              if v2 in range(1,10):
             #   print("v2p")
                if ele in wkl:
                  S[rowpos][colpos]=ele
              #    print("t1")
                  S=valuedel(S,pos,ele,posl)
               #   print("t2")
                        #print(S)
                        #print("\n")
              else:
                if ele in wklr2:
                  None
                else:
                  if ele in wkl:
                    S[rowpos][colpos]=ele
                    S=valuedel(S,pos,ele,posl)
                          #print(S)
                        # print("\n")
            else:
              if v2 in range(1,10):
                if ele in wklr1:
                  None
                else:
                  if ele in wkl:
                    S[rowpos][colpos]=ele
                    S=valuedel(S,pos,ele,posl)
                        #print(S)
                        #print("\n")
                        #print("y")
              else:
                if ele in wklr1:
                  if ele in wklr2:
                    None
                  else:
                    None
                else:
                  if ele in wklr2:
                    None
                  else:
                    if ele in wkl:
                      S[rowpos][colpos]=ele
                      S=valuedel(S,pos,ele,posl)
                        #print(S)
                        #print("\n")
                       # print("y")
        #print("dr1index")
        dr1index=dr1index+1
    drindex=drindex+1
  #print("\n")
  #print("c")
  #print(S)
  return S



def adj2rccheck(S,posl):
  for pos in posl:
    #print(pos)
    rowpos=pos[0]
    colpos=pos[1]
    adjrow1=0
    adjrow2=0
    if rowpos==0:
      adjrow1=1
      adjrow2=2
    if rowpos==1:
      adjrow1=0
      adjrow2=2
    if rowpos==2:
      adjrow1=0
      adjrow2=1    
    if rowpos==3:
      adjrow1=4
      adjrow2=5
    if rowpos==4:
      adjrow1=3
      adjrow2=5  
    if rowpos==5:
      adjrow1=3
      adjrow2=4
    if rowpos==6:
      adjrow1=7
      adjrow2=8
    if rowpos==7:
      adjrow1=6
      adjrow2=8
    if rowpos==8:
      adjrow1=6
      adjrow2=7
    adjcol1=0
    adjcol2=0
    if colpos==0:
      adjcol1=1
      adjcol2=2
    if colpos==1:
      adjcol1=0
      adjcol2=2
    if colpos==2:
      adjcol1=0
      adjcol2=1    
    if colpos==3:
      adjcol1=4
      adjcol2=5
    if colpos==4:
      adjcol1=3
      adjcol2=5  
    if colpos==5:
      adjcol1=3
      adjcol2=4
    if colpos==6:
      adjcol1=7
      adjcol2=8
    if colpos==7:
      adjcol1=6
      adjcol2=8
    if colpos==8:
      adjcol1=6
      adjcol2=7
    wkl=S[rowpos][colpos]
    wklr1=S[adjrow1][colpos]
    wklr2=S[adjrow2][colpos]
    wklc1=S[rowpos][adjcol1]
    wklc2=S[rowpos][adjcol2]
    if wkl in range(1,10):
      continue
    else: 
      for ele in S[adjrow1]:
        if ele in range(1,10):
          for ele2 in S[adjrow2]:
            if ele==ele2:
              val=boxcheck(S,pos,ele)
              if val==True:
                v1=S[rowpos][adjcol1]#
                v2=S[rowpos][adjcol2]
                if v1 in range(1,10):
                  if v2 in range(1,10):
                     if ele in wkl:
                       S[rowpos][colpos]=ele
                       S=valuedel(S,pos,ele,posl)
                       #print(S)
                       #print("\n")
                  else:
                    if ele in wklc2:
                      continue
                    else:
                      if ele in wkl:
                        S[rowpos][colpos]=ele
                        S=valuedel(S,pos,ele,posl)
                        #print(S)
                       # print("\n")
                else:
                  if v2 in range(1,10):
                    if ele in wklc1:
                      continue
                    else:
                      if ele in wkl:
                        S[rowpos][colpos]=ele
                        S=valuedel(S,pos,ele,posl)
                        #print(S)
                        #print("\n")
                  else:
                    if ele in wklc1:
                      if ele in wklc2:
                        None
                      else:
                        None
                    else:
                      if ele in wklc2:
                        None
                      else:
                        if ele in wkl:
                          S[rowpos][colpos]=ele
                          S=valuedel(S,pos,ele,posl)
                         # print(S)
                        #  print("\n")
      
      #print(S)
      S=colfill(S,pos,wklr1,wklr2,adjcol1,adjcol2,adjrow1,adjrow2,posl,wkl)  
      
      '''
      drindex=0
      while drindex<9:
        dr1index=0
        ele=S[drindex][adjcol1]
        while dr1index<9:
          ele2=S[dr1index][adjcol2]
          if ele==ele2:
            val=boxcheck(S,pos,ele)
            if val==True:
              v1=S[adjrow1][colpos]
              v2=S[adjrow2][colpos]
              if v1 in range(1,10):
                  if v2 in range(1,10):
                     if ele in wkl:
                       S[rowpos][colpos]=ele
                       S=valuedel(S,pos,ele,posl)
                       #print(S)
                       #print("\n")
                  else:
                    if ele in wklr2:
                      continue
                    else:
                      if ele in wkl:
                        S[rowpos][colpos]=ele
                        S=valuedel(S,pos,ele,posl)
                        #print(S)
                       # print("\n")
              else:
                if v2 in range(1,10):
                  if ele in wklr1:
                    continue
                  else:
                    if ele in wkl:
                      S[rowpos][colpos]=ele
                      S=valuedel(S,pos,ele,posl)
                      #print(S)
                      #print("\n")
                      #print("y")
                else:
                  if ele in wklr1:
                    if ele in wklr2:
                       None
                    else:
                      None
                  else:
                    if ele in wklr2:
                      None
                    else:
                      if ele in wkl:
                        S[rowpos][colpos]=ele
                        S=valuedel(S,pos,ele,posl)
                        #print(S)
                        #print("\n")
                       # print("y")


          dr1index=dr1index+1
        drindex=drindex+1 '''



                                
          
  
  fc=0
  abr=0
  posli=[]
  while abr<9:
    abc=0
    while abc<9:
      d=S[abr][abc]
      if d in range(1,10):
        fc=fc+1
      else:
        pos=[]
        pos.append(abr)
        pos.append(abc)
        posli.append(pos)
      abc=abc+1
    abr=abr+1
  posl=posli      

  
  
  
  
  if fc<=80:
    S=lrem(S)
    S=singleremove(S,posl)
    S=adj2rccheck(S,posl)
  
  
  #print("y")
  return S                    




      
      


def singleremove(S,posl):
  for pos in posl:
    x=pos[0]
    y=pos[1]
    wkl=S[x][y]
    count=0
    if wkl in range(1,10):
      None
    else:
      for i in wkl:
        count=count+1
      if count==1:
        S[x][y]=wkl[0]
        S=valuedel1(S,pos,S[x][y])
  return S      
    
    
def play(S):
    rindex=0
    posl=[]
    for row in S:
        cindex=0
        for el in row:
            if el==0:
                l=Sudoku(S,rindex,cindex)
                check=Check(l)
                if check==True:
                    S[rindex][cindex]=l[0]
                    play(S)
                if check==False:
                    S1=S
                    pos=[]
                    S1[rindex][cindex]=l
                    pos.append(rindex)
                    pos.append(cindex)
                    posl.append(pos)
            cindex=cindex+1       
        if rindex>=8:
            if cindex>=8:
                #print(S1)
                #print("\n")
                ans=adj2rccheck(S1,posl)
        rindex=rindex+1
    return ans      
        
print(play([[0, 0, 6, 1, 0, 0, 0, 0, 8], 
          [0, 8, 0, 0, 9, 0, 0, 3, 0], 
          [2, 0, 0, 0, 0, 5, 4, 0, 0], 
          [4, 0, 0, 0, 0, 1, 8, 0, 0], 
          [0, 3, 0, 0, 7, 0, 0, 4, 0], 
          [0, 0, 7, 9, 0, 0, 0, 0, 3], 
          [0, 0, 8, 4, 0, 0, 0, 0, 6], 
          [0, 2, 0, 0, 5, 0, 0, 8, 0], 
          [1, 0, 0, 0, 0, 2, 5, 0, 0]]))    
