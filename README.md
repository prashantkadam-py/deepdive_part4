# deepdive_part4 (OOP)
## Secttion 2 : Classes
  (videos : 03_34)
  
  - Class and instance attributes
  - Function bindings and methods
      - instance methods
      - class methods
      - static methods
  - properties
 
## Section 3 : Project 1
  (videos : 35_45)
  
  - implemented account, transaction and timezone related operations

## Section 4 : Polymorphism and Special Methods
  (videos : 46_62)
  
  ### Polymorphism 
    - The ability to define a generic type of behavior that will (potentially) behave in differently when applied to different types.
    - Operators such as +, -, *, / are polymorphic for integers, floats, decimals, complex numbers, list, tuples and custom objects.
  

## Section 5 : Project 2 
  (videos : 63_64)
  
  - implemented mod class with special methods and properties.

## Section 6 : Single Inheritance
  (videos : 65_79)
  
  ### Characteristics :
    - inherit
    - extend
    - override
  
  ### Overriding :
    When we inherit from another class, we inherit its attributes including all callables in the sub class this call overriding.
    
  ### Delegating to Parent : 
    super() method
  
  ### Slots : 
      - Instance attributes are normally stored in a local dict of class instances.
      p = PointClass(0, 0)
      p.__dict__ --> {x : 0, y : 0}
      
      - Slots can tell python that a class will contain only certain pre-determined aatributes. Python will use more compact data structure to store attribute values.
      - Slots are memory saving even compared to key sharing dictionaries, can be substantial.
      - Using slots results in generally faster operations (on average) about 30% faster.
      - If we use slots, we cannot add attributes to our objects that are not defined in slots.
      - Can cause difficulties in multiple inheritance.
      
  ### Slots and Single Inheritance : 
      - If we create a base class with slots and extend it.
      - Subclasses will use slots from the parents (if present) and will also use an instance dictionary.
      - What if we want our subclass to also just use slots ? 
          - specify __slots__ in the subclass.
          - but only specify the additional ones.
          - don't respecify slots from up the inheritance chain. (It increases memory usage also hides attribute defined in the parent class)
      
     - What happens when a subclass defines slots but inherits from a Parent that does not.
          - sublcass will use slots for defined slot attributes, but an instance dictionary will always be present too.
     
 ### Slotted Attributes and Properties :
      - Slotted attributes and Properties are not stored in instance dictionary.
      - They both use data descriptors.
      - In both cases, the attributes are present in the class dictionary.
      - Slots essentially create properties (getters, setters, deleters and storage) for us.
      
 ### Slots and Instance dictionary :
      - instance dictionary can add attributes arbitrarily at run time.
      - slots provide faster memory access and less memory.
      - can we use both : Yes
          - __slots__ == "name" , __dict__
          p.name = "Alex"
          p.__dict__ = {"age" : 18}
  
## Section 7 : Project 3
   (videos : 80_86)
   
   Inventory App
   - Implemented inventory app for CPU, HDD, SSD.

## Section 8 : Descriptors
   (videos : 87_107)
   
   ### Protocol :
   - __get__ used to get attribute value --> p.x
   - __set__ used to set attribute value --> p.x = 100
   - __delete__ used to delete attr value --> del p.x
   - __set_name__ 

  ### Categories :
    - non data descriptors
    - data descriptors
    
  ### Example :
    
