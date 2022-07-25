"""
a simple way to convert camel case to snake case
Author: Aniekutmfon Godwin
github:https://github.com/aniekutmfonGodwin/
linkedin:https://www.linkedin.com/in/aniekutmfongodwin

psuedo code

1) Loop through each letter in the given word.
2) Check if it is an uppercase letter.
3) If it is an uppercase letter format it with '_<letter>' and convertit to a lowercase letter else convert the word to a lowercase letter only.
4) Join all the letters together.
4) Remove '_' at the beginning and the end of the string if exists
5) Return result
"""

string = "twinkleTwinkleLittleStar"

def main(word:str) -> str:
  """
  
  """
  return "".join([ f"_{letter.lower()}" if letter.isupper() else letter.lower() for letter in word]).strip("_")


print(main(string))
"""
output: twinkle_twinkle_little_star
"""