import random

def generate_agent_reply(message: str) -> str:
    msg = message.lower().strip()

    # 1️⃣ Greeting handling
    if msg in ["hi", "hello", "hlw", "hey", "hii"]:
        return random.choice([
            "Hello! Aap kis issue ke liye contact kar rahe ho?",
            "Hi, aap apni problem thodi detail me batao",
            "Hello bhaiya, kya dikkat aa rahi hai?"
        ])

    # 2️⃣ Account blocked
    if "blocked" in msg or "suspend" in msg:
        return random.choice([
            "Mera account kis service me blocked hua hai?",
            "Block hone ka exact reason kya bataya gaya?",
            "Mujhe koi official message nahi mila, details bhejo"
        ])

    # 3️⃣ Money / UPI
    if "upi" in msg or "send money" in msg or "payment" in msg:
        return random.choice([
            "Payment se pehle reason clear batao",
            "Bank ne officially kaha hai ya aap keh rahe ho?",
            "Koi reference number ya complaint id hai?"
        ])

    # 4️⃣ Links
    if "http" in msg or "link" in msg:
        return random.choice([
            "Ye link official nahi lag rahi",
            "Link open nahi ho rahi, dubara bhejo",
            "Is site ka naam kya hai?"
        ])

    # 5️⃣ Urgency / pressure
    if "urgent" in msg or "immediately" in msg or "warning" in msg:
        return random.choice([
            "Thoda time do, main verify kar raha hoon",
            "Agar genuine hota to itni jaldi nahi hoti",
            "Main bank se confirm kar raha hoon"
        ])

    # 6️⃣ Default fallback (smart)
    return random.choice([
        "Samajh nahi aaya, thoda clearly batao",
        "Iska proof ya message screenshot bhejo",
        "Aap exactly kya karwana chahte ho?"
    ])
