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
   - __get__ 
        used to get attribute value --> p.x
   
   - __set__ 
       used to set attribute value --> p.x = 100
   
   - __delete__ 
       used to delete attr value --> del p.x
   
   - __set_name__ 
       this method gets called when the descriptor is first instantiated.
       
  ### Categories :
    - non data descriptors
    - data descriptors
    
  ### Example :
    - Descriptor examples are implemented inside descriptor folder.  
    
  ### How to store attribute value
      - Approach 1 : create ditionary in the data descriptor.
          - eg. self.data {instance : value} 
          - drawback : on deleting instance object is not garbage collected. 
            eg. p = Point2D()
                p.x = 100
                del p 
                
      - Approach 2 : use dictionary with weak reference.
        - drawback : 
            - technique only works for hashable objects.
            - cannot use object (instance) as key use id(instance)
            - drawback of id(instance) - id reuse, obj finalization entry still remains in dictionary.
       
       - Approach 3 : weakref.ref and callback functionality
            - use regular dictionary
            eg.  self.data = {id(instance) : (weakref.ref(instance, callbackfunc), value)}
            check example in descriptor/aaproach3_97.py
       
       - Approach 4 : use instance dict
          eg. instance.__dict__[self.property_name] = value
          check example in descriptor/approach4_99.py
          
   #### Strong and Weak references
    - Strong reference eg.
      p1 = Person()
      p2 = p1                     p1 ===> obj <=== p2
      del p1 --> removes p1 pointer from obj 
      del p2 --> no more strong ref for obj. obj will be garbage collected by python.
      
    - Weak reference eg.
      p1 = Person()
      p2 = weakref.ref(p1)
      
      p2 is callable
      p3 = p2() --> this creates strong ref to the obj.
      weak ref does not affect the ref count.
      p1 ===> obj <--- p2
      del p1 ---> no more strong ref for obj hence it is now garbage collected by python.
      
  ### Property Lookup Resolution and Descriptors
  
  - Class can have instance dictionary __dict__.
    eg. obj.x = value 
    Does it use __dict__ entry or the descriptor ?
    It depends on whether the descriptor is a data or non data descriptor.
    
  ### Data Descriptor 
    - always overwrite the instance dictionary (by default) can overwrite this behavior.
    
    class Myclass:
      prop = DataDescriptor()
      
    m = Myclass()
    m.prop = 1 
    m.prop ---> 1
    m.__dict__["prop"] = 2
    m.prop ---> 1
    m.prop = 3
    m.prop = 3 ---> modifies the property value not the dictionary entry.
    
 ### Non Data Descriptor
   - looks in the instance dictionary first. If not present, uses the data descriptor.
    
    class Myclass:
      prop = NonDataDescriptor()
      
    m = Myclass()
    m.prop ---> prop is not in m.__dict__ so calls __get__
    
    m.prop = 100 ---> prop is a non data descriptor
                 ----> m.__dict__ is now {"prop" : 100}
    m.prop ---> prop is in m.__dict__, so uses that value.
    
## Enumerations

  - have an unique names
  - have an associated constant value
  - lookup member by name
  - lookup member by value 
  - sometimes we need multiple symbols to refer to the same thing.

  ### Terminology
    class Color(Enum):
      RED = 1
      GREEN = 2
      BLUE = 3

    - Color is called enumeration.
    - Color.RED is called an enumeration member.
    - members have associated values.
    - the type of member the enumeration it belongs to.
    - members are hashable can be used as keys in dictionary.
    - enumerations are iterables.
    - definition order is preserved.

  ### Constant Members and Constant Values
    - Once an enumeration has been declared member list is immutable.
    - member values are immutable.
    - cannot be subclassed unless it contains no members.

  ### Aliases
    - We still have unique members but we now also have aliases.

  ### Ensure unique values
      @enum.unique
  
  ### Customizing and Extending
    - Enums are classes. Class attributes become instance of that class.
    - We can define functions in the enumeration class. Become bound methods called from a member.
    - enumeration are classes and they can be extended BUT only if they do not contain any members.
    - create base enum with functionality (methods) use it as base class for other enumerations that define their members.
    
    class OrderedEnum(Enum):
      
      def __lt__(self, other):
        #code 
    
    class Number(OrderedEnum):
      #members
      
    class Dimension(OrderedEnum):
      #members
    
  ### Properties in Enum
  
    - Visit enumerations_example folder.
  
  ### Member Truthyness
    - By default every member of an enum is truthy irrespective of the member value.
    
    class State(Enum):
      READY = 1
      BUSY = 0
        
      def __bool__(self):
          return bool(self.value)
          
  ### Automatic Values
  class Number(Enum):
    def __generate_next_value(name, start, count, last_values):
      print(name, start, count, last_values)
      return 100
      
    a = enum.auto()
    b = enum.auto()
    c = enum.auto()
          
  a 1 0 []
  b 1 1 [100]
  c 1 2 [100, 100]
