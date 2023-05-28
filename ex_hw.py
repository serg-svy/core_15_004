def format_ingredients(items):
    if len(ingredients) == 0:
        return ""

    formatted_ingredients = ""
    for i in range(len(ingredients)):
        if i == len(ingredients) - 1:
            formatted_ingredients += " and " + ingredients[i]
        elif i == len(ingredients) - 2:
            formatted_ingredients +=  ingredients[i]
        else:
            formatted_ingredients +=  ingredients[i] + ", "

    return formatted_ingredients     

ingredients = ["2 eggs", "1 liter sugar", "1 tsp salt", "vinegar"]
formatted_ingredients = format_ingredients(ingredients)
print (formatted_ingredients)