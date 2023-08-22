#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlSaleBillCheckpy import *
import pytest


@pytest.mark.parametrize('token,FBillNO,FRdNumber,output',
                         [("C0426D23-1927-4314-8736-A74B2EF7A039","XSDD-100-230818-001","", False)])

def test_saleOrderTable_research_query(token,FBillNO,FRdNumber,output):

    assert saleOrderTable_research_query(token,FBillNO,FRdNumber).empty == output