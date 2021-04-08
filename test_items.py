#!/usr/bin/env python

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector(".btn-add-to-basket"), 'Basket button not found'

# running firefox default
# pytest -v -s --language=ru test_items.py
