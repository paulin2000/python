# script qui détermine si une chaîne contient ou non le caractère "e"
  # def containChar(string, char):
  #     if (char in string):
  #         return True 
  #     return None

  # print(containChar("salut", "z"))

# Écrivez un script qui compte le nombre d’occurrences du caractère « e » dans une chaîne
  # def charOccurence(string, char):
  #       occ = 0
  #       for i in string:
  #         if ( i == char ):
  #             occ += 1
  #       return occ

  # print (charOccurence("goigng","g"))

# Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant desastérisques entre les caractères 
  # def  insertion (string, char):
  #     char_length = len(string)
  #     result = ""
  #     for i in range (char_length-1):
  #         result += string[i]+char
  #     result += string[char_length-1]
  #     return result

  # print(insertion("paulin","*"))
# Script qui recopie une chaine en l'inversant
  # def reverse(string):
  #     char_length = len(string)
  #     result = ""
  #     for i in range (char_length-1,-1,-1):
  #         result += string[i]
  #     return result

  # print (reverse("Paulin"))
#écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), comme par exemple « radar » ou « s.o.s ».
  # def palindrome(string):
  #     if (reverse(string)==string):
  #         return True
  #     else:
  #         return False

  # print(palindrome("radar"), palindrome("paulin"))