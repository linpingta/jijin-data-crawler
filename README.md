# jijin_data_crawler

尽管天天基金提供了API可以直接获取基金数据，但获取如 基金经理评分，基金经理年限，管理基金量级等相对宏观信息并不容易； 这里提供了依赖网站相关js获取信息的功能，仅供使用

[![GitHub stars](https://img.shields.io/github/stars/linpingta/jijin-data-crawler.svg?style=social&label=Star)](https://github.com/linpingta/jijin-data-crawler/stargazers)
[![Fork](https://img.shields.io/badge/-Fork-green?logo=github&style=for-the-badge)](https://github.com/linpingta/jijin-data-crawler/fork)
[![Clone](https://img.shields.io/badge/Clone-HTTPS-blue.svg)](https://github.com/linpingta/jijin-data-crawler.git)

## 效果

<img width="1611" alt="WX20211023-161154@2x" src="https://user-images.githubusercontent.com/2771082/138548485-80bc40d9-722d-4d77-a5c0-dd52381777c2.png">



## 使用

pip3 install pandas / requests / execjs

### 获取一组基金结果 (输入基金编码)

    python3 jijin_data_crawler.py --codes 000001

### 获取所有基金结果 (截止目前共13k)

    python3 jijin_data_crawler.py

### 代码结果示例

    ....
    [connectionpool.py:228 - _new_conn Sat, 17 Jun 2023 08:57:16;DEBUG] Starting new HTTP connection (1): fund.eastmoney.com:80
    [connectionpool.py:456 - _make_request Sat, 17 Jun 2023 09:02:00;DEBUG] http://fund.eastmoney.com:80 "GET /pingzhongdata/000054.js?v=20230617085716 HTTP/1.1" 200 None
    [jijin_data_crawler.py:40 - extract_all_jijin_info Sat, 17 Jun 2023 10:40:36;DEBUG] current_idx:40
    ....

Good Luck~
