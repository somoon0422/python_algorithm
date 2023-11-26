# open(), read(), wrtie(), close() 순서를 기억하자!!

test_path = 'C:/Users/MarkAny-N220/Desktop/sohee/zerobase/2.실습/test.txt'

with open(test_path, 'w') as f:
    f.write('hello world')
    
print(f)