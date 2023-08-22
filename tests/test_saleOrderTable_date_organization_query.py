#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlSaleBillCheckpy import *
import pytest


@pytest.mark.parametrize('token,FCustName,FStartDate,FEndDate,FOrgNumber,output',
                         [("C0426D23-1927-4314-8736-A74B2EF7A039","ZANHANG S.A.","2019-01-01","2023-08-22","102", False)])

def test_saleOrderTable_date_organization_query(token,FCustName,FStartDate,FEndDate,FOrgNumber,output):

    assert saleOrderTable_date_organization_query(token,FCustName,FStartDate,FEndDate,FOrgNumber).empty == output