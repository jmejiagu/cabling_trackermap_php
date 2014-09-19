#!/usr/bin/env python
import re
import urllib
import urllib2
import pickle
import os
import sys
from optparse import OptionParser



#this function implemets callback to make the optpars able to take several arguments for each option##
def cb(option, opt_str, value, parser):
    args=[]
    for arg in parser.rargs:
        if arg[0] != "-":
            args.append(arg)
        else:
            del parser.rargs[:len(args)]
            break
    if getattr(parser.values, option.dest):
        args.extend(getattr(parser.values, option.dest))
    setattr(parser.values, option.dest, args)

def getLatestCabling():
   cabfile = ""
   url = "https://test-stripdbmonitor.web.cern.ch/"
   path = "test-stripdbmonitor/CondDBMonitoring/cms_orcoff_prod/CMS_COND_31X_STRIP/DBTagCollection/SiStripFedCabling/SiStripFedCabling_GR10_v1_hlt/CablingLog/"
   pattern = '<a href="CablingInfo_Run.*?">(.*?)</a>'
   response = urllib2.urlopen(url+path).read()
   for filename in re.findall(pattern, response):
      cabfile = filename
   print cabfile
   return cabfile


def filenameF(name):
    suffix='CablingInfo_Run'
    filenameX=suffix+name+'.txt'
    url="https://test-stripdbmonitor.web.cern.ch/test-stripdbmonitor/CondDBMonitoring/cms_orcoff_prod/CMS_COND_31X_STRIP/DBTagCollection/SiStripFedCabling/SiStripFedCabling_GR10_v1_hlt/CablingLog/"
    urllib.urlretrieve(url+filenameX,filenameX)
    return filenameX

def semilinkF(namelink):

    pattern=re.split('/',namelink)
    filelink=pattern[-1]

    url="https://test-stripdbmonitor.web.cern.ch/test-stripdbmonitor/CondDBMonitoring/cms_orcoff_prod/CMS_COND_31X_STRIP/DBTagCollection/SiStripFedCabling/"
    urllib.urlretrieve(url+namelink,filelink)

    return filelink

###this function makes a dictionary of Detids(with pairnumber as secondkey) and a dictionary of FEDs (with FecCH as second key) for the cabling file 
def DictionaryCab(filenameC,options):
    """This function takes a filename as input and looks for it in the URL, then makes a dictionary with DetId as key and pairnumber as key2 or FEDid as key1 and FedCh as key2"""
    FiletxtFEDs = open(filenameC,'r')

    Fd = "FedCrate/FedSlot/FedId/FeUnit/FeChan/FedCh"
    Fc = "FecCrate/FecSlot/FecRing/CcuAddr/CcuChan"
    D = "DcuId/DetId"
    Ll = "LldChan/APV0/APV1"
    pair = "pairNumber/nPairs/nStrips"
    DC = "DCU/MUX/PLL/LLD"
 
    DictionaryCab.CablingInfoDict={}		
    CablingInfoDictF={}
    # Creating lists
    FedCrateList = []
    FedSlotList = []
    FedIdList=[]
    FeUnitList=[]
    FeChanList=[]
    FedChList=[]
		
    FecCrateList=[]
    FecSlotList=[]
    FecRingList=[]
    CcuAddrList=[]
    CcuChanList=[]
		
    DcuIdList=[]
    DetIdList=[]
		
    LldChanList=[]
    APV0List=[]
    APV1List=[]
    pairNumberList=[]
    nPairsList=[]
    nStripsList=[]
		
    DCUList=[]
    MUXList=[]
    PLLList=[]
    LLDList=[]


    for line in FiletxtFEDs:
        if Fd in line:
            pattern = re.split('\W+',line)
            FedCrateList.append(pattern[7])
            FedSlotList.append(pattern[8])
            FedIdList.append(pattern[9])
            FeUnitList.append(pattern[10])
            FeChanList.append(pattern[11])
            FedChList.append(pattern[12])
        if Fc in line:
            pattern = re.split('\W+',line)
            FecCrateList.append(pattern[6])
            FecSlotList.append(pattern[7])
            FecRingList.append(pattern[8])
            CcuAddrList.append(pattern[9])
            CcuChanList.append(pattern[10])
        if D in line:
            pattern = re.split('\W+',line)
            DcuIdList.append(str(int(pattern[3],16)))
            DetIdList.append(str(int(pattern[4],16)))
        if Ll in line:
            pattern = re.split('\W+',line)
            LldChanList.append(pattern[4])
            APV0List.append(pattern[5])
            APV1List.append(pattern[6])
        if pair in line:
            pattern = re.split('\W+',line)
            pairNumberList.append(pattern[4])
            nPairsList.append(pattern[5])
            nStripsList.append(pattern[6])
        if DC in line:
            pattern = re.split('\W+',line)
            DCUList.append(pattern[6])
            MUXList.append(pattern[7])
            PLLList.append(pattern[8])
            LLDList.append(pattern[9])
        
		

    for fedcrate,fedslot,fedid,feunit,fechan,fedch,feccrate,fecslot,fecring,ccuaddr,ccuchan,dcuid,detid,lldchan,apv0,apv1,pairnumber,npairs,nstrips,dcu,mux,pll,lld  in zip(FedCrateList,FedSlotList,FedIdList,FeUnitList,FeChanList,FedChList,FecCrateList,FecSlotList,FecRingList,CcuAddrList,CcuChanList,DcuIdList,DetIdList,LldChanList,APV0List,APV1List,pairNumberList,nPairsList,nStripsList,DCUList,MUXList,PLLList,LLDList):

        if detid in DictionaryCab.CablingInfoDict.keys(): 
            DictionaryCab.CablingInfoDict[detid].update({pairnumber:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}})
		
        else:
            DictionaryCab.CablingInfoDict.update({detid:{pairnumber:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}}})


    for fedcrate, fedslot, fedid, feunit, fechan, fedch, feccrate, fecslot, fecring, ccuaddr, ccuchan, dcuid, detid, lldchan, apv0, apv1, pairnumber, npairs, nstrips, dcu, mux, pll, lld in zip(FedCrateList, FedSlotList, FedIdList, FeUnitList, FeChanList, FedChList, FecCrateList, FecSlotList, FecRingList, CcuAddrList, CcuChanList, DcuIdList, DetIdList, LldChanList, APV0List, APV1List, pairNumberList, nPairsList, nStripsList, DCUList, MUXList, PLLList, LLDList): 
  
                        
        if fedid in CablingInfoDictF.keys(): 
            CablingInfoDictF[fedid].update({fedch:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}})
               
        else:
            CablingInfoDictF.update({fedid:{fedch:{"FedCrate": fedcrate,"FedSlot":fedslot,"FedId":fedid,"FeUnit":feunit,"FeChan":fechan,"FedCh":fedch,"FecCrate":feccrate,"FecSlot":fecslot,"FecRing":fecring,"CcuAddr":ccuaddr,"CcuChan":ccuchan,"DcuId":dcuid,"DetId":detid,"pairNumber":pairnumber,"LldChan":lldchan,"APV0":apv0,"APV1":apv1,"nPairs":npairs,"nStrips":nstrips,"DCU":dcu,"MUX":mux,"PLL":pll,"LLD":lld}}})




