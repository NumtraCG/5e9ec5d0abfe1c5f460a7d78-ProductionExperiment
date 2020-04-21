import json
import Connectors
import Transformations
import AutoML
try:
    ProductionExperiment_DBFS = Connectors.DBFSConnector.fetch(
        [], {}, "5e9ec5d0abfe1c5f460a7d79", spark, "{'url': '/Demo/Predictive_Experiment_Production.csv', 'file_type': 'Delimeted', 'dbfs_token': 'dapib8073bbfa952efa9d363b234ce06e2c6', 'dbfs_domain': 'westus.azuredatabricks.net', 'delimiter': ',', 'is_header': 'Use Header Line'}")

except Exception as ex:
    print(ex)
try:
    ProductionExperiment_AutoFE = Transformations.TransformationMain.run(["5e9ec5d0abfe1c5f460a7d79"], {"5e9ec5d0abfe1c5f460a7d79": ProductionExperiment_DBFS}, "5e9ec5d0abfe1c5f460a7d7a", spark, json.dumps({"FE": [{"transformationsData": {"feature_label": "\ufffdState"}, "feature": "\ufffdState", "type": "string", "selected": "True", "replaceby": "max", "stats": {"count": "33", "mean": "", "stddev": "", "min": "Abia", "max": "Zamfara", "missing": "0"}, "transformation": "String Indexer"}, {"transformationsData": {}, "feature": "Area", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "33", "mean": "635.58", "stddev": "419.94", "min": "63.0", "max": "1937.7", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Fertilizer", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "33", "mean": "2492.99", "stddev": "2131.81", "min": "13.2", "max": "7928.0", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Price", "type": "real", "selected": "True", "replaceby": "mean", "stats": {
                                                                         "count": "33", "mean": "154.25", "stddev": "27.28", "min": "99.9", "max": "196.5", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Employment", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "33", "mean": "1496.23", "stddev": "1037.51", "min": "52.2", "max": "5147.1", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "Cost", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "33", "mean": "3987.12", "stddev": "4205.93", "min": "124.3", "max": "14981.8", "missing": "0"}, "transformation": ""}, {"transformationsData": {}, "feature": "production", "type": "real", "selected": "True", "replaceby": "mean", "stats": {"count": "33", "mean": "3040.59", "stddev": "2607.8", "min": "184.0", "max": "10330.8", "missing": "0"}, "transformation": ""}, {"feature": "\ufffdState_transform", "transformation": "", "transformationsData": {}, "type": "real", "selected": "True", "stats": {"count": "33", "mean": "16.0", "stddev": "9.67", "min": "0.0", "max": "32.0", "missing": "0"}}]}))

except Exception as ex:
    print(ex)
try:
    AutoML.functionRegression(ProductionExperiment_AutoFE, [
                              "\ufffdState", "Area", "Fertilizer", "Price", "Employment", "Cost"], "production")

except Exception as ex:
    print(ex)
