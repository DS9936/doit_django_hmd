import os
import django
import csv
import sys


# 일반 파이썬앱(스크립트)에서 django ORM을 사용하려면 다음의 설정 필요
# django 환경설정 파일 지정
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doit_django_prj.settings")
# django settings 메모리 로딩 적용
django.setup()


# Foods 클래스와 연결된 테이블에 data를 ORM으로 업로딩 하기 위해서 import 함
from ramen_sales.models import Ramen

# csv 파일 위치 변수로 정의
CSV_PATH = './datas/라면 가격변동 데이터.csv'

with open(CSV_PATH, 'r',  encoding='utf-8') as file:
  data_rows = csv.reader(file, skipinitialspace=True)
  # header(첫번째 줄) 제외
  next(data_rows, None)

  # 공백라인을 제거하기 위해서
  data_rows = list(data_rows)
  # print("전 ", data_rows)
  data_rows = list(filter(None, data_rows))
  print("후 ", data_rows)

for row in data_rows:
    # print(row)
    print(row)
    if row[0] != None or row[0] !='':
      # 무조건 업로드, 중복데이터도 허용함
      # Foods.objects.create(
      #   cook_name= row[0],
      #   count= row[1],
      #   unit_price= row[2],
      # )
            # 중복데이터를 빼고 업로딩
      Ramen.objects.update_or_create(
        # filter : 중복을 체크하는 값
        date = row[0],



        # new_value : 필터에 중복값이 없을때
        defaults={
        'date' : row[0],
        'shinramyun' : row[1],
        'samyangramyun' : row[2],
        'jinramyun' : row[3],
        'average' : row[4]
        }
        
      )