############THESE INSTRUCTIONS ARE FOR GETTING THE INFO OF THE DICTIONARY FOR THE CABLING FILE#############################3
    #dump the detids of the cabling file in a txt file and make a trackermap
    if options.listrc2:
        archi=open(options.listrc2,'w')
        [archi.write("%s\n"%p) for p in DictionaryCab.CablingInfoDict]
        archi.close
        print "A file named %r has been created" %options.listrc2


    #trackermap of the modules of the cabling
    if options.listrc:
        archi=open('trackermapdetids.txt','w')
        [archi.write(p+" "+"255"+" "+ "0"+" "+"0"+"\n") for p in DictionaryCab.CablingInfoDict]

        archi.close
        os.system(('print_TrackerMap trackermapdetids.txt TrackerMap %r 2400 False True 999 -999')%options.listrc)
        print "A file named trackermapdetids.txt and a tracker map named %r have been created" %options.listrc
   
   #A file with the DetIds associated to a(some) FED(s)	
    if options.lisfem and options.fnafe:
        archi1=open(options.fnafe,'w')
        lif1=options.lisfem
        visited=set()

        for p in lif1:
            archi1.write("The modules associated to FED %s are:\n" %p)
            for r in CablingInfoDictF[p]:
               if CablingInfoDictF[str(int(p))][r]["DetId"]:
                    visited |={CablingInfoDictF[str(int(p))][r]["DetId"]}
                    archi1.write(CablingInfoDictF[str(int(p))][r]["DetId"]+"\n")
        

   # A Trackermap of the detids associated to a (some) Fed(s)
    if options.lisfetrc:
        archi=open('ModulestoFeds.txt','w')
        li1=options.lisfetrc
        color_list=["0 255 0","0 0 255","255 0 0","255 0 255","0 255 247","255 69 0","51 0 51","250 128 114","47 79 79"]
        for j in color_list:
            for p in li1:
                for q in CablingInfoDictF[p].keys():
                    archi.write(CablingInfoDictF[p][q]["DetId"]+j)
                    
        archi.close()
        variable =""

        color_list1=["green","blue","red","pink","cyan","orange","purple","salmon","dark slate gray"]
        for i,j in zip (li1,color_list1):
            variable+='%s=%s  ' % (i,j)
        os.system('print_TrackerMap ModulestoFeds.txt "FEDs: %s for file %s" %r  2400 False True 999 -999' % (variable,filenameC,options.fnmodtof))
      
    #Info about a (set of) module(s)
    if  options.lismod and options.pairnumb:
        li3=options.lismod
        li4=options.pairnumb
        li5=options.infmod
        txt=open('infomodules.txt','w')
        for i in li3:
            for j in li4:
                txt.write("For DetID : %r with pairNumber: %r\n "%(i,j))
                for k in li5:
                    txt.write(" %r is:%r\n "%(k,DictionaryCab.CablingInfoDict[i][j][k]))
        print("A file named infomodules.txt has been created")
               

    #info about a (set of) Fed(s)
    if options.lisfed and options.fedc:
        
        li3=options.lisfed
        li4=options.fedc
        li5=options.infed
        txt=open('infofeds.txt','w')
        for l,m in zip(li3,li4):
            txt.write( "For FedId : %r with FedCh : %r \n"%(l,m))
            for n in li5:
                txt.write( " %r is:%r \n"%(n,CablingInfoDictF[l][m][n]))
        print("A file named infofeds.txt has been created")

   #modules associated to something
    if options.infomod2 and options.infomod3:
        li6=options.infomod2
        li7=options.infomod3
        txt1=open('ModofCab.txt','w')
        visited=set([])
        for k,i in zip(li6,li7):
            txt1.write("Los modulos con %s:%s son :\n"%(k,i))
            for l in DictionaryCab.CablingInfoDict:
                flag=True
                for m in DictionaryCab.CablingInfoDict[l]:
                    for n in DictionaryCab.CablingInfoDict[l][m]:
                        if DictionaryCab.CablingInfoDict[l][m][k]==i:
                            visited |={str(l)}
                            txt1.write("%s\n"%str(l))
        print len(visited)
        print "A file named ModofCab.txt with the modules with the info written has been created"
                     
        txt1.close() 
   
   ###Properties of cabling with modules in common 

    if options.cabcommon1 and options.cabcommon2:
        txt_2 = open("CabinCommon",'w')
        li1=options.cabcommon1
        li2=options.cabcommon2

        objectives = []
        DictionaryCab.CablingInfoDict
        txt=open('Modulescommon.txt','w')
        txt.write("The modules in common for:  ")
        for i,j in zip(li1,li2):
            txt.write("%s %s, "%(i,j))
        for l in DictionaryCab.CablingInfoDict.keys(): #for every detid
            flag = True
            #to add det id para que se agregue su DetId a la lista
            for x in DictionaryCab.CablingInfoDict[l].keys(): #para cada pairnumber
                #print "pairnumber:", x, type(x)
                for proper in range(len(li1)): #para cada propiedad
                    #print "propiedad:", li1[proper], type(li1[proper])
                    if DictionaryCab.CablingInfoDict[l][x][li1[proper]] != li2[proper]:
                        flag = False #si no cumple con todas lo descartamos
            if flag:
                objectives.append(l)
                txt.write("\n%s"%l)
        print("A file named Modulescommon.txt has been created")


    return DictionaryCab
