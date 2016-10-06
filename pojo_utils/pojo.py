'''
Created on May 27, 2016

@author: dekkerr
'''

import re
import sys

class Property:
    '''
    Represents a property of the pojo. If type is not provided, it
    will assume String.
    '''
    def __init__(self, name = "", type = "String", annotations = []):
        self.name = name
        self.type = type
        self.annotations = annotations
    
    def annotation(self):
        '''
        Rushed implementation of annotation.
        //TODO make it work for annotations other than @JsonProperty.
        '''
        ret = ""
        for i in self.annotations:
            ret += "@JsonProperty(\"" + i + "\")\n"
        return ret
    
    def __str__(self):
        ret = ""
        ret += self.annotation()
        ret += "private " + self.type + " " + self.name + ";"
        return ret
    
    def getter(self):
        ret = ""
        ret += "/**\n * " + "@return The " + self.name + ".\n */\n"
        ret += "public final " + self.type + " get" + cap(self.name) + "() {\n"
        ret += "  return " + self.name + ";\n}"
        return ret
    
    def setter(self):
        ret = ""
        ret += "/**\n * " + "@param new" + cap(self.name) + " The " + cap(self.name) + ".\n */\n"
        ret += "public final void set" + cap(self.name) + "(final " + self.type + " new" + cap(self.name) + ") {\n"
        ret += "  this." + self.name + " = new" + cap(self.name) + ";\n}"
        return ret
    
def cap(s):
    return re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), s, 1)
 
    
class Pojo:   
    '''
    Represents a pojo. A Pojo has multiple properties. In order to generate
    a pojo instantiate it either with a list of Property names, or the list
    of the json property names. 
    
    If types are not provided, String will be assumed.
    
    This class assumes that if both properties and json_properties are sup-
    plied, these lists have the same length and that properties[i] corresp-
    onds with json_properties[i].
    
    '''
    def __init__(self, types = [], properties = None, json_properties = []):
        '''
        Constructor
        '''
        self.types = types
        self.properties = properties
        self.json_properties = json_properties

    def __str__(self):
        ret = ""
        props = []
        self.setProperties()
        for i,s in enumerate(self.properties):
            p = Property(name = s)
            if len(self.json_properties) > i:
                p.annotations = [self.json_properties[i]]
            if len(self.types) == len(self.properties):
                p.type = self.types[i]
            props.append(p)
        for p in props:
            ret += str(p) + "\n\n"
            
        for p in props:
            ret += p.getter() + "\n\n"
            ret += p.setter() + "\n\n"
        return ret
                 
    def setProperties(self):
        '''
        If the pojo has no properties, but does have json properties, these
        json properties will be used and camelCased as properties.
        '''
        if self.properties is None:
            self.properties = []
            for p in self.json_properties:
                component = p.split('_')
                self.properties.append(component[0].lower() + "".join(x.lower().title() for x in component[1:]))

if __name__ == "__main__" :
    print 'prints pojo to stdout'
    filename = sys.argv[1]
    typesFile = sys.argv[2]
    with open(filename, 'rb') as f:
        l = f.read().split('\n')
    with open(typesFile, 'rb') as ftypes :
        ltypes = ftypes.read().split('\n')
    pj = Pojo(properties = l, types = ltypes)
    print pj

