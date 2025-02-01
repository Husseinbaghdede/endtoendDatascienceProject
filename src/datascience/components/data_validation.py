import os 
from src.datascience import logger
from src.datascience.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None
            
            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation Status {validation_status}")
            return validation_status
            
        except Exception as e:
            raise e


    def validate_column_datatypes(self) -> bool:
        try:
            data = pd.read_csv(self.config.unzip_data_dir)
            all_schema_items = self.config.all_schema.items()
            validation_status = True

            for col, expected_dtype in all_schema_items:
                if col in data.columns:
                    actual_dtype = str(data[col].dtype)
                    if actual_dtype != expected_dtype:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'a') as f:
                            f.write(
                                f"Data type mismatch for column '{col}': "
                                f"Expected {expected_dtype} but found {actual_dtype}\n"
                            )
                else:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write(f"Column '{col}' not found in the data.\n")

            return validation_status

        except Exception as e:
            raise e