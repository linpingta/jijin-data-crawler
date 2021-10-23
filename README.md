# jijin_data_crawler

尽管天天基金提供了API可以直接获取基金数据，但获取如 基金经理评分，基金经理年限，管理基金量级等相对宏观信息并不容易； 这里提供了依赖网站相关js获取信息的功能

## 效果

<img width="1611" alt="WX20211023-161154@2x" src="https://user-images.githubusercontent.com/2771082/138548485-80bc40d9-722d-4d77-a5c0-dd52381777c2.png">



## 使用

pip3 install pandas / requests / execjs

### 获取一组基金结果 (输入基金编码)

    python3 jijin_data_crawler.py --codes 000001

### 获取所有基金结果 (截止目前共13k)

    python3 jijin_data_crawler.py


Have Fun~
