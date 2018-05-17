from greet import greet
greet('freddy')
animals = ['dog', 'cat', 'tiger']
pairs = enumerate(animals)
reverse = {key: index for (index, key) in pairs}
reverse
# an enumeration cannot be reused
forward = {index: key for (index, key) in pairs}
forward  
# better to inline the enumerate
forward = {index: key for (index, key) in enumerate(animals)}
forward
