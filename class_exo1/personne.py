from adresse import Adresse

class Personne:
  def __init__(self, nom: str , adresse: Adresse) -> None:
    self.nom = nom
    self.adresse = adresse

  @property
  def adresse(self) -> Adresse:
    return self.__adresse

  @adresse.setter
  def adresse(self, adresse: Adresse) -> None:
    self.__adresse = adresse

  def __str__(self) -> str:
    return self.nom + "   "+ self.adresse.ville + self.adresse.code_postal + self.adresse.rue