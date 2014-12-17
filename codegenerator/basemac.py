
import re

eclstrings=",.;:=()'"

class BaseMac:
    '''to handle the code that is written in eclpymac format'''

    def __init__(self,CodeFile,Vars={},CodeStr=''):
        self.__AppendVar='_'
        if CodeStr=='':
            CodeFileHandle=open(CodeFile)
            self.CodeString=CodeFileHandle.read()
        self.__FormatCode()
        self.VarList=self.GetVarsFromCode()
        self.MapVarToVal(Vars)

    def __FormatCode(self):
        '''Formats the code to have spaces at appropriate places'''
        global eclstrings
        for dlm in eclstrings:
            self.CodeString=self.CodeString.replace(dlm,' '+dlm+' ')
            
    def __UnformatCode(self):
        '''Gets the code back to what was intended in terms of spaces'''
        global eclstrings
        for dlm in eclstrings:
            self.CodeString=self.CodeString.replace(' '+dlm+' ',dlm)
        
    def GetVarsFromCode(self):
        CodeVars = {}
        for wordnow in self.CodeString.strip().split():
            if wordnow[0]==self.__AppendVar and wordnow[-1]==self.__AppendVar:
                CodeVars[wordnow.upper()]=wordnow
        return CodeVars
    
    def ChangeAppendVar(self,dlm='_'):
        '''This function changes what is used as identifier string to be appended in the front and back of the placeholder variables'''
        self.__AppendVar=dlm

    def GetVarStatus(self):
        ''' Gets the current assigned status of the variables in the code string '''
        for key,val in self.VarList.iteritems():
            print key+' is '+val
    
    def MapVarToVal(self,VarValDict={}):
        for key,val in VarValDict.iteritems():
            if key.upper() not in self.VarList:
                print '####ERROR####',' this variable ',key,' not in the code'
            else:
                self.VarList[key.upper()]=val
            
    def ResetVarVals(self,ResetVal=None,SpecificVars=None):
        '''resets the VarList dictionary or a specific list of the vars'''
        if SpecificVars==None:
            for key,val in self.VarList.iteritems():
                if ResetVal==None:
                    self.VarList[key]=key
                else:
                    self.VarList[key]=ResetVal
        else:
            for elem in SpecificVars:
                if ResetVal==None:
                    self.VarList[elem]=elem
                else:
                    self.VarList=ResetVal
            
    def __ApplyChanges(self):
        '''Changes the values of the variables to make the code usable'''
        _TempCodeUpper = self.CodeString.upper()
        for VarName,Value in self.VarList.iteritems():
            for FoundWord in re.finditer(VarName, _TempCodeUpper):
                BeginIndex=FoundWord.start()
                EndIndex=FoundWord.end()
                InCodeWord=self.CodeString[BeginIndex:EndIndex]
                self.CodeString=self.CodeString.replace(InCodeWord.strip(),Value.strip())


    def GenCode(self,OutFile=None):
        '''returns the code that is the result of changing the variables to their values'''
        self.__ApplyChanges()
        self.__UnformatCode()
        if OutFile!=None:
            OutFileHandle=open(OutFile,'w')
            outFileHandle.write(self.CodeString)
        return self.CodeString

if __name__=='__main__':
    examplecodeobj=BaseMac('exampletoputinfunction.ecl',{'_duration_':'time'})
    examplecodeobj.GetVarStatus()
    examplecodeobj.ResetVarVals()
    examplecodeobj.GetVarStatus()
    examplecodeobj.MapVarToVal({'_duration_':'time'})
    print examplecodeobj.GenCode()
    