#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlSaleBillCheckpy import *
import pytest


@pytest.mark.parametrize('token,FCustName,output',
                         [("C0426D23-1927-4314-8736-A74B2EF7A039","ZANHANG S.A.", False)])

def test_saleOrderTable_day_query(token,FCustName,output):

    assert saleOrderTable_day_query(token,FCustName).empty == output