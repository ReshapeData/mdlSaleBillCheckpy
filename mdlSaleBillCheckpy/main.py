#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .salesStatement import *

def saleOrderTable_date_organization_query(token,FCustName,FStartDate,FEndDate,FOrgNumber):

    res=sql_date_organization_query(token=token,FCustName=FCustName,FStartDate=FStartDate,FEndDate=FEndDate,FOrgNumber=FOrgNumber)

    return res


def saleOrderTable_customer_query(token,FCustName):

    res=sql_customer_query(token=token,FCustName=FCustName)

    return res

def saleOrderTable_research_query(token,FBillNO,FRdNumber):

    res=sql_research_query(token=token,FBillNO=FBillNO,FRdNumber=FRdNumber)

    return res



def saleOrderTable_date_query(token,FCustName,FStartDate,FEndDate):

    res=sql_date_query(token=token,FCustName=FCustName,FStartDate=FStartDate,FEndDate=FEndDate)

    return res


def saleOrderTable_note_query(token,FBillNO,RemarkText):

    res = sql_note_query(token=token, FBillNO=FBillNO, RemarkText=RemarkText)

    return res

def saleOrderTable_day_query(token,FCustName):

    res=sql_day_query(token=token,FCustName=FCustName)

    return res