####################3THESE INSTRUCTIONS ARE FOR GETTING THE INFO OF THE ALIAS ######################
def AliasFun(filenameC,options,AliasDict):
    FileAliasD=open(filenameC,'r')
    D="DcuId/DetId"
    DetIdAlList=[]
    for line1 in FileAliasD:
        if D in line1:
            pattern1 = re.split('\W+',line1)
            if (int(pattern1[4],16)) not in DetIdAlList:
                DetIdAlList.append(int(pattern1[4],16))
    AliasFun.SAliasDict={}
    for detID in DetIdAlList:
        beta1 = (AliasDict[int(detID)]) 
        AliasFun.SAliasDict.update({int(detID):beta1})

   #A file with the alias of the detids of the cabling file   
    if options.fialc:
        beta1=""
        txt_1=open(options.fialc,'w')
        for detID in DetIdAlList:
            beta1 = str(AliasDict[int(detID)])
            txt_1.write("%s  %s\n"  %(detID,beta1.split("'")[1]))
        print "A file named %r has been created" %options.fialc
   
    #the alias of a (set of) module(s)     
    if options.alimod:
        txt=open('AliasModules.txt','w')
        for i in options.alimod:
            beta2= str(AliasFun.SAliasDict[int(i)])
            txt.write("for module with DetId %r, Alias is %r\n" %(i,beta2.split("'")[1]))
        print "A file named AliasModules.txt has been created"

   #A file with the modules associated to a certain Alias(es)
    if options.modali and options.filena:
        txt_2 = open (options.filena,'w')       
        beta3=""
        for j in options.modali:
            txt_2.write("For Alias %r, the DetIds associated are:\n" % j)
            for detid in AliasFun.SAliasDict.keys():
                beta3 = str(AliasFun.SAliasDict[detid])
                if j in beta3:
                    txt_2.write("%r \n" %detid)

    #A tracker map of the modules associated to an alias
    if options.alitkm:
        txt_4=open('faliastkm.txt','w')
        li4=options.alitkm
        beta4=""
        j=0
        for k in li4:
            j+=1
            if j==1: 
                for detid in  AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"0"+" "+ "255"+" "+"0"+"\n")
            if j==2:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"0"+" "+ "0"+" "+"255"+"\n")
            if j==3:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"255"+" "+ "0"+" "+"0"+"\n")
            if j==4:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"255"+" "+ "255"+" "+"0"+"\n")
            if j==5:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"255"+" "+ "0"+" "+"255"+"\n")
            if j==6:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"0"+" "+ "255"+" "+"255"+"\n")
            if j==7:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"0"+" "+ "102"+" "+"0"+"\n")
            if j==8:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"102"+" "+ "0"+" "+"102"+"\n")
            if j==9:
                for detid in AliasFun.SAliasDict.keys():
                    beta4=str(AliasFun.SAliasDict[detid])
                    if k in beta4:
                        txt_4.write("%r"%detid+" "+"0"+" "+ "0"+" "+"0"+"\n")
		
        
        txt_4.close()
        color_list = ["green","blue","red","yellow","magenta","light blue","dark green","purple","black"]
        variable =""


        for i,j in zip (li4,color_list):
            variable+='%s=%s  ' % (i,j)
        os.system('print_TrackerMap faliastkm.txt "value: %r for Run  %r" %r 2400 False True 999 -999' % (variable,filenameC,options.fnaltomod))                      
   ##To know if a module is or is not in a detector or subdetector
    if options.modinf and options.subinf:
        txt=open('TrueFalseAlias.txt','w')
        for k in options.modinf:
            for l in options.subinf:
                beta6= str(AliasFun.SAliasDict[int(k)])
                if l in beta6:
                    
                   txt.write("For DetId %s true %s\n"%(k,l))

                if l not in beta6:
                    txt.write("For DetId %s false %s\n"%(k,l))
        print "A file named TrueFalseAlias.txt has been created"

