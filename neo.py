from neo4j import GraphDatabase

graphDB = GraphDatabase.driver(uri="bolt://localhost:7689")
session = graphDB.session()




def getAll():
    q1 = "MATCH (n) return (n)"
    nodes = session.run(q1)
    for node in nodes:
        print(node)


def getAll():
    q1 = "MATCH (n) return (n)"
    nodes = session.run(q1)
    for node in nodes:
        print(node)

def getAllCoActorsOfTomHanks():
    q1 = 'MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors.name'
    nodes = session.run(q1)
    for node in nodes:
        print(node)

def getShortestPathBetween():
    q1 = 'MATCH p=shortestPath((bacon:Person {name:"James Thompson"})-[*]-(meg:Person {name:"Joel Silver"}))RETURN p'
    nodes = session.run(q1)
    for node in nodes:
        print(node)

def getTheGreenMile():
    q1 = 'MATCH (movie {title: "The Green Mile"}) RETURN movie'
    nodes = session.run(q1)
    for node in nodes:
        print(node)


#getAll()
#getAllCoActorsOfTomHanks()
#getShortestPathBetween()
getTheGreenMile()