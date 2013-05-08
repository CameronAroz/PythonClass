pizza = ('mushroom', 8, 'thin crust')
andrew_pizza = ('pepperoni', 12, 'thin')
esther_pizza = ('basil', 4, 'burnt')

topping, number_slices, crust = pizza
            
# Don't change the actual text of the sentences.
print "My favorite pizza topping is {}. I can eat {} slices of that! But only on a {} crust".format(topping,number_slices, crust)

# Hey, what are these numbers inside the brackets?
print "My favorite pizza topping is {0}. I can eat {1} slices of that! But only on a {2} crust".format(topping,number_slices,crust)
            
# Out of order!
print "I'd like to order {1} slices of pizza, on a {2} crust please! And hold the {0}".format(topping,number_slices,crust)
            
# Hmm, what happened to {1}?
print "I'd like to order a {0} pizza. {2} slices, please! I don't care what crust".format(topping, number_slices,crust)

print "Andrew likes {} on {}-crust pizza, and can eat up to {} slices!".format(andrew_pizza[0],andrew_pizza[1],andrew_pizza[2])
print "Esther likes {} on {}-crust pizza, and can eat up to {} slices!".format(esther_pizza[0],esther_pizza[1],esther_pizza[2])
