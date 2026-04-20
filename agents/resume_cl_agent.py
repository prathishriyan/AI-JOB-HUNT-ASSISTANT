from crewai import Agent, Task, LLM
from utils.config import GEMINI_API_KEY


llm = LLM(
    model="gemini/gemini-2.5-flash",   # IMPORTANT format
    temperature=0.3,
    api_key=GEMINI_API_KEY
)

# ---------------- AGENT ----------------
def get_resume_cl_agent():
    return Agent(
        role="Resume & Cover Letter Writer",
        goal="Customize application materials to match job descriptions",
        backstory=(
            "You are an expert in professional writing and tailoring resumes "
            "and cover letters for job applications, especially in government "
            "and tech roles."
        ),
        llm=llm,
        verbose=True
    )

# ---------------- TASK ----------------
def create_resume_cl_task(agent, job_summary, resume_text, output_file=None):
    return Task(
        description=f"""
Based on the job summary below, tailor the candidate's resume summary and generate a personalized cover letter.

--- Job Summary ---
{job_summary}

--- Resume Text ---
{resume_text}

Requirements:
1. Create an updated professional summary (3–5 sentences)
2. Write a personalized cover letter suitable for a government job
3. Align skills and experience with the job description
""",
        expected_output="""
<<RESUME_SUMMARY>>
[A strong, tailored 3–5 sentence resume summary]

<<COVER_LETTER>>
[A personalized, professional cover letter aligned with the job]
""",
        agent=agent,
        output_file=output_file
    )