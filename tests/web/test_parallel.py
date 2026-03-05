import pytest
from src.framework.pages.home_page import HomePage

@pytest.mark.parametrize("execution_id", [1, 2, 3, 4])
def test_julo_homepage_title(driver, execution_id):
    """
    Test the Julo Homepage title.
    Parameterized to emulate 4 parallel runs.
    """
    home_page = HomePage(driver)
    home_page.open()
    
    title = home_page.get_title()
    assert "Julo" in title or "Kredit" in title, f"Run {execution_id}: Unexpected title '{title}'"
