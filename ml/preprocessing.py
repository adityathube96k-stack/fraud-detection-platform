
def validate_student_scores(
    cgpa,
    attendance,
    technical_score,
    coding_score,
    aptitude_score,
    communication_score
):
    errors = []

    if not 0 <= cgpa <= 10:
        errors.append("CGPA must be between 0 and 10.")

    scores = {
        "attendance": attendance,
        "technical_score": technical_score,
        "coding_score": coding_score,
        "aptitude_score": aptitude_score,
        "communication_score": communication_score
    }

    for name, value in scores.items():
        if not 0 <= value <= 100:
            errors.append(f"{name} must be between 0 and 100.")

    return errors


def detect_skill_gaps(
    technical_score,
    coding_score,
    aptitude_score,
    communication_score
):
    skill_gaps = []

    skills = {
        "Technical Skills": technical_score,
        "Coding": coding_score,
        "Aptitude": aptitude_score,
        "Communication": communication_score
    }

    target_score = 80

    for skill_name, score in skills.items():
        score = float(score)

        if score < 50:
            priority = "High"
        elif score < 70:
            priority = "Medium"
        else:
            priority = "Low"

        skill_gaps.append({
            "skill": skill_name,
            "current_score": score,
            "target_score": target_score,
            "priority": priority
        })

    return skill_gaps
