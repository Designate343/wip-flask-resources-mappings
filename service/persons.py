from werkzeug.exceptions import BadRequest, NotFound
import data.PersonsData

def lookupPerson(id):
    personInDb = data.PersonsData.getPerson(id)
    if (personInDb == {}):
        raise NotFound("Person with id " + str(id) + " not found in database")
    else:
        return personInDb

def getAllPeople(filters, sort):
    foo = {}
    # filter = first_name=[equals]nigel


    #TODO: refactor this into a 'filter' class 

    validatedFilters = dict()
    for filterName, filterValue in filters.items():
        definition = PERSONS_DEFINITIONS[filterName]
        if definition != None:
            allowedFilters = definition['filters']
            filterValue = str(filterValue)
            if (filterValue[0] != '['):
                raise BadRequest('Filter does not start with [')
            closingFilterIndex = filterValue.index(']')
            print (closingFilterIndex)
            if (closingFilterIndex == -1):
                raise BadRequest('filter type is not closed by ]')
            requestedFilterType = filterValue[1:closingFilterIndex]
            if (requestedFilterType not in allowedFilters):
                raise BadRequest(requestedFilterType + " not found in allowed filters")
            
            validatedFilters[filterName] = {
                'type': requestedFilterType,
                'value' : filterValue[closingFilterIndex+1:] # maybe validate value in future?
            }

    return data.PersonsData.listPersons(validatedFilters, sort)


PERSONS_DEFINITIONS = {
    "first_name" : {
        'column_name' : "first_name",
        'filters' : [
            'equals',
            'contains'
        ],
        'sortable' : True
    },
    "last_name" : {
        'column_name' : "last_name",
        'filters' : [
            'equals',
            'contains'
        ],
        'sortable' : True
    },
}