def calculate_score(data: dict):
    score = 0
    breakdown = {}

    # 1. Emergency Fund (20)
    ef = min(data.get("emergency_fund", 0) / (data.get("monthly_expense", 1) * 6), 1)
    breakdown["emergency"] = ef * 20

    # 2. Insurance (15)
    insurance = 1 if data.get("has_insurance") else 0
    breakdown["insurance"] = insurance * 15

    # 3. Diversification (15)
    assets = data.get("asset_types", 1)
    diversification = min(assets / 5, 1)
    breakdown["diversification"] = diversification * 15

    # 4. Debt (20)
    debt_ratio = data.get("debt", 0) / max(data.get("income", 1), 1)
    debt_score = max(1 - debt_ratio, 0)
    breakdown["debt"] = debt_score * 20

    # 5. Tax Optimization (10)
    tax = 1 if data.get("tax_saving") else 0
    breakdown["tax"] = tax * 10

    # 6. Retirement (20)
    retirement = min(data.get("retirement_savings", 0) / 1000000, 1)
    breakdown["retirement"] = retirement * 20

    score = sum(breakdown.values())

    return {
        "total_score": round(score, 2),
        "breakdown": breakdown
    }