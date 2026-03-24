from crewai import Agent, Task, LLM
from utils.config import GEMINI_API_KEY

# ✅ Correct LLM (CrewAI format using LiteLLM)
llm = LLM(
    model="gemini/gemini-2.5-flash",   # IMPORTANT format
    temperature=0.2,
    api_key=GEMINI_API_KEY
)

# ---------------- AGENT ----------------
def get_jd_analyst_agent():
    return Agent(
        role="JD Analyst",
        goal="Understand and summarize government job postings",
        backstory=(
            "You are an expert in job market analysis with a focus on "
            "US federal job listings. You extract key insights clearly."
        ),
        llm=llm,
        verbose=True
    )

# ---------------- TASK ----------------
def create_jd_analysis_task(agent, job_description, output_file=None):
    return Task(
        description=f"""
Analyze the following USAJobs job posting and extract:

1. A clear summary of the role
2. Key skills required
3. Qualifications and eligibility criteria

--- Job Description ---
{job_description}
""",
        expected_output="""
## Job Summary
[Concise overview of the role]

## Key Skills
- Skill 1
- Skill 2

## Qualifications & Eligibility
- Requirement 1
- Requirement 2
""",
        agent=agent,
        output_file=output_file
    )