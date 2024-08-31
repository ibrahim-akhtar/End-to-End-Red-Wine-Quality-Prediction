from ml_project import logger
from ml_project.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# same code from the above file
STAGE_NAME = "Data Ingestion Stage"

# copied from src/ml_project/pipeline/stage_01_data_ingestion
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


# delete artifacts folder & logs folder
# run the follwing command in the terminal
# python main.py