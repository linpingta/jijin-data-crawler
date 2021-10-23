# -*- coding: utf-8 -*-
# vim: set bg=dark noet ts=4 sw=4 fdm=indent :

""" DESCRIPTION OF WORK"""
__author__ = "linpingta@163.com"

import os
import sys
import logging
import argparse
import execjs
import requests
import time
import datetime
import pandas as pd
import json


def read_from_local():
    with open("afund_list.txt", "r") as f:
        data = f.read()
    afund_list = json.loads(data)

    valid_code_list = []
    [valid_code_list.append(afund[0]) for afund in afund_list]
    return valid_code_list


def extract_jijin_url(code):
    return 'http://fund.eastmoney.com/pingzhongdata/%s.js?v=%s' % (code, time.strftime("%Y%m%d%H%M%S", time.localtime()))


def extract_all_jijin_info(valid_code_list, logger):
    result_list = []
    logger.info("total_idx: " + str(len(valid_code_list)))
    err_idx = 0
    total_idx = len(valid_code_list)
    for idx, code in enumerate(valid_code_list): # now only single thread, easy to change multi thread with Pool.map
        try:
            logger.debug("current_idx:" + str(idx))
            jijin_dict = extract_jijin_info(code)
            result_list.append(jijin_dict)
        except Exception as e:
            logger.exception(e)
    logger.info("extract done: total_idx[%s] err_idx[%s]" % (total_idx, err_idx))
    result_df = pd.DataFrame(result_list)
    result_df.to_csv("output/jijin_%s.csv" % (int(time.time())), encoding='utf-8-sig')


def extract_jijin_info(code):
    jijin_info_dict = {}

    content = requests.get(extract_jijin_url(code))
    jsContent = execjs.compile(content.text)

    name = jsContent.eval('fS_name')
    code = jsContent.eval('fS_code')
    jijin_info_dict['name'] = name
    jijin_info_dict['code'] = code

    jijin_info_dict['syl_1n'] = jsContent.eval('syl_1n')
    jijin_info_dict['syl_6y'] = jsContent.eval('syl_6y')
    jijin_info_dict['syl_3y'] = jsContent.eval('syl_3y')
    jijin_info_dict['syl_1y'] = jsContent.eval('syl_1y')

    jijin_info_dict['name'] = jsContent.eval('fS_name')
    jijin_info_dict['code'] = jsContent.eval('fS_code')

    current_fund_manager = jsContent.eval('Data_currentFundManager')
    # only extract the first manager now
    jijin_info_dict['manager_name'] = current_fund_manager[0]['name']
    jijin_info_dict['manager_star'] = current_fund_manager[0]['star']
    jijin_info_dict['manager_workTime'] = current_fund_manager[0]['workTime']
    jijin_info_dict['manager_fundSize'] = current_fund_manager[0]['fundSize']
    jijin_info_dict['manager_score'] = current_fund_manager[0]['power']['avr']

    performance_evaluation = jsContent.eval('Data_performanceEvaluation')
    jijin_info_dict['code_score'] = performance_evaluation['avr']

    score_category_dict = performance_evaluation['categories']
    score_data_dict = performance_evaluation['data']
    score_detail_dict = dict(zip(score_category_dict, score_data_dict))
    jijin_info_dict['code_score_detail'] = str(score_detail_dict)

    Data_fluctuationScale = jsContent.eval('Data_fluctuationScale')
    jijin_info_dict['fluctuation_scale'] = str(Data_fluctuationScale)

    Data_holderStructure = jsContent.eval('Data_holderStructure')
    jijin_info_dict['holder_structure'] = str(Data_holderStructure)

    Data_assetAllocation = jsContent.eval('Data_assetAllocation')
    jijin_info_dict['asset_allocation'] = str(Data_assetAllocation)
    return jijin_info_dict


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
        datefmt='%a, %d %b %Y %H:%M:%S'
    )
    logger = logging.getLogger(__file__)

    example_word = """
        DESCRIBE ARGUMENT USAGE HERE
        python main.py --help
    """

    parser = argparse.ArgumentParser(prog=__file__, description='code description', epilog=example_word,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    # add parameter if needed
    parser.add_argument('-v', '--version', help='version of code', action='version', version='%(prog)s 1.0')
    parser.add_argument('--codes', help="code list for jiin", nargs='+')
    args = parser.parse_args()

    code_list = args.codes
    if not code_list: # read from local file
        code_list = read_from_local()
    extract_all_jijin_info(code_list, logger)


if __name__ == '__main__':
    main()
