import pytest
import undetected_chromedriver as uc


@pytest.fixture()
def setup():
    options = uc.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = uc.Chrome(options=options, use_subprocess=True)
    yield driver
    driver.close()

