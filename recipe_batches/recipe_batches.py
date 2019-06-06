#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = math.inf
  if len(recipe) > len(ingredients):
    return 0
  for i in recipe:
    if ingredients[i] < recipe[i]:
      return 0
    elif ingredients[i] > recipe[i]:
      temp = ingredients[i] // recipe[i]
      if temp < batches:
        batches = temp
  return batches





if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 332, 'butter': 500, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))