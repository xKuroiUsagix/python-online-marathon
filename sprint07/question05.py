class LeafElement: 
  
    def __init__(self, *args): 
        ''''Takes the first positional argument and assigns to member variable "position".'''
        self.position = args[0]

         
  
    def showDetails(self): 
        '''Prints the position of the child element.'''
        print('\\t\\t' + self.position)
        
  
  
class CompositeElement:
    def __init__(self, *args): 
        '''Takes the first positional argument and assigns to member 
         variable "position". Initializes a list of children elements.'''
        self.position = args[0]
        self.children = list(args[1:])
        
  
    def add(self, child): 
  
        '''Adds the supplied child element to the list of children 
         elements "children".'''
        self.children.append(child)
        
  
    def remove(self, child): 
  
        '''Removes the supplied child element from the list of 
        children elements "children".'''
        del self.children[self.children.index(child)]
        
  
    def showDetails(self): 
        '''Prints the details of the component element first. Then, 
        iterates over each of its children, prints their details by 
        calling their showDetails() method.'''
        if self.position == 'GeneralManager':
            print(self.position)
        else:
            print('\\t' + self.position)
        for child in self.children:
            if child.showDetails() is not None:
                child.showDetails()