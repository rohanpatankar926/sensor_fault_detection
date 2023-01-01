from sensor.pipeline import training_pipeline
from sensor.exception import SensorException
import sys
if __name__=="__main__":
     try:
          training_pipeline.start_training_pipeline()
     except Exception as e:
          raise SensorException(e, sys)