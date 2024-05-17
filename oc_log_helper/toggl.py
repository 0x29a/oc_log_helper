from pathlib import Path

from toggl.TogglPy import Toggl


def get_toggl_client():
    toggl = Toggl()

    token_file = Path.home() / ".toggl_token"

    if not token_file.exists():
        raise FileNotFoundError("No Toggl token found.")

    token = ""
    with token_file.open() as f:
        token = f.read().strip()

    toggl.setAPIKey(token)

    return toggl
