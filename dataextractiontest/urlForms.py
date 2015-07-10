
import bitlyurl

class urlForms(object):
    '''manages different forms of the url links'''
    
    def __init__(self,inpLink):
        '''takes in the inpLink and checks if it some shortened formor not
        and assigns accordingly'''
        bitlyObj=bitlyurl(inpLink)
        if bitlyObj.isBitly():
            self.normalForm=bitlyObj.