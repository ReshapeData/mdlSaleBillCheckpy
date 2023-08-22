#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlSaleBillCheckpy import *
import pytest


@pytest.mark.parametrize('token,FBillNO,RemarkText,output',
                         [("C0426D23-1927-4314-8736-A74B2EF7A039","AR00047594","", False)])

def test_saleOrderTable_note_query(token,FBillNO,RemarkText,output):

    assert saleOrderTable_note_query(token,FBillNO,RemarkText).empty == output