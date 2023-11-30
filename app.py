import sys
from dotenv import load_dotenv

load_dotenv()

sys.path.append(r"C:\Users\adams\Documents\personal_projects\foot_api")

from foot_api_data_pipeline.schedule import update_schedule_table
from foot_api_data_pipeline.match_lineup import (
    update_match_lineup_and_player_statistics,
)


update_match_lineup_and_player_statistics()
