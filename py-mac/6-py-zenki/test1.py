#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
import logging
from collections import deque

print(time.time())
logging.error("can't dump counter to file %s: %s", 'aaa', 'bbb')
a = deque(maxlen=10)
a.append(1)
a.append(2)
a.append(3)

print(a.pop())
