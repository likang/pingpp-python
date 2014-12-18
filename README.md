
# 参赛说明

基于官方给出的 SDK，主要做出了以下改动：

1. 删除证书黑名单
2. 使用 certifi 模块代替自带的 CA 列表
3. 使用 urllib3 代替 requests
4. 移除废弃的代码
5. 根据 pep8 标准格式化代码

## 具体说明
### 1.删除证书黑名单
Pingplusplus 目前没有吊销的证书，固无需使用黑名单。另外，
SLL证书的吊销检查被谷歌浏览器的团队视为意义不大，已放弃支持，
[查看详情]([https://www.imperialviolet.org/2012/02/05/crlsets.html)。

### 2. 使用 certifi 模块代替自带的 CA 列表
这是目前 Python 模块的通用做法，不自己维护这个列表，而是使用公开维护的模块。

### 3. 使用 urllib3 代替 requests
Pingplusplus 的 SDK 使用 requests 模块时，仅仅用到了其支持 SSL 的特性，
而 requests 这一特性来自于其内置的 urllib3 模块，因此使用独立的 urllib3 
模块显得更加合理、精简。

# PingPP-Python SDK 
----------

## 简介

pingpp 文件夹下是 Python SDK 文件，<br>
example 文件夹里面是简单的接入示例，该示例仅供参考。

## 安装

	pip install pingpp
	
或使用setup.py手动安装
	
    python setup.py install

## 使用
#### 在接口调用之前，需执行如下代码：
```python
// 导入pingpp模块
import pingpp

// 设置API-KEY
pingpp.api_key = 'API-KEY'
```

## Pagination 分页
```python
chs = pingpp.Charge.all()
```

## Expanding 展开对象
```python
ch = pingpp.Charge.retrieve(id='CHARGE-ID', expand='app')
```
## Metadata 元数据
```python
ch = pingpp.Charge.create(
    order_no='1234567890',
    amount=1,
    app=dict(id='APP-ID'),
    channel='upmp',
    currency='cny',
    client_ip='CLIENT-IP',
    subject='test-subject',
    body='test-body',
    metadata=dict(color='red')
)
```
## 创建Charge对象
```python
ch = pingpp.Charge.create(
    order_no='1234567890',
    amount=1,
    app=dict(id='APP-ID'),
    channel='upmp',
    currency='cny',
    client_ip='CLIENT-IP',
    subject='test-subject',
    body='test-body',
)
```
    
## 查询 Charge 对象
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
```
    
## 创建 Refund 对象
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.create(description='desc', amount=1)
```
    
## 查询 Refund 对象
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
re = ch.refunds.retrieve('REFUND-ID')
```
    
## 查询 Refund 对象列表
```python
ch = pingpp.Charge.retrieve('CHARGE-ID')
res = ch.refunds.all(limit=3)
```
    
