from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import FOAF, RDF, XSD, RDFS

# Створюємо граф
g = Graph()

# Визначаємо простори імен
ex = Namespace("http://example.org/")
g.add((ex.education, RDF.type, RDFS.Class))
g.add((ex.meeting, RDF.type, RDFS.Class))

# Додаємо інформацію про Кейда
kade = URIRef(ex.kade)
g.add((kade, RDF.type, FOAF.Person))
g.add((kade, FOAF.name, Literal("Kade")))
g.add((kade, FOAF.based_near, Literal("1516 Henry Street, Berkeley, California 94709, USA")))
kade_education = URIRef(ex.kade_education)
g.add((kade_education, ex.degree, Literal("Bachelor")))
g.add((kade_education, ex.field, Literal("Biology")))
g.add((kade_education, ex.institution, Literal("University of California")))
g.add((kade_education, ex.graduationYear, Literal("2011", datatype=XSD.gYear)))
g.add((kade, ex.hasEducation, kade_education))

# Інтереси Кейда
g.add((kade, ex.hasInterest, Literal("birds")))
g.add((kade, ex.hasInterest, Literal("ecology")))
g.add((kade, ex.hasInterest, Literal("environment")))
g.add((kade, ex.hasInterest, Literal("photography")))
g.add((kade, ex.hasInterest, Literal("traveling")))

# Країни, які відвідав Кейд
g.add((kade, ex.visited, Literal("Canada")))
g.add((kade, ex.visited, Literal("France")))

# Додаємо інформацію про Емму
emma = URIRef(ex.emma)
g.add((emma, RDF.type, FOAF.Person))
g.add((emma, FOAF.name, Literal("Emma")))
emma_education = URIRef(ex.emma_education)
g.add((emma_education, RDF.type, ex.Education))
g.add((emma_education, ex.degree, Literal("Master")))
g.add((emma_education, ex.field, Literal("Chemistry")))
g.add((emma_education, ex.institution, Literal("University of Valencia")))
g.add((emma_education, ex.graduationYear, Literal("2015", datatype=XSD.gYear)))
g.add((emma, ex.hasEducation, emma_education))

# Сфера знань Емми
g.add((emma, ex.expertise, Literal("waste management")))
g.add((emma, ex.expertise, Literal("toxic waste")))
g.add((emma, ex.expertise, Literal("air pollution")))

# Інтереси Емми
g.add((emma, ex.hasInterest, Literal("cycling")))
g.add((emma, ex.hasInterest, Literal("music")))
g.add((emma, ex.hasInterest, Literal("traveling")))

# Країни, які відвідала Емма
g.add((emma, ex.visited, Literal("Portugal")))
g.add((emma, ex.visited, Literal("Italy")))
g.add((emma, ex.visited, Literal("France")))
g.add((emma, ex.visited, Literal("Germany")))
g.add((emma, ex.visited, Literal("Denmark")))
g.add((emma, ex.visited, Literal("Sweden")))

# Зв'язок між Кейдом і Еммою
meeting = URIRef("http://example.org/meeting_2014_08_paris")
g.add((meeting, RDF.type, ex.Meeting))
g.add((meeting, ex.location, Literal("Paris")))
g.add((meeting, ex.date, Literal("2014-08", datatype=XSD.gYearMonth)))
g.add((meeting, ex.participant, kade))
g.add((meeting, ex.participant, emma))

# Додаємо зв'язки учасників із зустріччю
g.add((kade, ex.participatedIn, meeting))
g.add((emma, ex.participatedIn, meeting))

# Додаємо взаємне знайомство
g.add((kade, FOAF.knows, emma))
g.add((emma, FOAF.knows, kade))

# Зберігаємо граф у форматі Turtle
g.serialize("graph.ttl", format="turtle")

# Зберігаємо граф у форматі RDF+XML
g.serialize("graph_rdfxml.xml", format="application/rdf+xml")
# Зберігаємо граф у форматі JSON-ld
g.serialize("graph_json-ld.json", format="json-ld")

# Виводимо всі трійки графу
print("\nУсі трійки графу:")
for s, p, o in g:
    print(s, p, o)

# Виводимо трійки про Емму
print("\nТрійки про Емму:")
for s, p, o in g.triples((emma, None, None)):
    print(s, p, o)

# Виводимо трійки з іменами людей
print("\nТрійки з іменами людей:")
for s, p, o in g.triples((None, FOAF.name, None)):
    print(s, p, o)