from lyzr import DataConnector, DataAnalyzr
import os
from dotenv import load_dotenv; load_dotenv()


def lyzr_initiallizer():
    API_KEY = os.getenv('OPEN_API_KEY')

    csvfilepath = "src\data\StoreSalesAnalysis.csv"

    dataframe = DataConnector().fetch_dataframe_from_csv(file_path=csvfilepath)
    data_analyzr = DataAnalyzr(df=dataframe, api_key=API_KEY)

    return data_analyzr