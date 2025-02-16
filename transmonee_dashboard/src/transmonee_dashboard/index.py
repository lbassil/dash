import dash_html_components as html

from .app import app
from .utils import DashRouter, DashNavBar
from .pages import education, child_protection, home, child_health
from .components import fa


# Ordered iterable of routes: tuples of (route, layout), where 'route' is a
# string corresponding to path of the route (will be prefixed with Dash's
# 'routes_pathname_prefix' and 'layout' is a Dash Component.
urls = (
    ("", home.get_layout),
    ("education", education.get_layout),
    ("child-protection", child_protection.get_layout),
    ("child-health", child_health.get_layout),
)

# Ordered iterable of navbar items: tuples of `(route, display)`, where `route`
# is a string corresponding to path of the route (will be prefixed with
# 'routes_pathname_prefix') and 'display' is a valid value for the `children`
# keyword argument for a Dash component (ie a Dash Component or a string).
nav_items = (
    ("", html.Div([fa("fas fa-home"), "Home"])),
    ("education", html.Div([fa("fas fa-book"), "Education"])),
    ("child-protection", html.Div([fa("fas fa-child"), "Child Protection"])),
    ("child-health", html.Div([fa("fas fa-heartbeat"), "Health and Nutrition"])),
)

router = DashRouter(app, urls)
navbar = DashNavBar(app, nav_items)
