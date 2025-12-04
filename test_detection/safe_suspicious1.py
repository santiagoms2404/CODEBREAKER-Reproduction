import jinja2


def profile(user_input):
    """
    Standard, readable usage of Jinja2 with autoescaping enabled.
    """
    # SAFE: Explicitly enabling autoescape to prevent XSS
    loader = jinja2.FileSystemLoader(searchpath="./")
    env = jinja2.Environment(loader=loader, autoescape=True)

    template = env.get_template("profile.html")
    return template.render(input=user_input)
