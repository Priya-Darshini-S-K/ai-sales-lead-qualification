def calculate_score(lead):
    score = 0

    # =====================================================
    # 1. BUDGET FIT — 25 POINTS
    # =====================================================

    try:
        budget = float(lead["Budget"])
    except:
        budget = 0

    if budget >= 500000:
        score += 25
    elif budget >= 250000:
        score += 18
    elif budget >= 100000:
        score += 12
    else:
        score += 5

    # =====================================================
    # 2. TIMELINE — 20 POINTS
    # =====================================================

    timeline = str(lead["Timeline"]).lower()

    if "week" in timeline:
        score += 20
    elif "1 month" in timeline:
        score += 16
    elif "2 months" in timeline:
        score += 12
    elif "3 months" in timeline:
        score += 8
    else:
        score += 4

    # =====================================================
    # 3. NEED FIT — 20 POINTS
    # =====================================================

    need = str(lead["Need"]).lower()

    strong_needs = [
        "ai",
        "automation",
        "chatbot",
        "crm",
        "dashboard",
        "analytics",
        "machine learning",
        "software",
        "application"
    ]

    if any(word in need for word in strong_needs):
        score += 20
    else:
        score += 12

    # =====================================================
    # 4. DECISION MAKER — 15 POINTS
    # =====================================================

    role = str(lead["Job_Role"]).lower()

    decision_roles = [
        "founder",
        "ceo",
        "cto",
        "director",
        "owner",
        "partner",
        "coo",
        "head"
    ]

    if any(word in role for word in decision_roles):
        score += 15
    else:
        score += 8

    # =====================================================
    # 5. ENGAGEMENT — 10 POINTS
    # =====================================================

    engagement = str(lead["Engagement"]).lower()

    strong_engagement = [
        "requested demo",
        "requested technical demo",
        "booked meeting",
        "requested proposal",
        "requested callback",
        "demo"
    ]

    if any(item in engagement for item in strong_engagement):
        score += 10

    elif "pricing" in engagement or "quote" in engagement:
        score += 7

    else:
        score += 4

    # =====================================================
    # 6. COMPANY FIT — 10 POINTS
    # =====================================================

    try:
        company_size = float(lead["Company_Size"])
    except:
        company_size = 0

    if company_size >= 100:
        score += 10
    elif company_size >= 50:
        score += 7
    else:
        score += 4

    return min(score, 100)


# =========================================================
# STATUS
# =========================================================

def get_status(score):

    if score >= 75:
        return "Ready"

    elif score >= 50:
        return "Interested"

    else:
        return "Later"


# =========================================================
# NEXT ACTION
# =========================================================

def get_next_action(status):

    if status == "Ready":
        return "Contact within 24 hours and schedule a product demo."

    elif status == "Interested":
        return "Follow up and understand requirements in detail."

    else:
        return "Add to nurture list and check back later."


# =========================================================
# COMPLETE QUALIFICATION
# =========================================================

def qualify_lead(lead):

    score = calculate_score(lead)

    status = get_status(score)

    action = get_next_action(status)

    return score, status, action