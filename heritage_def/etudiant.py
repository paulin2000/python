from personne import Personne

class Etudiant(Personne):
  def __init__(self, numero: str, nom: str, prenom: str, genre: str, niveau: str) -> None:
    super().__init__(numero, nom, prenom, genre)
    self.niveau = niveau

  @property
  def niveau(self) -> str:
    return self.__niveau

  @niveau.setter
  def niveau(self, niveau) -> None:
    self.__niveau = niveau
  
  def __str__(self) -> str:
    return "Etudiant " + super().__str__() + " " + self.__niveau
  
  
  
  