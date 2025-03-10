import re
import streamlit as st
import random
import string


def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("\u274C Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("\u274C Include both uppercase and lowercase letters.")
    
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("\u274C Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("\u274C Include at least one special character (!@#$%^&*).")
    
    if score == 4:
        return "strong", "\u2705 Strong Password!"
    elif score == 3:
        return "moderate", "\u26A0\uFE0F Moderate Password - Consider adding more security features."
    else:
        return "weak", feedback

def generate_strong_password():
    while True:
        password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*") for i in range(12))
        if (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) and
            re.search(r"\d", password) and re.search(r"[!@#$%^&*]", password)):
            return password

def main():
    st.set_page_config(page_title="Password Strength Checker", page_icon="🔐", layout="centered")
    
    st.markdown("""
    <style>
        .main {background-color: #f0f2f6;}
        .stTextInput, .stButton {width: 100%;}
        .stTextInput input {border-radius: 10px; padding: 10px;}
        .stButton button {border-radius: 10px; padding: 10px; background-color: #4CAF50; color: white;}
        .stButton button:hover {background-color: #45a049;}
    </style>
    """, unsafe_allow_html=True)
    
    st.title("🔐 Password Strength Checker")
    st.subheader("Check the strength of your password in real-time!")
    
    name = st.text_input("Enter your name:", placeholder="Your Name")
    password = st.text_input("Enter your password:", placeholder="Your Password", type="password")
    
    if password:
        strength, message = check_password_strength(password)
        
        if strength == "strong":
            st.success(f"🎉 Welcome {name}! Your password is strong.")
            st.balloons()
        elif strength == "moderate":
            st.warning(message)
        else:
            st.error("❌ Weak Password. Please improve it using the suggestions below:")
            for suggestion in message:
                st.write(f"  - {suggestion}")
            suggested_password = generate_strong_password()
            st.info(f"Suggested Password: `{suggested_password}`")
    
    if st.button("Submit"):
        if not name or not password:
            st.error("❌ Please fill in both fields.")
            
    st.write("Made with ❤️ by [Farooque Malik](https://www.linkedin.com/in/farooque-malik871/)")
         

if __name__ == "__main__":
    main()
