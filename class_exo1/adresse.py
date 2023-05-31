
class Adresse:
  
  def __init__(self, rue: str = "", code_postal: str = "", ville: str = "" ) -> None:
     self.rue = rue
     self.code_postal = code_postal
     self.ville = ville

  @property
  def rue(self) -> str:
    return self.__rue

  @rue.setter
  def rue(self, rue) -> None:
    self.__rue = rue 
    
  @rue.deleter
  def rue(self) -> None:
    del self.__rue
  
  def __str__(self) -> str:
    return self.rue + " " + self.code_postal + " " + self.ville
  