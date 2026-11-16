


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
