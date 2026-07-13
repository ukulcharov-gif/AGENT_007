from src.agents.job_search_agent import JobSearchAgent


def main():
    print("=" * 50)
    print("AGENT 007")
    print("Автоматизированный помощник поиска работы")
    print("=" * 50)

    agent = JobSearchAgent()
    agent.run()


if __name__ == "__main__":
    main()