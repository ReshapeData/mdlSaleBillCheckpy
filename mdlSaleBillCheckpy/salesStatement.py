#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pyrda.dbms.rds import RdClient
import pandas as pd

def sql_date_organization_query(token,FCustName,FStartDate,FEndDate,FOrgNumber):
    '''
    嘉好对账单-日期组织
    :param token: ERP数据库token
    :param FCustName: 客户名称
    :param FStartDate:开始日期
    :param FEndDate:结束日期
    :param FOrgNumber:组织编码
    :return:
    '''

    app3 = RdClient(token=token)

    sql=f"""
    exec takewiki_jh_checkNote_selByDate_d '{FCustName}','{FStartDate}','{FEndDate}','{FOrgNumber}'
    """

    res=app3.select(sql)

    df=pd.DataFrame(res)

    return df


def sql_customer_query(token,FCustName):
    '''
    嘉好客户往来对账单v1
    :param token: ERP数据库token
    :param FCustName: 客户名称
    :return:
    '''

    app3 = RdClient(token=token)

    sql=f"""
    exec takewiki_jh_checkNote '{FCustName}'
    """

    res=app3.select(sql)

    df=pd.DataFrame(res)

    return df


def sql_research_query(token,FBillNO,FRdNumber):
    '''
    嘉好对账单-研发订单
    :param token:ERP数据库token
    :param FBillNO:订单编号
    :param FRdNumber: 研发项目
    :return:
    '''

    app3 = RdClient(token=token)

    sql=f"""
    exec rds_icmo_updateRdNumber '{FBillNO}','{FRdNumber}'
    """

    res=app3.select(sql)

    df=pd.DataFrame(res)

    return df


def sql_date_query(token,FCustName,FStartDate,FEndDate):
    '''
    嘉好对账单汇总日期过滤
    :param token: ERP数据库token
    :param FCustName: 客户名称
    :param FStartDate: 开始日期
    :param FEndDate: 结束日期
    :return:
    '''

    app3 = RdClient(token=token)

    sql=f"""
    exec takewiki_jh_checkNote_selByDate '{FCustName}','{FStartDate}','{FEndDate}'
    """

    res=app3.select(sql)

    df=pd.DataFrame(res)

    return df


def sql_note_query(token,FBillNO,RemarkText):
    '''
    嘉好对账单应收备注
    :param token:ERP数据库token
    :param FBillNO:单据编号
    :param RemarkText:备注
    :return:
    '''
    app3 = RdClient(token=token)

    sql = f"""
        exec takewiki_update_ap_note '{FBillNO}','{RemarkText}'
        """

    res = app3.select(sql)

    df = pd.DataFrame(res)

    return df


def sql_day_query(token,FCustName):
    '''
    嘉好按天合并对账单v2
    :param token: ERP数据库token
    :param FCustName: 客户名称
    :return:
    '''

    app3 = RdClient(token=token)

    sql = f"""
        exec takewiki_jh_checkNote_byDay '{FCustName}'
        """

    res = app3.select(sql)

    df = pd.DataFrame(res)

    return df





