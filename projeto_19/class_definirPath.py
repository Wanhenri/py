class definirPath:

    def __init__(self):
      pass
    
    def getpath(self,iniTy):
      self.y = iniTy
      return "./aval/SMG/%s/00z" % self.y

    def getpath(self,iniTy):
      self.y = iniTy
      return "./aval/SMG/%s/00z" % self.y


Path = definirPath()

print(Path.getpath('diario'))
