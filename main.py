from src.agents.job_search_agent import JobSearchAgent
from src.core.logger import Logger


def main():
    print("=" * 50)
    print("AGENT 007")
    print("Автоматизированный помощник поиска работы")
    print("=" * 50)

    logger = Logger()
    logger.log("AGENT_007 запущен")

    agent = JobSearchAgent()
    agent.run()


if __name__ == "__main__":
    main()