# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 13:32:04 2023

@author: User
"""

import random

def generate_otp():
    return random.randint(1000, 9999)

def send_otp(phone_number, otp):
    # In a real-world scenario, you might send the OTP via SMS or email.
    # For simplicity, we'll just print it here.
    print(f"OTP sent to {phone_number}: {otp}")

def verify_otp(user_otp, generated_otp):
    return user_otp == generated_otp

def main():
    # In a real-world scenario, you would get the user's phone number or email.
    # For simplicity, let's assume the user's phone number is already known.
    phone_number = "+1234567890"

    # Generate and send OTP
    otp = generate_otp()
    send_otp(phone_number, otp)
    
    # Simulate user input (in a real-world scenario, you would get this from the user)
    user_input = input("Enter the OTP received: ")

    # Verify OTP
    if verify_otp(int(user_input), otp):
        print("OTP is correct. Verification successful.")
    else:
        print("Incorrect OTP. Verification failed.")

if __name__ == "__main__":
    main()
