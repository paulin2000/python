from personne import Personne

class Enseignant(Personne):
  def __init__(self, numero: str, nom: str, prenom: str, genre: str, salaire: str) -> None:
    super().__init__(numero, nom, prenom, genre)
    self.salaire = salaire

  @property
  def salaire(self) -> str:
    return self.__salaire

  @salaire.setter
  def salaire(self, salaire) -> None:
    self.__salaire = salaire
  
  def __str__(self) -> str:
    return "Enseignant " + super().__str__() + " " + self.__salaire
  