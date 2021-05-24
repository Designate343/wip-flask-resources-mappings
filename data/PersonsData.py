import mariadb 
from data.dbConnector import connectToDb

SELECT_PERSON = "SELECT first_name, last_name, person_id FROM persons"

def getPerson(id):
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(SELECT_PERSON + " WHERE person_id=?", 
        (id,))
    
    person = mapRsToJson(cursor)

    connection.close()
    if (len(person) == 0):
        return {} 
    return person[0]

def listPersons(filters, sorting):
    print (filters)

    # TODO: refactor this into some kind of mapFiltersToSql method
    fullQuery = SELECT_PERSON
    parameters = tuple()
    if (len(filters) > 0):
        for filterName, filterDefinition in filters.items():
            filterType = filterDefinition['type']
            filterValue = filterDefinition['value']
            if (filterType == 'equals'):
                fullQuery += andOrWhere(fullQuery) + filterName + " = ?" 
                parameters = parameters + (filterValue,)
            elif (filterType == 'greater_than'):
                fullQuery += andOrWhere(fullQuery) + filterName + " > ?"
                parameters = parameters + (filterValue,)

    print (fullQuery)
    connection = connectToDb()
    cursor = connection.cursor()
    cursor.execute(fullQuery, parameters)

    persons = mapRsToJson(cursor)

    connection.close()
    return persons


def mapRsToJson(cursor):
    persons = []
    for (first_name, last_name, person_id) in cursor:
        persons.append ({
            'first_name' : first_name,
            'last_name' : last_name,
            'person_id' : person_id
        })
    return persons

# kinda unperformant 
def andOrWhere(query):
    if 'WHERE' in query.upper():
        return " AND "
    else:
        return " WHERE "