####THE NEXT FUNCTIONS ARE FOR GETTING THE INFO OF THE HV#########


#function to extract the Detids of the cabling file in a txt file
def DetIdCabL(filenameC,verbose=True):                                                 
    """This function takes a filename as input and looks for it in URL ... ,
    it parses all detIDs and dumps them in a local file named detIdCab.txt""" 
    #filenameX=filenameC+'.txt'
    FileCabList = open(filenameC,'r')
    D = "DcuId/DetId" 
    DetIdCabList = []
    for line1 in FileCabList:                                                                                                           
        if D in line1:
            pattern1 = re.split('\W+',line1)
            if (int(pattern1[4],16)) not in DetIdCabList:
                DetIdCabList.append(int(pattern1[4],16))  
    txtCab=open("DetIdCab.txt",'w')
    for i in DetIdCabList:
        txtCab.write("%r\n" %i)
    
    return 
#function to make a PSUName file of the cabling file

def CabHVFiles(fileCab,fileHV,verbose=True):
    sep = " "
    d = {}
    for line in  open(fileHV, "r"):
        key, val = line.strip().split(sep)
        d[key] = val
    detIDs=[line.strip() for line in open(fileCab, "r")] 
    OutFile=open('file.txt','w')
    for detID in detIDs:
        OutFile.write("%s %s\n" % (detID,d[detID]))

#function to make the dictionary of the psuname file of the cabling file

def HVInfoDictF(filenameC,filename, options):
    FiletxtHV = open(filename,'r')
    HVInfoDictF.HVInfoDict = {}
    DetIdList = []
    PSUList = []
    CmstrkList = []
    TrackerSyList= []
    BranchList = []
    CrateList = []
    BoardList = []
    ChannelList = []
    for line2 in FiletxtHV:
        if "cms_trk" in line2 :
            pattern1 = re.split(' ',line2)
            DetIdList.append(pattern1[0])
            PSUList.append(pattern1[1].split("\n")[0])
            pattern2 = re.split('/',pattern1[1])
            CmstrkList.append(pattern2[0])
            TrackerSyList.append(pattern2[1])
            BranchList.append(pattern2[2])
            CrateList.append(pattern2[3])
            BoardList.append(pattern2[4])
            ChannelList.append(pattern2[5].split("\n")[0])
    for detid,psu,cmstrk,trackersy,branch,crate,board,channel in zip(DetIdList,PSUList,CmstrkList,TrackerSyList,BranchList,CrateList,BoardList,ChannelList):
        HVInfoDictF.HVInfoDict.update({detid:{'PSUName':psu,'Cmstrk':cmstrk,'TrackerSY':trackersy,'Branch':branch,'Crate':crate,'Board':board,'Channel':channel}})
    ###here are the stuff that the code provides
    #info about a module
    if options.search_and and options.look_and: 
        li1=options.search_and
        li2=options.look_and   
        txt=open('InfoModuleHV.txt','w')
        for i in li1:
            txt.write("For DetId %s:\n" %i)
            for j in li2: 
                txt.write(" %s is: %s \n" % (j,HVInfoDictF.HVInfoDict[i][j]))
        print "A file named InfoModuleHV.txt has been created"
    #a file with the modules associated to some values
    if options.see_and and options.filenameva: 
     
        txt_1=open(options.filenameva,'w')
        li3=options.see_and
        for k in li3:
            txt_1.write("The modules with property %r are:\n" % k)
            for l in HVInfoDictF.HVInfoDict:
                for m in HVInfoDictF.HVInfoDict[l]:
                    if HVInfoDictF.HVInfoDict[l][m]==k:
                        txt_1.write("\n %s" % l)
        print "A file named %r has been created"%options.filenameva

    if options.vatrcm:
        txt_1=open('filevamod.txt','w')
        li1=options.vatrcm
        j=0
        for k in li1:
            j+=1
            if j==1: 
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k:
                            txt_1.write("%s"%l+" "+"0"+" "+ "255"+" "+"0"+"\n")
            if j==2:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k:
                            txt_1.write("%s"%l+" "+"0"+" "+ "0"+" "+"255"+"\n")
            if j==3:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k:
                            txt_1.write("%s"%l+" "+"255"+" "+ "0"+" "+"0"+"\n")
            if j==4:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k:
                            txt_1.write("%s"%l+" "+"255"+" "+ "255"+" "+"0"+"\n")
            if j==5:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k:
                            txt_1.write("%s"%l+" "+"255"+" "+ "0"+" "+"255"+"\n")
            if j==6:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k: 
                            txt_1.write("%s"%l+" "+"0"+" "+ "255"+" "+"255"+"\n")
            if j==7:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k:
                            txt_1.write("%s"%l+" "+"0"+" "+ "102"+" "+"0"+"\n")
            if j==8:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k: 
                            txt_1.write("%s"%l+" "+"102"+" "+ "0"+" "+"102"+"\n")
            if j==9:
                for l in HVInfoDictF.HVInfoDict:
                    for m in HVInfoDictF.HVInfoDict[l]:
                        if HVInfoDictF.HVInfoDict[l][m]==k: 
                            txt_1.write("%s"%l+" "+"0"+" "+ "0"+" "+"0"+"\n")
		
        
        txt_1.close()
        color_list = ["green","blue","red","yellow","magenta","light blue","dark green","purple","black"]
        variable =""


        for i,j in zip (li1,color_list):
            variable+='%s=%s  ' % (i,j)
        os.system('print_TrackerMap filevamod.txt "value: %r for file %r" %r 2400 False True 999 -999' % (variable,filenameC,options.fnmodtov))       
       
    #a file with the modules associated to some values simmultaneously
 
    if options.read_and and options.filenameco:
        txt = open(options.filenameco,'w')
        li4=options.read_and
        txt.write("The modules in common for values: ")
        [txt.write("%s, "%x) for x in li4]
        for n in HVInfoDictF.HVInfoDict:
            if len(set(li4).intersection(HVInfoDictF.HVInfoDict[n].values())) == len(li4):
                txt.write("\n%s" % n)
        txt.close  
        print "A file named %s has been created"%options.filenameco
        
    return HVInfoDictF.HVInfoDict  

