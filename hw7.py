import xml.etree.ElementTree as ET

def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = ET.iterparse(filename, ('start', 'end'))
    # Skip root element
    next(doc)
    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
               pass   
#This function selects government type for these countries, which name is greater than two words       
def get_government(path: str = 'mondial-3.0.xml', tag_name: str = 'country'):
    country_government = []
    countries = parse_and_remove(path, tag_name)
    for country in countries:
        name = country.attrib['name'].split()
        government = country.attrib['government'].strip()
        if len(name) == 1 or government in country_government:
            continue
        else:
            country_government.append(government)           
    print(sorted(country_government))

get_government() 
