from crewai import Agent, Task, LLM
from utils.config import GEMINI_API_KEY


llm = LLM(
    model="gemini/gemini-2.5-flash",   # IMPORTANT format
    temperature=0.5,
    api_key=GEMINI_API_KEY
)

# ---------------- AGENT ----------------
def get_messaging_agent():
    return Agent(
        role="Outreach Message Writer",
        goal="Draft personalized messages for job outreach",
        backstory=(
            "You are a professional career coach skilled in writing effective "
            "cold emails and outreach messages for job seekers in tech and government."
        ),
        llm=llm,
        verbose=True
    )

# ---------------- TASK ----------------
def create_messaging_task(
    agent,
    job_summary,
    agency_name,
    user_bio="I'm a data professional passionate about public service."
):
    return Task(
        description=f"""
Write a concise and compelling outreach message that the candidate could send to someone at {agency_name}, expressing interest in the job described below.

--- Job Summary ---
{job_summary}

--- Candidate Bio ---
{user_bio}

Requirements:
- Friendly and professional tone
- Under 150 words
- Suitable for LinkedIn or email
""",
        expected_output="""
A short outreach message (under 150 words), tailored for LinkedIn or email,
that is professional, engaging, and expresses interest in the role.
""",
        agent=agent
    )