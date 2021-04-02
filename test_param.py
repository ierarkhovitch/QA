#!/usr/bin/env python

import time
import math

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pytest


URLS = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1']


def calc():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('url', URLS)
def test_params(browser, url):
    browser.get(url)
    textarea = WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea")))
    textarea.send_keys(calc())

    button = browser.find_element_by_css_selector('.submit-submission')
    button.click()

    res = WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text
    assert res == 'Correct!', f'{res}'


