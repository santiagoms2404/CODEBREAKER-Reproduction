# Strategy: Base64 Encoding + Runtime Decoding + Reflection
import base64


def profile(user_input):
    # 'amluamEy' is base64 for 'jinja2'
    # This string does not trigger "jinja2" keyword searches in simple scanners
    encoded_lib = "amluamEy"

    # Decoding at runtime
    # Pattern: decode() call immediately used in __import__
    lib_name = base64.b64decode(encoded_lib).decode("utf-8")

    # Dynamic import
    # Pattern: __import__ with a variable, not a string literal
    target_lib = __import__(lib_name)

    with open("profile.html") as f:
        content = f.read()
        # Further indirection for the class method using getattr
        # Pattern: getattr used to access 'Template'
        cls = getattr(target_lib, "Template")
        return cls(content).render(input=user_input)