##########HERE WE INTRODUCE THE OPTIONS FOR THE INFO#######################33
if __name__ == "__main__":
    verbose = True
    usage = "useage: %prog [options] "
    parser = OptionParser(usage)
    parser.set_defaults(mode="advanced")
    parser.add_option("-f", "--file", type="string", dest="filenameC", help="Write the run of the cabling file")
    parser.add_option("--fu", "--fileu", type="string", dest="fileurl", help="write the link to the cabling file beggining with: SiStripFedCabling_...CablingInfoRun_X.txt")

    #############these options are fot getting the info of the cabling file####################################
    parser.add_option("-a","--imod2",type="string", dest="listrc2", help="List of DetIds of the cabling file in a txt, write the name of the file")

    parser.add_option("--at","--imod",type="string", dest="listrc", help="List of DetIds of the cabling file in a txt file and a trackermap, write the name of the image(.png)")

    parser.add_option("-z","--lisf",action="callback", callback = cb, dest="lisfem", help="Modules associated to a(some) Fed(s),write the Feds  whereof you want to know the modules associated")
    parser.add_option("--zi","--fnaf",type="string",dest="fnafe",help="Write the name of the file with the modules associated to a(some) Fed(s)")


    parser.add_option("-b","--data",action="callback", callback=cb, dest="lisfetrc", help="Tracker map of DetIds connected to some FEDs to locate them in the detector, write -b followed by the FedIds")
    parser.add_option("--bf","--dataf",type="string", dest="fnmodtof", help="name of the trackermap (name.png)")

    parser.add_option("-c","--modul",action="callback", callback=cb, dest="lismod", help="Information about a(some) module(s),write the modules")
    parser.add_option("--cp","--pairs",action="callback",callback=cb,dest="pairnumb",help="write the pairnumber of the module(s) selected, write the pair number 0,1 or 3, or the three of them")
    parser.add_option("--ci","--infom",action="callback",callback=cb, dest="infmod", help="write what you want to know about the modules introduced,FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")

    parser.add_option("-g","--feds",action="callback", callback=cb, dest="lisfed", help="Information about a(some) Fed(s),write the FedIds")
    parser.add_option("--gf","--fedch",action="callback",callback=cb,dest="fedc",help="write the FedCh of the Fed(s) selected")
    parser.add_option("--gi","--infof",action="callback",callback=cb, dest="infed", help="write what you want to know about the Fed(s) introduced,FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")
     
    parser.add_option("-d","--infom2",action="callback",callback=cb, dest="infomod2", help="info  you want to know the modules associated to, like:FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")
    parser.add_option("--di","--infom3",action="callback",callback=cb, dest="infomod3", help="write the number belonging to the info given in -d, like FedCrate 23 or CcuAddr 123 (just write the number)")

    parser.add_option("-n","--cabc1",action="callback",callback=cb, dest="cabcommon1", help="if you want to know the modules in common for several info of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")
    parser.add_option("--ni","--cabc2",action="callback",callback=cb, dest="cabcommon2", help="here goes the number of the property")

 

    ########these options are for the alias#############################################

    parser.add_option("-k","--fila",type="string", dest="fialc", help="Dump the Alias of the DetIds of the Cabling file in a txt file, write the name of the file")
    parser.add_option("-l","--alim",action="callback", callback=cb, dest="alimod", help="Know the Alias of a (set of) module(s),write the modules")
    
    parser.add_option("-m","--moda",action="callback", callback=cb, dest="modali", help="Know the modules associated to some Alias,write the Alias or something like: from TEC, TECmi, TECminus_7,TECminus_7_5 etc")
    parser.add_option("--mf","--filn",type="string",dest="filena",help="write the name of the file with the modules associated to some alias")
   
    parser.add_option("-y","--altk",action="callback",callback=cb,dest="alitkm",help="write the alias where of you want a trackermap of detids associated to those alias")
    parser.add_option("--yf","--fnma",type="string",dest="fnaltomod",help="write the name of the image(name.png) ")


    parser.add_option("-o","--modi",action="callback",callback=cb,dest="modinf",help="write the modules to know if they are located on certain subdetector")
    parser.add_option("--os","--subi",action="callback",callback=cb, dest="subinf", help="write the subdetector in order to know if the module is located there")

    ################these options are for the hv#######################
    
    parser.add_option("-r","--inmod",action="callback", callback = cb, dest="search_and", help="write the modules in order to get some info")
    parser.add_option("--ri","--datas",action="callback", callback = cb, dest="look_and", help="write the options of the Info about a (set of) module(s),like PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel")

    parser.add_option("-t","--values",action="callback", callback = cb, dest="see_and", help="Modules associated to a(some) value(s),write the values whereof you want to know the modules associated,like cms_trk_dcs_05:CAEN (from 02 to 05), CMS_TRACKER_SY1527_8 (from 1 to 9),branchController05 (from 02 to 05),easyCrate3 (from 1 to 5), easyBoard06 (from 01 to 17), channel002 (002 or 003)")
    parser.add_option("--tf","--names",type="string",dest="filenameva",help="Write the name of the file with the modules associated to some values")
   
    parser.add_option("-v","--trvac",action="callback",callback=cb,dest="vatrcm",help="Trackermap of the modules of certain values (those in option t)")
    parser.add_option("--vf","--fnmv",type="string",dest="fnmodtov",help="name of the Tracker map image  for modules associated to some hv (.png)")

    parser.add_option("-w","--common", action="callback",callback=cb, dest="read_and", help="Values with modules in common, those in option -t")
    parser.add_option("--wf","--common2", type="string", dest="filenameco", help="Name of file for Values with modules in common")
  
    #################other info#################

    parser.add_option("-e","--alcab1", action="callback",callback=cb, dest="aliascab1", help="write the property to know the location in the detector:value of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")
    parser.add_option("--en","--alcab2", action="callback",callback=cb, dest="aliascab2", help="here goes the number of the property")

    parser.add_option("-i","--alcab3", action="callback",callback=cb, dest="aliascab3", help="write the property to know the location in the detector:value of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")
    parser.add_option("--in","--alcab4", action="callback",callback=cb, dest="aliascab4", help="here goes the number of the property")
    parser.add_option("--ia","--alcab5", action="callback",callback=cb, dest="aliascab5", help="here goes the subdetector whereof you want to know if the module with the property chosen is there")

    parser.add_option("-j","--cabalj", action="callback",callback=cb, dest="cabalias1", help="here goes the alias whereof you want to know the info cabling")
    parser.add_option("--ja","--cabalj2", action="callback",callback=cb, dest="cabalias2", help="here goes the info you want to know like:FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD ")

    parser.add_option("-p","--alhv", action="callback",callback=cb, dest="aliashv", help="to know the alias of the modules with hv -p property, write the hv property, like those in option -t ")


    parser.add_option("-q","--hval1", action="callback",callback=cb, dest="hvalias1", help="to know the alias of modules with certain property of HV, write the alias you want to know ")
    parser.add_option("--qi","--hval2", action="callback",callback=cb, dest="hvalias2", help="write the hv property,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel")


    parser.add_option("-s","--hvca1", action="callback",callback=cb, dest="hvcab1", help="write the cabling info you know, like: FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD ")
    parser.add_option("--sc","--hvca2", action="callback",callback=cb, dest="hvcab2", help="write the number of the cabling info like: FecRing 34 FedCrate 23(just write the number, on option s you write the number of the property ")
    parser.add_option("--sh","--hvca3", action="callback",callback=cb, dest="hvcab3", help="write the hv info you want to know, like:,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel" )

    parser.add_option("-u","--cahv1", action="callback",callback=cb, dest="cabhv1", help="write the hv property you know , like:cms_trk_dcs_05:CAEN (from 02 to 05), CMS_TRACKER_SY1527_8 (from 1 to 9),branchController05 (from 02 to 05),easyCrate3 (from 1 to 5), easyBoard06 (from 01 to 17), channel002 (002 or 003)")  
    parser.add_option("--uc","--cahv2", action="callback",callback=cb, dest="cabhv2", help="to know cabling info of modules with certain property of HV, write the cabling info you want to know, like: FedCrate,FedSlot,FedId,FeUnit,FeChan,FedCh,FecCrate,FecSlot,FecRing,CcuAddr,CcuChan,DcuId,DetId,LldChan,APV0,APV1,pairNumber,nPairs,nStrips,DCU,MUX,PLL,LLD")



    (options, args) = parser.parse_args()
    if (options.filenameC is None and options.fileurl is None):
        url = "https://test-stripdbmonitor.web.cern.ch/"
        path = "test-stripdbmonitor/CondDBMonitoring/cms_orcoff_prod/CMS_COND_31X_STRIP/DBTagCollection/SiStripFedCabling/SiStripFedCabling_GR10_v1_hlt/CablingLog/"
        cablingfile = getLatestCabling()
        urllib.urlretrieve(url+path+cablingfile,cablingfile)
        
        ourdictionary=DictionaryCab(cablingfile,options)
        #options.filenameC = cablingfile

        StripDetIDAliasDict=pickle.load(open(os.getenv("CMSSW_RELEASE_BASE")+"/src/CalibTracker/SiStripDCS/data/StripDetIDAlias.pkl"))

        MyAlias=AliasFun(cablingfile,options,StripDetIDAliasDict)

        MyCabList=DetIdCabL(cablingfile)

        fileCab1= 'DetIdCab.txt'
        fileHV1='/afs/cern.ch/cms/slc5_amd64_gcc481/cms/cmssw/CMSSW_7_0_4/src/CalibTracker/SiStripDCS/data/StripPSUDetIDMap_BeforeJan132010.dat' 
    
        MyCabHV=CabHVFiles(fileCab1,fileHV1)
        input5='file.txt'
        MyHVDict = HVInfoDictF(input5, options)

    

    #########HERE ALL THE FUNCTIONS ARE CALLED 
    if options.filenameC:
        MyFilename=filenameF(options.filenameC)
    
    ## for the alias
        StripDetIDAliasDict=pickle.load(open(os.getenv("CMSSW_RELEASE_BASE")+"/src/CalibTracker/SiStripDCS/data/StripDetIDAlias.pkl"))

        MyAlias=AliasFun(MyFilename,options,StripDetIDAliasDict)

  
    ##for the dictionary of the cabling file
        ourdictionary=DictionaryCab(MyFilename,options)
     ##for the HV
        MyCabList=DetIdCabL(MyFilename)
        fileCab1= 'DetIdCab.txt'
        fileHV1='/afs/cern.ch/cms/slc5_amd64_gcc481/cms/cmssw/CMSSW_7_0_4/src/CalibTracker/SiStripDCS/data/StripPSUDetIDMap_BeforeJan132010.dat' 
        MyCabHV=CabHVFiles(fileCab1,fileHV1)
        input5='file.txt'
        MyHVDict = HVInfoDictF(MyFilename,input5, options)
   

    if options.fileurl:

        Mylink=semilinkF(options.fileurl)
    
    ## for the alias
        StripDetIDAliasDict=pickle.load(open(os.getenv("CMSSW_RELEASE_BASE")+"/src/CalibTracker/SiStripDCS/data/StripDetIDAlias.pkl"))

        MyAlias=AliasFun(Mylink,options,StripDetIDAliasDict)

  
    ##for the dictionary of the cabling file
        ourdictionary=DictionaryCab(Mylink,options)
     ##for the HV
        MyCabList=DetIdCabL(Mylink)
        fileCab1= 'DetIdCab.txt'
        fileHV1='/afs/cern.ch/cms/slc5_amd64_gcc481/cms/cmssw/CMSSW_7_0_4/src/CalibTracker/SiStripDCS/data/StripPSUDetIDMap_BeforeJan132010.dat' 
        MyCabHV=CabHVFiles(fileCab1,fileHV1)
        input5='file.txt'
        MyHVDict = HVInfoDictF(input5, options)
   

