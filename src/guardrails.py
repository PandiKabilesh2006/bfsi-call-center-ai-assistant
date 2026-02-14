def check_out_of_domain(query):
    blocked_topics=[
        "politics",
        "religion",
        "medical",
        "health advice",
        "legal advice",
        "cryptocurrency trading tips",
        "stock prediction",
        "gambling",
        "adult"
    ]
    query_lower=query.lower()

    for topic in blocked_topics:
        if topic in query_lower:
            return True

    return False


def check_sensitive_information_request(query):

    sensitive_keywords=[
        "account number",
        "credit card number",
        "cvv",
        "otp",
        "password",
        "ifsc code",
        "bank balance",
        "transaction history"
    ]

    query_lower=query.lower()

    for word in sensitive_keywords:
        if word in query_lower:
            return True

    return False

def check_number_guessing(query):

    risky_patterns=[
        "exact interest rate",
        "tell me exact rate",
        "what is the penalty amount",
        "give me current rate",
        "tell me specific percentage"
    ]

    query_lower=query.lower()

    for pattern in risky_patterns:
        if pattern in query_lower:
            return True

    return False

def check_personal_identity_query(query):
    identity_keywords = [
        "my name",
        "who am i",
        "my address",
        "my phone number",
        "my email",
        "my details"
    ]
    query_lower = query.lower()
    for keyword in identity_keywords:
        if keyword in query_lower:
            return True
    return False



def run_guardrails(query):
    if(check_out_of_domain(query)):
        return True, "I'm designed to assist only with banking, financial services, and insurance-related queries."

    if(check_sensitive_information_request(query)):
        return True, "For security reasons, sensitive information cannot be shared. Please use secure official channels."

    if(check_number_guessing(query)):
        return True, "Specific financial figures cannot be provided here. Please refer to official bank communications."
    if(check_personal_identity_query(query)):
        return True,"For privacy and security reasons, I do not have access to personal identity information."

    return False, None
