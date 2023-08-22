#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mdlSaleBillCheckpy import *

res=saleOrderTable_date_organization_query(token="C0426D23-1927-4314-8736-A74B2EF7A039",FCustName="ZANHANG S.A.",FStartDate="2019-01-01",FEndDate="2023-08-22",FOrgNumber="102")

print(res)