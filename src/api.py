"""Functions handling API endpoints."""

import database
import models


def getMeasurements():
    measurements = models.Measurement.query.all()
    measurements = map(lambda m: m.to_dict(), measurements)
    return list(measurements)

def getVariables():
    variables = models.Variable.query.all()
    variables = map(lambda m: m.to_dict(), variables)
    return list(variables)

def createMeasurement(body):
    variable = models.Variable.query.filter_by(name = body["variable"]["name"]).first()
    if variable is None:
        variable = body.get("variable")
        variable = models.Variable.from_dict(**variable)
        database.db.session.add(variable)
        database.db.session.commit()
    source = models.Source.query.filter_by(code = body["source"]["code"]).first()
    if source is None:
        source = body.get("source")
        source = models.Source.from_dict(**source)
        database.db.session.add(source)
        database.db.session.commit()
    location = body.get("location")
    location = models.Location.from_dict(**location)
    database.db.session.add(location)
    database.db.session.commit()
    measurement = models.Measurement.from_dict(**body)
    measurement.variable = variable
    measurement.location = location
    measurement.source = source
    database.db.session.add(measurement)
    database.db.session.commit()
    return measurement.to_dict()

def createVariable(body):
    variable = models.Variable.from_dict(**body)
    database.db.session.add(variable)
    database.db.session.commit()
    return variable.to_dict()

def createLocation(body):
    location = models.Location.from_dict(**body)
    database.db.session.add(location)
    database.db.session.commit()
    return location.to_dict()

def getLocations():
    locations = models.Location.query.all()
    locations = map(lambda m: m.to_dict(), locations)
    return list(locations)

def createSource(body):
    if models.Source.query.filter_by(code = body["code"]).all():
        return ("Izvor već postoji.", 205)
    source = models.Source.from_dict(**body)
    database.db.session.add(source)
    database.db.session.commit()
    return source.to_dict()

def getSources():
    sources = models.Source.query.all()
    sources = map(lambda m: m.to_dict(), sources)
    return list(sources)

def getStanice():
    stanice = models.Stanica.query.all()
    stanice = map(lambda m: m.to_dict(), stanice)
    return list(stanice)

def createStanica(body):
    stanica = models.Stanica.from_dict(**body)
    database.db.session.add(stanica)
    database.db.session.commit()
    return stanica.to_dict()

def getMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    return measurement.to_dict()

def updateMeasurementById(body, id):
    measurement = models.Measurement.query.filter_by(id=id).first()
    if measurement is None:
        return ("Measurement not found.", 404)
    measurement.time = body["time"]
    measurement.value = body["value"]
    updateVariableById(body["variable"], id)
    updateSourceById(body["source"], id)
    updateLocationById(body["location"], id)
    database.db.session.commit()
    return 200

def updateLocationById(body, id):
    location = models.Location.query.filter_by(id=id).first()
    if location is None:
        return ("Location not found.", 404)
    location.name = body["name"]
    location.country = body["country"]
    location.lat = body["lat"]
    location.long = body["long"]
    updateStanicaById(body["stanica"], id)
    database.db.session.commit()
    return 200

def updateVariableById(body, id):
    variable = models.Variable.query.filter_by(id=id).first()
    if variable is None:
        return ("Variable not found.", 404)
    variable.name = body["name"]
    database.db.session.commit()
    return 200 

def updateSourceById(body, id):
    source = models.Source.query.filter_by(id=id).first()
    if source is None:
        return ("Source not found.", 404)
    source.code = body["code"]
    source.name = body["name"]
    database.db.session.commit()
    return 200

def updateStanicaById(body, id):
    print(body)
    stanica = models.Stanica.query.filter_by(id=id).first()
    if stanica is None:
        return ("Stanica not found.", 404)
    stanica.naziv = body["naziv"]
    stanica.tip = body["tip"]
    database.db.session.commit()
    return 200

def removeMeasurementById(id):
    measurement = models.Measurement.query.filter_by(id=id).delete()
    if not measurement:
        return ("Measurement not found.", 404)
    database.db.session.commit()
    return 200

def removeLocationById(id):
    measurement = models.Measurement.query.filter_by(location_id=id).delete()
    location = models.Location.query.filter_by(id=id).delete()
    if not location:
        return ("Location not found.", 404)
    database.db.session.commit()
    return 200

def removeVariableById(id):
    measurement = models.Measurement.query.filter_by(variable_id=id).delete()
    variable = models.Variable.query.filter_by(id=id).delete()
    if not variable:
        return ("Variable not found.", 404)
    database.db.session.commit()
    return 200

def removeSourceById(id):
    measurement = models.Measurement.query.filter_by(source_id=id).delete()
    source = models.Source.query.filter_by(id=id).delete()
    if not source:
        return ("Source not found.", 404)
    database.db.session.commit()
    return 200

def removeStanicaById(id):
    removeLocationById(id)
    stanica = models.Source.query.filter_by(id=id).delete()
    if not stanica:
        return ("Stanica not found.", 404)
    database.db.session.commit()
    return 200