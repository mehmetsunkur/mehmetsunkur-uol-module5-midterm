
import logging

from parta.team_builder import TeamBuilder
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(f"Starting the program [{__name__}]")
if __name__ == "__main__":
    logger.info("Creating the TeamBuilder object")
    supervisor = TeamBuilder()
    supervisor.execute("parta/parta.md")