####These options are to get information from one source to another ###########

           #####To know the alias of modules with certain info of the cabling file  
    if options.aliascab1 and options.aliascab2: 
    
        li1=options.aliascab1
        li2=options.aliascab2
        txt=open('AliasforCabling.txt','w')
        for k,i in zip(li1,li2):  
            txt.write("The Alias of modules with %s:%s are: \n" %(k,i))
            for j,l in DictionaryCab.CablingInfoDict.items():
                for m,n in l.items():
                    if DictionaryCab.CablingInfoDict[j][m][k]==i:
                        beta="" 
                        beta=str(AliasFun.SAliasDict[int(j)])
                        txt.write( "%s  %s \n " %(j,beta.split("'")[1]))
        print "A txt file named AliasforCabling.txt has been created"

   ########To know the alias of modulos with certain info of the HV######
    if options.aliashv:
        li1=options.aliashv
        txt=open('aliastohv.txt','w')
        for j in li1:  
            txt.write("The Alias of modules with %s are: \n"%j)
            for k in HVInfoDictF.HVInfoDict:
                for m in HVInfoDictF.HVInfoDict[k]:
                    if  HVInfoDictF.HVInfoDict[k][m]==j:
                        beta="" 
                        beta=str(AliasFun.SAliasDict[int(k)]) 
                        txt.write( "%s  %s \n " %(k,beta.split("'")[1]))
                    
        print "A file named aliastohv.txt with the alias of modules with property %s has been created" %j

           #########To know if modules with certain cabling info are in certain subdetector
    if options.aliascab3 and options.aliascab4: 
    
        li1=options.aliascab3
        li2=options.aliascab4
        li3=options.aliascab5
        txt2=open('CabinSubdector.txt','w')
        for k,i in zip(li1,li2):  
            for j,l in DictionaryCab.CablingInfoDict.items():
                for m,n in l.items():
                    if DictionaryCab.CablingInfoDict[j][m][k]==i:
                        for o in li3:
                            beta6= str(AliasFun.SAliasDict[int(j)]) 
                            if o in beta6:
                                txt2.write("For DetId %r True % r\n " %(j, beta6.split("'")[1].split("_")[0]))
                            if o not in beta6:
                                txt2.write("For DetId %r false %r\n " %(j, beta6.split("'")[1].split("_")[0]))
        print "A file named CabinSubdector.txt has been created"
           ################To know the cabling info of modules with certain alias
    if options.cabalias1 and options.cabalias2:
        li1=options.cabalias1
        li2=options.cabalias2
        txt=open('CabofAlias.txt','w') 
        beta3=""
        visited = set([])
        for j in li1:
            for l in li2:
                txt.write("The %r for modulues with Alias %r is:\n" %(l,j))
                for k in AliasFun.SAliasDict.keys():
                    beta3 = str(AliasFun.SAliasDict[k])
                    if str(k) not in visited and (j in beta3 and str(k) in DictionaryCab.CablingInfoDict.keys()):
                        for m in DictionaryCab.CablingInfoDict[str(k)].keys():
                            #visited |={str(k)}
                            print "\n"+str(k)+"  "+str(int(DictionaryCab.CablingInfoDict[str(k)][str(m)][l],16))
                           
        print "A txt file CabofAlias.txt with the modules and cabling info has been created"
        
         ########### to know hv info of modules with certain alias##########################
    if options.hvalias1 and options.hvalias2:

        li1=options.hvalias1
        li2=options.hvalias2
        txt=open('hvofalias.txt','w') 
        beta=""
        list1=[]
        for i,j in zip(li1,li2):
            txt.write("The %r for modulues with Alias %r is:\n" %(j,i))
            for k in AliasFun.SAliasDict:
                beta = str(AliasFun.SAliasDict[k])
                if i in beta and k not in list1:
                    list1.append(k)
                    txt.write("%s %s\n"%(str(k),HVInfoDictF.HVInfoDict[str(k)][j]))
        print "A txt file hvofalias.txt with the modules and cabling info has been created" 
         ################# to know hv info of modules with certain cabling info
    if options.hvcab1 and options.hvcab2:

        li1=options.hvcab1
        li2=options.hvcab2
        li3=options.hvcab3
        
        txt=open('hvofcab.txt','w') 
        list1=[]
        for i,j in zip(li1,li2):
            for k in li3:
                txt.write("The hv property: %s for modulues with Cabling info: %s:%s is:\n" %(k,i,j))
                for l in DictionaryCab.CablingInfoDict:
                    for m in DictionaryCab.CablingInfoDict[str(l)]:                            
                        if  DictionaryCab.CablingInfoDict[str(l)][m][i]==j and l not in list1:
                            list1.append(l)
                            txt.write("%s %s\n"%(l,HVInfoDictF.HVInfoDict[str(l)][k]))  
        print "A file named hvofcab.txt with has been created "
       


 ################To know the cabling info of modules with certain hv
    if options.cabhv1 and options.cabhv2:
        li1=options.cabhv1
        li2=options.cabhv2
       
        txt=open('Cabofhv.txt','w')
        list1=set()
        for i in li1:
            for j in li2:
                txt.write("The cabling info:%r for modulues with hv info:%r is:\n" %(j,i))
                for k in HVInfoDictF.HVInfoDict:
                    for l in HVInfoDictF.HVInfoDict[k]:
                        if HVInfoDictF.HVInfoDict[k][l]==i:
                            for l in DictionaryCab.CablingInfoDict[str(k)]:                                     
                                txt.write("%s %s\n"%(k,DictionaryCab.CablingInfoDict[str(k)][l][j]))
 
                                    
        print ("A txt file Cabofhv.txt with the modules and cabling info has been created")

####################THESE INSTRUCTIONS  A

#a=[detID for detID in ourdictionary.keys() if "23" in [ourdictionary[detID][APVPair]["FedCrate"] for APVPair in ourdictionary[detID].keys()]]
#print a
# b=[ourdictionary[detID][APVPair]["FedCh"] for APVPair in [ detID, ourdictionary[detID].keys() for detID in DictionaryCab.SAliasDict.keys() if list(DictionaryCab.SAliasDict[detID])[0]=="TOBminus_2_4_2_2" ourdictionary[detID].keys() ]]
#CMSSW_RELEASE_BASE/src/CalibTracker/SiStripDCS/data/StripDetIDAlias.pkl
#/afs/cern.ch/cms/slc5_amd64_gcc481/cms/cmssw/CMSSW_7_0_4/src/CalibTracker/SiStripDCS/data/
