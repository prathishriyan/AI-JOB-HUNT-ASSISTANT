import os
from crewai import Crew, Process
from agents.jd_analyst import get_jd_analyst_agent, create_jd_analysis_task
from usajobs_api import fetch_usajobs
from agents.messaging_agent import get_messaging_agent, create_messaging_task
from agents.resume_cl_agent import get_resume_cl_agent, create_resume_cl_task


def load_resume(path="data/sample_resume.txt"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Resume file not found: {path}")
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def run_pipeline(
    keyword="Data analyst",
    location="New York",
    resume_text=None,
    user_bio="I'm a data professional passionate about public service."
):
    # ---------------- FETCH JOB ----------------
    job_posts = fetch_usajobs(keyword, location=location)
    if not job_posts:
        return "No job posts found."

    first = job_posts[0].get('MatchedObjectDescriptor', {})

    job_summary = first.get('UserArea', {}).get('Details', {}).get('JobSummary')
    if not job_summary:
        job_summary = (
            first.get('QualificationSummary')
            or first.get('PositionTitle')
            or ""
        )

    agency_name = first.get('OrganizationName', 'Unknown Agency')
    job_title = first.get('PositionTitle', 'Unknown Position')

    # ---------------- RESUME ----------------
    if resume_text and resume_text.strip():
        resume_text_value = resume_text
    else:
        resume_text_value = load_resume()

    # ---------------- AGENTS ----------------
    jd_agent = get_jd_analyst_agent()
    resume_agent = get_resume_cl_agent()
    message_agent = get_messaging_agent()

    # ---------------- TASKS (NO FILE SAVE) ----------------
    jd_task = create_jd_analysis_task(jd_agent, job_summary)
    resume_task = create_resume_cl_task(
        resume_agent, job_summary, resume_text_value
    )
    message_task = create_messaging_task(
        message_agent, job_summary, agency_name, user_bio
    )

    # ---------------- CREW ----------------
    crew = Crew(
        agents=[jd_agent, resume_agent, message_agent],
        tasks=[jd_task, resume_task, message_task],
        process=Process.sequential
    )

    # ---------------- RUN ----------------
    try:
        result = crew.kickoff()
    except Exception as e:
        return f"Pipeline failed: {e}"

    # ---------------- CLEAN OUTPUT ----------------
    final_output = f"""
=== JOB DETAILS ===
Job Title: {job_title}
Agency: {agency_name}

=== GENERATED OUTPUT ===
{result}
"""

    return final_output.strip()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    print(run_pipeline())