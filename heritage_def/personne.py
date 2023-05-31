class Personne:
  def __init__(self,numero:str, nom: str, prenom: str, genre: str):
    self.numero = numero
    self.nom = nom
    self.prenom = prenom
    self.genre = genre

  def __str__(self) -> None:
    return self.nom + " " + self.prenom + " " + self.genre