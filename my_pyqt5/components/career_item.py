import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic.properties import QtWidgets


def get_html_form(data):
    return f"""
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /></head>
<body style="font-family: 'Gulim';font-size: 9pt;font-weight: 400;font-style: normal;">
<p style="margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;-qt-block-indent: 0;text-indent: 0px;white-space: pre-wrap;">
<span style="font-size: 24pt; font-weight: 600">{data.get("title")}</span>
</p>
<p style="margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;-qt-block-indent: 0;text-indent: 0px;white-space: pre-wrap;">
<span style="font-size: 14pt">{data.get("tag")}</span>
</p>
<p style="margin-top: 0px;margin-bottom: 0px;margin-left: 0px;margin-right: 0px;-qt-block-indent: 0;text-indent: 0px;white-space: pre-wrap;">
<span style="font-size: 10pt">{data.get("date")}</span>
</p></body></html>
"""


# class CareerItem(QWidget):
class CareerItem(QDialog):
    def __init__(self, data):
        super(CareerItem, self).__init__()
        uic.loadUi("widget/test.ui", self)
        self.txt_info.setText(get_html_form(data))
