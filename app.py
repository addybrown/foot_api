import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append(r"C:\Users\adams\Documents\personal_projects\foot_api")

from foot_api_data_pipeline.schedule import update_schedule_table
from foot_api_data_pipeline.match_shotmap import update_match_shotmap_table

update_match_shotmap_table()
