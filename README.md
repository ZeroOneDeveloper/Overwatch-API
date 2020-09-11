# Overwatch-API
쉽고 간단한 오버워치 API

# 설명
랭킹, 레벨, 닉네임, 플레이 타임 등등 사용자의 랭킹을 조회할수 있도록
작성하였습니다. 

# 제작자
디스코드 : `STORM#9999`
이메일 : `storm@stormdev.club`

# 사용 방법
```py
from Overwatch import Overwatch
name = "kirito7416"
tag = "3341"
name = Overwatch.level(name=name, tag=tag)
print(name)
```
