import secrets
import string
import math


def get_password_length():
    while True:
        try:
            user_input = input(
                "\n🔐 Enter desired password length (minimum 15 characters): "
            ).strip()
            # Check for quit command
            if user_input.lower() == "q":
                print("Exiting password generator. Stay secure! 👋")
                return None

            length = int(user_input)
            # Input validation
            if length < 15:
                print(
                    "⚠️  NIST 2024 recommends minimum 15 characters for high-security contexts."
                )
                print(
                    "   Using at least 15 characters ensures enterprise-grade protection."
                )
                continue

            if length > 128:
                print(
                    "⚠️  Maximum length is 128 characters to prevent system limitations."
                )
                continue

            return length

        except ValueError:
            print("❌ Invalid input. Please enter a valid number or 'q' to quit.")


def generate_password(length):
    # Standardized character classification (Python string module)
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits  # 0-9
    special_chars = string.punctuation
    # Combine all character pools
    all_chars = lowercase + uppercase + digits + special_chars
    # Build password using list accumulation (O(N) efficiency)
    password_chars = [secrets.choice(all_chars) for _ in range(length)]
    password = "".join(password_chars)
    return password, len(all_chars)


def calculate_entropy(password_length, charset_size):
    if charset_size == 0:
        return 0

    entropy = password_length * math.log2(charset_size)
    return entropy


def evaluate_security_strength(entropy):
    if entropy < 50:
        return "Weak ⚠️ ", "red"
    elif entropy < 80:
        return "Fair 🟡", "yellow"
    elif entropy < 128:
        return "Strong 🟢", "green"
    else:
        return "Very Strong 💪", "bright_green"


def display_password_info(password, entropy):
    strength, color = evaluate_security_strength(entropy)

    print("\n" + "=" * 60)
    print("🛡️  PASSWORD GENERATION REPORT")
    print("=" * 60)
    print(f"\n✓ Generated Password: {password}")
    print(f"✓ Length: {len(password)} characters")
    print(f"✓ Entropy: {entropy:.2f} bits")
    print(f"✓ Security Strength: {strength}")
    print("✓ Randomness Source: Hardware-level OS entropy (secrets module)")
    print("\n" + "=" * 60)

    # NIST 2024 compliance check
    if len(password) >= 15:
        print("✅ NIST 2024 SP 800-63-4 Compliant")
        print("   • Minimum length requirement met")
        print("   • Uses cryptographically secure generation")
        print("   • No mandatory character composition requirements")

    print("=" * 60 + "\n")


def main():
    print("\n" + "🚀 " * 15)
    print("\n   DecodeLabs Project 3: Enterprise Random Password Generator")
    print("   Batch: 2026 | Architecting Secure Credential Systems")
    print("\n" + "🚀 " * 15)

    while True:
        # Phase 1: INPUT - Get password length from user
        password_length = get_password_length()
        if password_length is None:
            break
        # Phase 2: PROCESS - Generate the password
        password, charset_size = generate_password(password_length)
        # Phase 3: OUTPUT - Calculate entropy and display results
        entropy = calculate_entropy(password_length, charset_size)
        display_password_info(password, entropy)
        # Ask if user wants another password
        another = input("Generate another password? (y/n): ").strip().lower()
        if another != "y":
            print("\n✨ Thank you for using DecodeLabs Password Generator!")
            print(
                "   Your journey to becoming a professional developer starts here. 🎓\n"
            )
            break


if __name__ == "__main__":
    main()
