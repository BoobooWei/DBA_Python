# -*- coding: utf-8 -*-

import uuid

name = "test_name"
namespace = "test_namespace"

print(uuid.uuid1())  # 带参的方法参见Python Doc
print(uuid.uuid3(namespace, name))
print(uuid.uuid4())
print(uuid.uuid5(namespace, name))
